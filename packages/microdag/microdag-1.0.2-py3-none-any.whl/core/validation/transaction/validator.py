"""
Transaction Validator
Implements the 5 validation rules from specification
"""

from dataclasses import dataclass
from typing import Optional, Callable
from enum import Enum

from ...types.transaction import Transaction, TransactionType
from ...crypto import verify


class ValidationError(Enum):
    """Validation error types"""
    INVALID_SIGNATURE = "Invalid signature"
    INVALID_PREVIOUS = "Invalid previous hash"
    INSUFFICIENT_BALANCE = "Insufficient balance"
    INVALID_LINK = "Invalid link"
    DUPLICATE_TRANSACTION = "Duplicate transaction"
    INVALID_STRUCTURE = "Invalid transaction structure"


@dataclass
class ValidationResult:
    """
    Result of transaction validation
    
    Attributes:
        valid: Whether transaction is valid
        error: Error type if invalid
        message: Detailed error message
    """
    valid: bool
    error: Optional[ValidationError] = None
    message: Optional[str] = None
    
    @staticmethod
    def success() -> 'ValidationResult':
        """Create successful validation result"""
        return ValidationResult(valid=True)
    
    @staticmethod
    def failure(error: ValidationError, message: str = None) -> 'ValidationResult':
        """Create failed validation result"""
        return ValidationResult(
            valid=False,
            error=error,
            message=message or error.value
        )


