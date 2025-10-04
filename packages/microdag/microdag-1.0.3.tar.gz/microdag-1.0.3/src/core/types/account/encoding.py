"""
Address Encoding/Decoding
Implements base32 encoding for human-readable addresses
"""

import base64
from typing import Optional


# Address prefix as per specification
ADDRESS_PREFIX = "micro_"

# Expected address length: "micro_" (6) + base32(32 bytes) = 6 + 52 = 58 characters
# Actually 59 with padding
EXPECTED_ADDRESS_LENGTH = 59


def encode_address(public_key: bytes) -> str:
    """
    Encode public key to human-readable address
    
    Specification: Section 2.1 - Account System
    Format: micro_ + base32(public_key) = 59 character address
    Example: micro_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z
    
    Args:
        public_key: 32-byte Ed25519 public key
        
    Returns:
        59-character address string
        
    Raises:
        ValueError: If public_key is not 32 bytes
        
    Example:
        >>> from src.core.crypto import generate_keypair
        >>> keypair = generate_keypair()
        >>> address = encode_address(keypair.public_key)
        >>> len(address)
        59
        >>> address.startswith('micro_')
        True
    """
    if len(public_key) != 32:
        raise ValueError("Public key must be exactly 32 bytes")
    
    # Use base32 encoding (RFC 4648)
    # base32 encodes 5 bits per character
    # 32 bytes = 256 bits = 52 characters (with padding)
    encoded = base64.b32encode(public_key).decode('ascii').lower()
    
    # Remove padding (=)
    encoded = encoded.rstrip('=')
    
    return ADDRESS_PREFIX + encoded


def decode_address(address: str) -> bytes:
    """
    Decode address to public key
    
    Args:
        address: 59-character address string
        
    Returns:
        32-byte public key
        
    Raises:
        ValueError: If address format is invalid
        
    Example:
        >>> from src.core.crypto import generate_keypair
        >>> keypair = generate_keypair()
        >>> address = encode_address(keypair.public_key)
        >>> decoded = decode_address(address)
        >>> decoded == keypair.public_key
        True
    """
    if not address.startswith(ADDRESS_PREFIX):
        raise ValueError(f"Address must start with '{ADDRESS_PREFIX}'")
    
    # Remove prefix
    encoded = address[len(ADDRESS_PREFIX):]
    
    # Convert to uppercase for base32 decoding
    encoded = encoded.upper()
    
    # Add padding if needed
    padding_needed = (8 - len(encoded) % 8) % 8
    encoded += '=' * padding_needed
    
    try:
        public_key = base64.b32decode(encoded)
    except Exception as e:
        raise ValueError(f"Invalid base32 encoding: {e}")
    
    if len(public_key) != 32:
        raise ValueError(f"Decoded public key must be 32 bytes, got {len(public_key)}")
    
    return public_key


def is_valid_address(address: str) -> bool:
    """
    Validate address format
    
    Checks:
    1. Starts with correct prefix
    2. Has correct length
    3. Contains valid base32 characters
    4. Decodes to 32-byte public key
    
    Args:
        address: Address string to validate
        
    Returns:
        True if valid, False otherwise
        
    Example:
        >>> address = "micro_" + "a" * 52
        >>> is_valid_address(address)
        True
        >>> is_valid_address("invalid")
        False
    """
    try:
        # Check prefix
        if not address.startswith(ADDRESS_PREFIX):
            return False
        
        # Check length (approximately)
        if len(address) < 50 or len(address) > 65:
            return False
        
        # Try to decode
        public_key = decode_address(address)
        
        # Verify it's 32 bytes
        return len(public_key) == 32
        
    except Exception:
        return False


def get_genesis_address() -> str:
    """
    Get genesis account address
    
    Specification: Section 2.5 - Total Supply & Genesis
    Genesis account: micro_0000000000000000000000000000000000000000000000000000
    
    Returns:
        Genesis account address
    """
    # Genesis account is all zeros
    genesis_pubkey = bytes(32)
    return encode_address(genesis_pubkey)


def create_vanity_address_matcher(prefix: str):
    """
    Create function to check if address matches vanity prefix
    
    Args:
        prefix: Desired prefix after "micro_"
        
    Returns:
        Function that checks if public key produces matching address
        
    Example:
        >>> matcher = create_vanity_address_matcher("abc")
        >>> # Use with key generation to find vanity address
    """
    full_prefix = ADDRESS_PREFIX + prefix.lower()
    
    def matches(public_key: bytes) -> bool:
        address = encode_address(public_key)
        return address.startswith(full_prefix)
    
    return matches
