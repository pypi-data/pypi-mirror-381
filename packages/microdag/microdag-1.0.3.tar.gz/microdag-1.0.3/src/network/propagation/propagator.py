"""
Transaction Propagator
Broadcasts transactions to network using flood algorithm
"""

import logging
import threading
from typing import List

from ..protocol.message_types import Message, MessageType, create_publish_transaction_payload
from ..peers.peer_manager import PeerManager
from .deduplication import DuplicateDetector
from ...core.types.transaction import Transaction, serialize_transaction


logger = logging.getLogger(__name__)


class TransactionPropagator:
    """
    Transaction propagation using flood algorithm
    
    Specification: Section 4.3 - Transaction Propagation
    
    Flood Algorithm:
    1. Node receives new transaction
    2. Validates transaction
    3. If valid, forward to all connected peers
    4. Each peer does same (with duplicate detection)
    5. Transaction reaches entire network in <1 second
    
    Example:
        >>> propagator = TransactionPropagator(peer_manager)
        >>> 
        >>> # Broadcast transaction
        >>> propagator.broadcast(transaction)
    """
    
    def __init__(self, peer_manager: PeerManager):
        """
        Initialize transaction propagator
        
        Args:
            peer_manager: Peer manager instance
        """
        self.peer_manager = peer_manager
        self.duplicate_detector = DuplicateDetector()
        
        # Statistics
        self.broadcast_count = 0
        self.duplicate_count = 0
    
    def broadcast(self, tx: Transaction) -> int:
        """
        Broadcast transaction to all connected peers
        
        Args:
            tx: Transaction to broadcast
            
        Returns:
            Number of peers transaction was sent to
        """
        # Check for duplicate
        if self.duplicate_detector.is_duplicate(tx.tx_hash):
            self.duplicate_count += 1
            logger.debug(f"Skipping duplicate transaction: {tx.tx_hash.hex()[:16]}...")
            return 0
        
        # Mark as seen
        self.duplicate_detector.mark_seen(tx.tx_hash)
        
        # Serialize transaction
        tx_bytes = serialize_transaction(tx)
        
        # Create message
        payload = create_publish_transaction_payload(tx_bytes)
        message = Message(MessageType.PUBLISH_TRANSACTION, payload)
        
        # Get active peers
        peers = self.peer_manager.get_active_peers()
        
        if not peers:
            logger.warning("No active peers to broadcast to")
            return 0
        
        # Broadcast to all peers in parallel
        success_count = 0
        threads = []
        
        for peer in peers:
            thread = threading.Thread(
                target=self._send_to_peer,
                args=(peer, message),
                daemon=True
            )
            thread.start()
            threads.append(thread)
        
        # Wait for all sends to complete (with timeout)
        for thread in threads:
            thread.join(timeout=1.0)
            if not thread.is_alive():
                success_count += 1
        
        self.broadcast_count += 1
        logger.info(f"Broadcast transaction {tx.tx_hash.hex()[:16]}... to {success_count}/{len(peers)} peers")
        
        return success_count
    
    def _send_to_peer(self, peer, message: Message):
        """
        Send message to peer (runs in separate thread)
        
        Args:
            peer: Peer to send to
            message: Message to send
        """
        try:
            import socket
            
            # Create socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2.0)  # 2 second timeout
            
            # Connect
            sock.connect(peer.address)
            
            # Send message
            sock.sendall(message.to_bytes())
            
            # Close (no response expected for PUBLISH_TRANSACTION)
            sock.close()
            
            peer.mark_success()
            
        except Exception as e:
            logger.debug(f"Failed to send to {peer}: {e}")
            peer.mark_failure()
    
    def handle_received_transaction(self, tx: Transaction) -> bool:
        """
        Handle transaction received from peer
        
        Checks for duplicates and decides whether to rebroadcast.
        
        Args:
            tx: Received transaction
            
        Returns:
            True if transaction is new and should be processed
        """
        # Check for duplicate
        if self.duplicate_detector.is_duplicate(tx.tx_hash):
            self.duplicate_count += 1
            return False
        
        # Mark as seen
        self.duplicate_detector.mark_seen(tx.tx_hash)
        
        # New transaction - should be processed and rebroadcast
        return True
    
    def get_stats(self) -> dict:
        """Get propagation statistics"""
        detector_stats = self.duplicate_detector.get_stats()
        
        return {
            'broadcast_count': self.broadcast_count,
            'duplicate_count': self.duplicate_count,
            'seen_transactions': detector_stats['seen_count'],
            'active_peers': len(self.peer_manager.get_active_peers())
        }
