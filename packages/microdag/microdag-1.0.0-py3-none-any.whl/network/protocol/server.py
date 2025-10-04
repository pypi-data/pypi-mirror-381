"""
Network Server
TCP server for handling peer connections
"""

import socket
import threading
import logging
from typing import Optional, Callable

from .message_types import Message
from .handlers import MessageHandler


logger = logging.getLogger(__name__)


class NetworkServer:
    """
    TCP network server
    
    Specification: Section 4.1 - Node Communication
    Protocol: Raw TCP Sockets
    Port: 7075 (main network)
    
    Handles incoming peer connections and processes messages.
    
    Example:
        >>> server = NetworkServer(
        ...     port=7075,
        ...     handler=message_handler
        ... )
        >>> server.start()
        >>> # Server running in background thread
        >>> server.stop()
    """
    
    def __init__(
        self,
        port: int,
        handler: MessageHandler,
        host: str = '0.0.0.0',
        max_connections: int = 32
    ):
        """
        Initialize network server
        
        Args:
            port: Port to listen on (default: 7075)
            handler: Message handler instance
            host: Host to bind to (default: 0.0.0.0)
            max_connections: Maximum concurrent connections
        """
        self.port = port
        self.host = host
        self.handler = handler
        self.max_connections = max_connections
        
        self.socket: Optional[socket.socket] = None
        self.running = False
        self.server_thread: Optional[threading.Thread] = None
        self.client_threads: list[threading.Thread] = []
    
    def start(self):
        """Start server in background thread"""
        if self.running:
            return
        
        self.running = True
        self.server_thread = threading.Thread(target=self._run_server, daemon=True)
        self.server_thread.start()
        
        logger.info(f"Network server started on {self.host}:{self.port}")
    
    def stop(self):
        """Stop server and close all connections"""
        if not self.running:
            return
        
        self.running = False
        
        # Close server socket
        if self.socket:
            try:
                self.socket.close()
            except Exception:
                pass
        
        # Wait for threads to finish
        if self.server_thread:
            self.server_thread.join(timeout=1.0)
        
        for thread in self.client_threads:
            thread.join(timeout=0.5)
        
        logger.info("Network server stopped")
    
    def _run_server(self):
        """Main server loop"""
        try:
            # Create TCP socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Bind and listen
            self.socket.bind((self.host, self.port))
            self.socket.listen(self.max_connections)
            self.socket.settimeout(1.0)  # Timeout for checking running flag
            
            logger.info(f"Listening on {self.host}:{self.port}")
            
            while self.running:
                try:
                    # Accept connection
                    client_socket, address = self.socket.accept()
                    
                    # Handle in separate thread
                    client_thread = threading.Thread(
                        target=self._handle_client,
                        args=(client_socket, address),
                        daemon=True
                    )
                    client_thread.start()
                    self.client_threads.append(client_thread)
                    
                    # Clean up finished threads
                    self.client_threads = [t for t in self.client_threads if t.is_alive()]
                    
                except socket.timeout:
                    continue
                except Exception as e:
                    if self.running:
                        logger.error(f"Error accepting connection: {e}")
        
        except Exception as e:
            logger.error(f"Server error: {e}")
        
        finally:
            if self.socket:
                self.socket.close()
    
    def _handle_client(self, client_socket: socket.socket, address: tuple):
        """
        Handle client connection
        
        Args:
            client_socket: Client socket
            address: Client address (ip, port)
        """
        logger.debug(f"New connection from {address}")
        
        try:
            while self.running:
                # Receive message header (3 bytes)
                header = self._recv_exact(client_socket, 3)
                if not header:
                    break
                
                # Parse header to get payload length
                import struct
                payload_length = struct.unpack('<H', header[1:3])[0]
                
                # Receive payload
                payload = self._recv_exact(client_socket, payload_length)
                if not payload:
                    break
                
                # Reconstruct full message
                message_data = header + payload
                
                try:
                    # Parse message
                    message = Message.from_bytes(message_data)
                    
                    # Handle message
                    response = self.handler.handle(message)
                    
                    # Send response if any
                    if response:
                        client_socket.sendall(response.to_bytes())
                
                except Exception as e:
                    logger.error(f"Error handling message: {e}")
                    break
        
        except Exception as e:
            logger.error(f"Client error: {e}")
        
        finally:
            client_socket.close()
            logger.debug(f"Connection closed: {address}")
    
    def _recv_exact(self, sock: socket.socket, n: int) -> Optional[bytes]:
        """
        Receive exactly n bytes from socket
        
        Args:
            sock: Socket to receive from
            n: Number of bytes to receive
            
        Returns:
            Bytes received or None if connection closed
        """
        data = bytearray()
        while len(data) < n:
            chunk = sock.recv(n - len(data))
            if not chunk:
                return None
            data.extend(chunk)
        return bytes(data)
