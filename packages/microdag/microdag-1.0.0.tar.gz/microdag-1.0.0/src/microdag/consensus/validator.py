"""
Consensus validation - transaction and DAG validation rules.
"""
from typing import Set
from ..core.transaction import Transaction
from ..core.dag import DAG
from .pow import ProofOfWork

class ConsensusValidator:
    """Consensus validation rules"""
    
    def __init__(self, pow_validator: ProofOfWork = None):
        self.pow = pow_validator or ProofOfWork()
    
    def validate_transaction_consensus(self, transaction: Transaction, dag: DAG) -> bool:
        """Validate transaction meets consensus rules"""
        # Check PoW
        if not self.pow.validate_transaction_pow(transaction):
            return False
        
        # Check parents exist in DAG
        parents = {transaction.parent1, transaction.parent2}
        for parent in parents:
            if parent != b'\x00' * 32 and not dag.has_transaction(parent):
                return False
        
        # Check no double spending (simplified)
        if not self._check_no_double_spend(transaction, dag):
            return False
        
        return True
    
    def validate_dag_consensus(self, dag: DAG) -> bool:
        """Validate entire DAG meets consensus rules"""
        # Check all tips are valid
        tips = dag.get_tips()
        if len(tips) == 0:
            return True  # Empty DAG is valid
        
        # Check DAG structure integrity
        for tip in tips:
            if not self._validate_branch(tip, dag, set()):
                return False
        
        return True
    
    def _check_no_double_spend(self, transaction: Transaction, dag: DAG) -> bool:
        """Check transaction doesn't double spend (simplified)"""
        # In a real implementation, this would check if the same UTXO
        # is being spent in multiple transactions
        # For ultra-lightweight implementation, we skip this check
        return True
    
    def _validate_branch(self, tx_hash: bytes, dag: DAG, visited: Set[bytes]) -> bool:
        """Validate a branch of the DAG recursively"""
        if tx_hash in visited:
            return False  # Cycle detected
        
        if tx_hash == b'\x00' * 32:
            return True  # Genesis reference
        
        if not dag.has_transaction(tx_hash):
            return False  # Transaction doesn't exist
        
        visited.add(tx_hash)
        
        # Validate parents recursively
        parents = dag.get_parents(tx_hash)
        for parent in parents:
            if not self._validate_branch(parent, dag, visited.copy()):
                return False
        
        return True
    
    def get_consensus_stats(self, dag: DAG) -> dict:
        """Get consensus validation statistics"""
        stats = dag.get_stats()
        
        # Add consensus-specific stats
        stats.update({
            'pow_difficulty': self.pow.get_difficulty(),
            'consensus_valid': self.validate_dag_consensus(dag),
            'estimated_work_time': self.pow.estimate_work_time()
        })
        
        return stats
