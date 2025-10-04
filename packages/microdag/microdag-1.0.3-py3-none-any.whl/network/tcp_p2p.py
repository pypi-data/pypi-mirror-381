"""
TCP P2P Networking for MicroDAG
Implements direct TCP peer-to-peer communication with fallback to HTTP
"""

import asyncio
import socket
import json
import time
import logging
import threading
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field
from collections import defaultdict
import struct
import hashlib

logger = logging.getLogger(__name__)


@dataclass
class TCPPeerInfo:
    """Information about a TCP peer"""
    peer_id: str
    host: str
    tcp_port: int
    http_port: int
    last_seen: float = field(default_factory=time.time)
    connection_attempts: int = 0
    successful_connections: int = 0
    avg_latency_ms: float = 0.0
    is_connected: bool = False
    supports_tcp: bool = True
    firewall_friendly: bool = True


@dataclass
class NetworkMetrics:
    """Network performance metrics"""
    tcp_connections: int = 0
    http_fallbacks: int = 0
    total_messages: int = 0
    avg_tcp_latency_ms: float = 0.0
    avg_http_latency_ms: float = 0.0
    connection_success_rate: float = 0.0
    firewall_issues: int = 0
    tcp_vs_http_preference: str = "tcp"


class TCPMessageProtocol:
    """Protocol for TCP message framing"""
    
    MAGIC_BYTES = b'MDAG'
    VERSION = 1
    
    @staticmethod
    def encode_message(message_type: str, data: dict) -> bytes:
        """Encode message for TCP transmission"""
        # Create message
        message = {
            'type': message_type,
            'data': data,
            'timestamp': time.time()
        }
        
        # Serialize to JSON
        json_data = json.dumps(message).encode('utf-8')
        
        # Create header: MAGIC(4) + VERSION(1) + LENGTH(4) + CHECKSUM(4)
        header = struct.pack(
            '>4sBII',
            TCPMessageProtocol.MAGIC_BYTES,
            TCPMessageProtocol.VERSION,
            len(json_data),
            hashlib.crc32(json_data) & 0xffffffff
        )
        
        return header + json_data
    
    @staticmethod
    def decode_message(data: bytes) -> Optional[Tuple[str, dict]]:
        """Decode message from TCP transmission"""
        if len(data) < 13:  # Minimum header size
            return None
        
        try:
            # Parse header
            magic, version, length, checksum = struct.unpack('>4sBII', data[:13])
            
            if magic != TCPMessageProtocol.MAGIC_BYTES:
                logger.warning("Invalid magic bytes in TCP message")
                return None
            
            if version != TCPMessageProtocol.VERSION:
                logger.warning(f"Unsupported protocol version: {version}")
                return None
            
            if len(data) < 13 + length:
                logger.debug("Incomplete message received")
                return None
            
            # Extract and verify payload
            payload = data[13:13 + length]
            if hashlib.crc32(payload) & 0xffffffff != checksum:
                logger.warning("Message checksum mismatch")
                return None
            
            # Parse JSON
            message = json.loads(payload.decode('utf-8'))
            return message.get('type'), message.get('data', {})
            
        except Exception as e:
            logger.error(f"Failed to decode TCP message: {e}")
            return None


