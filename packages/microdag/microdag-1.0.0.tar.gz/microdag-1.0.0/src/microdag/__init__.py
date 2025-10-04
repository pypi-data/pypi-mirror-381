"""
MicroDAG - Ultra-lightweight DAG blockchain for IoT and micropayments.

This package provides a complete blockchain implementation optimized for
resource-constrained environments like IoT devices.
"""

__version__ = "1.0.0"
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
    
    def start(self, port: int = 7076):
        """Start MicroDAG node"""
        self.api.start(port)
        self.network.start(port + 1)
        print(f"MicroDAG node started on port {port}")
    
    def send(self, to_address: str, amount: float) -> str:
        """Send transaction"""
        try:
            tx = Transaction.create(to_address, amount)
            
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
            return self.dag.get_balance(address)
        return 0.0  # Default balance for new addresses

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
