"""
Duplicate Detection
Prevents forwarding duplicate transactions
"""

import time
from collections import deque
from typing import Set


class DuplicateDetector:
    """
    Duplicate transaction detector
    
    Specification: Section 4.3 - Transaction Propagation
    
    Duplicate Detection:
    - Keep in-memory set of seen tx hashes (last 10,000)
    - Don't forward duplicates
    - Clear set every hour
    
    Uses a ring buffer approach for memory efficiency.
    
    Example:
        >>> detector = DuplicateDetector()
        >>> 
        >>> tx_hash = bytes(32)
        >>> if detector.is_duplicate(tx_hash):
        ...     print("Already seen")
        ... else:
        ...     detector.mark_seen(tx_hash)
        ...     print("New transaction")
    """
    
    def __init__(self, max_size: int = 10000, clear_interval: int = 3600):
        """
        Initialize duplicate detector
        
        Args:
            max_size: Maximum number of hashes to track (default: 10,000)
            clear_interval: Interval to clear old hashes in seconds (default: 3600 = 1 hour)
        """
        self.max_size = max_size
        self.clear_interval = clear_interval
        
        # Use set for O(1) lookup
        self.seen_hashes: Set[bytes] = set()
        
        # Use deque for FIFO removal
        self.hash_queue: deque = deque(maxlen=max_size)
        
        # Track last clear time
        self.last_clear = time.time()
    
    def is_duplicate(self, tx_hash: bytes) -> bool:
        """
        Check if transaction hash has been seen
        
        Args:
            tx_hash: 32-byte transaction hash
            
        Returns:
            True if duplicate (already seen)
        """
        # Check if time to clear
        if time.time() - self.last_clear > self.clear_interval:
            self.clear()
        
        return tx_hash in self.seen_hashes
    
    def mark_seen(self, tx_hash: bytes):
        """
        Mark transaction hash as seen
        
        Args:
            tx_hash: 32-byte transaction hash
        """
        if tx_hash in self.seen_hashes:
            return
        
        # Add to set
        self.seen_hashes.add(tx_hash)
        
        # Add to queue
        self.hash_queue.append(tx_hash)
        
        # If queue is full, remove oldest
        if len(self.hash_queue) >= self.max_size:
            oldest = self.hash_queue[0]
            if oldest in self.seen_hashes:
                self.seen_hashes.discard(oldest)
    
    def clear(self):
        """Clear all seen hashes"""
        self.seen_hashes.clear()
        self.hash_queue.clear()
        self.last_clear = time.time()
    
    def get_stats(self) -> dict:
        """Get statistics"""
        return {
            'seen_count': len(self.seen_hashes),
            'max_size': self.max_size,
            'last_clear': self.last_clear,
            'time_until_clear': max(0, self.clear_interval - (time.time() - self.last_clear))
        }
