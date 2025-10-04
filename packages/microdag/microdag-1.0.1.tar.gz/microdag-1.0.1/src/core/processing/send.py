"""
SEND Transaction Processing
Implements specification Section 5.3 - Process SEND
"""

from ..types.transaction import Transaction
from ..types.account import AccountState


class SendProcessor:
    """
    Processes SEND transactions
    
    Specification: Section 5.3 - Process SEND
    
    def process_send(tx):
        # Update sender state
        account = get_account(tx.account)
        account.balance -= tx.amount
        account.frontier = tx.hash
        save_account(tx.account, account)
        
        # Add to pending for recipient
        add_pending(tx.link, tx.hash)
        
        # Store transaction
        save_transaction(tx.hash, tx)
        append_to_chain(tx.account, tx.hash)
    """
    
    def __init__(self, storage):
        """
        Initialize SEND processor
        
        Args:
            storage: LevelDBStorage instance
        """
        self.storage = storage
    
    def process(self, tx: Transaction):
        """
        Process SEND transaction
        
        Steps:
        1. Update sender's balance (subtract amount)
        2. Update sender's frontier (to this tx hash)
        3. Add to pending for recipient
        4. Store transaction
        5. Append to sender's chain
        
        Args:
            tx: SEND transaction to process
            
        Raises:
            ValueError: If transaction is not SEND type
        """
        if not tx.is_send:
            raise ValueError("Transaction must be SEND type")
        
        # Get sender account (or create if first transaction)
        account_state = self.storage.get_account(tx.account)
        
        if account_state is None:
            # First transaction - should not happen for SEND
            # (account must exist with balance)
            raise ValueError("Sender account does not exist")
        
        # Update sender state
        new_balance = account_state.balance - tx.amount
        new_state = AccountState(
            balance=new_balance,
            frontier=tx.tx_hash
        )
        
        # Save updated account state
        self.storage.put_account(tx.account, new_state)
        
        # Add to pending for recipient
        self.storage.add_pending(tx.link, tx.tx_hash)
        
        # Store transaction
        self.storage.put_transaction(tx)
        
        # Append to sender's chain
        self.storage.append_to_chain(tx.account, tx.tx_hash)


def process_send(tx: Transaction, storage) -> AccountState:
    """
    Standalone function to process SEND transaction
    
    Args:
        tx: SEND transaction
        storage: Storage instance
        
    Returns:
        Updated sender account state
    """
    processor = SendProcessor(storage)
    processor.process(tx)
    return storage.get_account(tx.account)
