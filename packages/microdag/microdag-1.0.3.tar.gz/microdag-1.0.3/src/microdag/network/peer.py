"""
Peer management - lightweight peer discovery and connection management.
"""
import time
from typing import Set, Tuple, Dict, Optional

class PeerManager:
    """Ultra-lightweight peer management"""
    
    def __init__(self):
        self._peers: Set[Tuple[str, int]] = set()
        self._connections: Dict[Tuple[str, int], float] = {}  # peer -> last_seen
        self._stats = {'messages_sent': 0, 'messages_received': 0}
    
    def add_peer(self, ip: str, port: int) -> None:
        """Add peer to network"""
        peer = (ip, port)
        self._peers.add(peer)
        self._connections[peer] = time.time()
    
    def remove_peer(self, ip: str, port: int) -> None:
        """Remove peer from network"""
        peer = (ip, port)
        self._peers.discard(peer)
        self._connections.pop(peer, None)
    
    def get_peers(self) -> Set[Tuple[str, int]]:
        """Get all peers"""
        return self._peers.copy()
    
    def get_active_peers(self, max_age: int = 300) -> Set[Tuple[str, int]]:
        """Get peers active within max_age seconds"""
        current_time = time.time()
        active_peers = set()
        
        for peer, last_seen in self._connections.items():
            if current_time - last_seen <= max_age:
                active_peers.add(peer)
        
        return active_peers
    
    def update_peer_activity(self, ip: str, port: int) -> None:
        """Update peer last seen time"""
        peer = (ip, port)
        if peer in self._peers:
            self._connections[peer] = time.time()
    
    def cleanup_old_peers(self, max_age: int = 600) -> int:
        """Remove peers not seen for max_age seconds"""
        current_time = time.time()
        to_remove = []
        
        for peer, last_seen in self._connections.items():
            if current_time - last_seen > max_age:
                to_remove.append(peer)
        
        for peer in to_remove:
            self._peers.discard(peer)
            self._connections.pop(peer, None)
        
        return len(to_remove)
    
    def get_peer_info(self, ip: str, port: int) -> Optional[Dict]:
        """Get peer information"""
        peer = (ip, port)
        if peer not in self._peers:
            return None
        
        last_seen = self._connections.get(peer, 0)
        return {
            'ip': ip,
            'port': port,
            'last_seen': last_seen,
            'age': time.time() - last_seen if last_seen else 0
        }
    
    def get_stats(self) -> Dict:
        """Get peer manager statistics"""
        return {
            **self._stats,
            'total_peers': len(self._peers),
            'active_peers': len(self.get_active_peers()),
            'oldest_peer': min(self._connections.values()) if self._connections else 0
        }
    
    def increment_message_count(self, sent: bool = True) -> None:
        """Increment message statistics"""
        if sent:
            self._stats['messages_sent'] += 1
        else:
            self._stats['messages_received'] += 1
