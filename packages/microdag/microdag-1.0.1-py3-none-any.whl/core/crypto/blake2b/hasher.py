"""
BLAKE2b-256 Hashing Functions
Implements Function 4 from specification
"""

import hashlib

# Hash output size in bytes (256 bits = 32 bytes)
HASH_SIZE = 32


def hash_bytes(data: bytes) -> bytes:
    """
    Hash arbitrary bytes with BLAKE2b-256
    
    Args:
        data: Bytes to hash
        
    Returns:
        32-byte BLAKE2b hash
        
    Example:
        >>> data = b"Hello, MicroDAG!"
        >>> hash_value = hash_bytes(data)
        >>> len(hash_value)
        32
    """
    return hashlib.blake2b(data, digest_size=HASH_SIZE).digest()


def hash_transaction(tx_bytes: bytes) -> bytes:
    """
    Hash transaction using BLAKE2b-256
    
    Specification: Function 4 - Transaction Hash
    Input: Transaction bytes[0-104]
    Output: 32-byte hash
    
    Implementation:
    - return BLAKE2b-256(bytes[0-104])
    
    This function hashes only the first 105 bytes of a transaction,
    which excludes the signature. This allows the hash to be used
    as the message that gets signed.
    
    Args:
        tx_bytes: Transaction bytes (at least 105 bytes)
        
    Returns:
        32-byte BLAKE2b hash of first 105 bytes
        
    Raises:
        ValueError: If tx_bytes is less than 105 bytes
        
    Example:
        >>> tx = bytes(141)  # Full transaction
        >>> tx_hash = hash_transaction(tx)
        >>> len(tx_hash)
        32
    """
    if len(tx_bytes) < 105:
        raise ValueError(
            f"Transaction bytes must be at least 105 bytes, got {len(tx_bytes)}"
        )
    
    # Hash only first 105 bytes (excludes 36-byte signature)
    return hashlib.blake2b(tx_bytes[:105], digest_size=HASH_SIZE).digest()


def verify_hash(data: bytes, expected_hash: bytes) -> bool:
    """
    Verify that data matches expected hash
    
    Args:
        data: Data to hash
        expected_hash: Expected hash value
        
    Returns:
        True if hash matches, False otherwise
        
    Example:
        >>> data = b"test"
        >>> hash_val = hash_bytes(data)
        >>> verify_hash(data, hash_val)
        True
    """
    if len(expected_hash) != HASH_SIZE:
        return False
    
    actual_hash = hash_bytes(data)
    return actual_hash == expected_hash
