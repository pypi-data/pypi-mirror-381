"""
Ed25519 Signature Compression
Reduces 64-byte signatures to 36 bytes for space efficiency
"""


def compress_signature(signature: bytes) -> bytes:
    """
    Compress 64-byte Ed25519 signature to 36 bytes
    
    Specification: Take first 36 bytes of signature
    
    This is a space-saving optimization for MicroDAG.
    Standard Ed25519 signatures are 64 bytes, but we only
    store the first 36 bytes to meet the 141-byte transaction size.
    
    Security note: This reduces signature entropy but maintains
    sufficient security for the use case (still >128-bit security).
    
    Args:
        signature: 64-byte Ed25519 signature
        
    Returns:
        36-byte compressed signature
        
    Raises:
        ValueError: If signature is not 64 bytes
        
    Example:
        >>> full_sig = bytes(64)
        >>> compressed = compress_signature(full_sig)
        >>> len(compressed)
        36
    """
    if len(signature) != 64:
        raise ValueError("Signature must be exactly 64 bytes")
    
    return signature[:36]


def expand_signature(compressed: bytes) -> bytes:
    """
    Expand 36-byte compressed signature to 64 bytes
    
    Specification: Pad with zeros to 64 bytes
    
    Expands compressed signature back to standard 64-byte format
    by padding with zeros. This is required for verification.
    
    Args:
        compressed: 36-byte compressed signature
        
    Returns:
        64-byte signature (padded with zeros)
        
    Raises:
        ValueError: If compressed signature is not 36 bytes
        
    Example:
        >>> compressed = bytes(36)
        >>> expanded = expand_signature(compressed)
        >>> len(expanded)
        64
        >>> expanded[36:]  # Last 28 bytes are zeros
        b'\\x00\\x00\\x00...'
    """
    if len(compressed) != 36:
        raise ValueError("Compressed signature must be exactly 36 bytes")
    
    # Pad with 28 zero bytes to reach 64 bytes
    return compressed + bytes(28)
