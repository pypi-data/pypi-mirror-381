"""
Cryptographic hash functions - lightweight hashing utilities.
"""
import hashlib

def blake2b_hash(data: bytes, digest_size: int = 32) -> bytes:
    """Blake2b hash function - fast and secure"""
    return hashlib.blake2b(data, digest_size=digest_size).digest()

def sha256_hash(data: bytes) -> bytes:
    """SHA256 hash function"""
    return hashlib.sha256(data).digest()

def double_sha256(data: bytes) -> bytes:
    """Double SHA256 hash (Bitcoin-style)"""
    return sha256_hash(sha256_hash(data))

def hash_to_hex(hash_bytes: bytes) -> str:
    """Convert hash bytes to hex string"""
    return hash_bytes.hex()

def hex_to_hash(hex_string: str) -> bytes:
    """Convert hex string to hash bytes"""
    return bytes.fromhex(hex_string)
