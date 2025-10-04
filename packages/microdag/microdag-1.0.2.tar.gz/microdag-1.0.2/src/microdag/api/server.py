"""
Ultra-lightweight HTTP API server.
"""
import socket
import threading
import json
from typing import Callable, Dict, Any
from .handlers import APIHandlers

class APIServer:
    """Ultra-lightweight HTTP API server"""
    
    def __init__(self, dag=None, database=None, network=None):
        self.dag = dag
        self.database = database
        self.network = network
        self.handlers = APIHandlers(dag, database, network)
        self._server_socket = None
        self._running = False
    
    def start(self, port: int = 7076):
        """Start HTTP server"""
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server_socket.bind(('0.0.0.0', port))
        self._server_socket.listen(5)
        self._running = True
        
        print(f"API server started on http://localhost:{port}")
        
        # Start server thread
        server_thread = threading.Thread(target=self._server_loop, daemon=True)
        server_thread.start()
    
    def stop(self):
        """Stop HTTP server"""
        self._running = False
        if self._server_socket:
            self._server_socket.close()
    
    def _server_loop(self):
        """Main server loop"""
        while self._running:
            try:
                conn, addr = self._server_socket.accept()
                client_thread = threading.Thread(
                    target=self._handle_request, 
                    args=(conn,), 
                    daemon=True
                )
                client_thread.start()
            except:
                break
    
    def _handle_request(self, conn: socket.socket):
        """Handle HTTP request"""
        try:
            # Read request
            data = conn.recv(4096).decode('utf-8')
            if not data:
                return
            
            # Parse request line
            lines = data.split('\r\n')
            if not lines:
                return
            
            request_line = lines[0]
            parts = request_line.split(' ')
            if len(parts) < 2:
                return
            
            method, path = parts[0], parts[1]
            
            # Parse body for POST requests
            body = None
            if method == 'POST':
                try:
                    body_start = data.find('\r\n\r\n')
                    if body_start != -1:
                        body_data = data[body_start + 4:]
                        if body_data:
                            body = json.loads(body_data)
                except:
                    pass
            
            # Route request
            response = self._route_request(method, path, body)
            
            # Send response
            self._send_response(conn, response)
            
        except Exception as e:
            self._send_error(conn, 500, str(e))
        finally:
            conn.close()
    
    def _route_request(self, method: str, path: str, body: Dict[str, Any] = None) -> Dict[str, Any]:
        """Route request to appropriate handler"""
        if method == 'GET':
            if path == '/health':
                return self.handlers.health()
            elif path == '/stats':
                return self.handlers.stats()
            elif path == '/tips':
                return self.handlers.get_tips()
            elif path.startswith('/transaction/'):
                tx_hash = path.split('/')[-1]
                return self.handlers.get_transaction(tx_hash)
            elif path == '/peers':
                return self.handlers.get_peers()
        
        elif method == 'POST':
            if path == '/transaction':
                return self.handlers.create_transaction(body)
            elif path == '/peer':
                return self.handlers.add_peer(body)
        
        return {'error': 'Not found', 'status': 404}
    
    def _send_response(self, conn: socket.socket, response: Dict[str, Any]):
        """Send JSON response"""
        status_code = response.pop('status', 200)
        
        json_data = json.dumps(response)
        response_data = (
            f"HTTP/1.1 {status_code} OK\r\n"
            f"Content-Type: application/json\r\n"
            f"Content-Length: {len(json_data)}\r\n"
            f"Access-Control-Allow-Origin: *\r\n"
            f"\r\n"
            f"{json_data}"
        ).encode('utf-8')
        
        conn.send(response_data)
    
    def _send_error(self, conn: socket.socket, status_code: int, message: str):
        """Send error response"""
        response = {'error': message, 'status': status_code}
        self._send_response(conn, response)
