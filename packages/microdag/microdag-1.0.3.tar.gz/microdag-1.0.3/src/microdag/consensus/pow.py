"""
Proof of Work consensus - minimal PoW for spam protection.
"""
import struct
from ..utils.hash import blake2b_hash
from ..core.transaction import Transaction

class ProofOfWork:
    """Ultra-lightweight Proof of Work for spam protection"""
    
    def __init__(self, difficulty: int = 1):
        """Initialize with difficulty level (number of leading zeros)"""
        self.difficulty = difficulty
        self.target = b'\x00' * difficulty + b'\xff' * (32 - difficulty)
    
    def mine(self, transaction: Transaction) -> bytes:
        """Mine transaction with minimal PoW"""
        nonce = 0
        while True:
            # Create candidate hash with nonce
            nonce_bytes = struct.pack('!Q', nonce)
            candidate_data = transaction.pack()[:-32] + nonce_bytes + b'\x00' * 24
            candidate_hash = blake2b_hash(candidate_data)
            
            if self.validate_hash(candidate_hash):
                # Update transaction with valid nonce in signature field
                transaction.signature = nonce_bytes + b'\x00' * 56
                transaction.hash = candidate_hash
                return candidate_hash
            
            nonce += 1
            
            # Prevent infinite loops in testing
            if nonce > 1000000:
                break
        
        return transaction.hash
    
    def validate_hash(self, hash_bytes: bytes) -> bool:
        """Validate hash meets difficulty requirement"""
        return hash_bytes[:self.difficulty] == b'\x00' * self.difficulty
    
    def validate_transaction_pow(self, transaction: Transaction) -> bool:
        """Validate transaction has valid PoW"""
        return self.validate_hash(transaction.hash)
    
    def set_difficulty(self, difficulty: int) -> None:
        """Adjust difficulty level"""
        self.difficulty = max(0, min(difficulty, 4))  # Limit to reasonable range
        self.target = b'\x00' * self.difficulty + b'\xff' * (32 - self.difficulty)
    
    def get_difficulty(self) -> int:
        """Get current difficulty"""
        return self.difficulty
    
    def estimate_work_time(self, hash_rate: int = 1000) -> float:
        """Estimate time to find valid hash at given hash rate"""
        expected_attempts = 256 ** self.difficulty
        return expected_attempts / hash_rate
