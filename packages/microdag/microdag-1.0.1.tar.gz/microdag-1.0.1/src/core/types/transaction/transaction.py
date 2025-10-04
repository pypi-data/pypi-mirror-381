"""
Transaction Data Structure
Implements the 141-byte transaction format from specification
"""

from dataclasses import dataclass
from enum import IntEnum
from typing import Optional


class TransactionType(IntEnum):
    """
    Transaction types as per specification
    
    0x00 = SEND: Transfer tokens to another account
    0x01 = RECEIVE: Claim pending tokens from a SEND transaction
    """
    SEND = 0x00
    RECEIVE = 0x01


@dataclass
class Transaction:
    """
    MicroDAG Transaction
    
    Specification: Section 2.2 - Transaction Format
    Every transaction is exactly 141 bytes:
    
    [0]       Type (1 byte) - SEND or RECEIVE
    [1-32]    Account (32 bytes) - sender/receiver public key
    [33-64]   Previous (32 bytes) - hash of previous tx in account's chain
    [65-96]   Link (32 bytes) - recipient (SEND) or send_tx_hash (RECEIVE)
    [97-104]  Amount (8 bytes, uint64, little-endian)
    [105-140] Signature (36 bytes) - Ed25519 compressed signature
    
    Attributes:
        tx_type: Transaction type (SEND or RECEIVE)
        account: 32-byte public key of account
        previous: 32-byte hash of previous transaction (zeros for first tx)
        link: 32-byte link (recipient for SEND, send_tx_hash for RECEIVE)
        amount: Amount in base units (uint64)
        signature: 36-byte compressed Ed25519 signature
        tx_hash: 32-byte transaction hash (computed from first 105 bytes)
    """
    tx_type: TransactionType
    account: bytes
    previous: bytes
    link: bytes
    amount: int
    signature: bytes
    tx_hash: Optional[bytes] = None
    
    def __post_init__(self):
        """Validate transaction structure"""
        # Validate field sizes
        if len(self.account) != 32:
            raise ValueError("Account must be 32 bytes")
        if len(self.previous) != 32:
            raise ValueError("Previous must be 32 bytes")
        if len(self.link) != 32:
            raise ValueError("Link must be 32 bytes")
        if not 0 <= self.amount <= 0xFFFFFFFFFFFFFFFF:
            raise ValueError("Amount must be uint64")
        if len(self.signature) != 36:
            raise ValueError("Signature must be 36 bytes")
        if self.tx_hash is not None and len(self.tx_hash) != 32:
            raise ValueError("Transaction hash must be 32 bytes")
        
        # Validate transaction type
        if self.tx_type not in [TransactionType.SEND, TransactionType.RECEIVE]:
            raise ValueError(f"Invalid transaction type: {self.tx_type}")
    
    @property
    def is_send(self) -> bool:
        """Check if this is a SEND transaction"""
        return self.tx_type == TransactionType.SEND
    
    @property
    def is_receive(self) -> bool:
        """Check if this is a RECEIVE transaction"""
        return self.tx_type == TransactionType.RECEIVE
    
    @property
    def is_first_transaction(self) -> bool:
        """Check if this is the first transaction in account's chain"""
        return self.previous == bytes(32)
    
    def __repr__(self) -> str:
        """String representation of transaction"""
        tx_type_str = "SEND" if self.is_send else "RECEIVE"
        hash_str = self.tx_hash.hex()[:16] if self.tx_hash else "not computed"
        return (
            f"Transaction("
            f"type={tx_type_str}, "
            f"hash={hash_str}..., "
            f"amount={self.amount})"
        )
    
    def to_dict(self) -> dict:
        """Convert transaction to dictionary"""
        return {
            'type': 'SEND' if self.is_send else 'RECEIVE',
            'account': self.account.hex(),
            'previous': self.previous.hex(),
            'link': self.link.hex(),
            'amount': self.amount,
            'signature': self.signature.hex(),
            'hash': self.tx_hash.hex() if self.tx_hash else None
        }


def create_zeros_hash() -> bytes:
    """Create a zero-filled 32-byte hash (for first transaction)"""
    return bytes(32)
