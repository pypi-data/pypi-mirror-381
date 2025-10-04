"""
P2P networking - lightweight peer-to-peer communication.
"""
import socket
import threading
from typing import Callable, Optional
from .protocol import MessageProtocol, MessageType
from .peer import PeerManager

class P2PNetwork:
    """Ultra-lightweight P2P network"""
    
    def __init__(self):
        self.peer_manager = PeerManager()
        self.protocol = MessageProtocol()
        self._server_socket: Optional[socket.socket] = None
        self._running = False
        self._handlers = {}
    
    def start(self, port: int) -> None:
        """Start P2P server"""
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server_socket.bind(('0.0.0.0', port))
        self._server_socket.listen(5)
        self._running = True
        
        # Start server thread
        server_thread = threading.Thread(target=self._server_loop, daemon=True)
        server_thread.start()
        
        print(f"P2P server started on port {port}")
    
    def stop(self) -> None:
        """Stop P2P server"""
        self._running = False
        if self._server_socket:
            self._server_socket.close()
    
    def _server_loop(self) -> None:
        """Main server loop"""
        while self._running:
            try:
                conn, addr = self._server_socket.accept()
                client_thread = threading.Thread(
                    target=self._handle_client, 
                    args=(conn, addr), 
                    daemon=True
                )
                client_thread.start()
            except:
                break
    
    def _handle_client(self, conn: socket.socket, addr) -> None:
        """Handle client connection"""
        try:
            data = conn.recv(1024)
            if data:
                result = self.protocol.unpack_message(data)
                if result:
                    msg_type, timestamp, payload = result
                    self._process_message(msg_type, payload, addr[0], addr[1])
                    self.peer_manager.increment_message_count(sent=False)
        except:
            pass
        finally:
            conn.close()
    
    def _process_message(self, msg_type: int, payload: bytes, ip: str, port: int) -> None:
        """Process received message"""
        # Update peer activity
        self.peer_manager.update_peer_activity(ip, port)
        
        # Handle message based on type
        if msg_type == MessageType.PING:
            self._send_message(ip, port, self.protocol.create_pong())
        elif msg_type == MessageType.TX_BROADCAST:
            tx_data = self.protocol.parse_tx_broadcast(payload)
            if tx_data and MessageType.TX_BROADCAST in self._handlers:
                self._handlers[MessageType.TX_BROADCAST](tx_data)
        elif msg_type in self._handlers:
            self._handlers[msg_type](payload)
    
    def _send_message(self, ip: str, port: int, message: bytes) -> bool:
        """Send message to peer"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((ip, port))
            sock.send(message)
            sock.close()
            self.peer_manager.increment_message_count(sent=True)
            return True
        except:
            return False
    
    def add_peer(self, ip: str, port: int) -> None:
        """Add peer to network"""
        self.peer_manager.add_peer(ip, port)
    
    def broadcast(self, message: bytes) -> int:
        """Broadcast message to all active peers"""
        active_peers = self.peer_manager.get_active_peers()
        success_count = 0
        
        for ip, port in active_peers:
            if self._send_message(ip, port, message):
                success_count += 1
        
        return success_count
    
    def broadcast_transaction(self, tx_data: bytes) -> int:
        """Broadcast transaction to network"""
        message = self.protocol.create_tx_broadcast(tx_data)
        return self.broadcast(message)
    
    def set_handler(self, msg_type: int, handler: Callable) -> None:
        """Set message handler"""
        self._handlers[msg_type] = handler
    
    def ping_peer(self, ip: str, port: int) -> bool:
        """Ping specific peer"""
        ping_msg = self.protocol.create_ping()
        return self._send_message(ip, port, ping_msg)
    
    def get_stats(self) -> dict:
        """Get network statistics"""
        return {
            'running': self._running,
            'peer_stats': self.peer_manager.get_stats(),
            'handlers': len(self._handlers)
        }
