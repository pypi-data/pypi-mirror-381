"""
RECEIVE Transaction Processing
Implements specification Section 5.3 - Process RECEIVE
"""

from ..types.transaction import Transaction
from ..types.account import AccountState


class ReceiveProcessor:
    """
    Processes RECEIVE transactions
    
    Specification: Section 5.3 - Process RECEIVE
    
    def process_receive(tx):
        # Get corresponding SEND
        send_tx = get_transaction(tx.link)
        
        # Update receiver state
        account = get_account(tx.account)
        account.balance += tx.amount
        account.frontier = tx.hash
        save_account(tx.account, account)
        
        # Remove from pending
        remove_pending(tx.account, tx.link)
        
        # Store transaction
        save_transaction(tx.hash, tx)
        append_to_chain(tx.account, tx.hash)
    """
    
    def __init__(self, storage):
        """
        Initialize RECEIVE processor
        
        Args:
            storage: LevelDBStorage instance
        """
        self.storage = storage
    
    def process(self, tx: Transaction):
        """
        Process RECEIVE transaction
        
        Steps:
        1. Get corresponding SEND transaction
        2. Update receiver's balance (add amount)
        3. Update receiver's frontier (to this tx hash)
        4. Remove from pending
        5. Store transaction
        6. Append to receiver's chain
        
        Args:
            tx: RECEIVE transaction to process
            
        Raises:
            ValueError: If transaction is not RECEIVE type
            ValueError: If SEND transaction not found
        """
        if not tx.is_receive:
            raise ValueError("Transaction must be RECEIVE type")
        
        # Get corresponding SEND transaction
        send_tx = self.storage.get_transaction(tx.link)
        if send_tx is None:
            raise ValueError(f"SEND transaction not found: {tx.link.hex()}")
        
        # Get receiver account (or create if first transaction)
        account_state = self.storage.get_account(tx.account)
        
        if account_state is None:
            # First transaction - create new account
            account_state = AccountState(
                balance=0,
                frontier=bytes(32)
            )
        
        # Update receiver state
        new_balance = account_state.balance + tx.amount
        new_state = AccountState(
            balance=new_balance,
            frontier=tx.tx_hash
        )
        
        # Save updated account state
        self.storage.put_account(tx.account, new_state)
        
        # Remove from pending
        self.storage.remove_pending(tx.account, tx.link)
        
        # Store transaction
        self.storage.put_transaction(tx)
        
        # Append to receiver's chain
        self.storage.append_to_chain(tx.account, tx.tx_hash)


def process_receive(tx: Transaction, storage) -> AccountState:
    """
    Standalone function to process RECEIVE transaction
    
    Args:
        tx: RECEIVE transaction
        storage: Storage instance
        
    Returns:
        Updated receiver account state
    """
    processor = ReceiveProcessor(storage)
    processor.process(tx)
    return storage.get_account(tx.account)