class TCPPeerConnection:
    """Manages a single TCP peer connection"""
    
    def __init__(self, peer_info: TCPPeerInfo):
        self.peer_info = peer_info
        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None
        self.connected = False
        self.last_ping = 0
        self.latency_samples = []
        self._lock = asyncio.Lock()
    
    async def connect(self, timeout: float = 5.0) -> bool:
        """Connect to peer via TCP"""
        try:
            self.peer_info.connection_attempts += 1
            
            # Attempt TCP connection
            future = asyncio.open_connection(
                self.peer_info.host, 
                self.peer_info.tcp_port
            )
            
            self.reader, self.writer = await asyncio.wait_for(future, timeout=timeout)
            
            self.connected = True
            self.peer_info.is_connected = True
            self.peer_info.successful_connections += 1
            self.peer_info.last_seen = time.time()
            
            logger.debug(f"TCP connection established to {self.peer_info.peer_id}")
            return True
            
        except asyncio.TimeoutError:
            logger.warning(f"TCP connection timeout to {self.peer_info.peer_id}")
            self.peer_info.supports_tcp = False
            return False
        except ConnectionRefusedError:
            logger.warning(f"TCP connection refused by {self.peer_info.peer_id}")
            self.peer_info.firewall_friendly = False
            return False
        except Exception as e:
            logger.error(f"TCP connection failed to {self.peer_info.peer_id}: {e}")
            return False
    
    async def send_message(self, message_type: str, data: dict) -> bool:
        """Send message via TCP"""
        if not self.connected or not self.writer:
            return False
        
        try:
            async with self._lock:
                # Encode message
                encoded = TCPMessageProtocol.encode_message(message_type, data)
                
                # Send message
                self.writer.write(encoded)
                await self.writer.drain()
                
                return True
                
        except Exception as e:
            logger.error(f"Failed to send TCP message: {e}")
            await self.disconnect()
            return False
    
    async def receive_message(self, timeout: float = 1.0) -> Optional[Tuple[str, dict]]:
        """Receive message via TCP"""
        if not self.connected or not self.reader:
            return None
        
        try:
            # Read header first
            header_data = await asyncio.wait_for(
                self.reader.readexactly(13), 
                timeout=timeout
            )
            
            # Parse header to get payload length
            _, _, length, _ = struct.unpack('>4sBII', header_data)
            
            # Read payload
            payload_data = await asyncio.wait_for(
                self.reader.readexactly(length),
                timeout=timeout
            )
            
            # Decode complete message
            full_message = header_data + payload_data
            return TCPMessageProtocol.decode_message(full_message)
            
        except asyncio.TimeoutError:
            return None
        except Exception as e:
            logger.error(f"Failed to receive TCP message: {e}")
            await self.disconnect()
            return None
    
    async def ping(self) -> Optional[float]:
        """Ping peer and measure latency"""
        if not self.connected:
            return None
        
        try:
            start_time = time.time()
            
            # Send ping
            success = await self.send_message('ping', {'timestamp': start_time})
            if not success:
                return None
            
            # Wait for pong
            message_type, data = await self.receive_message(timeout=2.0) or (None, None)
            
            if message_type == 'pong':
                latency = (time.time() - start_time) * 1000  # Convert to ms
                
                # Update latency tracking
                self.latency_samples.append(latency)
                if len(self.latency_samples) > 10:
                    self.latency_samples = self.latency_samples[-10:]
                
                self.peer_info.avg_latency_ms = sum(self.latency_samples) / len(self.latency_samples)
                self.last_ping = time.time()
                
                return latency
            
            return None
            
        except Exception as e:
            logger.error(f"Ping failed: {e}")
            return None
    
    async def disconnect(self):
        """Disconnect from peer"""
        self.connected = False
        self.peer_info.is_connected = False
        
        if self.writer:
            try:
                self.writer.close()
                await self.writer.wait_closed()
            except:
                pass
            self.writer = None
        
        self.reader = None


