"""
MicroDAG Cryptographic Utilities
Pure implementation of Ed25519 and BLAKE2b as per specification
"""

import hashlib
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature


def generate_keypair(seed: bytes = None) -> tuple[bytes, bytes]:
    """
    Generate Ed25519 keypair
    
    Input: 32-byte random seed (optional)
    Output: (32-byte private key, 32-byte public key)
    
    As per spec: Function 1 - Key Generation
    """
    if seed is not None:
        if len(seed) != 32:
            raise ValueError("Seed must be exactly 32 bytes")
        private_key = Ed25519PrivateKey.from_private_bytes(seed)
    else:
        private_key = Ed25519PrivateKey.generate()
    
    # Get raw bytes (32 bytes for Ed25519)
    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    public_bytes = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    
    return private_bytes, public_bytes


def hash_transaction(tx_bytes: bytes) -> bytes:
    """
    Hash transaction using BLAKE2b-256
    
    Input: Transaction bytes[0-104]
    Output: 32-byte hash
    
    As per spec: Function 4 - Transaction Hash
    """
    if len(tx_bytes) < 105:
        raise ValueError("Transaction bytes must be at least 105 bytes")
    
    # BLAKE2b with 32-byte digest (256 bits)
    return hashlib.blake2b(tx_bytes[:105], digest_size=32).digest()


def sign_transaction(tx_bytes: bytes, private_key: bytes) -> bytes:
    """
    Sign transaction with Ed25519
    
    Input: Transaction bytes[0-104], private key
    Output: 36-byte compressed signature
    
    As per spec: Function 2 - Transaction Signing
    """
    if len(tx_bytes) < 105:
        raise ValueError("Transaction bytes must be at least 105 bytes")
    if len(private_key) != 32:
        raise ValueError("Private key must be exactly 32 bytes")
    
    # Hash the transaction
    tx_hash = hash_transaction(tx_bytes)
    
    # Sign the hash
    key = Ed25519PrivateKey.from_private_bytes(private_key)
    signature = key.sign(tx_hash)
    
    # Compress to 36 bytes (take first 36 bytes of 64-byte signature)
    return compress_signature(signature)


def verify_signature(tx_bytes: bytes) -> bool:
    """
    Verify transaction signature
    
    Input: Transaction bytes[0-140] (full transaction with signature)
    Output: true/false
    
    As per spec: Function 3 - Signature Verification
    """
    if len(tx_bytes) != 141:
        raise ValueError("Transaction must be exactly 141 bytes")
    
    # Extract components
    public_key_bytes = tx_bytes[1:33]  # Account public key
    signature_compressed = tx_bytes[105:141]  # 36-byte compressed signature
    
    # Expand signature to 64 bytes
    signature = expand_signature(signature_compressed)
    
    # Hash transaction
    tx_hash = hash_transaction(tx_bytes)
    
    # Verify
    try:
        public_key = Ed25519PublicKey.from_public_bytes(public_key_bytes)
        public_key.verify(signature, tx_hash)
        return True
    except InvalidSignature:
        return False
    except Exception:
        return False


def compress_signature(signature: bytes) -> bytes:
    """
    Compress 64-byte Ed25519 signature to 36 bytes
    
    As per spec: Take first 36 bytes of signature
    """
    if len(signature) != 64:
        raise ValueError("Signature must be exactly 64 bytes")
    return signature[:36]


def expand_signature(compressed: bytes) -> bytes:
    """
    Expand 36-byte compressed signature to 64 bytes
    
    As per spec: Pad with zeros to 64 bytes
    """
    if len(compressed) != 36:
        raise ValueError("Compressed signature must be exactly 36 bytes")
    return compressed + bytes(28)  # Pad with 28 zero bytes
