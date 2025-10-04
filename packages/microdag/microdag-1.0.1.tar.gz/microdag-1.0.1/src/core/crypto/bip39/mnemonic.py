"""
BIP39 Mnemonic Generation and Validation
Implements Function 5 from specification
"""

import secrets
import hashlib
from typing import List
from mnemonic import Mnemonic

# Standard BIP39 word count (24 words = 256 bits entropy)
WORD_COUNT = 24

# Initialize BIP39 with English wordlist
_mnemonic_generator = Mnemonic("english")


def generate_mnemonic(entropy_bits: int = 256) -> str:
    """
    Generate BIP39 mnemonic phrase
    
    Specification: Function 5 - Seed Phrase
    Input: 256-bit random entropy
    Output: 24-word BIP39 mnemonic
    
    Implementation:
    - Use standard BIP39 wordlist
    - Generate checksum
    - Return 24 words
    
    Args:
        entropy_bits: Bits of entropy (default: 256 for 24 words)
        
    Returns:
        Space-separated mnemonic phrase (24 words)
        
    Raises:
        ValueError: If entropy_bits is not valid (must be 128-256, multiple of 32)
        
    Example:
        >>> mnemonic = generate_mnemonic()
        >>> len(mnemonic.split())
        24
        >>> validate_mnemonic(mnemonic)
        True
    """
    if entropy_bits not in [128, 160, 192, 224, 256]:
        raise ValueError(
            "Entropy must be 128, 160, 192, 224, or 256 bits"
        )
    
    # Generate cryptographically secure random entropy
    entropy_bytes = secrets.token_bytes(entropy_bits // 8)
    
    # Generate mnemonic from entropy
    mnemonic = _mnemonic_generator.to_mnemonic(entropy_bytes)
    
    return mnemonic


def mnemonic_to_seed(mnemonic: str, passphrase: str = "") -> bytes:
    """
    Convert mnemonic to 512-bit seed
    
    This seed is used for hierarchical key derivation (BIP44).
    
    Args:
        mnemonic: BIP39 mnemonic phrase
        passphrase: Optional passphrase for additional security
        
    Returns:
        64-byte seed (512 bits)
        
    Raises:
        ValueError: If mnemonic is invalid
        
    Example:
        >>> mnemonic = generate_mnemonic()
        >>> seed = mnemonic_to_seed(mnemonic)
        >>> len(seed)
        64
    """
    if not validate_mnemonic(mnemonic):
        raise ValueError("Invalid mnemonic phrase")
    
    # BIP39 seed derivation using PBKDF2
    seed = _mnemonic_generator.to_seed(mnemonic, passphrase)
    
    return seed


def validate_mnemonic(mnemonic: str) -> bool:
    """
    Validate BIP39 mnemonic phrase
    
    Checks:
    1. Word count is valid (12, 15, 18, 21, or 24)
    2. All words are in BIP39 wordlist
    3. Checksum is valid
    
    Args:
        mnemonic: Mnemonic phrase to validate
        
    Returns:
        True if valid, False otherwise
        
    Example:
        >>> mnemonic = generate_mnemonic()
        >>> validate_mnemonic(mnemonic)
        True
        >>> validate_mnemonic("invalid mnemonic phrase")
        False
    """
    try:
        return _mnemonic_generator.check(mnemonic)
    except Exception:
        return False


def get_wordlist() -> List[str]:
    """
    Get BIP39 English wordlist
    
    Returns:
        List of 2048 words
        
    Example:
        >>> wordlist = get_wordlist()
        >>> len(wordlist)
        2048
        >>> "abandon" in wordlist
        True
    """
    return _mnemonic_generator.wordlist


def entropy_to_mnemonic(entropy: bytes) -> str:
    """
    Convert raw entropy to mnemonic
    
    Args:
        entropy: Raw entropy bytes (16, 20, 24, 28, or 32 bytes)
        
    Returns:
        BIP39 mnemonic phrase
        
    Raises:
        ValueError: If entropy length is invalid
    """
    if len(entropy) not in [16, 20, 24, 28, 32]:
        raise ValueError(
            "Entropy must be 16, 20, 24, 28, or 32 bytes"
        )
    
    return _mnemonic_generator.to_mnemonic(entropy)


def mnemonic_to_entropy(mnemonic: str) -> bytes:
    """
    Convert mnemonic back to entropy
    
    Args:
        mnemonic: BIP39 mnemonic phrase
        
    Returns:
        Original entropy bytes
        
    Raises:
        ValueError: If mnemonic is invalid
    """
    if not validate_mnemonic(mnemonic):
        raise ValueError("Invalid mnemonic phrase")
    
    return _mnemonic_generator.to_entropy(mnemonic)
