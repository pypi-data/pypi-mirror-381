"""
Transaction Serialization
Converts transactions to/from 141-byte binary format
"""

import struct
from .transaction import Transaction, TransactionType
from ...crypto import hash_transaction


def serialize_transaction(tx: Transaction) -> bytes:
    """
    Serialize transaction to 141-byte binary format
    
    Specification: Section 2.2 - Transaction Format
    
    Format:
    [0]       Type (1 byte)
    [1-32]    Account (32 bytes)
    [33-64]   Previous (32 bytes)
    [65-96]   Link (32 bytes)
    [97-104]  Amount (8 bytes, uint64, little-endian)
    [105-140] Signature (36 bytes)
    
    Args:
        tx: Transaction object to serialize
        
    Returns:
        141-byte binary representation
        
    Example:
        >>> tx = Transaction(...)
        >>> tx_bytes = serialize_transaction(tx)
        >>> len(tx_bytes)
        141
    """
    # Create 141-byte buffer
    buffer = bytearray(141)
    
    # [0] Type
    buffer[0] = int(tx.tx_type)
    
    # [1-32] Account
    buffer[1:33] = tx.account
    
    # [33-64] Previous
    buffer[33:65] = tx.previous
    
    # [65-96] Link
    buffer[65:97] = tx.link
    
    # [97-104] Amount (uint64, little-endian)
    struct.pack_into('<Q', buffer, 97, tx.amount)
    
    # [105-140] Signature
    buffer[105:141] = tx.signature
    
    return bytes(buffer)


def deserialize_transaction(tx_bytes: bytes) -> Transaction:
    """
    Deserialize 141-byte binary data to Transaction object
    
    Args:
        tx_bytes: 141-byte transaction data
        
    Returns:
        Transaction object
        
    Raises:
        ValueError: If tx_bytes is not exactly 141 bytes
        
    Example:
        >>> tx_bytes = bytes(141)
        >>> tx = deserialize_transaction(tx_bytes)
        >>> isinstance(tx, Transaction)
        True
    """
    if len(tx_bytes) != 141:
        raise ValueError(f"Transaction must be 141 bytes, got {len(tx_bytes)}")
    
    # Parse fields
    tx_type = TransactionType(tx_bytes[0])
    account = tx_bytes[1:33]
    previous = tx_bytes[33:65]
    link = tx_bytes[65:97]
    amount = struct.unpack('<Q', tx_bytes[97:105])[0]
    signature = tx_bytes[105:141]
    
    # Compute transaction hash
    tx_hash = hash_transaction(tx_bytes)
    
    return Transaction(
        tx_type=tx_type,
        account=account,
        previous=previous,
        link=link,
        amount=amount,
        signature=signature,
        tx_hash=tx_hash
    )


def serialize_unsigned_transaction(tx: Transaction) -> bytes:
    """
    Serialize transaction without signature (first 105 bytes)
    
    This is used for:
    1. Computing transaction hash
    2. Signing the transaction
    
    Args:
        tx: Transaction object
        
    Returns:
        105-byte unsigned transaction data
    """
    # Create 105-byte buffer (excludes signature)
    buffer = bytearray(105)
    
    # [0] Type
    buffer[0] = int(tx.tx_type)
    
    # [1-32] Account
    buffer[1:33] = tx.account
    
    # [33-64] Previous
    buffer[33:65] = tx.previous
    
    # [65-96] Link
    buffer[65:97] = tx.link
    
    # [97-104] Amount (uint64, little-endian)
    struct.pack_into('<Q', buffer, 97, tx.amount)
    
    return bytes(buffer)


def compute_transaction_hash(tx: Transaction) -> bytes:
    """
    Compute transaction hash from first 105 bytes
    
    Args:
        tx: Transaction object
        
    Returns:
        32-byte BLAKE2b hash
    """
    unsigned_bytes = serialize_unsigned_transaction(tx)
    return hash_transaction(unsigned_bytes)
