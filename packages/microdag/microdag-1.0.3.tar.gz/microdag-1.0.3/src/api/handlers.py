"""
API Request Handlers
Implements all 6 API endpoints
"""

import json
import logging
from typing import Optional

from ..core.types.transaction import deserialize_transaction, serialize_transaction
from ..core.types.account import encode_address


logger = logging.getLogger(__name__)


class APIHandler:
    """
    Handles HTTP API requests
    
    Specification: Section 7.1 - API Endpoints
    
    Endpoints:
    - GET /account/:address - Returns account state
    - GET /transaction/:hash - Returns transaction by hash
    - GET /pending/:address - Returns pending transactions
    - POST /broadcast - Broadcasts transaction
    - GET /peers - Returns peer list
    - GET /supply - Returns supply info
    
    Example:
        >>> handler = APIHandler(storage, propagator, peer_manager)
        >>> response = handler.handle_get_account(address)
    """
    
    def __init__(self, storage, propagator, peer_manager):
        """
        Initialize API handler
        
        Args:
            storage: LevelDBStorage instance
            propagator: TransactionPropagator instance
            peer_manager: PeerManager instance
        """
        self.storage = storage
        self.propagator = propagator
        self.peer_manager = peer_manager
    
    def handle_get_account(self, address: str) -> tuple[int, dict]:
        """
        GET /account/:address
        
        Returns account state
        Response: { "balance": 123456, "frontier": "0x..." }
        Status: 200 OK or 404 Not Found
        
        Args:
            address: Account address (micro_...)
            
        Returns:
            Tuple of (status_code, response_dict)
        """
        try:
            from ..core.types.account import decode_address
            
            # Decode address to public key
            public_key = decode_address(address)
            
            # Get account state
            state = self.storage.get_account(public_key)
            
            if state is None:
                return (404, {'error': 'Account not found'})
            
            return (200, {
                'balance': state.balance,
                'frontier': state.frontier.hex()
            })
        
        except Exception as e:
            logger.error(f"Error getting account: {e}")
            return (400, {'error': str(e)})
    
    def handle_get_transaction(self, tx_hash_hex: str) -> tuple[int, bytes]:
        """
        GET /transaction/:hash
        
        Returns transaction by hash
        Response: 141 bytes (raw transaction)
        Status: 200 OK or 404 Not Found
        
        Args:
            tx_hash_hex: Transaction hash (hex string)
            
        Returns:
            Tuple of (status_code, response_bytes)
        """
        try:
            # Parse hash
            tx_hash = bytes.fromhex(tx_hash_hex)
            
            # Get transaction
            tx = self.storage.get_transaction(tx_hash)
            
            if tx is None:
                return (404, b'')
            
            # Serialize transaction
            tx_bytes = serialize_transaction(tx)
            return (200, tx_bytes)
        
        except Exception as e:
            logger.error(f"Error getting transaction: {e}")
            return (400, b'')
    
    def handle_get_pending(self, address: str) -> tuple[int, dict]:
        """
        GET /pending/:address
        
        Returns pending transactions for account
        Response: ["0x...", "0x...", ...]
        Status: 200 OK
        
        Args:
            address: Account address (micro_...)
            
        Returns:
            Tuple of (status_code, response_dict)
        """
        try:
            from ..core.types.account import decode_address
            
            # Decode address
            public_key = decode_address(address)
            
            # Get pending transactions
            pending = self.storage.get_pending(public_key)
            
            # Convert to hex strings
            pending_hex = [h.hex() for h in pending]
            
            return (200, {'pending': pending_hex})
        
        except Exception as e:
            logger.error(f"Error getting pending: {e}")
            return (400, {'error': str(e)})
    
    def handle_broadcast(self, tx_bytes: bytes) -> tuple[int, dict]:
        """
        POST /broadcast
        
        Broadcasts transaction to network
        Body: 141 bytes (raw transaction)
        Response: { "hash": "0x..." }
        Status: 200 OK or 400 Bad Request
        
        Args:
            tx_bytes: Raw transaction bytes
            
        Returns:
            Tuple of (status_code, response_dict)
        """
        try:
            # Validate length
            if len(tx_bytes) != 141:
                return (400, {'error': 'Transaction must be 141 bytes'})
            
            # Deserialize transaction
            tx = deserialize_transaction(tx_bytes)
            
            # Broadcast to network
            peers_reached = self.propagator.broadcast(tx)
            
            return (200, {
                'hash': tx.tx_hash.hex(),
                'peers_reached': peers_reached
            })
        
        except Exception as e:
            logger.error(f"Error broadcasting transaction: {e}")
            return (400, {'error': str(e)})
    
    def handle_get_peers(self) -> tuple[int, dict]:
        """
        GET /peers
        
        Returns list of peer nodes
        Response: ["http://node1:7076", ...]
        Status: 200 OK
        
        Returns:
            Tuple of (status_code, response_dict)
        """
        try:
            # Get active peers
            peers = self.peer_manager.get_active_peers()
            
            # Format as URLs
            peer_urls = [f"http://{p.host}:{p.port}" for p in peers]
            
            return (200, {
                'peers': peer_urls,
                'count': len(peer_urls)
            })
        
        except Exception as e:
            logger.error(f"Error getting peers: {e}")
            return (500, {'error': str(e)})
    
    def handle_get_supply(self) -> tuple[int, dict]:
        """
        GET /supply
        
        Returns total supply info
        Response: { "total": 100000000, "circulating": 50000000 }
        Status: 200 OK
        
        Returns:
            Tuple of (status_code, response_dict)
        """
        try:
            from ..core.genesis import TOTAL_SUPPLY_BASE_UNITS, BASE_UNIT
            
            # Get genesis account balance
            genesis_pubkey = bytes(32)
            genesis_state = self.storage.get_account(genesis_pubkey)
            
            if genesis_state:
                genesis_balance = genesis_state.balance
            else:
                genesis_balance = 0
            
            # Calculate circulating supply
            circulating = TOTAL_SUPPLY_BASE_UNITS - genesis_balance
            
            return (200, {
                'total': TOTAL_SUPPLY_BASE_UNITS // BASE_UNIT,
                'total_base_units': TOTAL_SUPPLY_BASE_UNITS,
                'circulating': circulating // BASE_UNIT,
                'circulating_base_units': circulating,
                'decimals': 6
            })
        
        except Exception as e:
            logger.error(f"Error getting supply: {e}")
            return (500, {'error': str(e)})
