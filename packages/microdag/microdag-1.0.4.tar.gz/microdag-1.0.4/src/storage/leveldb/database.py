"""
LevelDB Database Wrapper
Provides high-level interface to LevelDB storage
"""

import os
import plyvel
from typing import Optional, Iterator, Tuple
from pathlib import Path

from ..models import StorageKey, StorageTable
from ...core.types.account import AccountState
from ...core.types.transaction import Transaction, deserialize_transaction


class LevelDBStorage:
    """
    LevelDB storage implementation
    
    Specification: Section 5.1 - Data Storage
    
    Tables:
    - accounts: key=32-byte pubkey, value=40-byte state
    - transactions: key=32-byte hash, value=141-byte transaction
    - account_chain: key=32-byte pubkey + 8-byte index, value=32-byte tx hash
    - pending: key=32-byte recipient + 32-byte send_tx_hash, value=1 byte
    
    Total Database Size: ~1GB for 10 million transactions
    
    Example:
        >>> db = LevelDBStorage("./data")
        >>> db.open()
        >>> 
        >>> # Store account
        >>> state = AccountState(balance=1000, frontier=bytes(32))
        >>> db.put_account(public_key, state)
        >>> 
        >>> # Get account
        >>> loaded_state = db.get_account(public_key)
        >>> 
        >>> db.close()
    """
    
    def __init__(self, data_dir: str):
        """
        Initialize LevelDB storage
        
        Args:
            data_dir: Directory for database files
        """
        self.data_dir = Path(data_dir)
        self.db: Optional[plyvel.DB] = None
    
    def open(self, create_if_missing: bool = True):
        """
        Open database connection
        
        Args:
            create_if_missing: Create database if it doesn't exist
        """
        # Create directory if needed
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Open LevelDB
        self.db = plyvel.DB(
            str(self.data_dir),
            create_if_missing=create_if_missing,
            compression='snappy'  # Enable compression
        )
    
    def close(self):
        """Close database connection"""
        if self.db is not None:
            self.db.close()
            self.db = None
    
    def __enter__(self):
        """Context manager entry"""
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()
    
    # ==================== Account Operations ====================
    
    def put_account(self, public_key: bytes, state: AccountState):
        """
        Store account state
        
        Args:
            public_key: 32-byte account public key
            state: Account state (40 bytes)
        """
        key = StorageKey.account(public_key)
        value = state.to_bytes()
        self.db.put(key, value)
    
    def get_account(self, public_key: bytes) -> Optional[AccountState]:
        """
        Get account state
        
        Args:
            public_key: 32-byte account public key
            
        Returns:
            AccountState or None if not found
        """
        key = StorageKey.account(public_key)
        value = self.db.get(key)
        
        if value is None:
            return None
        
        return AccountState.from_bytes(value)
    
    def delete_account(self, public_key: bytes):
        """
        Delete account state
        
        Args:
            public_key: 32-byte account public key
        """
        key = StorageKey.account(public_key)
        self.db.delete(key)
    
    def account_exists(self, public_key: bytes) -> bool:
        """
        Check if account exists
        
        Args:
            public_key: 32-byte account public key
            
        Returns:
            True if account exists
        """
        key = StorageKey.account(public_key)
        return self.db.get(key) is not None
    
    # ==================== Transaction Operations ====================
    
    def put_transaction(self, tx: Transaction):
        """
        Store transaction
        
        Args:
            tx: Transaction to store
        """
        from ...core.types.transaction import serialize_transaction
        
        key = StorageKey.transaction(tx.tx_hash)
        value = serialize_transaction(tx)
        self.db.put(key, value)
    
    def get_transaction(self, tx_hash: bytes) -> Optional[Transaction]:
        """
        Get transaction by hash
        
        Args:
            tx_hash: 32-byte transaction hash
            
        Returns:
            Transaction or None if not found
        """
        key = StorageKey.transaction(tx_hash)
        value = self.db.get(key)
        
        if value is None:
            return None
        
        return deserialize_transaction(value)
    
    def delete_transaction(self, tx_hash: bytes):
        """
        Delete transaction
        
        Args:
            tx_hash: 32-byte transaction hash
        """
        key = StorageKey.transaction(tx_hash)
        self.db.delete(key)
    
    def transaction_exists(self, tx_hash: bytes) -> bool:
        """
        Check if transaction exists
        
        Args:
            tx_hash: 32-byte transaction hash
            
        Returns:
            True if transaction exists
        """
        key = StorageKey.transaction(tx_hash)
        return self.db.get(key) is not None
    
    # ==================== Account Chain Operations ====================
    
    def append_to_chain(self, public_key: bytes, tx_hash: bytes):
        """
        Append transaction to account's chain
        
        Args:
            public_key: 32-byte account public key
            tx_hash: 32-byte transaction hash
        """
        # Get current chain length
        chain_length = self.get_chain_length(public_key)
        
        # Append at next index
        key = StorageKey.account_chain(public_key, chain_length)
        self.db.put(key, tx_hash)
    
    def get_chain_transaction(self, public_key: bytes, index: int) -> Optional[bytes]:
        """
        Get transaction hash at index in account's chain
        
        Args:
            public_key: 32-byte account public key
            index: Transaction index
            
        Returns:
            32-byte transaction hash or None
        """
        key = StorageKey.account_chain(public_key, index)
        return self.db.get(key)
    
    def get_chain_length(self, public_key: bytes) -> int:
        """
        Get length of account's transaction chain
        
        Args:
            public_key: 32-byte account public key
            
        Returns:
            Number of transactions in chain
        """
        count = 0
        prefix = StorageTable.ACCOUNT_CHAIN.value + public_key
        
        for _ in self.db.iterator(prefix=prefix):
            count += 1
        
        return count
    
    def iterate_chain(self, public_key: bytes) -> Iterator[Tuple[int, bytes]]:
        """
        Iterate over account's transaction chain
        
        Args:
            public_key: 32-byte account public key
            
        Yields:
            Tuples of (index, tx_hash)
        """
        prefix = StorageTable.ACCOUNT_CHAIN.value + public_key
        
        for key, tx_hash in self.db.iterator(prefix=prefix):
            _, index = StorageKey.parse_account_chain_key(key)
            yield index, tx_hash
    
    # ==================== Pending Operations ====================
    
    def add_pending(self, recipient_pubkey: bytes, send_tx_hash: bytes):
        """
        Add pending SEND transaction
        
        Args:
            recipient_pubkey: 32-byte recipient public key
            send_tx_hash: 32-byte SEND transaction hash
        """
        key = StorageKey.pending(recipient_pubkey, send_tx_hash)
        self.db.put(key, b'\x01')  # 1 byte marker
    
    def remove_pending(self, recipient_pubkey: bytes, send_tx_hash: bytes):
        """
        Remove pending SEND transaction
        
        Args:
            recipient_pubkey: 32-byte recipient public key
            send_tx_hash: 32-byte SEND transaction hash
        """
        key = StorageKey.pending(recipient_pubkey, send_tx_hash)
        self.db.delete(key)
    
    def pending_exists(self, recipient_pubkey: bytes, send_tx_hash: bytes) -> bool:
        """
        Check if pending transaction exists
        
        Args:
            recipient_pubkey: 32-byte recipient public key
            send_tx_hash: 32-byte SEND transaction hash
            
        Returns:
            True if pending transaction exists
        """
        key = StorageKey.pending(recipient_pubkey, send_tx_hash)
        return self.db.get(key) is not None
    
    def get_pending(self, recipient_pubkey: bytes) -> list[bytes]:
        """
        Get all pending SEND transactions for account
        
        Args:
            recipient_pubkey: 32-byte recipient public key
            
        Returns:
            List of SEND transaction hashes
        """
        prefix = StorageTable.PENDING.value + recipient_pubkey
        pending = []
        
        for key, _ in self.db.iterator(prefix=prefix):
            _, send_tx_hash = StorageKey.parse_pending_key(key)
            pending.append(send_tx_hash)
        
        return pending
    
    # ==================== Utility Operations ====================
    
    def get_stats(self) -> dict:
        """
        Get database statistics
        
        Returns:
            Dictionary with database stats
        """
        stats = {
            'accounts': 0,
            'transactions': 0,
            'pending': 0,
            'chain_entries': 0
        }
        
        # Count each table
        for table in StorageTable:
            count = 0
            for _ in self.db.iterator(prefix=table.value):
                count += 1
            
            if table == StorageTable.ACCOUNTS:
                stats['accounts'] = count
            elif table == StorageTable.TRANSACTIONS:
                stats['transactions'] = count
            elif table == StorageTable.PENDING:
                stats['pending'] = count
            elif table == StorageTable.ACCOUNT_CHAIN:
                stats['chain_entries'] = count
        
        return stats
    
    def compact(self):
        """Compact database to reclaim space"""
        if self.db is not None:
            self.db.compact_range()
