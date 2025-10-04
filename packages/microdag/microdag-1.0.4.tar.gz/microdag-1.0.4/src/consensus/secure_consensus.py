"""
Secure Consensus System for MicroDAG
Enhanced balance-weighted voting with malicious node detection and Sybil resistance
"""

import time
import hashlib
import logging
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import asyncio
import aiohttp
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.exceptions import InvalidSignature

logger = logging.getLogger(__name__)


@dataclass
class Vote:
    """Cryptographically signed vote"""
    tx_hash: str
    voter_pubkey: bytes
    voter_balance: int
    vote_type: str  # 'approve', 'reject', 'abstain'
    timestamp: float
    signature: bytes
    nonce: int = 0  # Prevent replay attacks
    
    def __post_init__(self):
        if self.timestamp == 0:
            self.timestamp = time.time()
    
    def to_bytes(self) -> bytes:
        """Serialize vote for signature verification"""
        return (
            self.tx_hash.encode() +
            self.voter_pubkey +
            self.voter_balance.to_bytes(8, 'big') +
            self.vote_type.encode() +
            int(self.timestamp).to_bytes(8, 'big') +
            self.nonce.to_bytes(4, 'big')
        )
    
    def verify_signature(self) -> bool:
        """Verify vote signature"""
        try:
            public_key = ed25519.Ed25519PublicKey.from_public_bytes(self.voter_pubkey)
            public_key.verify(self.signature, self.to_bytes())
            return True
        except (InvalidSignature, ValueError):
            return False
    
    def get_voter_id(self) -> str:
        """Get unique voter identifier"""
        return hashlib.sha256(self.voter_pubkey).hexdigest()[:16]


@dataclass
class ConsensusMetrics:
    """Consensus system metrics"""
    total_votes_received: int = 0
    valid_votes: int = 0
    invalid_votes: int = 0
    malicious_attempts: int = 0
    consensus_rounds: int = 0
    avg_consensus_time: float = 0.0
    sybil_attacks_detected: int = 0
    replay_attacks_blocked: int = 0


@dataclass
class NodeReputation:
    """Node reputation tracking"""
    node_id: str
    public_key: bytes
    valid_votes: int = 0
    invalid_votes: int = 0
    malicious_attempts: int = 0
    first_seen: float = field(default_factory=time.time)
    last_activity: float = field(default_factory=time.time)
    reputation_score: float = 1.0  # 0.0 = malicious, 1.0 = trusted
    
    def update_reputation(self, is_valid: bool, is_malicious: bool = False):
        """Update reputation based on behavior"""
        self.last_activity = time.time()
        
        if is_malicious:
            self.malicious_attempts += 1
            self.reputation_score = max(0.0, self.reputation_score - 0.3)
        elif is_valid:
            self.valid_votes += 1
            self.reputation_score = min(1.0, self.reputation_score + 0.01)
        else:
            self.invalid_votes += 1
            self.reputation_score = max(0.0, self.reputation_score - 0.05)
    
    def is_trusted(self) -> bool:
        """Check if node is trusted"""
        return self.reputation_score > 0.5
    
    def is_malicious(self) -> bool:
        """Check if node appears malicious"""
        return self.reputation_score < 0.2 or self.malicious_attempts > 5


