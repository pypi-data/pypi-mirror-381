"""
Ed25519 Keypair Generation
Implements Function 1 from specification
"""

from dataclasses import dataclass
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey
)
from cryptography.hazmat.primitives import serialization


@dataclass(frozen=True)
class Keypair:
    """
    Ed25519 keypair container
    
    Attributes:
        private_key: 32-byte private key
        public_key: 32-byte public key
    """
    private_key: bytes
    public_key: bytes
    
    def __post_init__(self):
        """Validate keypair sizes"""
        if len(self.private_key) != 32:
            raise ValueError("Private key must be exactly 32 bytes")
        if len(self.public_key) != 32:
            raise ValueError("Public key must be exactly 32 bytes")


def generate_keypair(seed: bytes = None) -> Keypair:
    """
    Generate Ed25519 keypair
    
    Specification: Function 1 - Key Generation
    Input: 32-byte random seed (optional)
    Output: Ed25519 keypair (32-byte private, 32-byte public)
    
    Implementation:
    - Use standard Ed25519 key generation
    - Library: cryptography (libsodium-based)
    
    Args:
        seed: Optional 32-byte seed for deterministic generation
        
    Returns:
        Keypair object containing private and public keys
        
    Raises:
        ValueError: If seed is provided but not 32 bytes
        
    Example:
        >>> keypair = generate_keypair()
        >>> len(keypair.private_key)
        32
        >>> len(keypair.public_key)
        32
    """
    if seed is not None:
        if len(seed) != 32:
            raise ValueError("Seed must be exactly 32 bytes")
        private_key_obj = Ed25519PrivateKey.from_private_bytes(seed)
    else:
        private_key_obj = Ed25519PrivateKey.generate()
    
    # Extract raw bytes (32 bytes for Ed25519)
    private_bytes = private_key_obj.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    public_bytes = private_key_obj.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    
    return Keypair(
        private_key=private_bytes,
        public_key=public_bytes
    )


def keypair_from_private(private_key: bytes) -> Keypair:
    """
    Derive public key from private key
    
    Args:
        private_key: 32-byte Ed25519 private key
        
    Returns:
        Complete keypair with derived public key
        
    Raises:
        ValueError: If private key is not 32 bytes
    """
    if len(private_key) != 32:
        raise ValueError("Private key must be exactly 32 bytes")
    
    private_key_obj = Ed25519PrivateKey.from_private_bytes(private_key)
    public_bytes = private_key_obj.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    
    return Keypair(
        private_key=private_key,
        public_key=public_bytes
    )
