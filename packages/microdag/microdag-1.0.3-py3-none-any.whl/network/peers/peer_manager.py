"""
Peer Manager
Manages peer connections and discovery
"""

import socket
import time
import logging
from typing import Optional, List

from .peer_info import PeerInfo, PeerStatus
from ..protocol.message_types import Message, MessageType, create_ping_payload


logger = logging.getLogger(__name__)


# Default seed nodes (hardcoded as per specification)
DEFAULT_SEED_NODES = [
    ('seed1.microdag.io', 7075),
    ('seed2.microdag.io', 7075),
    ('seed3.microdag.io', 7075),
    ('seed4.microdag.io', 7075),
    ('seed5.microdag.io', 7075),
]


class PeerManager:
    """
    Peer connection manager
    
    Specification: Section 4.2 - Peer Discovery
    
    Bootstrap:
    1. Hardcode 5 seed node IPs in source code
    2. Connect to seed nodes on startup
    3. Request peers via REQUEST_PEERS
    4. Store up to 1000 known peers in memory
    5. Periodically ping peers, remove dead ones
    
    Peer Maintenance:
    - Keep 32 active connections
    - Replace dead peers automatically
    - Prioritize peers with low latency
    - No DHT (too complex)
    
    Example:
        >>> manager = PeerManager()
        >>> manager.bootstrap()
        >>> 
        >>> # Get active peers
        >>> peers = manager.get_active_peers()
        >>> print(f"Connected to {len(peers)} peers")
    """
    
    def __init__(
        self,
        max_peers: int = 1000,
        target_connections: int = 32,
        seed_nodes: Optional[List[tuple[str, int]]] = None
    ):
        """
        Initialize peer manager
        
        Args:
            max_peers: Maximum peers to track (default: 1000)
            target_connections: Target active connections (default: 32)
            seed_nodes: Seed node addresses (optional)
        """
        self.max_peers = max_peers
        self.target_connections = target_connections
        self.seed_nodes = seed_nodes or DEFAULT_SEED_NODES
        
        # Peer storage
        self.peers: dict[tuple[str, int], PeerInfo] = {}
        
        # Add seed nodes
        for host, port in self.seed_nodes:
            self.add_peer(host, port)
    
    def add_peer(self, host: str, port: int) -> PeerInfo:
        """
        Add peer to known peers
        
        Args:
            host: Peer IP address
            port: Peer port
            
        Returns:
            PeerInfo object
        """
        address = (host, port)
        
        if address in self.peers:
            return self.peers[address]
        
        # Check if we have room
        if len(self.peers) >= self.max_peers:
            # Remove oldest dead peer
            self._remove_dead_peers()
            
            if len(self.peers) >= self.max_peers:
                logger.warning("Peer list full, cannot add new peer")
                return None
        
        # Create peer info
        peer = PeerInfo(host=host, port=port)
        self.peers[address] = peer
        
        logger.debug(f"Added peer: {peer}")
        return peer
    
    def get_peer(self, host: str, port: int) -> Optional[PeerInfo]:
        """Get peer by address"""
        return self.peers.get((host, port))
    
    def get_all_peers(self) -> List[PeerInfo]:
        """Get all known peers"""
        return list(self.peers.values())
    
    def get_active_peers(self) -> List[PeerInfo]:
        """Get connected peers"""
        return [p for p in self.peers.values() if p.is_connected]
    
    def get_alive_peers(self) -> List[PeerInfo]:
        """Get recently active peers"""
        return [p for p in self.peers.values() if p.is_alive]
    
    def bootstrap(self):
        """
        Bootstrap from seed nodes
        
        Connects to seed nodes and requests peer lists.
        """
        logger.info("Bootstrapping from seed nodes...")
        
        for host, port in self.seed_nodes:
            try:
                # Try to connect and ping
                peer = self.get_peer(host, port)
                if peer:
                    self.ping_peer(peer)
                    
                    # Request peers
                    self.request_peers(peer)
            
            except Exception as e:
                logger.error(f"Failed to bootstrap from {host}:{port}: {e}")
        
        logger.info(f"Bootstrap complete. Known peers: {len(self.peers)}")
    
    def ping_peer(self, peer: PeerInfo) -> bool:
        """
        Ping peer to check connectivity
        
        Args:
            peer: Peer to ping
            
        Returns:
            True if ping successful
        """
        try:
            # Create ping message
            timestamp = int(time.time() * 1000)
            payload = create_ping_payload(timestamp)
            message = Message(MessageType.PING, payload)
            
            # Send ping
            start_time = time.time()
            response = self._send_message(peer, message)
            latency = (time.time() - start_time) * 1000  # Convert to ms
            
            if response and response.msg_type == MessageType.PING:
                # Ping successful
                peer.update_latency(latency)
                peer.mark_success()
                return True
            
        except Exception as e:
            logger.debug(f"Ping failed for {peer}: {e}")
        
        peer.mark_failure()
        return False
    
    def request_peers(self, peer: PeerInfo) -> List[PeerInfo]:
        """
        Request peer list from peer
        
        Args:
            peer: Peer to request from
            
        Returns:
            List of new peers discovered
        """
        try:
            # Create request message
            from ..protocol.message_types import create_request_peers_payload
            payload = create_request_peers_payload()
            message = Message(MessageType.REQUEST_PEERS, payload)
            
            # Send request
            response = self._send_message(peer, message)
            
            if response and response.msg_type == MessageType.REQUEST_PEERS:
                # Parse peer list
                new_peers = []
                payload = response.payload
                
                # Each peer is 6 bytes (4 bytes IP + 2 bytes port)
                for i in range(0, len(payload), 6):
                    if i + 6 > len(payload):
                        break
                    
                    # Parse IP and port
                    ip_bytes = payload[i:i+4]
                    port_bytes = payload[i+4:i+6]
                    
                    import struct
                    ip = '.'.join(str(b) for b in ip_bytes)
                    port = struct.unpack('<H', port_bytes)[0]
                    
                    # Add peer
                    new_peer = self.add_peer(ip, port)
                    if new_peer:
                        new_peers.append(new_peer)
                
                logger.info(f"Discovered {len(new_peers)} new peers from {peer}")
                return new_peers
        
        except Exception as e:
            logger.error(f"Failed to request peers from {peer}: {e}")
        
        return []
    
    def maintain_connections(self):
        """
        Maintain target number of connections
        
        - Ping existing peers
        - Remove dead peers
        - Connect to new peers if needed
        """
        # Ping all connected peers
        for peer in self.get_active_peers():
            self.ping_peer(peer)
        
        # Remove dead peers
        self._remove_dead_peers()
        
        # Connect to new peers if below target
        active_count = len(self.get_active_peers())
        if active_count < self.target_connections:
            needed = self.target_connections - active_count
            
            # Try to connect to disconnected peers
            disconnected = [p for p in self.peers.values() 
                          if p.status == PeerStatus.DISCONNECTED]
            
            # Sort by latency (prefer low latency)
            disconnected.sort(key=lambda p: p.latency_ms if p.latency_ms > 0 else 999999)
            
            for peer in disconnected[:needed]:
                self.ping_peer(peer)
    
    def _send_message(self, peer: PeerInfo, message: Message) -> Optional[Message]:
        """
        Send message to peer and wait for response
        
        Args:
            peer: Peer to send to
            message: Message to send
            
        Returns:
            Response message or None
        """
        try:
            # Create socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5.0)  # 5 second timeout
            
            # Connect
            sock.connect(peer.address)
            
            # Send message
            sock.sendall(message.to_bytes())
            
            # Receive response header (3 bytes)
            header = self._recv_exact(sock, 3)
            if not header:
                return None
            
            # Parse payload length
            import struct
            payload_length = struct.unpack('<H', header[1:3])[0]
            
            # Receive payload
            payload = self._recv_exact(sock, payload_length)
            if not payload:
                return None
            
            # Parse response
            response_data = header + payload
            response = Message.from_bytes(response_data)
            
            sock.close()
            return response
        
        except Exception as e:
            logger.debug(f"Failed to send message to {peer}: {e}")
            return None
    
    def _recv_exact(self, sock: socket.socket, n: int) -> Optional[bytes]:
        """Receive exactly n bytes"""
        data = bytearray()
        while len(data) < n:
            chunk = sock.recv(n - len(data))
            if not chunk:
                return None
            data.extend(chunk)
        return bytes(data)
    
    def _remove_dead_peers(self):
        """Remove failed and old peers"""
        to_remove = []
        
        for address, peer in self.peers.items():
            # Remove if failed or not seen in 24 hours
            if peer.status == PeerStatus.FAILED or \
               (time.time() - peer.last_seen > 86400):
                to_remove.append(address)
        
        for address in to_remove:
            del self.peers[address]
            logger.debug(f"Removed dead peer: {address}")
    
    def get_stats(self) -> dict:
        """Get peer statistics"""
        return {
            'total_peers': len(self.peers),
            'active_peers': len(self.get_active_peers()),
            'alive_peers': len(self.get_alive_peers()),
            'target_connections': self.target_connections,
            'avg_latency': sum(p.latency_ms for p in self.get_active_peers()) / 
                          max(len(self.get_active_peers()), 1)
        }
