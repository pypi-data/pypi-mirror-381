"""
Ed25519 Signing and Verification
Implements Functions 2 and 3 from specification
"""

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey
)
from cryptography.exceptions import InvalidSignature


def sign(message: bytes, private_key: bytes) -> bytes:
    """
    Sign message with Ed25519 private key
    
    Specification: Function 2 - Transaction Signing
    Input: Message bytes, private key
    Output: 64-byte signature
    
    Note: This returns the full 64-byte signature.
    Use compress_signature() to get 36-byte compressed version.
    
    Args:
        message: Message to sign (typically transaction hash)
        private_key: 32-byte Ed25519 private key
        
    Returns:
        64-byte Ed25519 signature
        
    Raises:
        ValueError: If private key is not 32 bytes
        
    Example:
        >>> from .keypair import generate_keypair
        >>> keypair = generate_keypair()
        >>> message = b"test message"
        >>> signature = sign(message, keypair.private_key)
        >>> len(signature)
        64
    """
    if len(private_key) != 32:
        raise ValueError("Private key must be exactly 32 bytes")
    
    key = Ed25519PrivateKey.from_private_bytes(private_key)
    signature = key.sign(message)
    
    return signature


def verify(message: bytes, signature: bytes, public_key: bytes) -> bool:
    """
    Verify Ed25519 signature
    
    Specification: Function 3 - Signature Verification
    Input: Message, signature, public key
    Output: true/false
    
    Note: Accepts both 64-byte full signatures and 36-byte compressed.
    Compressed signatures are automatically expanded.
    
    Args:
        message: Original message that was signed
        signature: 64-byte or 36-byte signature
        public_key: 32-byte Ed25519 public key
        
    Returns:
        True if signature is valid, False otherwise
        
    Example:
        >>> from .keypair import generate_keypair
        >>> keypair = generate_keypair()
        >>> message = b"test message"
        >>> signature = sign(message, keypair.private_key)
        >>> verify(message, signature, keypair.public_key)
        True
    """
    if len(public_key) != 32:
        raise ValueError("Public key must be exactly 32 bytes")
    
    # Handle compressed signatures (36 bytes)
    if len(signature) == 36:
        from .compression import expand_signature
        signature = expand_signature(signature)
    elif len(signature) != 64:
        raise ValueError("Signature must be 36 or 64 bytes")
    
    try:
        key = Ed25519PublicKey.from_public_bytes(public_key)
        key.verify(signature, message)
        return True
    except InvalidSignature:
        return False
    except Exception:
        return False
