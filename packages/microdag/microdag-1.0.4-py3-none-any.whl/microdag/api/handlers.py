"""
API request handlers - lightweight endpoint implementations.
"""
import json
from typing import Dict, Any, Optional
from ..core.transaction import Transaction
from ..utils.hash import hex_to_hash, hash_to_hex
from ..utils.validation import validate_address, validate_amount

class APIHandlers:
    """Ultra-lightweight API request handlers"""
    
    def __init__(self, dag=None, database=None, network=None):
        self.dag = dag
        self.database = database
        self.network = network
    
    def health(self) -> Dict[str, Any]:
        """Health check endpoint"""
        return {
            'status': 'ok',
            'service': 'MicroDAG',
            'version': '1.0.0',
            'timestamp': int(__import__('time').time())
        }
    
    def stats(self) -> Dict[str, Any]:
        """Get system statistics"""
        stats = {'dag': {}, 'storage': {}, 'network': {}}
        
        if self.dag:
            stats['dag'] = self.dag.get_stats()
        
        if self.database:
            stats['storage'] = self.database.get_stats()
        
        if self.network:
            stats['network'] = self.network.get_stats()
        
        return stats
    
    def get_tips(self) -> Dict[str, Any]:
        """Get DAG tips"""
        if not self.dag:
            return {'error': 'DAG not available', 'status': 503}
        
        tips = self.dag.get_tips()
        return {
            'tips': [hash_to_hex(tip) for tip in tips],
            'count': len(tips)
        }
    
    def get_transaction(self, tx_hash_hex: str) -> Dict[str, Any]:
        """Get transaction by hash"""
        if not self.database:
            return {'error': 'Database not available', 'status': 503}
        
        try:
            tx_hash = hex_to_hash(tx_hash_hex)
            tx_data = self.database.load(tx_hash)
            
            if not tx_data:
                return {'error': 'Transaction not found', 'status': 404}
            
            # Parse transaction
            tx = Transaction.unpack(tx_data)
            
            return {
                'hash': hash_to_hex(tx.hash),
                'from_address': f"micro_{tx.from_addr.hex()[:16]}",
                'to_address': f"micro_{tx.to_addr.hex()[:16]}",
                'amount': tx.get_amount_float(),
                'timestamp': tx.timestamp,
                'parents': [
                    hash_to_hex(tx.parent1) if tx.parent1 != b'\x00' * 32 else None,
                    hash_to_hex(tx.parent2) if tx.parent2 != b'\x00' * 32 else None
                ]
            }
        
        except Exception as e:
            return {'error': f'Invalid transaction hash: {str(e)}', 'status': 400}
    
    def create_transaction(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """Create new transaction"""
        if not body:
            return {'error': 'Request body required', 'status': 400}
        
        # Validate required fields
        required_fields = ['to_address', 'amount']
        for field in required_fields:
            if field not in body:
                return {'error': f'Missing required field: {field}', 'status': 400}
        
        to_address = body['to_address']
        amount = body.get('amount', 0)
        
        # Validate inputs
        if not validate_address(to_address):
            return {'error': 'Invalid to_address format', 'status': 400}
        
        if not validate_amount(amount):
            return {'error': 'Invalid amount', 'status': 400}
        
        try:
            # Get current tips as parents
            parents = (b'\x00' * 32, b'\x00' * 32)
            if self.dag:
                tips = list(self.dag.get_tips())
                if tips:
                    parents = (tips[0], tips[1] if len(tips) > 1 else b'\x00' * 32)
            
            # Create transaction
            tx = Transaction.create(to_address, amount, parents)
            
            # Add to DAG
            if self.dag:
                parent_set = {p for p in parents if p != b'\x00' * 32}
                self.dag.add_transaction(tx.hash, parent_set)
            
            # Store in database
            if self.database:
                self.database.store(tx.hash, tx.pack())
            
            # Broadcast to network
            if self.network:
                self.network.broadcast_transaction(tx.pack())
            
            return {
                'hash': hash_to_hex(tx.hash),
                'status': 'created',
                'amount': tx.get_amount_float(),
                'to_address': to_address
            }
        
        except Exception as e:
            return {'error': f'Transaction creation failed: {str(e)}', 'status': 500}
    
    def get_peers(self) -> Dict[str, Any]:
        """Get network peers"""
        if not self.network:
            return {'error': 'Network not available', 'status': 503}
        
        peers = self.network.peer_manager.get_peers()
        active_peers = self.network.peer_manager.get_active_peers()
        
        return {
            'total_peers': len(peers),
            'active_peers': len(active_peers),
            'peers': [{'ip': ip, 'port': port} for ip, port in peers]
        }
    
    def add_peer(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """Add network peer"""
        if not self.network:
            return {'error': 'Network not available', 'status': 503}
        
        if not body:
            return {'error': 'Request body required', 'status': 400}
        
        ip = body.get('ip')
        port = body.get('port')
        
        if not ip or not port:
            return {'error': 'ip and port required', 'status': 400}
        
        try:
            self.network.add_peer(ip, int(port))
            return {
                'status': 'added',
                'peer': {'ip': ip, 'port': port}
            }
        
        except Exception as e:
            return {'error': f'Failed to add peer: {str(e)}', 'status': 500}
