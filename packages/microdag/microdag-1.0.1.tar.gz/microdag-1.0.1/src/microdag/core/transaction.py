"""
Ultra-lightweight transaction implementation - 208 bytes fixed size.

This module provides a high-performance, memory-efficient transaction
implementation with fixed-size binary serialization for blockchain use.
"""
import struct
import time
from typing import Tuple, Optional
from ..utils.hash import blake2b_hash
from ..crypto.keys import compress_address


class Transaction:
    """
    Ultra-compact transaction with exactly 208 bytes serialization.
    
    This implementation uses fixed-size binary packing to ensure consistent
    memory usage and optimal network transmission efficiency.
    
    Attributes:
        from_addr: 32-byte sender address
        to_addr: 32-byte recipient address  
        amount: Transaction amount in smallest units (int64)
        timestamp: Unix timestamp of transaction creation
        parent1: First parent transaction hash (32 bytes)
        parent2: Second parent transaction hash (32 bytes)
        signature: Cryptographic signature (36 bytes)
        hash: Transaction hash (32 bytes, calculated)
    """
    
    def __init__(self, from_addr: bytes, to_addr: bytes, amount: int, 
                 timestamp: int, parent1: bytes, parent2: bytes, signature: bytes) -> None:
        """
        Initialize transaction with validation.
        
        Args:
            from_addr: 32-byte sender address
            to_addr: 32-byte recipient address
            amount: Transaction amount (must be positive)
            timestamp: Unix timestamp
            parent1: First parent transaction hash (32 bytes)
            parent2: Second parent transaction hash (32 bytes)
            signature: 36-byte cryptographic signature
            
        Raises:
            ValueError: If any parameter is invalid
        """
        # Validate inputs
        if not isinstance(from_addr, bytes) or len(from_addr) != 32:
            raise ValueError("from_addr must be 32 bytes")
        if not isinstance(to_addr, bytes) or len(to_addr) != 32:
            raise ValueError("to_addr must be 32 bytes")
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("amount must be non-negative integer")
        if not isinstance(timestamp, int) or timestamp < 0:
            raise ValueError("timestamp must be non-negative integer")
        if not isinstance(parent1, bytes) or len(parent1) != 32:
            raise ValueError("parent1 must be 32 bytes")
        if not isinstance(parent2, bytes) or len(parent2) != 32:
            raise ValueError("parent2 must be 32 bytes")
        if not isinstance(signature, bytes) or len(signature) != 36:
            raise ValueError("signature must be 36 bytes")
        
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount
        self.timestamp = timestamp
        self.parent1 = parent1
        self.parent2 = parent2
        self.signature = signature
        self.hash = self._calculate_hash()
    
    def _calculate_hash(self) -> bytes:
        """
        Calculate cryptographic hash of transaction data.
        
        Returns:
            bytes: 32-byte Blake2b hash of transaction
            
        Raises:
            RuntimeError: If hash calculation fails
        """
        try:
            data = struct.pack('!32s32sQI32s32s36s', 
                              self.from_addr, self.to_addr, self.amount,
                              self.timestamp, self.parent1, self.parent2, self.signature)
            return blake2b_hash(data)
        except (struct.error, OverflowError) as e:
            raise RuntimeError(f"Failed to calculate transaction hash: {e}") from e
    
    def pack(self) -> bytes:
        """
        Pack transaction to exactly 208 bytes for network transmission.
        
        Returns:
            bytes: 208-byte packed transaction data
            
        Raises:
            RuntimeError: If packing fails
        """
        try:
            data = struct.pack('!32s32sQI32s32s36s', 
                              self.from_addr, self.to_addr, self.amount,
                              self.timestamp, self.parent1, self.parent2, self.signature)
            return data + self.hash
        except (struct.error, OverflowError) as e:
            raise RuntimeError(f"Failed to pack transaction: {e}") from e
    
    @classmethod
    def unpack(cls, data: bytes) -> 'Transaction':
        """
        Unpack 208-byte transaction data.
        
        Args:
            data: 208-byte packed transaction data
            
        Returns:
            Transaction: Unpacked transaction instance
            
        Raises:
            ValueError: If data is not exactly 208 bytes
            RuntimeError: If unpacking fails
        """
        if not isinstance(data, bytes):
            raise ValueError("Data must be bytes")
        if len(data) != 208:
            raise ValueError("Transaction must be exactly 208 bytes")
        
        try:
            parts = struct.unpack('!32s32sQI32s32s36s32s', data)
            from_addr, to_addr, amount, timestamp, parent1, parent2, signature, tx_hash = parts
            
            tx = cls(from_addr, to_addr, amount, timestamp, parent1, parent2, signature)
            tx.hash = tx_hash
            return tx
        except (struct.error, ValueError) as e:
            raise RuntimeError(f"Failed to unpack transaction: {e}") from e
    
    @classmethod
    def create(cls, to_address: str, amount: float, parents: Optional[Tuple[bytes, bytes]] = None) -> 'Transaction':
        """
        Create new transaction with validation.
        
        Args:
            to_address: Recipient address string (must start with 'micro_')
            amount: Transaction amount in MICRO (must be positive)
            parents: Optional tuple of parent transaction hashes
            
        Returns:
            Transaction: New transaction instance
            
        Raises:
            ValueError: If parameters are invalid
        """
        # Validate inputs
        if not isinstance(to_address, str):
            raise ValueError("to_address must be string")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("amount must be positive number")
        
        if parents is None:
            parents = (b'\x00' * 32, b'\x00' * 32)
        
        if not isinstance(parents, tuple) or len(parents) != 2:
            raise ValueError("parents must be tuple of 2 elements")
        
        try:
            from_addr = b'\x00' * 32  # Placeholder - would use wallet address
            to_addr = compress_address(to_address)
            amount_int = int(amount * 100000000)  # 8 decimal places
            timestamp = int(time.time())
            signature = b'\x00' * 36  # Placeholder - would use real signature
            
            return cls(from_addr, to_addr, amount_int, timestamp, parents[0], parents[1], signature)
        except Exception as e:
            raise ValueError(f"Failed to create transaction: {e}") from e
    
    def get_amount_float(self) -> float:
        """
        Get transaction amount as float value.
        
        Returns:
            float: Amount in MICRO units (8 decimal places)
        """
        return self.amount / 100000000
    
    def __str__(self) -> str:
        """
        String representation of transaction.
        
        Returns:
            str: Transaction hash prefix for identification
        """
        return f"Transaction({self.hash.hex()[:8]}...)"
