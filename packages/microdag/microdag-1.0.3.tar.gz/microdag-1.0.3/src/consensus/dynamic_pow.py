"""
Dynamic Proof-of-Work Difficulty Adjustment
Automatically adjusts PoW difficulty based on network load and spam detection
"""

import time
import hashlib
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from collections import deque
import statistics
import threading

logger = logging.getLogger(__name__)


@dataclass
class NetworkMetrics:
    """Network performance metrics for PoW adjustment"""
    timestamp: float
    tps: float
    pending_transactions: int
    spam_detected: int
    legitimate_transactions: int
    avg_confirmation_time: float
    node_count: int


@dataclass
class PoWDifficultyConfig:
    """PoW difficulty configuration"""
    base_difficulty: int = 4  # Base number of leading zeros required
    min_difficulty: int = 2   # Minimum difficulty (for low load)
    max_difficulty: int = 8   # Maximum difficulty (for high spam)
    target_tps: int = 500     # Target TPS threshold
    adjustment_window: int = 60  # Seconds to consider for adjustment
    spam_threshold: float = 0.3  # 30% spam ratio triggers adjustment
    emergency_threshold: float = 0.7  # 70% spam ratio triggers emergency mode


class DynamicPoWAdjuster:
    """Dynamically adjusts PoW difficulty based on network conditions"""
    
    def __init__(self, config: PoWDifficultyConfig = None):
        self.config = config or PoWDifficultyConfig()
        self.current_difficulty = self.config.base_difficulty
        self.metrics_history = deque(maxlen=1000)  # Keep last 1000 metrics
        self.last_adjustment = time.time()
        self.adjustment_lock = threading.Lock()
        
        # Emergency mode tracking
        self.emergency_mode = False
        self.emergency_start_time = None
        
        # Performance tracking
        self.tps_samples = deque(maxlen=100)
        self.spam_ratio_samples = deque(maxlen=100)
        
        logger.info(f"Dynamic PoW initialized with base difficulty {self.current_difficulty}")
    
    def add_network_metrics(self, metrics: NetworkMetrics):
        """Add new network metrics for analysis"""
        with self.adjustment_lock:
            self.metrics_history.append(metrics)
            
            # Update rolling samples
            self.tps_samples.append(metrics.tps)
            
            total_txs = metrics.spam_detected + metrics.legitimate_transactions
            spam_ratio = metrics.spam_detected / max(1, total_txs)
            self.spam_ratio_samples.append(spam_ratio)
            
            # Check if adjustment is needed
            self._check_adjustment_needed(metrics)
    
    def _check_adjustment_needed(self, current_metrics: NetworkMetrics):
        """Check if PoW difficulty adjustment is needed"""
        now = time.time()
        
        # Don't adjust too frequently (minimum 30 seconds between adjustments)
        if now - self.last_adjustment < 30:
            # Still check for emergency mode even if not adjusting
            total_txs = current_metrics.spam_detected + current_metrics.legitimate_transactions
            spam_ratio = current_metrics.spam_detected / max(1, total_txs)
            if spam_ratio >= self.config.emergency_threshold and not self.emergency_mode:
                logger.warning(f"Entering emergency mode: {spam_ratio:.1%} spam detected")
                self.emergency_mode = True
                self.emergency_start_time = time.time()
            return
        
        # Get recent metrics for analysis
        recent_metrics = [m for m in self.metrics_history 
                         if now - m.timestamp <= self.config.adjustment_window]
        
        if len(recent_metrics) < 5:  # Need sufficient data
            return
        
        # Calculate average metrics over adjustment window
        avg_tps = statistics.mean([m.tps for m in recent_metrics])
        avg_spam_ratio = statistics.mean([
            m.spam_detected / max(1, m.spam_detected + m.legitimate_transactions)
            for m in recent_metrics
        ])
        avg_confirmation_time = statistics.mean([m.avg_confirmation_time for m in recent_metrics])
        
        logger.debug(f"PoW adjustment analysis: TPS={avg_tps:.1f}, Spam={avg_spam_ratio:.1%}, "
                    f"Confirmation={avg_confirmation_time:.1f}ms")
        
        # Determine if adjustment is needed
        new_difficulty = self._calculate_optimal_difficulty(
            avg_tps, avg_spam_ratio, avg_confirmation_time, current_metrics.node_count
        )
        
        if new_difficulty != self.current_difficulty:
            self._adjust_difficulty(new_difficulty, avg_tps, avg_spam_ratio)
    
    def _calculate_optimal_difficulty(self, avg_tps: float, spam_ratio: float, 
                                    confirmation_time: float, node_count: int) -> int:
        """Calculate optimal PoW difficulty based on network conditions"""
        
        # Start with current difficulty
        optimal_difficulty = self.current_difficulty
        
        # Emergency mode: Very high spam ratio
        if spam_ratio >= self.config.emergency_threshold:
            if not self.emergency_mode:
                logger.warning(f"Entering emergency mode: {spam_ratio:.1%} spam detected")
                self.emergency_mode = True
                self.emergency_start_time = time.time()
            
            # Aggressive difficulty increase in emergency mode
            optimal_difficulty = min(self.config.max_difficulty, self.current_difficulty + 2)
        
        # High spam mode: Moderate spam ratio
        elif spam_ratio >= self.config.spam_threshold:
            if self.emergency_mode:
                logger.info("Exiting emergency mode")
                self.emergency_mode = False
            
            # Moderate difficulty increase for high spam
            optimal_difficulty = min(self.config.max_difficulty, self.current_difficulty + 1)
        
        # Low TPS mode: Network overloaded
        elif avg_tps < self.config.target_tps:
            # Increase difficulty to reduce load
            optimal_difficulty = min(self.config.max_difficulty, self.current_difficulty + 1)
        
        # Normal/low load mode
        else:
            if self.emergency_mode:
                logger.info("Exiting emergency mode - network stabilized")
                self.emergency_mode = False
            
            # Consider reducing difficulty if load is very low
            if avg_tps > self.config.target_tps * 1.5 and spam_ratio < 0.1:
                optimal_difficulty = max(self.config.min_difficulty, self.current_difficulty - 1)
        
        # Additional constraints based on node count
        if node_count < 10:  # Small network
            optimal_difficulty = max(self.config.min_difficulty, 
                                   min(optimal_difficulty, self.config.base_difficulty))
        elif node_count > 100:  # Large network
            optimal_difficulty = min(self.config.max_difficulty, optimal_difficulty)
        
        return optimal_difficulty
    
    def _adjust_difficulty(self, new_difficulty: int, avg_tps: float, spam_ratio: float):
        """Adjust PoW difficulty"""
        old_difficulty = self.current_difficulty
        self.current_difficulty = new_difficulty
        self.last_adjustment = time.time()
        
        direction = "increased" if new_difficulty > old_difficulty else "decreased"
        
        logger.info(f"PoW difficulty {direction} from {old_difficulty} to {new_difficulty}")
        logger.info(f"Trigger conditions: TPS={avg_tps:.1f}, Spam={spam_ratio:.1%}")
        
        # Emit metrics for monitoring
        self._emit_adjustment_metrics(old_difficulty, new_difficulty, avg_tps, spam_ratio)
    
    def _emit_adjustment_metrics(self, old_difficulty: int, new_difficulty: int, 
                               avg_tps: float, spam_ratio: float):
        """Emit metrics for monitoring systems"""
        adjustment_data = {
            'timestamp': time.time(),
            'old_difficulty': old_difficulty,
            'new_difficulty': new_difficulty,
            'trigger_tps': avg_tps,
            'trigger_spam_ratio': spam_ratio,
            'emergency_mode': self.emergency_mode
        }
        
        # In a real system, this would be sent to monitoring/alerting
        logger.info(f"PoW adjustment metrics: {adjustment_data}")
    
    def get_current_difficulty(self) -> int:
        """Get current PoW difficulty"""
        return self.current_difficulty
    
    def is_emergency_mode(self) -> bool:
        """Check if system is in emergency mode"""
        return self.emergency_mode
    
    def get_adjustment_status(self) -> Dict:
        """Get current adjustment status and metrics"""
        recent_tps = list(self.tps_samples)[-10:] if self.tps_samples else []
        recent_spam = list(self.spam_ratio_samples)[-10:] if self.spam_ratio_samples else []
        
        return {
            'current_difficulty': self.current_difficulty,
            'base_difficulty': self.config.base_difficulty,
            'emergency_mode': self.emergency_mode,
            'last_adjustment': self.last_adjustment,
            'recent_avg_tps': statistics.mean(recent_tps) if recent_tps else 0,
            'recent_avg_spam_ratio': statistics.mean(recent_spam) if recent_spam else 0,
            'target_tps': self.config.target_tps,
            'metrics_count': len(self.metrics_history)
        }
    
    def force_difficulty(self, difficulty: int, reason: str = "Manual override"):
        """Force specific difficulty (for testing or manual intervention)"""
        if difficulty < self.config.min_difficulty or difficulty > self.config.max_difficulty:
            raise ValueError(f"Difficulty must be between {self.config.min_difficulty} and {self.config.max_difficulty}")
        
        old_difficulty = self.current_difficulty
        self.current_difficulty = difficulty
        self.last_adjustment = time.time()
        
        logger.warning(f"PoW difficulty manually set from {old_difficulty} to {difficulty}: {reason}")


