"""
Key management - lightweight cryptographic key operations.
"""
import hashlib
import secrets
from typing import Tuple
from ..utils.hash import blake2b_hash

class KeyManager:
    """Ultra-lightweight key management"""
    
    def __init__(self):
        self.private_key: bytes = None
        self.public_key: bytes = None
        self.address: bytes = None
    
    def generate_keys(self) -> Tuple[bytes, bytes]:
        """Generate new keypair (simplified)"""
        # Generate 32-byte private key
        self.private_key = secrets.token_bytes(32)
        
        # Derive public key (simplified - in real implementation would use Ed25519)
        self.public_key = blake2b_hash(self.private_key)
        
        # Generate address from public key
        self.address = compress_address_from_pubkey(self.public_key)
        
        return self.private_key, self.public_key
    
    def load_keys(self, private_key: bytes) -> bytes:
        """Load keys from private key"""
        self.private_key = private_key
        self.public_key = blake2b_hash(private_key)
        self.address = compress_address_from_pubkey(self.public_key)
        return self.public_key
    
    def get_address(self) -> bytes:
        """Get address as bytes"""
        return self.address
    
    def get_address_string(self) -> str:
        """Get address as string"""
        return f"micro_{self.address.hex()[:16]}"

def generate_keypair() -> Tuple[bytes, bytes]:
    """Generate new keypair"""
    private_key = secrets.token_bytes(32)
    public_key = blake2b_hash(private_key)
    return private_key, public_key

def compress_address(address_str: str) -> bytes:
    """Compress string address to 32 bytes"""
    if address_str.startswith('micro_'):
        address_str = address_str[6:]
    return blake2b_hash(address_str.encode())

def compress_address_from_pubkey(public_key: bytes) -> bytes:
    """Generate address from public key"""
    return blake2b_hash(b'addr' + public_key)

def derive_address(private_key: bytes) -> str:
    """Derive address string from private key"""
    public_key = blake2b_hash(private_key)
    address_bytes = compress_address_from_pubkey(public_key)
    return f"micro_{address_bytes.hex()[:16]}"
