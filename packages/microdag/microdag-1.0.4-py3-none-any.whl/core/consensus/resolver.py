"""
Conflict Resolver
Orchestrates conflict detection and resolution
"""

import logging
from typing import Optional

from ..types.transaction import Transaction
from .conflict_detector import ConflictDetector, ConflictPair
from .voter import VoteCollector, VoteResult


logger = logging.getLogger(__name__)


class ConflictResolver:
    """
    Orchestrates complete conflict resolution process
    
    Specification: Section 5.4 - Conflict Resolution
    
    Example:
        >>> resolver = ConflictResolver(storage, processor)
        >>> result = resolver.process_transaction(tx)
    """
    
    def __init__(self, storage, processor, vote_timeout: float = 2.0):
        """
        Initialize conflict resolver
        
        Args:
            storage: LevelDBStorage instance
            processor: TransactionProcessor instance
            vote_timeout: Voting timeout in seconds
        """
        self.storage = storage
        self.processor = processor
        
        self.detector = ConflictDetector(storage)
        self.vote_collector = VoteCollector(storage, vote_timeout)
    
    def process_transaction(self, tx: Transaction) -> str:
        """
        Process transaction with conflict resolution
        
        Args:
            tx: Transaction to process
            
        Returns:
            Status: 'processed', 'conflict', or 'rejected'
        """
        # Check for conflicts
        conflict = self.detector.check_conflict(tx)
        
        if conflict is None:
            # No conflict - process normally
            result = self.processor.process(tx)
            if result.valid:
                return 'processed'
            else:
                return 'rejected'
        
        # Conflict detected - start voting
        self.vote_collector.start_voting(conflict.tx1, conflict.tx2)
        return 'conflict'
    
    def resolve_conflict(self, tx1_hash: bytes, tx2_hash: bytes) -> Optional[bytes]:
        """
        Resolve conflict and return winner
        
        Args:
            tx1_hash: First transaction hash
            tx2_hash: Second transaction hash
            
        Returns:
            Winner transaction hash or None if still pending
        """
        result, winner_hash = self.vote_collector.get_result(tx1_hash, tx2_hash)
        
        if result == VoteResult.PENDING:
            return None
        
        # Clean up voting session
        self.vote_collector.cleanup_session(tx1_hash, tx2_hash)
        self.detector.mark_conflict_resolved(tx1_hash, tx2_hash)
        
        return winner_hash
