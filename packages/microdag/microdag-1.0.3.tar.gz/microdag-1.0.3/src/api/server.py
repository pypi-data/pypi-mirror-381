"""
HTTP API Server
Implements REST API on port 7076
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import logging
import threading
from typing import Optional
from urllib.parse import urlparse

from .handlers import APIHandler


logger = logging.getLogger(__name__)


class APIRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for API endpoints"""
    
    def do_GET(self):
        """Handle GET requests"""
        parsed = urlparse(self.path)
        path_parts = parsed.path.strip('/').split('/')
        
        if not path_parts:
            self.send_error(404)
            return
        
        handler: APIHandler = self.server.api_handler
        
        try:
            # Route to appropriate handler
            if path_parts[0] == 'account' and len(path_parts) == 2:
                status, response = handler.handle_get_account(path_parts[1])
                self.send_json_response(status, response)
            
            elif path_parts[0] == 'transaction' and len(path_parts) == 2:
                status, response = handler.handle_get_transaction(path_parts[1])
                self.send_binary_response(status, response)
            
            elif path_parts[0] == 'pending' and len(path_parts) == 2:
                status, response = handler.handle_get_pending(path_parts[1])
                self.send_json_response(status, response)
            
            elif path_parts[0] == 'peers':
                status, response = handler.handle_get_peers()
                self.send_json_response(status, response)
            
            elif path_parts[0] == 'supply':
                status, response = handler.handle_get_supply()
                self.send_json_response(status, response)
            
            else:
                self.send_error(404)
        
        except Exception as e:
            logger.error(f"Error handling GET request: {e}")
            self.send_error(500)
    
    def do_POST(self):
        """Handle POST requests"""
        parsed = urlparse(self.path)
        path_parts = parsed.path.strip('/').split('/')
        
        if not path_parts:
            self.send_error(404)
            return
        
        handler: APIHandler = self.server.api_handler
        
        try:
            if path_parts[0] == 'broadcast':
                # Read request body
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length)
                
                # Handle broadcast
                status, response = handler.handle_broadcast(body)
                self.send_json_response(status, response)
            
            else:
                self.send_error(404)
        
        except Exception as e:
            logger.error(f"Error handling POST request: {e}")
            self.send_error(500)
    
    def do_OPTIONS(self):
        """Handle OPTIONS requests (CORS preflight)"""
        self.send_response(200)
        self.send_cors_headers()
        self.end_headers()
    
    def send_json_response(self, status: int, data: dict):
        """Send JSON response"""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_cors_headers()
        self.end_headers()
        
        json_data = json.dumps(data).encode('utf-8')
        self.wfile.write(json_data)
    
    def send_binary_response(self, status: int, data: bytes):
        """Send binary response"""
        self.send_response(status)
        self.send_header('Content-Type', 'application/octet-stream')
        self.send_cors_headers()
        self.end_headers()
        
        self.wfile.write(data)
    
    def send_cors_headers(self):
        """Send CORS headers"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    
    def log_message(self, format, *args):
        """Override to use logger"""
        logger.debug(f"{self.address_string()} - {format % args}")


class APIServer:
    """
    HTTP API Server
    
    Specification: Section 7.2 - HTTP Server Implementation
    
    Implements REST API on port 7076 with CORS support.
    
    Example:
        >>> server = APIServer(
        ...     port=7076,
        ...     storage=storage,
        ...     propagator=propagator,
        ...     peer_manager=peer_manager
        ... )
        >>> server.start()
        >>> # Server running in background
        >>> server.stop()
    """
    
    def __init__(
        self,
        port: int,
        storage,
        propagator,
        peer_manager,
        host: str = '0.0.0.0'
    ):
        """
        Initialize API server
        
        Args:
            port: Port to listen on (default: 7076)
            storage: LevelDBStorage instance
            propagator: TransactionPropagator instance
            peer_manager: PeerManager instance
            host: Host to bind to (default: 0.0.0.0)
        """
        self.port = port
        self.host = host
        
        # Create API handler
        self.api_handler = APIHandler(storage, propagator, peer_manager)
        
        # Server state
        self.httpd: Optional[HTTPServer] = None
        self.server_thread: Optional[threading.Thread] = None
        self.running = False
    
    def start(self):
        """Start API server in background thread"""
        if self.running:
            return
        
        self.running = True
        
        # Create HTTP server
        self.httpd = HTTPServer((self.host, self.port), APIRequestHandler)
        self.httpd.api_handler = self.api_handler
        
        # Start in background thread
        self.server_thread = threading.Thread(target=self._run_server, daemon=True)
        self.server_thread.start()
        
        logger.info(f"API server started on {self.host}:{self.port}")
    
    def stop(self):
        """Stop API server"""
        if not self.running:
            return
        
        self.running = False
        
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
        
        if self.server_thread:
            self.server_thread.join(timeout=2.0)
        
        logger.info("API server stopped")
    
    def _run_server(self):
        """Run server (called in background thread)"""
        try:
            logger.info(f"API server listening on {self.host}:{self.port}")
            self.httpd.serve_forever()
        except Exception as e:
            logger.error(f"API server error: {e}")
        finally:
            self.running = False