class ProofOfWorkValidator:
    """Validates PoW solutions with dynamic difficulty"""
    
    def __init__(self, adjuster: DynamicPoWAdjuster):
        self.adjuster = adjuster
    
    def generate_challenge(self, transaction_data: str) -> Tuple[str, int]:
        """Generate PoW challenge for transaction"""
        difficulty = self.adjuster.get_current_difficulty()
        challenge = hashlib.sha256(f"{transaction_data}{time.time()}".encode()).hexdigest()
        return challenge, difficulty
    
    def validate_solution(self, transaction_data: str, nonce: int, expected_difficulty: int = None) -> bool:
        """Validate PoW solution"""
        if expected_difficulty is None:
            expected_difficulty = self.adjuster.get_current_difficulty()
        
        # Create hash with transaction data and nonce
        hash_input = f"{transaction_data}{nonce}".encode()
        solution_hash = hashlib.sha256(hash_input).hexdigest()
        
        # Check if solution meets difficulty requirement
        required_zeros = '0' * expected_difficulty
        is_valid = solution_hash.startswith(required_zeros)
        
        if is_valid:
            logger.debug(f"Valid PoW solution: {solution_hash} (difficulty {expected_difficulty})")
        else:
            logger.debug(f"Invalid PoW solution: {solution_hash} (required {expected_difficulty} zeros)")
        
        return is_valid
    
    def estimate_work_time(self, difficulty: int) -> float:
        """Estimate average time to solve PoW at given difficulty"""
        # Rough estimate: each additional zero increases work by factor of 16
        base_time = 0.1  # 100ms for difficulty 1
        return base_time * (16 ** (difficulty - 1))