class MaliciousNodeDetector:
    """Detect and handle malicious nodes"""
    
    def __init__(self):
        self.node_reputations: Dict[str, NodeReputation] = {}
        self.vote_history: Dict[str, List[Vote]] = defaultdict(list)  # tx_hash -> votes
        self.used_nonces: Dict[str, Set[int]] = defaultdict(set)  # voter_id -> nonces
        
    def add_vote(self, vote: Vote) -> Tuple[bool, str]:
        """
        Add vote and check for malicious behavior
        
        Returns:
            (is_valid, reason)
        """
        voter_id = vote.get_voter_id()
        
        # Update or create reputation
        if voter_id not in self.node_reputations:
            self.node_reputations[voter_id] = NodeReputation(
                node_id=voter_id,
                public_key=vote.voter_pubkey
            )
        
        reputation = self.node_reputations[voter_id]
        
        # Check if node is already flagged as malicious
        if reputation.is_malicious():
            return False, "Node flagged as malicious"
        
        # Check signature validity
        if not vote.verify_signature():
            reputation.update_reputation(is_valid=False, is_malicious=True)
            return False, "Invalid signature"
        
        # Check for replay attacks
        if vote.nonce in self.used_nonces[voter_id]:
            reputation.update_reputation(is_valid=False, is_malicious=True)
            return False, "Replay attack detected"
        
        # Check for double voting
        existing_votes = [v for v in self.vote_history[vote.tx_hash] if v.get_voter_id() == voter_id]
        if existing_votes:
            reputation.update_reputation(is_valid=False, is_malicious=True)
            return False, "Double voting detected"
        
        # Check timestamp validity (not too old or in future)
        now = time.time()
        if abs(vote.timestamp - now) > 300:  # 5 minutes tolerance
            reputation.update_reputation(is_valid=False)
            return False, "Invalid timestamp"
        
        # Vote appears valid
        self.used_nonces[voter_id].add(vote.nonce)
        self.vote_history[vote.tx_hash].append(vote)
        reputation.update_reputation(is_valid=True)
        
        return True, "Valid vote"
    
    def detect_sybil_attack(self, votes: List[Vote]) -> List[str]:
        """Detect potential Sybil attack patterns"""
        suspicious_nodes = []
        
        # Group votes by timing patterns
        time_groups = defaultdict(list)
        for vote in votes:
            time_bucket = int(vote.timestamp / 10) * 10  # 10-second buckets
            time_groups[time_bucket].append(vote)
        
        # Look for suspicious patterns
        for time_bucket, bucket_votes in time_groups.items():
            if len(bucket_votes) > 10:  # Many votes in short time
                voter_ids = [v.get_voter_id() for v in bucket_votes]
                
                # Check for new nodes voting together
                new_nodes = []
                for voter_id in voter_ids:
                    if voter_id in self.node_reputations:
                        rep = self.node_reputations[voter_id]
                        if time.time() - rep.first_seen < 3600:  # New node (< 1 hour)
                            new_nodes.append(voter_id)
                
                if len(new_nodes) > 5:  # Many new nodes voting together
                    suspicious_nodes.extend(new_nodes)
        
        return suspicious_nodes
    
    def get_trusted_votes(self, tx_hash: str) -> List[Vote]:
        """Get votes from trusted nodes only"""
        all_votes = self.vote_history[tx_hash]
        trusted_votes = []
        
        for vote in all_votes:
            voter_id = vote.get_voter_id()
            if voter_id in self.node_reputations:
                reputation = self.node_reputations[voter_id]
                if reputation.is_trusted():
                    trusted_votes.append(vote)
        
        return trusted_votes
    
    def cleanup_old_data(self):
        """Clean up old vote data"""
        now = time.time()
        cutoff = now - 86400  # 24 hours
        
        # Clean old vote history
        for tx_hash in list(self.vote_history.keys()):
            self.vote_history[tx_hash] = [
                v for v in self.vote_history[tx_hash] 
                if v.timestamp > cutoff
            ]
            if not self.vote_history[tx_hash]:
                del self.vote_history[tx_hash]
        
        # Clean old nonces
        for voter_id in self.used_nonces:
            # Keep recent nonces only (simple cleanup)
            if len(self.used_nonces[voter_id]) > 1000:
                # Keep most recent 500 nonces
                sorted_nonces = sorted(self.used_nonces[voter_id])
                self.used_nonces[voter_id] = set(sorted_nonces[-500:])