class TransactionValidator:
    """
    Validates transactions according to specification
    
    Specification: Section 5.2 - Transaction Validation Rules
    
    Rule 1: Signature Valid
    Rule 2: Previous Hash Valid
    Rule 3: Balance Valid (SEND)
    Rule 4: Link Valid (RECEIVE)
    Rule 5: No Duplicate
    
    Example:
        >>> from src.core.types.transaction import TransactionBuilder
        >>> from src.core.crypto import generate_keypair
        >>> 
        >>> keypair = generate_keypair()
        >>> tx = TransactionBuilder.create_send(...)
        >>> 
        >>> validator = TransactionValidator(
        ...     get_account=lambda pk: account_state,
        ...     get_transaction=lambda h: transaction,
        ...     transaction_exists=lambda h: False
        ... )
        >>> 
        >>> result = validator.validate(tx)
        >>> if result.valid:
        ...     print("Transaction is valid")
    """
    
    def __init__(
        self,
        get_account: Callable[[bytes], Optional[dict]],
        get_transaction: Callable[[bytes], Optional[Transaction]],
        transaction_exists: Callable[[bytes], bool],
        get_pending: Callable[[bytes, bytes], bool] = None
    ):
        """
        Initialize validator with database access functions
        
        Args:
            get_account: Function to get account state by public key
                Returns dict with 'balance' and 'frontier' or None
            get_transaction: Function to get transaction by hash
            transaction_exists: Function to check if transaction exists
            get_pending: Function to check if pending transaction exists
        """
        self.get_account = get_account
        self.get_transaction = get_transaction
        self.transaction_exists = transaction_exists
        self.get_pending = get_pending or (lambda pk, h: True)
    
    def validate(self, tx: Transaction) -> ValidationResult:
        """
        Validate transaction against all rules
        
        Args:
            tx: Transaction to validate
            
        Returns:
            ValidationResult indicating success or failure
        """
        # Rule 1: Signature Valid
        result = self.validate_signature(tx)
        if not result.valid:
            return result
        
        # Rule 2: Previous Hash Valid
        result = self.validate_previous_hash(tx)
        if not result.valid:
            return result
        
        # Rule 3: Balance Valid (SEND only)
        if tx.is_send:
            result = self.validate_balance(tx)
            if not result.valid:
                return result
        
        # Rule 4: Link Valid (RECEIVE only)
        if tx.is_receive:
            result = self.validate_link(tx)
            if not result.valid:
                return result
        
        # Rule 5: No Duplicate
        result = self.validate_no_duplicate(tx)
        if not result.valid:
            return result
        
        return ValidationResult.success()
    
    def validate_signature(self, tx: Transaction) -> ValidationResult:
        """
        Rule 1: Signature Valid
        
        Specification:
        Ed25519.verify(tx.signature, tx.hash, tx.account) == true
        
        Args:
            tx: Transaction to validate
            
        Returns:
            ValidationResult
        """
        from ...types.transaction import serialize_transaction
        
        try:
            # Serialize full transaction
            tx_bytes = serialize_transaction(tx)
            
            # Verify signature
            if not verify(tx.tx_hash, tx.signature, tx.account):
                return ValidationResult.failure(
                    ValidationError.INVALID_SIGNATURE,
                    "Ed25519 signature verification failed"
                )
            
            return ValidationResult.success()
            
        except Exception as e:
            return ValidationResult.failure(
                ValidationError.INVALID_SIGNATURE,
                f"Signature verification error: {str(e)}"
            )
    
    def validate_previous_hash(self, tx: Transaction) -> ValidationResult:
        """
        Rule 2: Previous Hash Valid
        
        Specification:
        If first tx: previous == zeros
        Else: previous == account.frontier
        
        Args:
            tx: Transaction to validate
            
        Returns:
            ValidationResult
        """
        account = self.get_account(tx.account)
        
        # First transaction in account's chain
        if tx.is_first_transaction:
            if account is not None and account['frontier'] != bytes(32):
                return ValidationResult.failure(
                    ValidationError.INVALID_PREVIOUS,
                    "First transaction but account already exists"
                )
            return ValidationResult.success()
        
        # Subsequent transaction
        if account is None:
            return ValidationResult.failure(
                ValidationError.INVALID_PREVIOUS,
                "Account does not exist but previous hash is not zeros"
            )
        
        if tx.previous != account['frontier']:
            return ValidationResult.failure(
                ValidationError.INVALID_PREVIOUS,
                f"Previous hash does not match account frontier. "
                f"Expected: {account['frontier'].hex()[:16]}..., "
                f"Got: {tx.previous.hex()[:16]}..."
            )
        
        return ValidationResult.success()
    
    def validate_balance(self, tx: Transaction) -> ValidationResult:
        """
        Rule 3: Balance Valid (SEND)
        
        Specification:
        new_balance = account.balance - tx.amount
        new_balance >= 0
        
        Args:
            tx: SEND transaction to validate
            
        Returns:
            ValidationResult
        """
        if not tx.is_send:
            return ValidationResult.success()
        
        account = self.get_account(tx.account)
        
        if account is None:
            return ValidationResult.failure(
                ValidationError.INSUFFICIENT_BALANCE,
                "Account does not exist"
            )
        
        new_balance = account['balance'] - tx.amount
        
        if new_balance < 0:
            return ValidationResult.failure(
                ValidationError.INSUFFICIENT_BALANCE,
                f"Insufficient balance. "
                f"Balance: {account['balance']}, "
                f"Amount: {tx.amount}, "
                f"Deficit: {-new_balance}"
            )
        
        return ValidationResult.success()
    
    def validate_link(self, tx: Transaction) -> ValidationResult:
        """
        Rule 4: Link Valid (RECEIVE)
        
        Specification:
        send_tx = get_transaction(tx.link)
        send_tx exists
        send_tx.type == SEND
        send_tx.link == tx.account (recipient matches)
        tx.amount == send_tx.amount
        pending(tx.account, tx.link) exists
        
        Args:
            tx: RECEIVE transaction to validate
            
        Returns:
            ValidationResult
        """
        if not tx.is_receive:
            return ValidationResult.success()
        
        # Get corresponding SEND transaction
        send_tx = self.get_transaction(tx.link)
        
        if send_tx is None:
            return ValidationResult.failure(
                ValidationError.INVALID_LINK,
                f"SEND transaction not found: {tx.link.hex()[:16]}..."
            )
        
        # Check SEND transaction type
        if not send_tx.is_send:
            return ValidationResult.failure(
                ValidationError.INVALID_LINK,
                "Linked transaction is not a SEND"
            )
        
        # Check recipient matches
        if send_tx.link != tx.account:
            return ValidationResult.failure(
                ValidationError.INVALID_LINK,
                f"Recipient mismatch. "
                f"SEND recipient: {send_tx.link.hex()[:16]}..., "
                f"RECEIVE account: {tx.account.hex()[:16]}..."
            )
        
        # Check amounts match
        if tx.amount != send_tx.amount:
            return ValidationResult.failure(
                ValidationError.INVALID_LINK,
                f"Amount mismatch. "
                f"SEND amount: {send_tx.amount}, "
                f"RECEIVE amount: {tx.amount}"
            )
        
        # Check pending exists
        if not self.get_pending(tx.account, tx.link):
            return ValidationResult.failure(
                ValidationError.INVALID_LINK,
                "Pending transaction not found"
            )
        
        return ValidationResult.success()
    
    def validate_no_duplicate(self, tx: Transaction) -> ValidationResult:
        """
        Rule 5: No Duplicate
        
        Specification:
        tx.hash not in transactions table
        
        Args:
            tx: Transaction to validate
            
        Returns:
            ValidationResult
        """
        if self.transaction_exists(tx.tx_hash):
            return ValidationResult.failure(
                ValidationError.DUPLICATE_TRANSACTION,
                f"Transaction already exists: {tx.tx_hash.hex()[:16]}..."
            )
        
        return ValidationResult.success()