class TCPPeerManager:
    """Manages TCP peer connections and fallback to HTTP"""
    
    def __init__(self, node_id: str, tcp_port: int, http_port: int):
        self.node_id = node_id
        self.tcp_port = tcp_port
        self.http_port = http_port
        self.peers: Dict[str, TCPPeerInfo] = {}
        self.connections: Dict[str, TCPPeerConnection] = {}
        self.server: Optional[asyncio.Server] = None
        self.metrics = NetworkMetrics()
        self.running = False
        
        # HTTP fallback (simplified)
        self.http_session = None
    
    async def start_server(self):
        """Start TCP server for incoming connections"""
        try:
            self.server = await asyncio.start_server(
                self._handle_client,
                '0.0.0.0',
                self.tcp_port
            )
            
            self.running = True
            logger.info(f"TCP P2P server started on port {self.tcp_port}")
            
        except Exception as e:
            logger.error(f"Failed to start TCP server: {e}")
            raise
    
    async def stop_server(self):
        """Stop TCP server"""
        self.running = False
        
        if self.server:
            self.server.close()
            await self.server.wait_closed()
        
        # Close all peer connections
        for connection in self.connections.values():
            await connection.disconnect()
        
        self.connections.clear()
    
    async def _handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """Handle incoming TCP client connection"""
        client_addr = writer.get_extra_info('peername')
        logger.debug(f"TCP client connected from {client_addr}")
        
        try:
            while self.running:
                # Read message header
                try:
                    header_data = await asyncio.wait_for(reader.readexactly(13), timeout=30.0)
                except asyncio.TimeoutError:
                    break
                
                # Parse header to get payload length
                try:
                    _, _, length, _ = struct.unpack('>4sBII', header_data)
                    payload_data = await asyncio.wait_for(reader.readexactly(length), timeout=10.0)
                    
                    # Decode message
                    full_message = header_data + payload_data
                    message_type, data = TCPMessageProtocol.decode_message(full_message) or (None, None)
                    
                    if message_type:
                        await self._handle_message(message_type, data, writer)
                    
                except Exception as e:
                    logger.warning(f"Failed to process client message: {e}")
                    break
                    
        except Exception as e:
            logger.error(f"Client handler error: {e}")
        finally:
            try:
                writer.close()
                await writer.wait_closed()
            except:
                pass
    
    async def _handle_message(self, message_type: str, data: dict, writer: asyncio.StreamWriter):
        """Handle received message"""
        if message_type == 'ping':
            # Respond with pong
            response = TCPMessageProtocol.encode_message('pong', {
                'timestamp': data.get('timestamp', time.time())
            })
            writer.write(response)
            await writer.drain()
            
        elif message_type == 'broadcast':
            # Handle broadcast message
            logger.debug(f"Received broadcast: {data.get('type', 'unknown')}")
            
        elif message_type == 'peer_discovery':
            # Handle peer discovery
            logger.debug("Received peer discovery request")
    
    def add_peer(self, peer_id: str, host: str, tcp_port: int, http_port: int):
        """Add peer to connection pool"""
        peer_info = TCPPeerInfo(
            peer_id=peer_id,
            host=host,
            tcp_port=tcp_port,
            http_port=http_port
        )
        
        self.peers[peer_id] = peer_info
        logger.debug(f"Added peer {peer_id} at {host}:{tcp_port}")
    
    async def connect_to_peer(self, peer_id: str) -> bool:
        """Connect to specific peer"""
        if peer_id not in self.peers:
            return False
        
        peer_info = self.peers[peer_id]
        
        # Check if already connected
        if peer_id in self.connections and self.connections[peer_id].connected:
            return True
        
        # Create new connection
        connection = TCPPeerConnection(peer_info)
        success = await connection.connect()
        
        if success:
            self.connections[peer_id] = connection
            self.metrics.tcp_connections += 1
        else:
            self.metrics.firewall_issues += 1
        
        return success
    
    async def broadcast_message(self, message_type: str, data: dict, prefer_tcp: bool = True) -> Dict[str, bool]:
        """Broadcast message to all peers with TCP/HTTP fallback"""
        results = {}
        
        for peer_id, peer_info in self.peers.items():
            success = False
            
            if prefer_tcp and peer_info.supports_tcp:
                # Try TCP first
                success = await self._send_tcp_message(peer_id, message_type, data)
                
                if success:
                    self.metrics.tcp_connections += 1
                else:
                    # Fallback to HTTP
                    success = await self._send_http_message(peer_id, message_type, data)
                    if success:
                        self.metrics.http_fallbacks += 1
            else:
                # Use HTTP directly
                success = await self._send_http_message(peer_id, message_type, data)
                if success:
                    self.metrics.http_fallbacks += 1
            
            results[peer_id] = success
            self.metrics.total_messages += 1
        
        # Update success rate
        successful = sum(1 for success in results.values() if success)
        self.metrics.connection_success_rate = successful / len(results) if results else 0
        
        return results
    
    async def _send_tcp_message(self, peer_id: str, message_type: str, data: dict) -> bool:
        """Send message via TCP"""
        # Ensure connection exists
        if not await self.connect_to_peer(peer_id):
            return False
        
        connection = self.connections.get(peer_id)
        if not connection:
            return False
        
        # Measure latency
        start_time = time.time()
        success = await connection.send_message(message_type, data)
        
        if success:
            latency = (time.time() - start_time) * 1000
            # Update TCP latency metrics
            if self.metrics.avg_tcp_latency_ms == 0:
                self.metrics.avg_tcp_latency_ms = latency
            else:
                self.metrics.avg_tcp_latency_ms = (self.metrics.avg_tcp_latency_ms + latency) / 2
        
        return success
    
    async def _send_http_message(self, peer_id: str, message_type: str, data: dict) -> bool:
        """Send message via HTTP fallback"""
        peer_info = self.peers.get(peer_id)
        if not peer_info:
            return False
        
        try:
            import aiohttp
            
            if not self.http_session:
                self.http_session = aiohttp.ClientSession(
                    timeout=aiohttp.ClientTimeout(total=5)
                )
            
            url = f"http://{peer_info.host}:{peer_info.http_port}/api/p2p"
            payload = {
                'type': message_type,
                'data': data,
                'from': self.node_id
            }
            
            start_time = time.time()
            
            async with self.http_session.post(url, json=payload) as response:
                success = response.status in [200, 201, 202]
                
                if success:
                    latency = (time.time() - start_time) * 1000
                    # Update HTTP latency metrics
                    if self.metrics.avg_http_latency_ms == 0:
                        self.metrics.avg_http_latency_ms = latency
                    else:
                        self.metrics.avg_http_latency_ms = (self.metrics.avg_http_latency_ms + latency) / 2
                
                return success
        
        except Exception as e:
            logger.error(f"HTTP fallback failed for {peer_id}: {e}")
            return False
    
    async def measure_peer_latencies(self) -> Dict[str, float]:
        """Measure latency to all connected TCP peers"""
        latencies = {}
        
        for peer_id, connection in self.connections.items():
            if connection.connected:
                latency = await connection.ping()
                if latency is not None:
                    latencies[peer_id] = latency
        
        return latencies
    
    def get_network_metrics(self) -> NetworkMetrics:
        """Get current network metrics"""
        # Update preference based on performance
        if self.metrics.avg_tcp_latency_ms > 0 and self.metrics.avg_http_latency_ms > 0:
            if self.metrics.avg_tcp_latency_ms < self.metrics.avg_http_latency_ms:
                self.metrics.tcp_vs_http_preference = "tcp"
            else:
                self.metrics.tcp_vs_http_preference = "http"
        
        return self.metrics
    
    def get_peer_status(self) -> Dict[str, Dict]:
        """Get status of all peers"""
        status = {}
        
        for peer_id, peer_info in self.peers.items():
            connection = self.connections.get(peer_id)
            
            status[peer_id] = {
                'connected': peer_info.is_connected,
                'supports_tcp': peer_info.supports_tcp,
                'firewall_friendly': peer_info.firewall_friendly,
                'avg_latency_ms': peer_info.avg_latency_ms,
                'connection_attempts': peer_info.connection_attempts,
                'successful_connections': peer_info.successful_connections,
                'last_seen': peer_info.last_seen,
                'tcp_connection_active': connection.connected if connection else False
            }
        
        return status


