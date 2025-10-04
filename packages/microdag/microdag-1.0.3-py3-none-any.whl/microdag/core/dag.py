"""
Ultra-lightweight DAG implementation - core blockchain structure.

This module provides a high-performance, memory-efficient implementation
of a Directed Acyclic Graph for blockchain transactions.
"""
import struct
from typing import Dict, Set, Optional, Tuple
from ..utils.hash import blake2b_hash


class DAG:
    """
    Ultra-lightweight Directed Acyclic Graph for transactions.
    
    This implementation uses packed binary data structures to minimize
    memory usage while maintaining full DAG functionality.
    
    Attributes:
        _nodes: Dictionary mapping transaction hashes to packed parent data
        _tips: Set of current DAG tip hashes
        _count: Total number of transactions in the DAG
    """
    
    def __init__(self) -> None:
        """Initialize empty DAG with optimized data structures."""
        self._nodes: Dict[bytes, bytes] = {}  # hash -> packed_parents
        self._tips: Set[bytes] = set()
        self._count: int = 0
    
    def add_transaction(self, tx_hash: bytes, parents: Optional[Set[bytes]] = None) -> bool:
        """
        Add transaction to DAG with parent relationships.
        
        Args:
            tx_hash: 32-byte hash of the transaction
            parents: Set of parent transaction hashes (max 2 for efficiency)
            
        Returns:
            bool: True if transaction was added successfully
            
        Raises:
            ValueError: If tx_hash is invalid or already exists
        """
        if not isinstance(tx_hash, bytes) or len(tx_hash) != 32:
            raise ValueError("tx_hash must be 32 bytes")
            
        if tx_hash in self._nodes:
            raise ValueError("Transaction already exists in DAG")
        
        if parents is None:
            parents = set()
        
        # Validate parents
        for parent in parents:
            if not isinstance(parent, bytes) or len(parent) != 32:
                raise ValueError("All parents must be 32-byte hashes")
        
        # Pack parents (max 2 for efficiency)
        p_list = list(parents)[:2]
        while len(p_list) < 2:
            p_list.append(b'\x00' * 32)
        
        try:
            # Store packed node
            self._nodes[tx_hash] = struct.pack('!32s32s', p_list[0], p_list[1])
            
            # Update tips
            for parent in parents:
                self._tips.discard(parent)
            self._tips.add(tx_hash)
            
            self._count += 1
            return True
            
        except (struct.error, MemoryError) as e:
            # Rollback on failure
            self._nodes.pop(tx_hash, None)
            raise RuntimeError(f"Failed to add transaction: {e}") from e
    
    def get_parents(self, tx_hash: bytes) -> Set[bytes]:
        """
        Get parent transaction hashes for a given transaction.
        
        Args:
            tx_hash: 32-byte hash of the transaction
            
        Returns:
            Set[bytes]: Set of parent transaction hashes
            
        Raises:
            ValueError: If tx_hash is invalid
        """
        if not isinstance(tx_hash, bytes) or len(tx_hash) != 32:
            raise ValueError("tx_hash must be 32 bytes")
            
        if tx_hash not in self._nodes:
            return set()
        
        try:
            p1, p2 = struct.unpack('!32s32s', self._nodes[tx_hash])
            return {p for p in [p1, p2] if p != b'\x00' * 32}
        except struct.error as e:
            raise RuntimeError(f"Failed to unpack parents: {e}") from e
    
    def get_tips(self) -> Set[bytes]:
        """
        Get current DAG tips (transactions with no children).
        
        Returns:
            Set[bytes]: Set of tip transaction hashes
        """
        return self._tips.copy()
    
    def has_transaction(self, tx_hash: bytes) -> bool:
        """
        Check if transaction exists in DAG.
        
        Args:
            tx_hash: 32-byte hash of the transaction
            
        Returns:
            bool: True if transaction exists
            
        Raises:
            ValueError: If tx_hash is invalid
        """
        if not isinstance(tx_hash, bytes) or len(tx_hash) != 32:
            raise ValueError("tx_hash must be 32 bytes")
            
        return tx_hash in self._nodes
    
    def get_stats(self) -> Dict[str, int]:
        """
        Get DAG statistics and metrics.
        
        Returns:
            Dict[str, int]: Dictionary containing DAG statistics
        """
        return {
            'transactions': self._count,
            'tips': len(self._tips),
            'memory_bytes': len(self._nodes) * 64
        }
    
    def get_balance(self, address: str) -> float:
        """
        Get address balance (placeholder - needs transaction data).
        
        Note: This is a simplified implementation for ultra-lightweight demo.
        A full implementation would require access to transaction data.
        
        Args:
            address: Address string to check balance for
            
        Returns:
            float: Balance (always 0.0 in this implementation)
        """
        # This would require access to transaction data
        # Simplified for ultra-lightweight implementation
        return 0.0
    
    def clear(self) -> None:
        """
        Clear all DAG data (primarily for testing).
        
        Warning: This operation is irreversible and will remove all
        transactions and tips from the DAG.
        """
        self._nodes.clear()
        self._tips.clear()
        self._count = 0