class SecureConsensusEngine:
    """Enhanced consensus engine with malicious node detection"""
    
    def __init__(self, min_votes: int = 3, consensus_threshold: float = 0.51):
        """
        Args:
            min_votes: Minimum votes required for consensus
            consensus_threshold: Threshold for consensus (0.51 = 51%)
        """
        self.min_votes = min_votes
        self.consensus_threshold = consensus_threshold
        self.detector = MaliciousNodeDetector()
        self.metrics = ConsensusMetrics()
        self.consensus_cache: Dict[str, Tuple[bool, float]] = {}  # tx_hash -> (result, timestamp)
        
    def add_vote(self, vote: Vote) -> bool:
        """Add a vote to the consensus system"""
        self.metrics.total_votes_received += 1
        
        is_valid, reason = self.detector.add_vote(vote)
        
        if is_valid:
            self.metrics.valid_votes += 1
            logger.debug(f"Valid vote added: {vote.get_voter_id()}")
        else:
            self.metrics.invalid_votes += 1
            if "malicious" in reason.lower() or "attack" in reason.lower():
                self.metrics.malicious_attempts += 1
            logger.warning(f"Invalid vote rejected: {reason}")
        
        return is_valid
    
    def check_consensus(self, tx_hash: str) -> Tuple[bool, Dict]:
        """
        Check if transaction has reached consensus
        
        Returns:
            (has_consensus, consensus_info)
        """
        start_time = time.time()
        
        # Check cache first
        if tx_hash in self.consensus_cache:
            cached_result, cached_time = self.consensus_cache[tx_hash]
            if time.time() - cached_time < 60:  # Cache for 1 minute
                return cached_result, {"cached": True}
        
        # Get trusted votes only
        trusted_votes = self.detector.get_trusted_votes(tx_hash)
        
        if len(trusted_votes) < self.min_votes:
            return False, {
                "reason": "Insufficient votes",
                "votes_received": len(trusted_votes),
                "min_required": self.min_votes
            }
        
        # Calculate weighted consensus
        total_weight = 0
        approve_weight = 0
        reject_weight = 0
        
        vote_breakdown = {"approve": 0, "reject": 0, "abstain": 0}
        
        for vote in trusted_votes:
            total_weight += vote.voter_balance
            vote_breakdown[vote.vote_type] += 1
            
            if vote.vote_type == "approve":
                approve_weight += vote.voter_balance
            elif vote.vote_type == "reject":
                reject_weight += vote.voter_balance
        
        if total_weight == 0:
            return False, {"reason": "No voting weight"}
        
        # Check for consensus
        approve_ratio = approve_weight / total_weight
        reject_ratio = reject_weight / total_weight
        
        has_consensus = False
        consensus_type = None
        
        if approve_ratio > self.consensus_threshold:
            has_consensus = True
            consensus_type = "approve"
        elif reject_ratio > self.consensus_threshold:
            has_consensus = True
            consensus_type = "reject"
        
        # Check for Sybil attacks
        suspicious_nodes = self.detector.detect_sybil_attack(trusted_votes)
        if suspicious_nodes:
            self.metrics.sybil_attacks_detected += 1
            logger.warning(f"Potential Sybil attack detected: {len(suspicious_nodes)} suspicious nodes")
        
        # Update metrics
        self.metrics.consensus_rounds += 1
        consensus_time = time.time() - start_time
        self.metrics.avg_consensus_time = (
            (self.metrics.avg_consensus_time * (self.metrics.consensus_rounds - 1) + consensus_time)
            / self.metrics.consensus_rounds
        )
        
        # Cache result
        self.consensus_cache[tx_hash] = (has_consensus, time.time())
        
        consensus_info = {
            "consensus_type": consensus_type,
            "approve_ratio": approve_ratio,
            "reject_ratio": reject_ratio,
            "total_weight": total_weight,
            "vote_breakdown": vote_breakdown,
            "trusted_votes": len(trusted_votes),
            "suspicious_nodes": len(suspicious_nodes),
            "consensus_time_ms": consensus_time * 1000
        }
        
        return has_consensus, consensus_info
    
    def simulate_51_percent_attack(self, tx_hash: str, attacker_balance: int, total_supply: int) -> Dict:
        """
        Simulate a 51% attack scenario for testing
        
        Returns:
            Attack simulation results
        """
        attack_ratio = attacker_balance / total_supply
        
        if attack_ratio <= 0.51:
            return {
                "attack_possible": False,
                "reason": "Insufficient balance for 51% attack",
                "attacker_ratio": attack_ratio,
                "required_ratio": 0.51
            }
        
        # Simulate malicious votes
        malicious_votes = []
        for i in range(10):  # Create 10 malicious votes
            # Generate fake keypair for simulation
            private_key = ed25519.Ed25519PrivateKey.generate()
            public_key = private_key.public_key()
            
            vote_data = Vote(
                tx_hash=tx_hash,
                voter_pubkey=public_key.public_bytes(
                    encoding=serialization.Encoding.Raw,
                    format=serialization.PublicFormat.Raw
                ),
                voter_balance=attacker_balance // 10,  # Split balance across fake nodes
                vote_type="approve",
                timestamp=time.time(),
                signature=b"fake_signature",  # This will fail verification
                nonce=i
            )
            
            malicious_votes.append(vote_data)
        
        # Try to add malicious votes
        accepted_votes = 0
        for vote in malicious_votes:
            if self.add_vote(vote):
                accepted_votes += 1
        
        # Check if attack succeeded
        has_consensus, info = self.check_consensus(tx_hash)
        
        return {
            "attack_possible": True,
            "attacker_ratio": attack_ratio,
            "malicious_votes_created": len(malicious_votes),
            "malicious_votes_accepted": accepted_votes,
            "attack_succeeded": has_consensus and info.get("consensus_type") == "approve",
            "consensus_info": info,
            "defense_effectiveness": 1.0 - (accepted_votes / len(malicious_votes))
        }
    
    def get_security_metrics(self) -> Dict:
        """Get comprehensive security metrics"""
        total_attempts = self.metrics.malicious_attempts + self.metrics.valid_votes
        
        return {
            "consensus_metrics": {
                "total_votes_received": self.metrics.total_votes_received,
                "valid_votes": self.metrics.valid_votes,
                "invalid_votes": self.metrics.invalid_votes,
                "malicious_attempts": self.metrics.malicious_attempts,
                "consensus_rounds": self.metrics.consensus_rounds,
                "avg_consensus_time_ms": self.metrics.avg_consensus_time * 1000,
                "sybil_attacks_detected": self.metrics.sybil_attacks_detected,
                "replay_attacks_blocked": self.metrics.replay_attacks_blocked
            },
            "security_effectiveness": {
                "malicious_rejection_rate": (
                    self.metrics.malicious_attempts / max(1, total_attempts)
                ),
                "trusted_nodes": len([
                    r for r in self.detector.node_reputations.values() 
                    if r.is_trusted()
                ]),
                "malicious_nodes": len([
                    r for r in self.detector.node_reputations.values() 
                    if r.is_malicious()
                ]),
                "avg_node_reputation": (
                    sum(r.reputation_score for r in self.detector.node_reputations.values()) 
                    / max(1, len(self.detector.node_reputations))
                )
            }
        }
    
    def cleanup(self):
        """Clean up old data"""
        self.detector.cleanup_old_data()
        
        # Clean old consensus cache
        now = time.time()
        expired_keys = [
            tx_hash for tx_hash, (_, timestamp) in self.consensus_cache.items()
            if now - timestamp > 3600  # 1 hour
        ]
        for key in expired_keys:
            del self.consensus_cache[key]


# Helper functions for creating signed votes
def create_signed_vote(
    tx_hash: str,
    private_key: ed25519.Ed25519PrivateKey,
    voter_balance: int,
    vote_type: str = "approve",
    nonce: int = None
) -> Vote:
    """Create a cryptographically signed vote"""
    if nonce is None:
        nonce = int(time.time() * 1000) % (2**32)  # Use timestamp as nonce
    
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    
    vote = Vote(
        tx_hash=tx_hash,
        voter_pubkey=public_key_bytes,
        voter_balance=voter_balance,
        vote_type=vote_type,
        timestamp=time.time(),
        signature=b"",  # Will be filled below
        nonce=nonce
    )
    
    # Sign the vote
    vote_bytes = vote.to_bytes()
    signature = private_key.sign(vote_bytes)
    vote.signature = signature
    
    return vote


def generate_test_keypair() -> ed25519.Ed25519PrivateKey:
    """Generate a test keypair for voting"""
    return ed25519.Ed25519PrivateKey.generate()
