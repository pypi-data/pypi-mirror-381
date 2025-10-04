"""
Vote Collector
Collects and tallies votes for conflicting transactions
"""

from dataclasses import dataclass
from enum import Enum
import time
import logging
from typing import Dict, List, Optional, Tuple

from ..types.transaction import Transaction


logger = logging.getLogger(__name__)


class VoteResult(Enum):
    """Vote result status"""
    PENDING = "pending"
    TX1_WINS = "tx1_wins"
    TX2_WINS = "tx2_wins"
    TIMEOUT = "timeout"


@dataclass
class Vote:
    """
    Vote on conflicting transaction
    
    Specification: Section 5.4 - Resolving Conflicts
    Voting message: 65 bytes (tx_hash + voter_pubkey + signature)
    
    Attributes:
        tx_hash: Transaction being voted for
        voter_pubkey: Public key of voter
        voter_balance: Balance of voter (vote weight)
        timestamp: When vote was cast
    """
    tx_hash: bytes
    voter_pubkey: bytes
    voter_balance: int
    timestamp: float
    
    def __post_init__(self):
        """Validate vote"""
        if len(self.tx_hash) != 32:
            raise ValueError("Transaction hash must be 32 bytes")
        if len(self.voter_pubkey) != 32:
            raise ValueError("Voter public key must be 32 bytes")
        if self.voter_balance < 0:
            raise ValueError("Voter balance must be non-negative")


class VoteCollector:
    """
    Collects and tallies votes for conflict resolution
    
    Specification: Section 2.4 - Consensus Model
    
    Simplified Voting System:
    - No representatives. No delegation. Direct voting by balance.
    - When conflicting transactions detected (double-spend):
      1. Both transactions broadcast to network
      2. Full nodes vote by balance (1 token = 1 vote)
      3. Transaction with most vote weight within 2 seconds wins
      4. Losing transaction discarded
      5. Voting message: 65 bytes (tx_hash + voter_pubkey + signature)
    
    Finality:
    - Transaction final when 51% of online balance has voted
    - Online balance = sum of accounts that voted in last 24 hours
    - Simple majority rule
    
    Example:
        >>> collector = VoteCollector(storage)
        >>> 
        >>> # Start collecting votes
        >>> collector.start_voting(tx1, tx2)
        >>> 
        >>> # Add votes
        >>> collector.add_vote(tx1.tx_hash, voter_pubkey, balance)
        >>> 
        >>> # Get result after timeout
        >>> result = collector.get_result(tx1.tx_hash, tx2.tx_hash)
    """
    
    def __init__(self, storage, vote_timeout: float = 2.0):
        """
        Initialize vote collector
        
        Args:
            storage: LevelDBStorage instance
            vote_timeout: Voting timeout in seconds (default: 2.0)
        """
        self.storage = storage
        self.vote_timeout = vote_timeout
        
        # Active voting sessions: (tx1_hash, tx2_hash) -> start_time
        self.voting_sessions: Dict[tuple[bytes, bytes], float] = {}
        
        # Votes: tx_hash -> set of voter_pubkeys
        self.votes: Dict[bytes, Set[bytes]] = {}
        
        # Vote weights: tx_hash -> total weight
        self.vote_weights: Dict[bytes, int] = {}
    
    def start_voting(self, tx1: Transaction, tx2: Transaction):
        """
        Start voting session for conflicting transactions
        
        Args:
            tx1: First transaction
            tx2: Second transaction
        """
        session_key = self._make_session_key(tx1.tx_hash, tx2.tx_hash)
        
        if session_key not in self.voting_sessions:
            self.voting_sessions[session_key] = time.time()
            self.votes[tx1.tx_hash] = set()
            self.votes[tx2.tx_hash] = set()
            self.vote_weights[tx1.tx_hash] = 0
            self.vote_weights[tx2.tx_hash] = 0
            
            logger.info(
                f"Started voting session: "
                f"{tx1.tx_hash.hex()[:16]}... vs "
                f"{tx2.tx_hash.hex()[:16]}..."
            )
    
    def add_vote(self, tx_hash: bytes, voter_pubkey: bytes, voter_balance: int) -> bool:
        """
        Add vote for transaction
        
        Args:
            tx_hash: Transaction being voted for
            voter_pubkey: Public key of voter
            voter_balance: Balance of voter (vote weight)
            
        Returns:
            True if vote was added, False if duplicate or invalid
        """
        # Check if transaction is in active voting
        if tx_hash not in self.votes:
            logger.debug(f"Vote for unknown transaction: {tx_hash.hex()[:16]}...")
            return False
        
        # Check for duplicate vote
        if voter_pubkey in self.votes[tx_hash]:
            logger.debug(f"Duplicate vote from {voter_pubkey.hex()[:16]}...")
            return False
        
        # Add vote
        self.votes[tx_hash].add(voter_pubkey)
        self.vote_weights[tx_hash] += voter_balance
        
        logger.debug(
            f"Vote added for {tx_hash.hex()[:16]}... "
            f"from {voter_pubkey.hex()[:16]}... "
            f"weight={voter_balance}"
        )
        
        return True
    
    def get_result(self, tx1_hash: bytes, tx2_hash: bytes) -> tuple[VoteResult, Optional[bytes]]:
        """
        Get voting result
        
        Args:
            tx1_hash: First transaction hash
            tx2_hash: Second transaction hash
            
        Returns:
            Tuple of (result, winner_hash)
        """
        session_key = self._make_session_key(tx1_hash, tx2_hash)
        
        if session_key not in self.voting_sessions:
            return (VoteResult.PENDING, None)
        
        start_time = self.voting_sessions[session_key]
        elapsed = time.time() - start_time
        
        # Check if voting period has ended
        if elapsed < self.vote_timeout:
            return (VoteResult.PENDING, None)
        
        # Tally votes
        weight1 = self.vote_weights.get(tx1_hash, 0)
        weight2 = self.vote_weights.get(tx2_hash, 0)
        
        logger.info(
            f"Voting complete: "
            f"tx1={weight1} vs tx2={weight2}"
        )
        
        # Determine winner
        if weight1 > weight2:
            return (VoteResult.TX1_WINS, tx1_hash)
        elif weight2 > weight1:
            return (VoteResult.TX2_WINS, tx2_hash)
        else:
            # Tie - use hash comparison as tiebreaker
            if tx1_hash < tx2_hash:
                return (VoteResult.TX1_WINS, tx1_hash)
            else:
                return (VoteResult.TX2_WINS, tx2_hash)
    
    def cleanup_session(self, tx1_hash: bytes, tx2_hash: bytes):
        """
        Clean up voting session
        
        Args:
            tx1_hash: First transaction hash
            tx2_hash: Second transaction hash
        """
        session_key = self._make_session_key(tx1_hash, tx2_hash)
        
        # Remove session
        self.voting_sessions.pop(session_key, None)
        
        # Remove votes
        self.votes.pop(tx1_hash, None)
        self.votes.pop(tx2_hash, None)
        self.vote_weights.pop(tx1_hash, None)
        self.vote_weights.pop(tx2_hash, None)
    
    def _make_session_key(self, hash1: bytes, hash2: bytes) -> tuple[bytes, bytes]:
        """Create normalized session key (order-independent)"""
        if hash1 < hash2:
            return (hash1, hash2)
        else:
            return (hash2, hash1)
    
    def get_stats(self) -> dict:
        """Get voting statistics"""
        return {
            'active_sessions': len(self.voting_sessions),
            'total_votes': sum(len(v) for v in self.votes.values()),
            'vote_timeout': self.vote_timeout
        }
