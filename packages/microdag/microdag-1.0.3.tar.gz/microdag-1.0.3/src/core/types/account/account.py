"""
Account Data Structure
Implements the 40-byte account state format from specification
"""

from dataclasses import dataclass
import struct


@dataclass
class AccountState:
    """
    Account State (40 bytes)
    
    Specification: Section 2.1 - Account System
    
    [0-7]   Balance (uint64, little-endian) - in base units
    [8-39]  Frontier (32 bytes) - hash of latest transaction
    
    No representative field. No timestamps. Just balance and frontier.
    
    Attributes:
        balance: Account balance in base units (uint64)
        frontier: 32-byte hash of latest transaction
    """
    balance: int
    frontier: bytes
    
    def __post_init__(self):
        """Validate account state structure"""
        if not 0 <= self.balance <= 0xFFFFFFFFFFFFFFFF:
            raise ValueError("Balance must be uint64")
        if len(self.frontier) != 32:
            raise ValueError("Frontier must be 32 bytes")
    
    def to_bytes(self) -> bytes:
        """
        Serialize account state to 40 bytes
        
        Returns:
            40-byte binary representation
        """
        buffer = bytearray(40)
        
        # [0-7] Balance (uint64, little-endian)
        struct.pack_into('<Q', buffer, 0, self.balance)
        
        # [8-39] Frontier (32 bytes)
        buffer[8:40] = self.frontier
        
        return bytes(buffer)
    
    @staticmethod
    def from_bytes(data: bytes) -> 'AccountState':
        """
        Deserialize account state from 40 bytes
        
        Args:
            data: 40-byte account state data
            
        Returns:
            AccountState object
            
        Raises:
            ValueError: If data is not 40 bytes
        """
        if len(data) != 40:
            raise ValueError(f"Account state must be 40 bytes, got {len(data)}")
        
        # Parse balance
        balance = struct.unpack('<Q', data[0:8])[0]
        
        # Parse frontier
        frontier = data[8:40]
        
        return AccountState(balance=balance, frontier=frontier)
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            'balance': self.balance,
            'frontier': self.frontier.hex()
        }
    
    def __repr__(self) -> str:
        """String representation"""
        return (
            f"AccountState("
            f"balance={self.balance}, "
            f"frontier={self.frontier.hex()[:16]}...)"
        )


@dataclass
class Account:
    """
    Complete account information
    
    Combines public key with account state for convenience.
    
    Attributes:
        public_key: 32-byte Ed25519 public key
        state: Account state (balance and frontier)
        address: Human-readable address (computed)
    """
    public_key: bytes
    state: AccountState
    
    def __post_init__(self):
        """Validate account structure"""
        if len(self.public_key) != 32:
            raise ValueError("Public key must be 32 bytes")
    
    @property
    def address(self) -> str:
        """Get human-readable address"""
        from .encoding import encode_address
        return encode_address(self.public_key)
    
    @property
    def balance(self) -> int:
        """Get account balance"""
        return self.state.balance
    
    @property
    def frontier(self) -> bytes:
        """Get account frontier"""
        return self.state.frontier
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            'public_key': self.public_key.hex(),
            'address': self.address,
            'balance': self.balance,
            'frontier': self.frontier.hex()
        }
    
    def __repr__(self) -> str:
        """String representation"""
        return (
            f"Account("
            f"address={self.address[:20]}..., "
            f"balance={self.balance})"
        )


def create_genesis_account(public_key: bytes, total_supply: int) -> Account:
    """
    Create genesis account with total supply
    
    Args:
        public_key: Genesis account public key
        total_supply: Total token supply
        
    Returns:
        Genesis account with full supply
    """
    state = AccountState(
        balance=total_supply,
        frontier=bytes(32)  # No previous transactions
    )
    
    return Account(
        public_key=public_key,
        state=state
    )


def create_empty_account(public_key: bytes) -> Account:
    """
    Create empty account (no balance, no transactions)
    
    Args:
        public_key: Account public key
        
    Returns:
        Empty account
    """
    state = AccountState(
        balance=0,
        frontier=bytes(32)
    )
    
    return Account(
        public_key=public_key,
        state=state
    )
