"""
Transaction Processor
Main entry point for processing transactions
"""

from typing import Optional
from ..types.transaction import Transaction
from ..types.account import AccountState
from ..validation.transaction import TransactionValidator, ValidationResult
from .send import SendProcessor
from .receive import ReceiveProcessor


class TransactionProcessor:
    """
    Main transaction processor
    
    Specification: Section 5.3 - Transaction Processing
    
    Validates and processes SEND and RECEIVE transactions,
    updating account states and database accordingly.
    
    Example:
        >>> from src.storage import LevelDBStorage
        >>> 
        >>> db = LevelDBStorage("./data")
        >>> db.open()
        >>> 
        >>> processor = TransactionProcessor(db)
        >>> result = processor.process(transaction)
        >>> 
        >>> if result.valid:
        ...     print("Transaction processed successfully")
        >>> else:
        ...     print(f"Error: {result.message}")
    """
    
    def __init__(self, storage):
        """
        Initialize transaction processor
        
        Args:
            storage: LevelDBStorage instance
        """
        self.storage = storage
        
        # Create validator
        self.validator = TransactionValidator(
            get_account=self._get_account_for_validation,
            get_transaction=lambda h: storage.get_transaction(h),
            transaction_exists=lambda h: storage.transaction_exists(h),
            get_pending=lambda pk, h: storage.pending_exists(pk, h)
        )
        
        # Create processors
        self.send_processor = SendProcessor(storage)
        self.receive_processor = ReceiveProcessor(storage)
    
    def process(self, tx: Transaction) -> ValidationResult:
        """
        Process transaction (validate and execute)
        
        Args:
            tx: Transaction to process
            
        Returns:
            ValidationResult indicating success or failure
        """
        # Validate transaction
        result = self.validator.validate(tx)
        if not result.valid:
            return result
        
        # Process based on type
        try:
            if tx.is_send:
                self.send_processor.process(tx)
            else:  # RECEIVE
                self.receive_processor.process(tx)
            
            return ValidationResult.success()
            
        except Exception as e:
            from ..validation.transaction import ValidationError
            return ValidationResult.failure(
                ValidationError.INVALID_STRUCTURE,
                f"Processing error: {str(e)}"
            )
    
    def _get_account_for_validation(self, public_key: bytes) -> Optional[dict]:
        """
        Get account state for validation
        
        Returns dict with 'balance' and 'frontier' or None
        """
        state = self.storage.get_account(public_key)
        if state is None:
            return None
        
        return {
            'balance': state.balance,
            'frontier': state.frontier
        }
