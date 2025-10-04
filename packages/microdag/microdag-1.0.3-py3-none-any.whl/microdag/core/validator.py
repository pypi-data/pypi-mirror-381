"""
Transaction validation - lightweight validation logic.
"""
from typing import Set
from .transaction import Transaction

class Validator:
    """Ultra-lightweight transaction validator"""
    
    @staticmethod
    def validate_transaction(tx: Transaction) -> bool:
        """Validate transaction structure and basic rules"""
        # Check transaction size
        if len(tx.pack()) != 208:
            return False
        
        # Check amount is positive
        if tx.amount <= 0:
            return False
        
        # Check addresses are not zero (except for coinbase)
        if tx.from_addr == b'\x00' * 32 and tx.to_addr == b'\x00' * 32:
            return False
        
        # Check timestamp is reasonable (within 1 hour)
        import time
        current_time = int(time.time())
        if abs(tx.timestamp - current_time) > 3600:
            return False
        
        return True
    
    @staticmethod
    def validate_dag_structure(tx_hash: bytes, parents: Set[bytes], dag) -> bool:
        """Validate DAG structure rules"""
        # Check parents exist in DAG (except for genesis)
        if parents:
            for parent in parents:
                if parent != b'\x00' * 32 and not dag.has_transaction(parent):
                    return False
        
        # Check no cycles (simplified check)
        if tx_hash in parents:
            return False
        
        # Check maximum 2 parents
        if len(parents) > 2:
            return False
        
        return True
    
    @staticmethod
    def validate_balance(tx: Transaction, get_balance_func) -> bool:
        """Validate sender has sufficient balance"""
        if tx.from_addr == b'\x00' * 32:  # Coinbase transaction
            return True
        
        balance = get_balance_func(tx.from_addr)
        return balance >= tx.amount
