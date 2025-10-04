"""
Genesis Block Creation
Implements genesis account initialization as per specification
"""

from dataclasses import dataclass
from typing import Optional

from ..crypto import generate_keypair, Keypair
from ..types.account import AccountState, create_genesis_account
from ..types.transaction import Transaction, TransactionBuilder


# Total supply as per specification: 100 million tokens
TOTAL_SUPPLY_TOKENS = 100_000_000
BASE_UNIT = 1_000_000  # 1 token = 1,000,000 base units (6 decimals)
TOTAL_SUPPLY_BASE_UNITS = TOTAL_SUPPLY_TOKENS * BASE_UNIT


@dataclass
class GenesisConfig:
    """
    Genesis configuration
    
    Specification: Section 2.5 - Total Supply & Genesis
    
    Attributes:
        total_supply: Total token supply (100 million)
        genesis_keypair: Genesis account keypair (optional, generated if not provided)
    """
    total_supply: int = TOTAL_SUPPLY_BASE_UNITS
    genesis_keypair: Optional[Keypair] = None
    
    def __post_init__(self):
        """Generate genesis keypair if not provided"""
        if self.genesis_keypair is None:
            # Generate deterministic genesis keypair from known seed
            # In production, this should be a secure, pre-generated keypair
            genesis_seed = bytes(32)  # All zeros for deterministic genesis
            self.genesis_keypair = generate_keypair(genesis_seed)


def create_genesis(config: Optional[GenesisConfig] = None) -> tuple[Keypair, AccountState]:
    """
    Create genesis account with total supply
    
    Specification: Section 2.5 - Total Supply & Genesis
    - Total Supply: 100,000,000 tokens (100 million)
    - All tokens created in genesis transaction
    - Genesis account: micro_0000000000000000000000000000000000000000000000000000
    - No inflation, no mining, no staking rewards
    
    Args:
        config: Genesis configuration (optional)
        
    Returns:
        Tuple of (genesis_keypair, genesis_account_state)
        
    Example:
        >>> keypair, state = create_genesis()
        >>> state.balance
        100000000000000
        >>> state.frontier
        b'\\x00\\x00\\x00...'
    """
    if config is None:
        config = GenesisConfig()
    
    # Create genesis account state
    genesis_state = AccountState(
        balance=config.total_supply,
        frontier=bytes(32)  # No previous transactions
    )
    
    return config.genesis_keypair, genesis_state


def initialize_genesis(storage, config: Optional[GenesisConfig] = None) -> Keypair:
    """
    Initialize genesis account in database
    
    This should be called once when setting up a new node.
    
    Args:
        storage: LevelDBStorage instance
        config: Genesis configuration (optional)
        
    Returns:
        Genesis keypair
        
    Raises:
        ValueError: If genesis already exists
        
    Example:
        >>> from src.storage import LevelDBStorage
        >>> 
        >>> db = LevelDBStorage("./data")
        >>> db.open()
        >>> 
        >>> # Initialize genesis (only once)
        >>> genesis_keypair = initialize_genesis(db)
        >>> 
        >>> # Verify genesis account
        >>> state = db.get_account(genesis_keypair.public_key)
        >>> print(f"Genesis balance: {state.balance}")
    """
    # Create genesis
    genesis_keypair, genesis_state = create_genesis(config)
    
    # Check if genesis already exists
    if storage.account_exists(genesis_keypair.public_key):
        raise ValueError("Genesis account already exists")
    
    # Store genesis account
    storage.put_account(genesis_keypair.public_key, genesis_state)
    
    return genesis_keypair


def create_genesis_distribution(
    storage,
    genesis_keypair: Keypair,
    recipients: list[tuple[bytes, int]]
) -> list[Transaction]:
    """
    Create initial token distribution from genesis
    
    Distributes tokens from genesis account to initial recipients.
    Useful for faucet setup, team allocation, etc.
    
    Args:
        storage: LevelDBStorage instance
        genesis_keypair: Genesis account keypair
        recipients: List of (recipient_pubkey, amount) tuples
        
    Returns:
        List of SEND transactions
        
    Example:
        >>> # Distribute to faucet and team
        >>> recipients = [
        ...     (faucet_pubkey, 10_000_000 * BASE_UNIT),  # 10M to faucet
        ...     (team_pubkey, 5_000_000 * BASE_UNIT),     # 5M to team
        ... ]
        >>> 
        >>> txs = create_genesis_distribution(db, genesis_keypair, recipients)
        >>> print(f"Created {len(txs)} distribution transactions")
    """
    from ..processing import TransactionProcessor
    
    # Get genesis account state
    genesis_state = storage.get_account(genesis_keypair.public_key)
    if genesis_state is None:
        raise ValueError("Genesis account not found")
    
    # Create transaction chain builder
    chain_builder = TransactionBuilder.TransactionChainBuilder(genesis_keypair)
    chain_builder.set_frontier(genesis_state.frontier)
    
    # Create processor
    processor = TransactionProcessor(storage)
    
    # Create and process distribution transactions
    transactions = []
    
    for recipient_pubkey, amount in recipients:
        # Create SEND transaction
        tx = chain_builder.send(recipient_pubkey, amount)
        
        # Process transaction
        result = processor.process(tx)
        if not result.valid:
            raise ValueError(f"Failed to process distribution: {result.message}")
        
        transactions.append(tx)
    
    return transactions


def get_genesis_address() -> str:
    """
    Get genesis account address
    
    Returns:
        Genesis address string
    """
    from ..types.account import encode_address
    
    # Genesis is all zeros
    genesis_pubkey = bytes(32)
    return encode_address(genesis_pubkey)


def verify_genesis(storage) -> bool:
    """
    Verify genesis account exists and has correct initial state
    
    Args:
        storage: LevelDBStorage instance
        
    Returns:
        True if genesis is valid
    """
    # Get genesis account
    genesis_pubkey = bytes(32)
    genesis_state = storage.get_account(genesis_pubkey)
    
    if genesis_state is None:
        return False
    
    # Verify initial balance (should be total supply minus distributions)
    # Note: Balance will be less than total supply after distributions
    if genesis_state.balance > TOTAL_SUPPLY_BASE_UNITS:
        return False
    
    return True
