"""
Enhanced Spam Protection for MicroDAG
Multi-layered defense against spam attacks in feeless systems
"""

import time
import hashlib
import struct
from collections import defaultdict
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class SpamMetrics:
    """Spam protection metrics"""
    total_requests: int = 0
    blocked_requests: int = 0
    pow_challenges: int = 0
    valid_transactions: int = 0
    spam_score: float = 0.0


class ProofOfWork:
    """Light Proof of Work for spam prevention"""
    
    def __init__(self, difficulty: int = 4):
        """
        Args:
            difficulty: Number of leading zeros required (4 = ~1ms on modern CPU)
        """
        self.difficulty = difficulty
        self.target = 2 ** (256 - difficulty * 4)
    
    def generate_challenge(self, data: bytes) -> str:
        """Generate PoW challenge for transaction data"""
        timestamp = int(time.time())
        challenge_data = data + struct.pack('<Q', timestamp)
        return hashlib.sha256(challenge_data).hexdigest()[:16]
    
    def verify_work(self, data: bytes, nonce: int, challenge: str) -> bool:
        """Verify proof of work solution"""
        work_data = data + struct.pack('<Q', nonce) + challenge.encode()
        hash_result = hashlib.sha256(work_data).digest()
        hash_int = int.from_bytes(hash_result, 'big')
        return hash_int < self.target
    
    def estimate_work_time(self) -> float:
        """Estimate time to solve PoW (milliseconds)"""
        return (2 ** (self.difficulty * 4)) / (1000000)  # Assume 1M hashes/sec


