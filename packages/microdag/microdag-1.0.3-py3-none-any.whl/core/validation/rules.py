"""
Validation Rules Module
Individual validation rules for MicroDAG transactions and accounts
"""

from typing import Dict, Any, Optional
from ..crypto import verify
from ..types.transaction import Transaction


def validate_signature(transaction: Dict[str, Any], public_key: bytes) -> bool:
    """Validate transaction signature"""
    try:
        # Extract signature and transaction data
        signature = transaction.get('signature')
        if not signature:
            return False
        
        # Create transaction hash for verification
        tx_data = {k: v for k, v in transaction.items() if k != 'signature'}
        tx_bytes = str(tx_data).encode('utf-8')
        
        # Verify signature
        return verify(public_key, tx_bytes, signature)
    except Exception:
        return False


def validate_previous_hash(transaction: Dict[str, Any], account_state: Dict[str, Any]) -> bool:
    """Validate previous transaction hash"""
    try:
        previous_hash = transaction.get('previous_hash')
        expected_hash = account_state.get('last_transaction_hash')
        
        # Genesis transactions have no previous hash
        if transaction.get('type') == 'genesis':
            return previous_hash is None or previous_hash == '0' * 64
        
        return previous_hash == expected_hash
    except Exception:
        return False


def validate_balance(transaction: Dict[str, Any], account_state: Dict[str, Any]) -> bool:
    """Validate account balance for transaction"""
    try:
        tx_type = transaction.get('type')
        amount = int(transaction.get('amount', 0))
        current_balance = int(account_state.get('balance', 0))
        
        if tx_type == 'send':
            # Must have sufficient balance
            return current_balance >= amount
        elif tx_type == 'receive':
            # Receiving always valid (increases balance)
            return True
        elif tx_type == 'genesis':
            # Genesis creates initial balance
            return amount > 0
        
        return False
    except Exception:
        return False


def validate_link(transaction: Dict[str, Any]) -> bool:
    """Validate transaction link (for receive transactions)"""
    try:
        tx_type = transaction.get('type')
        
        if tx_type == 'receive':
            # Receive transactions must have a link to send transaction
            link = transaction.get('link')
            return link is not None and len(link) == 64  # 64-char hex hash
        
        # Other transaction types don't require links
        return True
    except Exception:
        return False


def validate_no_duplicate(transaction: Dict[str, Any], existing_transactions: list) -> bool:
    """Validate no duplicate transaction"""
    try:
        tx_hash = transaction.get('hash')
        if not tx_hash:
            return False
        
        # Check if transaction hash already exists
        existing_hashes = {tx.get('hash') for tx in existing_transactions}
        return tx_hash not in existing_hashes
    except Exception:
        return False


def validate_account_format(account: str) -> bool:
    """Validate account address format"""
    try:
        # MicroDAG accounts start with 'micro_' and are 58 characters total
        if not account.startswith('micro_'):
            return False
        
        if len(account) != 58:
            return False
        
        # Check that the rest is valid base32
        account_part = account[6:]  # Remove 'micro_' prefix
        
        # Basic validation - should be alphanumeric
        return account_part.replace('_', '').isalnum()
    except Exception:
        return False


def validate_amount_format(amount: Any) -> bool:
    """Validate amount format"""
    try:
        # Amount should be a positive integer (in base units)
        if isinstance(amount, str):
            amount = int(amount)
        
        return isinstance(amount, int) and amount > 0
    except Exception:
        return False


def validate_transaction_structure(transaction: Dict[str, Any]) -> bool:
    """Validate basic transaction structure"""
    try:
        required_fields = ['type', 'account', 'signature']
        
        # Check required fields exist
        for field in required_fields:
            if field not in transaction:
                return False
        
        # Validate transaction type
        valid_types = ['send', 'receive', 'genesis']
        if transaction['type'] not in valid_types:
            return False
        
        # Type-specific validation
        tx_type = transaction['type']
        
        if tx_type == 'send':
            required_send_fields = ['destination', 'amount']
            for field in required_send_fields:
                if field not in transaction:
                    return False
        
        elif tx_type == 'receive':
            if 'link' not in transaction:
                return False
        
        elif tx_type == 'genesis':
            if 'amount' not in transaction:
                return False
        
        return True
    except Exception:
        return False
