"""
Transaction Builder
Provides convenient API for creating and signing transactions
"""

from typing import Optional
from .transaction import Transaction, TransactionType, create_zeros_hash
from .serialization import serialize_unsigned_transaction, compute_transaction_hash
from ...crypto import sign as crypto_sign, compress_signature


class TransactionBuilder:
    """
    Builder pattern for creating transactions
    
    Provides a fluent API for constructing SEND and RECEIVE transactions
    with automatic signing and hash computation.
    
    Example:
        >>> from src.core.crypto import generate_keypair
        >>> keypair = generate_keypair()
        >>> 
        >>> # Create SEND transaction
        >>> tx = TransactionBuilder.create_send(
        ...     sender_keypair=keypair,
        ...     recipient_pubkey=bytes(32),
        ...     amount=1000000,
        ...     previous_hash=bytes(32)
        ... )
    """
    
    @staticmethod
    def create_send(
        sender_keypair,
        recipient_pubkey: bytes,
        amount: int,
        previous_hash: bytes
    ) -> Transaction:
        """
        Create and sign a SEND transaction
        
        Args:
            sender_keypair: Keypair object with private_key and public_key
            recipient_pubkey: 32-byte recipient public key
            amount: Amount to send (in base units)
            previous_hash: Hash of previous transaction (zeros for first tx)
            
        Returns:
            Signed SEND transaction
            
        Raises:
            ValueError: If parameters are invalid
            
        Example:
            >>> from src.core.crypto import generate_keypair
            >>> sender = generate_keypair()
            >>> recipient = generate_keypair()
            >>> tx = TransactionBuilder.create_send(
            ...     sender_keypair=sender,
            ...     recipient_pubkey=recipient.public_key,
            ...     amount=1000000,
            ...     previous_hash=bytes(32)
            ... )
            >>> tx.is_send
            True
        """
        # Validate inputs
        if len(recipient_pubkey) != 32:
            raise ValueError("Recipient public key must be 32 bytes")
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        if len(previous_hash) != 32:
            raise ValueError("Previous hash must be 32 bytes")
        
        # Create unsigned transaction
        unsigned_tx = Transaction(
            tx_type=TransactionType.SEND,
            account=sender_keypair.public_key,
            previous=previous_hash,
            link=recipient_pubkey,
            amount=amount,
            signature=bytes(36)  # Placeholder
        )
        
        # Sign transaction
        return TransactionBuilder._sign_transaction(unsigned_tx, sender_keypair.private_key)
    
    @staticmethod
    def create_receive(
        receiver_keypair,
        send_tx_hash: bytes,
        amount: int,
        previous_hash: bytes
    ) -> Transaction:
        """
        Create and sign a RECEIVE transaction
        
        Args:
            receiver_keypair: Keypair object with private_key and public_key
            send_tx_hash: Hash of the SEND transaction being received
            amount: Amount to receive (must match SEND amount)
            previous_hash: Hash of previous transaction (zeros for first tx)
            
        Returns:
            Signed RECEIVE transaction
            
        Raises:
            ValueError: If parameters are invalid
            
        Example:
            >>> from src.core.crypto import generate_keypair
            >>> receiver = generate_keypair()
            >>> send_hash = bytes(32)  # Hash of SEND transaction
            >>> tx = TransactionBuilder.create_receive(
            ...     receiver_keypair=receiver,
            ...     send_tx_hash=send_hash,
            ...     amount=1000000,
            ...     previous_hash=bytes(32)
            ... )
            >>> tx.is_receive
            True
        """
        # Validate inputs
        if len(send_tx_hash) != 32:
            raise ValueError("Send transaction hash must be 32 bytes")
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        if len(previous_hash) != 32:
            raise ValueError("Previous hash must be 32 bytes")
        
        # Create unsigned transaction
        unsigned_tx = Transaction(
            tx_type=TransactionType.RECEIVE,
            account=receiver_keypair.public_key,
            previous=previous_hash,
            link=send_tx_hash,
            amount=amount,
            signature=bytes(36)  # Placeholder
        )
        
        # Sign transaction
        return TransactionBuilder._sign_transaction(unsigned_tx, receiver_keypair.private_key)
    
    @staticmethod
    def create_genesis_send(
        genesis_keypair,
        recipient_pubkey: bytes,
        amount: int
    ) -> Transaction:
        """
        Create genesis SEND transaction (first transaction from genesis account)
        
        Args:
            genesis_keypair: Genesis account keypair
            recipient_pubkey: Recipient public key
            amount: Amount to send
            
        Returns:
            Signed genesis SEND transaction
        """
        return TransactionBuilder.create_send(
            sender_keypair=genesis_keypair,
            recipient_pubkey=recipient_pubkey,
            amount=amount,
            previous_hash=create_zeros_hash()  # First transaction
        )
    
    @staticmethod
    def _sign_transaction(tx: Transaction, private_key: bytes) -> Transaction:
        """
        Sign a transaction and compute its hash
        
        Args:
            tx: Unsigned transaction (with placeholder signature)
            private_key: 32-byte Ed25519 private key
            
        Returns:
            Signed transaction with computed hash
        """
        # Serialize unsigned transaction (first 105 bytes)
        unsigned_bytes = serialize_unsigned_transaction(tx)
        
        # Compute transaction hash
        tx_hash = compute_transaction_hash(tx)
        
        # Sign the hash
        signature = crypto_sign(tx_hash, private_key)
        
        # Compress signature to 36 bytes
        compressed_sig = compress_signature(signature)
        
        # Create signed transaction
        signed_tx = Transaction(
            tx_type=tx.tx_type,
            account=tx.account,
            previous=tx.previous,
            link=tx.link,
            amount=tx.amount,
            signature=compressed_sig,
            tx_hash=tx_hash
        )
        
        return signed_tx


