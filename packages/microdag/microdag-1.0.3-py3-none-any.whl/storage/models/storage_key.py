"""
Storage Key Models
Defines key formats for LevelDB tables
"""

from enum import Enum
import struct


class StorageTable(Enum):
    """
    LevelDB table prefixes
    
    Specification: Section 5.1 - Data Storage
    
    Tables:
    - accounts: Current state of each account
    - transactions: All transactions (for querying)
    - account_chain: Ordered list of transactions per account
    - pending: Unreceived SEND transactions
    """
    ACCOUNTS = b'a:'
    TRANSACTIONS = b't:'
    ACCOUNT_CHAIN = b'c:'
    PENDING = b'p:'


class StorageKey:
    """
    Helper for creating LevelDB keys
    
    All keys are prefixed with table identifier for namespace separation.
    """
    
    @staticmethod
    def account(public_key: bytes) -> bytes:
        """
        Create key for account state
        
        Format: 'a:' + 32-byte public key
        
        Args:
            public_key: 32-byte account public key
            
        Returns:
            34-byte key
        """
        if len(public_key) != 32:
            raise ValueError("Public key must be 32 bytes")
        return StorageTable.ACCOUNTS.value + public_key
    
    @staticmethod
    def transaction(tx_hash: bytes) -> bytes:
        """
        Create key for transaction
        
        Format: 't:' + 32-byte transaction hash
        
        Args:
            tx_hash: 32-byte transaction hash
            
        Returns:
            34-byte key
        """
        if len(tx_hash) != 32:
            raise ValueError("Transaction hash must be 32 bytes")
        return StorageTable.TRANSACTIONS.value + tx_hash
    
    @staticmethod
    def account_chain(public_key: bytes, index: int) -> bytes:
        """
        Create key for account chain entry
        
        Format: 'c:' + 32-byte public key + 8-byte index (uint64, big-endian)
        
        Args:
            public_key: 32-byte account public key
            index: Transaction index in account's chain
            
        Returns:
            42-byte key
        """
        if len(public_key) != 32:
            raise ValueError("Public key must be 32 bytes")
        if index < 0:
            raise ValueError("Index must be non-negative")
        
        # Use big-endian for proper sorting
        index_bytes = struct.pack('>Q', index)
        return StorageTable.ACCOUNT_CHAIN.value + public_key + index_bytes
    
    @staticmethod
    def pending(recipient_pubkey: bytes, send_tx_hash: bytes) -> bytes:
        """
        Create key for pending transaction
        
        Format: 'p:' + 32-byte recipient + 32-byte send_tx_hash
        
        Args:
            recipient_pubkey: 32-byte recipient public key
            send_tx_hash: 32-byte SEND transaction hash
            
        Returns:
            66-byte key
        """
        if len(recipient_pubkey) != 32:
            raise ValueError("Recipient public key must be 32 bytes")
        if len(send_tx_hash) != 32:
            raise ValueError("Send transaction hash must be 32 bytes")
        
        return StorageTable.PENDING.value + recipient_pubkey + send_tx_hash
    
    @staticmethod
    def parse_account_chain_key(key: bytes) -> tuple[bytes, int]:
        """
        Parse account chain key to extract public key and index
        
        Args:
            key: 42-byte account chain key
            
        Returns:
            Tuple of (public_key, index)
        """
        if len(key) != 42:
            raise ValueError("Account chain key must be 42 bytes")
        
        # Skip prefix (2 bytes)
        public_key = key[2:34]
        index = struct.unpack('>Q', key[34:42])[0]
        
        return public_key, index
    
    @staticmethod
    def parse_pending_key(key: bytes) -> tuple[bytes, bytes]:
        """
        Parse pending key to extract recipient and send tx hash
        
        Args:
            key: 66-byte pending key
            
        Returns:
            Tuple of (recipient_pubkey, send_tx_hash)
        """
        if len(key) != 66:
            raise ValueError("Pending key must be 66 bytes")
        
        # Skip prefix (2 bytes)
        recipient_pubkey = key[2:34]
        send_tx_hash = key[34:66]
        
        return recipient_pubkey, send_tx_hash
