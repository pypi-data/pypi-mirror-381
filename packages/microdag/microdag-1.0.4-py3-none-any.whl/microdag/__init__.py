"""
MicroDAG - Ultra-lightweight DAG blockchain for IoT and micropayments.

This package provides a complete blockchain implementation optimized for
resource-constrained environments like IoT devices.
"""

__version__ = "1.0.4"
__author__ = "MicroDAG Team"
__email__ = "team@microdag.org"

# Import main interface
from .core.dag import DAG
from .core.transaction import Transaction
from .network.p2p import P2PNetwork
from .storage.database import Database
from .consensus.pow import ProofOfWork
from .api.server import APIServer
from .cli.interface import CLI

class MicroDAG:
    """Main MicroDAG interface - ultra-lightweight blockchain"""
    
    def __init__(self, db_path: str = 'microdag.db'):
        self.dag = DAG()
        self.database = Database(db_path)
        self.network = P2PNetwork()
        self.consensus = ProofOfWork()
        self.api = APIServer()
        self.cli = CLI()
        self._balances = {}  # In-memory balance tracking
        self._load_balances()
    
    def start(self, port: int = 7076):
        """Start MicroDAG node"""
        self.api.start(port)
        self.network.start(port + 1)
        print(f"MicroDAG node started on port {port}")
    
    def send(self, to_address: str, amount: float, from_address: str = None) -> str:
        """Send transaction"""
        try:
            # If no from_address specified, use genesis account
            if from_address is None:
                from_address = "micro_6121e37cb53c82dc"  # Genesis account
            
            # Check if sender has sufficient balance
            sender_balance = self._balances.get(from_address, 0.0)
            if sender_balance < amount:
                raise ValueError(f"Insufficient balance: {sender_balance} < {amount}")
            
            tx = Transaction.create(to_address, amount)
            
            # Update balances
            self._update_balance(from_address, to_address, amount)
            
            # Add to DAG
            self.dag.add_transaction(tx.hash)
            
            # Store in database
            self.database.store(tx.hash, tx.pack())
            
            # Broadcast to network (if available)
            if hasattr(self.network, 'broadcast_transaction'):
                self.network.broadcast_transaction(tx.pack())
            
            return tx.hash.hex()
        except Exception as e:
            raise RuntimeError(f"Failed to send transaction: {e}") from e
    
    def balance(self, address: str = None) -> float:
        """Get balance for address"""
        if address:
            return self._balances.get(address, 0.0)
        return 0.0  # Default balance for new addresses
    
    def _load_balances(self):
        """Load balances from database"""
        try:
            # Try to load existing balances
            import json
            balance_data = self.database.load(b'balances')
            if balance_data:
                self._balances = json.loads(balance_data.decode())
            else:
                self._balances = {}
            
            # Initialize genesis account with full supply if not exists
            genesis_address = "micro_6121e37cb53c82dc"  # Derived from all-zero private key
            if genesis_address not in self._balances:
                self._balances[genesis_address] = 100_000_000.0  # 100M MICRO tokens
                self._save_balances()
        except Exception:
            # Fallback: initialize with genesis only
            genesis_address = "micro_6121e37cb53c82dc"
            self._balances = {genesis_address: 100_000_000.0}
    
    def _update_balance(self, from_address: str, to_address: str, amount: float):
        """Update balances after transaction"""
        # Deduct from sender
        if from_address in self._balances:
            self._balances[from_address] -= amount
        else:
            self._balances[from_address] = -amount  # Negative balance (debt)
        
        # Add to recipient
        if to_address in self._balances:
            self._balances[to_address] += amount
        else:
            self._balances[to_address] = amount
        
        # Save balances to database
        self._save_balances()
    
    def _save_balances(self):
        """Save balances to database"""
        try:
            import json
            balance_data = json.dumps(self._balances).encode()
            self.database.store(b'balances', balance_data)
        except Exception:
            pass

def connect(url: str = "http://localhost:7076") -> MicroDAG:
    """
    Connect to MicroDAG node (convenience function for IoT).
    
    Args:
        url: Node URL (for future remote connection support)
        
    Returns:
        MicroDAG: Connected MicroDAG instance
    """
    # For now, create local instance (future: support remote connections)
    return MicroDAG()

def main():
    """Main CLI entry point"""
    from .cli.interface import CLI
    cli = CLI()
    cli.run()

# Main exports
__all__ = [
    'MicroDAG',
    'connect',
    'DAG', 
    'Transaction',
    'P2PNetwork',
    'Database',
    'ProofOfWork',
    'APIServer',
    'CLI'
]