class SpamDetectionIntegration:
    """Integrates spam detection with dynamic PoW adjustment"""
    
    def __init__(self, pow_adjuster: DynamicPoWAdjuster):
        self.pow_adjuster = pow_adjuster
        self.transaction_stats = {
            'total_processed': 0,
            'spam_detected': 0,
            'legitimate_confirmed': 0,
            'pow_failures': 0
        }
        self.last_metrics_update = time.time()
    
    def process_transaction(self, transaction: Dict, is_spam: bool, 
                          confirmation_time_ms: float, node_count: int) -> bool:
        """Process transaction and update metrics for PoW adjustment"""
        
        # Update transaction statistics
        self.transaction_stats['total_processed'] += 1
        
        if is_spam:
            self.transaction_stats['spam_detected'] += 1
        else:
            self.transaction_stats['legitimate_confirmed'] += 1
        
        # Update metrics every 10 seconds
        now = time.time()
        if now - self.last_metrics_update >= 10:
            self._update_pow_metrics(now, node_count)
            self.last_metrics_update = now
        
        return not is_spam  # Return whether transaction should be processed
    
    def _update_pow_metrics(self, timestamp: float, node_count: int):
        """Update PoW adjuster with current network metrics"""
        
        # Calculate TPS over last 10 seconds
        time_window = 10.0
        tps = self.transaction_stats['total_processed'] / time_window
        
        # Create metrics object
        metrics = NetworkMetrics(
            timestamp=timestamp,
            tps=tps,
            pending_transactions=0,  # Would be actual pending count
            spam_detected=self.transaction_stats['spam_detected'],
            legitimate_transactions=self.transaction_stats['legitimate_confirmed'],
            avg_confirmation_time=100.0,  # Would be actual average
            node_count=node_count
        )
        
        # Send to PoW adjuster
        self.pow_adjuster.add_network_metrics(metrics)
        
        # Reset counters for next window
        self.transaction_stats = {
            'total_processed': 0,
            'spam_detected': 0,
            'legitimate_confirmed': 0,
            'pow_failures': 0
        }
    
    def get_current_pow_requirement(self) -> Dict:
        """Get current PoW requirements for new transactions"""
        return {
            'difficulty': self.pow_adjuster.get_current_difficulty(),
            'emergency_mode': self.pow_adjuster.is_emergency_mode(),
            'estimated_solve_time': ProofOfWorkValidator(self.pow_adjuster).estimate_work_time(
                self.pow_adjuster.get_current_difficulty()
            )
        }


# Helper functions for easy integration
def create_dynamic_pow_system(target_tps: int = 500, max_difficulty: int = 8) -> Tuple[DynamicPoWAdjuster, ProofOfWorkValidator, SpamDetectionIntegration]:
    """Create complete dynamic PoW system"""
    
    config = PoWDifficultyConfig(
        target_tps=target_tps,
        max_difficulty=max_difficulty
    )
    
    adjuster = DynamicPoWAdjuster(config)
    validator = ProofOfWorkValidator(adjuster)
    integration = SpamDetectionIntegration(adjuster)
    
    return adjuster, validator, integration


def simulate_pow_adjustment(spam_ratio: float, tps: float, node_count: int = 50) -> Dict:
    """Simulate PoW adjustment for given conditions"""
    
    adjuster, validator, integration = create_dynamic_pow_system()
    
    # Simulate metrics
    metrics = NetworkMetrics(
        timestamp=time.time(),
        tps=tps,
        pending_transactions=100,
        spam_detected=int(1000 * spam_ratio),
        legitimate_transactions=int(1000 * (1 - spam_ratio)),
        avg_confirmation_time=150.0,
        node_count=node_count
    )
    
    old_difficulty = adjuster.get_current_difficulty()
    adjuster.add_network_metrics(metrics)
    new_difficulty = adjuster.get_current_difficulty()
    
    return {
        'old_difficulty': old_difficulty,
        'new_difficulty': new_difficulty,
        'adjustment_made': old_difficulty != new_difficulty,
        'emergency_mode': adjuster.is_emergency_mode(),
        'estimated_solve_time': validator.estimate_work_time(new_difficulty)
    }
