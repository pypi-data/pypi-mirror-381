"""
MicroDAG Core Cryptography Module

Provides all cryptographic primitives needed for MicroDAG:
- Ed25519 digital signatures
- BLAKE2b-256 hashing
- BIP39/BIP44 key derivation
"""

# Ed25519 signatures
from .ed25519 import (
    generate_keypair,
    Keypair,
    sign,
    verify,
    compress_signature,
    expand_signature
)

# BLAKE2b hashing
from .blake2b import (
    hash_bytes,
    hash_transaction,
    HASH_SIZE
)

# BIP39/BIP44 key derivation
from .bip39 import (
    generate_mnemonic,
    mnemonic_to_seed,
    validate_mnemonic,
    derive_keypair,
    WORD_COUNT,
    DERIVATION_PATH
)

__all__ = [
    # Ed25519
    'generate_keypair',
    'Keypair',
    'sign',
    'verify',
    'compress_signature',
    'expand_signature',
    
    # BLAKE2b
    'hash_bytes',
    'hash_transaction',
    'HASH_SIZE',
    
    # BIP39/BIP44
    'generate_mnemonic',
    'mnemonic_to_seed',
    'validate_mnemonic',
    'derive_keypair',
    'WORD_COUNT',
    'DERIVATION_PATH'
]

__version__ = '1.0.0'