class TransactionChainBuilder:
    """
    Helper for building transaction chains for an account
    
    Maintains state of the account's frontier (latest transaction hash)
    to simplify creating sequential transactions.
    
    Example:
        >>> from src.core.crypto import generate_keypair
        >>> keypair = generate_keypair()
        >>> chain = TransactionChainBuilder(keypair)
        >>> 
        >>> # First transaction
        >>> tx1 = chain.send(recipient=bytes(32), amount=100)
        >>> 
        >>> # Second transaction (automatically uses tx1 hash as previous)
        >>> tx2 = chain.send(recipient=bytes(32), amount=50)
    """
    
    def __init__(self, keypair):
        """
        Initialize chain builder
        
        Args:
            keypair: Account keypair
        """
        self.keypair = keypair
        self.frontier = create_zeros_hash()  # Start with zeros
    
    def send(self, recipient: bytes, amount: int) -> Transaction:
        """
        Create SEND transaction using current frontier
        
        Args:
            recipient: Recipient public key
            amount: Amount to send
            
        Returns:
            Signed SEND transaction
        """
        tx = TransactionBuilder.create_send(
            sender_keypair=self.keypair,
            recipient_pubkey=recipient,
            amount=amount,
            previous_hash=self.frontier
        )
        
        # Update frontier
        self.frontier = tx.tx_hash
        
        return tx
    
    def receive(self, send_tx_hash: bytes, amount: int) -> Transaction:
        """
        Create RECEIVE transaction using current frontier
        
        Args:
            send_tx_hash: Hash of SEND transaction
            amount: Amount to receive
            
        Returns:
            Signed RECEIVE transaction
        """
        tx = TransactionBuilder.create_receive(
            receiver_keypair=self.keypair,
            send_tx_hash=send_tx_hash,
            amount=amount,
            previous_hash=self.frontier
        )
        
        # Update frontier
        self.frontier = tx.tx_hash
        
        return tx
    
    def get_frontier(self) -> bytes:
        """Get current frontier hash"""
        return self.frontier
    
    def set_frontier(self, frontier: bytes):
        """Set frontier hash (e.g., when loading existing account)"""
        if len(frontier) != 32:
            raise ValueError("Frontier must be 32 bytes")
        self.frontier = frontier