class AdaptiveRateLimiter:
    """Adaptive rate limiter that adjusts based on network load"""
    
    def __init__(self, base_limit: int = 10, max_limit: int = 100):
        self.base_limit = base_limit
        self.max_limit = max_limit
        self.current_limit = base_limit
        self.requests: Dict[str, List[float]] = defaultdict(list)
        self.network_load = 0.0
        self.last_adjustment = time.time()
    
    def update_network_load(self, tps: float, target_tps: float = 1000):
        """Update rate limits based on network load"""
        self.network_load = min(tps / target_tps, 1.0)
        
        # Adjust limits every 10 seconds
        if time.time() - self.last_adjustment > 10:
            if self.network_load > 0.8:  # High load
                self.current_limit = max(self.base_limit // 2, 5)
            elif self.network_load < 0.3:  # Low load
                self.current_limit = min(self.base_limit * 2, self.max_limit)
            else:  # Normal load
                self.current_limit = self.base_limit
            
            self.last_adjustment = time.time()
            logger.info(f"Adjusted rate limit to {self.current_limit} req/s (load: {self.network_load:.1%})")
    
    def is_allowed(self, ip: str) -> bool:
        """Check if request is allowed under current limits"""
        now = time.time()
        
        # Clean old requests
        self.requests[ip] = [t for t in self.requests[ip] if now - t < 1.0]
        
        # Check current limit
        if len(self.requests[ip]) < self.current_limit:
            self.requests[ip].append(now)
            return True
        
        return False


class EnhancedSpamProtection:
    """Multi-layered spam protection system"""
    
    def __init__(self, 
                 rate_limit: int = 10,
                 pow_difficulty: int = 4,
                 reputation_enabled: bool = True):
        """
        Args:
            rate_limit: Base requests per second per IP
            pow_difficulty: PoW difficulty (4 = ~1ms)
            reputation_enabled: Enable IP reputation tracking
        """
        self.rate_limiter = AdaptiveRateLimiter(rate_limit)
        self.pow = ProofOfWork(pow_difficulty)
        self.reputation_enabled = reputation_enabled
        
        # Reputation system
        self.ip_reputation: Dict[str, float] = defaultdict(lambda: 0.5)  # 0=bad, 1=good
        self.ip_history: Dict[str, List[Tuple[float, str]]] = defaultdict(list)  # (timestamp, action)
        
        # Metrics
        self.metrics = SpamMetrics()
        
        # Challenge cache
        self.active_challenges: Dict[str, Tuple[str, float]] = {}  # ip -> (challenge, timestamp)
    
    def should_challenge_pow(self, ip: str, tx_data: bytes) -> Optional[str]:
        """Determine if transaction should be challenged with PoW"""
        self.metrics.total_requests += 1
        
        # Always allow if rate limit not exceeded and good reputation
        if self.rate_limiter.is_allowed(ip):
            if not self.reputation_enabled or self.ip_reputation[ip] > 0.7:
                self.metrics.valid_transactions += 1
                self._update_reputation(ip, 'valid_tx')
                return None
        
        # Rate limited or bad reputation - require PoW
        challenge = self.pow.generate_challenge(tx_data)
        self.active_challenges[ip] = (challenge, time.time())
        self.metrics.pow_challenges += 1
        
        logger.info(f"PoW challenge issued to {ip} (reputation: {self.ip_reputation[ip]:.2f})")
        return challenge
    
    def verify_pow_solution(self, ip: str, tx_data: bytes, nonce: int) -> bool:
        """Verify PoW solution and process transaction"""
        if ip not in self.active_challenges:
            return False
        
        challenge, issued_time = self.active_challenges[ip]
        
        # Check if challenge expired (5 minutes)
        if time.time() - issued_time > 300:
            del self.active_challenges[ip]
            return False
        
        # Verify work
        if self.pow.verify_work(tx_data, nonce, challenge):
            del self.active_challenges[ip]
            self.metrics.valid_transactions += 1
            self._update_reputation(ip, 'solved_pow')
            logger.info(f"PoW solution verified for {ip}")
            return True
        
        # Invalid solution - penalize reputation
        self._update_reputation(ip, 'invalid_pow')
        self.metrics.blocked_requests += 1
        return False
    
    def _update_reputation(self, ip: str, action: str):
        """Update IP reputation based on actions"""
        if not self.reputation_enabled:
            return
        
        now = time.time()
        self.ip_history[ip].append((now, action))
        
        # Keep only last 24 hours
        self.ip_history[ip] = [(t, a) for t, a in self.ip_history[ip] if now - t < 86400]
        
        # Calculate reputation score
        recent_actions = [a for t, a in self.ip_history[ip] if now - t < 3600]  # Last hour
        
        if not recent_actions:
            return
        
        score_changes = {
            'valid_tx': +0.1,
            'solved_pow': +0.05,
            'invalid_pow': -0.2,
            'spam_detected': -0.3
        }
        
        # Apply changes
        for action in recent_actions:
            if action in score_changes:
                self.ip_reputation[ip] += score_changes[action]
        
        # Clamp between 0 and 1
        self.ip_reputation[ip] = max(0.0, min(1.0, self.ip_reputation[ip]))
    
    def detect_spam_patterns(self, ip: str, tx_data: bytes) -> bool:
        """Detect spam patterns in transactions"""
        # Check for duplicate transactions
        tx_hash = hashlib.sha256(tx_data).hexdigest()
        recent_hashes = [h for t, h in getattr(self, '_recent_hashes', {}).get(ip, []) 
                        if time.time() - t < 60]
        
        if tx_hash in recent_hashes:
            self._update_reputation(ip, 'spam_detected')
            return True
        
        # Store recent hash
        if not hasattr(self, '_recent_hashes'):
            self._recent_hashes = defaultdict(list)
        
        self._recent_hashes[ip].append((time.time(), tx_hash))
        
        # Keep only last 100 hashes per IP
        self._recent_hashes[ip] = self._recent_hashes[ip][-100:]
        
        return False
    
    def update_network_metrics(self, tps: float, memory_usage: float):
        """Update protection based on network metrics"""
        self.rate_limiter.update_network_load(tps)
        
        # Calculate overall spam score
        if self.metrics.total_requests > 0:
            self.metrics.spam_score = (
                self.metrics.blocked_requests + self.metrics.pow_challenges
            ) / self.metrics.total_requests
    
    def get_protection_stats(self) -> Dict:
        """Get comprehensive protection statistics"""
        return {
            'metrics': {
                'total_requests': self.metrics.total_requests,
                'blocked_requests': self.metrics.blocked_requests,
                'pow_challenges': self.metrics.pow_challenges,
                'valid_transactions': self.metrics.valid_transactions,
                'spam_score': self.metrics.spam_score
            },
            'rate_limiter': {
                'current_limit': self.rate_limiter.current_limit,
                'network_load': self.rate_limiter.network_load,
                'tracked_ips': len(self.rate_limiter.requests)
            },
            'pow': {
                'difficulty': self.pow.difficulty,
                'estimated_work_time_ms': self.pow.estimate_work_time(),
                'active_challenges': len(self.active_challenges)
            },
            'reputation': {
                'enabled': self.reputation_enabled,
                'tracked_ips': len(self.ip_reputation),
                'avg_reputation': sum(self.ip_reputation.values()) / len(self.ip_reputation) if self.ip_reputation else 0.5
            }
        }
    
    def cleanup(self):
        """Clean up old data"""
        now = time.time()
        
        # Clean expired challenges
        expired = [ip for ip, (_, t) in self.active_challenges.items() if now - t > 300]
        for ip in expired:
            del self.active_challenges[ip]
        
        # Clean old reputation data
        for ip in list(self.ip_history.keys()):
            self.ip_history[ip] = [(t, a) for t, a in self.ip_history[ip] if now - t < 86400]
            if not self.ip_history[ip]:
                del self.ip_history[ip]
