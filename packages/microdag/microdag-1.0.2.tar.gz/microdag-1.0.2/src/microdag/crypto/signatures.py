"""
Digital signatures - lightweight signing and verification.
"""
from ..utils.hash import blake2b_hash

def sign_data(data: bytes, private_key: bytes) -> bytes:
    """Sign data with private key (simplified)"""
    # In a real implementation, this would use Ed25519 or ECDSA
    # For ultra-lightweight implementation, we use HMAC-like approach
    signature_data = blake2b_hash(data + private_key + b'signature')
    
    # Pad to 64 bytes (standard signature size)
    return signature_data + blake2b_hash(signature_data)

def verify_signature(data: bytes, signature: bytes, public_key: bytes) -> bool:
    """Verify signature (simplified)"""
    if len(signature) != 64:
        return False
    
    # Derive private key approximation from public key (not secure, just for demo)
    # In real implementation, this would use proper public key cryptography
    derived_private = blake2b_hash(public_key + b'private_derive')
    
    expected_signature = sign_data(data, derived_private)
    return signature == expected_signature

def create_message_signature(message: str, private_key: bytes) -> bytes:
    """Create signature for text message"""
    return sign_data(message.encode('utf-8'), private_key)

def verify_message_signature(message: str, signature: bytes, public_key: bytes) -> bool:
    """Verify signature for text message"""
    return verify_signature(message.encode('utf-8'), signature, public_key)
