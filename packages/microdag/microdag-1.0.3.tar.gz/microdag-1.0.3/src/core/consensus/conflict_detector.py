"""
Conflict Detector
Detects double-spend attempts and conflicting transactions
"""

from dataclasses import dataclass
from typing import Optional, List
import logging

from ..types.transaction import Transaction


logger = logging.getLogger(__name__)


@dataclass
class ConflictPair:
    """
    Pair of conflicting transactions
    
    Attributes:
        tx1: First transaction
        tx2: Second transaction (conflicts with tx1)
        reason: Reason for conflict
    """
    tx1: Transaction
    tx2: Transaction
    reason: str
    
    def __repr__(self) -> str:
        return (
            f"ConflictPair("
            f"tx1={self.tx1.tx_hash.hex()[:16]}..., "
            f"tx2={self.tx2.tx_hash.hex()[:16]}..., "
            f"reason={self.reason})"
        )


class ConflictDetector:
    """
    Detects conflicting transactions (double-spends)
    
    Specification: Section 5.4 - Conflict Resolution
    
    Detecting Conflicts:
    Two transactions with same previous hash = conflict
    
    This indicates a double-spend attempt where an account
    tries to spend the same balance twice.
    
    Example:
        >>> detector = ConflictDetector(storage)
        >>> 
        >>> # Check for conflicts
        >>> conflict = detector.check_conflict(new_tx)
        >>> if conflict:
        ...     print(f"Conflict detected: {conflict.reason}")
        ...     # Initiate voting
    """
    
    def __init__(self, storage):
        """
        Initialize conflict detector
        
        Args:
            storage: LevelDBStorage instance
        """
        self.storage = storage
        
        # Track known conflicts (to avoid re-processing)
        self.known_conflicts: set[tuple[bytes, bytes]] = set()
    
    def check_conflict(self, tx: Transaction) -> Optional[ConflictPair]:
        """
        Check if transaction conflicts with existing transaction
        
        Specification: Section 5.4 - Detecting Conflicts
        
        def check_conflict(tx):
            # Two transactions with same previous hash = conflict
            for existing_tx in get_transactions_by_account(tx.account):
                if existing_tx.previous == tx.previous and existing_tx.hash != tx.hash:
                    return existing_tx
            return None
        
        Args:
            tx: Transaction to check
            
        Returns:
            ConflictPair if conflict found, None otherwise
        """
        # Get all transactions for this account
        chain_length = self.storage.get_chain_length(tx.account)
        
        for i in range(chain_length):
            existing_tx_hash = self.storage.get_chain_transaction(tx.account, i)
            if existing_tx_hash is None:
                continue
            
            existing_tx = self.storage.get_transaction(existing_tx_hash)
            if existing_tx is None:
                continue
            
            # Check for same previous hash (double-spend)
            if existing_tx.previous == tx.previous and existing_tx.tx_hash != tx.tx_hash:
                # Found conflict!
                conflict_key = self._make_conflict_key(existing_tx.tx_hash, tx.tx_hash)
                
                if conflict_key not in self.known_conflicts:
                    self.known_conflicts.add(conflict_key)
                    
                    logger.warning(
                        f"Conflict detected: "
                        f"{existing_tx.tx_hash.hex()[:16]}... vs "
                        f"{tx.tx_hash.hex()[:16]}..."
                    )
                    
                    return ConflictPair(
                        tx1=existing_tx,
                        tx2=tx,
                        reason="Double-spend: same previous hash"
                    )
        
        return None
    
    def is_known_conflict(self, tx1_hash: bytes, tx2_hash: bytes) -> bool:
        """
        Check if conflict between two transactions is already known
        
        Args:
            tx1_hash: First transaction hash
            tx2_hash: Second transaction hash
            
        Returns:
            True if conflict is known
        """
        conflict_key = self._make_conflict_key(tx1_hash, tx2_hash)
        return conflict_key in self.known_conflicts
    
    def mark_conflict_resolved(self, tx1_hash: bytes, tx2_hash: bytes):
        """
        Mark conflict as resolved
        
        Args:
            tx1_hash: First transaction hash
            tx2_hash: Second transaction hash
        """
        conflict_key = self._make_conflict_key(tx1_hash, tx2_hash)
        self.known_conflicts.discard(conflict_key)
    
    def _make_conflict_key(self, hash1: bytes, hash2: bytes) -> tuple[bytes, bytes]:
        """
        Create normalized conflict key (order-independent)
        
        Args:
            hash1: First hash
            hash2: Second hash
            
        Returns:
            Tuple of (smaller_hash, larger_hash)
        """
        if hash1 < hash2:
            return (hash1, hash2)
        else:
            return (hash2, hash1)
    
    def get_conflict_count(self) -> int:
        """Get number of known conflicts"""
        return len(self.known_conflicts)