# Helper functions for testing and integration
async def test_tcp_vs_http_latency(peer_manager: TCPPeerManager, test_message: dict, iterations: int = 10) -> Dict:
    """Test TCP vs HTTP latency performance"""
    tcp_latencies = []
    http_latencies = []
    
    for peer_id in peer_manager.peers.keys():
        # Test TCP latency
        for _ in range(iterations):
            start_time = time.time()
            success = await peer_manager._send_tcp_message(peer_id, 'test', test_message)
            if success:
                tcp_latencies.append((time.time() - start_time) * 1000)
        
        # Test HTTP latency
        for _ in range(iterations):
            start_time = time.time()
            success = await peer_manager._send_http_message(peer_id, 'test', test_message)
            if success:
                http_latencies.append((time.time() - start_time) * 1000)
    
    return {
        'tcp_avg_latency_ms': sum(tcp_latencies) / len(tcp_latencies) if tcp_latencies else 0,
        'http_avg_latency_ms': sum(http_latencies) / len(http_latencies) if http_latencies else 0,
        'tcp_samples': len(tcp_latencies),
        'http_samples': len(http_latencies),
        'tcp_advantage_ms': (sum(http_latencies) / len(http_latencies) - sum(tcp_latencies) / len(tcp_latencies)) if tcp_latencies and http_latencies else 0
    }


def create_tcp_peer_manager(node_id: str, tcp_port: int, http_port: int) -> TCPPeerManager:
    """Create TCP peer manager instance"""
    return TCPPeerManager(node_id, tcp_port, http_port)
