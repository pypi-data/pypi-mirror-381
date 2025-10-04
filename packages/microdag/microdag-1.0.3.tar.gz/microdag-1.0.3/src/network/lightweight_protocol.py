"""
Ultra-lightweight network protocol optimized for minimal bandwidth and IoT devices.
"""

import struct
import zlib
import asyncio
import time
from typing import Dict, List, Optional, Tuple, Union
from enum import IntEnum
from dataclasses import dataclass
import msgpack

class MessageType(IntEnum):
    """Compact message types using single byte."""
    PING = 0x01
    PONG = 0x02
    TX_BROADCAST = 0x03
    TX_REQUEST = 0x04
    TX_RESPONSE = 0x05
    PEER_LIST = 0x06
    DAG_SYNC = 0x07
    ERROR = 0xFF

@dataclass
class CompactMessage:
    """Ultra-compact message format for minimal bandwidth usage."""
    
    __slots__ = ['msg_type', 'payload', 'timestamp']
    
    msg_type: MessageType
    payload: bytes
    timestamp: int  # 4 bytes
    
    def serialize(self) -> bytes:
        """Serialize to minimal binary format."""
        # Header: 1 byte type + 4 bytes timestamp + 2 bytes payload length
        header = struct.pack('!BIH', self.msg_type, self.timestamp, len(self.payload))
        return header + self.payload
    
    @classmethod
    def deserialize(cls, data: bytes) -> 'CompactMessage':
        """Deserialize from binary format."""
        if len(data) < 7:  # Minimum header size
            raise ValueError("Invalid message format")
        
        msg_type, timestamp, payload_len = struct.unpack('!BIH', data[:7])
        payload = data[7:7+payload_len]
        
        return cls(
            msg_type=MessageType(msg_type),
            payload=payload,
            timestamp=timestamp
        )

class LightweightProtocol:
    """
    Ultra-lightweight protocol optimized for IoT devices and minimal bandwidth.
    
    Features:
    - Binary message format (7 byte header + payload)
    - Optional compression for large messages
    - Connection pooling and reuse
    - Minimal memory allocation
    - UDP support for non-critical messages
    """
    
    def __init__(self, compress_threshold: int = 100):
        self.compress_threshold = compress_threshold
        self.connection_pool: Dict[str, asyncio.StreamWriter] = {}
        self.message_cache: Dict[bytes, CompactMessage] = {}
        self.stats = {
            'messages_sent': 0,
            'messages_received': 0,
            'bytes_sent': 0,
            'bytes_received': 0,
            'compression_ratio': 0.0
        }
    
    def create_ping_message(self) -> CompactMessage:
        """Create minimal ping message."""
        return CompactMessage(
            msg_type=MessageType.PING,
            payload=b'',  # Empty payload for ping
            timestamp=int(time.time())
        )
    
    def create_pong_message(self) -> CompactMessage:
        """Create minimal pong response."""
        return CompactMessage(
            msg_type=MessageType.PONG,
            payload=b'',  # Empty payload for pong
            timestamp=int(time.time())
        )
    
    def create_transaction_broadcast(self, tx_data: bytes) -> CompactMessage:
        """Create transaction broadcast message with optional compression."""
        payload = tx_data
        
        # Compress if payload is large
        if len(payload) > self.compress_threshold:
            compressed = zlib.compress(payload, level=1)  # Fast compression
            if len(compressed) < len(payload):
                payload = b'\x01' + compressed  # Compression flag + data
                self.stats['compression_ratio'] = len(compressed) / len(payload)
            else:
                payload = b'\x00' + payload  # No compression flag + data
        else:
            payload = b'\x00' + payload  # No compression flag + data
        
        return CompactMessage(
            msg_type=MessageType.TX_BROADCAST,
            payload=payload,
            timestamp=int(time.time())
        )
    
    def create_transaction_request(self, tx_hashes: List[bytes]) -> CompactMessage:
        """Create transaction request with compact hash list."""
        # Pack multiple 32-byte hashes efficiently
        payload = struct.pack('!H', len(tx_hashes))  # Hash count
        for tx_hash in tx_hashes:
            payload += tx_hash
        
        return CompactMessage(
            msg_type=MessageType.TX_REQUEST,
            payload=payload,
            timestamp=int(time.time())
        )
    
    def create_peer_list_message(self, peers: List[Tuple[str, int]]) -> CompactMessage:
        """Create compact peer list message."""
        # Use msgpack for efficient serialization of peer data
        peer_data = [(peer[0], peer[1]) for peer in peers[:20]]  # Limit to 20 peers
        payload = msgpack.packb(peer_data)
        
        return CompactMessage(
            msg_type=MessageType.PEER_LIST,
            payload=payload,
            timestamp=int(time.time())
        )
    
    def parse_transaction_broadcast(self, message: CompactMessage) -> bytes:
        """Parse transaction broadcast and handle decompression."""
        if not message.payload:
            raise ValueError("Empty transaction payload")
        
        compression_flag = message.payload[0]
        data = message.payload[1:]
        
        if compression_flag == 0x01:  # Compressed
            return zlib.decompress(data)
        else:  # Not compressed
            return data
    
    def parse_transaction_request(self, message: CompactMessage) -> List[bytes]:
        """Parse transaction request and extract hash list."""
        if len(message.payload) < 2:
            return []
        
        hash_count = struct.unpack('!H', message.payload[:2])[0]
        hashes = []
        
        offset = 2
        for _ in range(hash_count):
            if offset + 32 <= len(message.payload):
                hashes.append(message.payload[offset:offset+32])
                offset += 32
        
        return hashes
    
    def parse_peer_list(self, message: CompactMessage) -> List[Tuple[str, int]]:
        """Parse peer list message."""
        try:
            return msgpack.unpackb(message.payload)
        except:
            return []
    
    async def send_message(self, writer: asyncio.StreamWriter, message: CompactMessage):
        """Send message with minimal overhead."""
        data = message.serialize()
        writer.write(data)
        await writer.drain()
        
        self.stats['messages_sent'] += 1
        self.stats['bytes_sent'] += len(data)
    
    async def receive_message(self, reader: asyncio.StreamReader) -> Optional[CompactMessage]:
        """Receive message with minimal memory allocation."""
        try:
            # Read header first
            header_data = await reader.readexactly(7)
            msg_type, timestamp, payload_len = struct.unpack('!BIH', header_data)
            
            # Read payload
            payload = await reader.readexactly(payload_len) if payload_len > 0 else b''
            
            message = CompactMessage(
                msg_type=MessageType(msg_type),
                payload=payload,
                timestamp=timestamp
            )
            
            self.stats['messages_received'] += 1
            self.stats['bytes_received'] += len(header_data) + len(payload)
            
            return message
            
        except asyncio.IncompleteReadError:
            return None
        except Exception:
            return None
    
    async def get_connection(self, host: str, port: int) -> Optional[asyncio.StreamWriter]:
        """Get connection from pool or create new one."""
        connection_key = f"{host}:{port}"
        
        if connection_key in self.connection_pool:
            writer = self.connection_pool[connection_key]
            if not writer.is_closing():
                return writer
            else:
                del self.connection_pool[connection_key]
        
        try:
            reader, writer = await asyncio.open_connection(host, port)
            self.connection_pool[connection_key] = writer
            return writer
        except:
            return None
    
    def close_all_connections(self):
        """Close all pooled connections."""
        for writer in self.connection_pool.values():
            if not writer.is_closing():
                writer.close()
        self.connection_pool.clear()
    
    def get_statistics(self) -> Dict:
        """Get protocol statistics."""
        return self.stats.copy()

class UDPLightweightProtocol:
    """
    Ultra-lightweight UDP protocol for non-critical messages.
    Used for peer discovery and heartbeats to minimize connection overhead.
    """
    
    def __init__(self):
        self.transport = None
        self.protocol = None
        self.stats = {
            'udp_messages_sent': 0,
            'udp_messages_received': 0,
            'udp_bytes_sent': 0,
            'udp_bytes_received': 0
        }
    
    async def start_server(self, host: str, port: int):
        """Start UDP server for lightweight messages."""
        loop = asyncio.get_event_loop()
        
        self.transport, self.protocol = await loop.create_datagram_endpoint(
            lambda: UDPProtocolHandler(self),
            local_addr=(host, port)
        )
    
    async def send_udp_message(self, message: CompactMessage, host: str, port: int):
        """Send UDP message for non-critical communications."""
        if self.transport:
            data = message.serialize()
            self.transport.sendto(data, (host, port))
            
            self.stats['udp_messages_sent'] += 1
            self.stats['udp_bytes_sent'] += len(data)
    
    def stop_server(self):
        """Stop UDP server."""
        if self.transport:
            self.transport.close()

class UDPProtocolHandler(asyncio.DatagramProtocol):
    """Handler for UDP protocol messages."""
    
    def __init__(self, parent: UDPLightweightProtocol):
        self.parent = parent
    
    def datagram_received(self, data: bytes, addr: Tuple[str, int]):
        """Handle received UDP datagram."""
        try:
            message = CompactMessage.deserialize(data)
            self.parent.stats['udp_messages_received'] += 1
            self.parent.stats['udp_bytes_received'] += len(data)
            
            # Handle UDP-specific message types (ping, peer discovery, etc.)
            asyncio.create_task(self._handle_udp_message(message, addr))
            
        except Exception:
            pass  # Ignore malformed UDP messages
    
    async def _handle_udp_message(self, message: CompactMessage, addr: Tuple[str, int]):
        """Handle specific UDP message types."""
        if message.msg_type == MessageType.PING:
            # Respond with pong
            pong = CompactMessage(
                msg_type=MessageType.PONG,
                payload=b'',
                timestamp=int(time.time())
            )
            await self.parent.send_udp_message(pong, addr[0], addr[1])

class MessageBatcher:
    """
    Batch multiple small messages together to reduce network overhead.
    Useful for IoT devices with limited network resources.
    """
    
    def __init__(self, max_batch_size: int = 1024, max_wait_time: float = 0.1):
        self.max_batch_size = max_batch_size
        self.max_wait_time = max_wait_time
        self.pending_messages: List[CompactMessage] = []
        self.batch_timer = None
        self.protocol = None
    
    def add_message(self, message: CompactMessage):
        """Add message to batch."""
        self.pending_messages.append(message)
        
        # Check if we should send immediately
        total_size = sum(len(msg.serialize()) for msg in self.pending_messages)
        
        if total_size >= self.max_batch_size or len(self.pending_messages) >= 10:
            asyncio.create_task(self._send_batch())
        elif self.batch_timer is None:
            # Start timer for delayed send
            self.batch_timer = asyncio.create_task(self._delayed_send())
    
    async def _send_batch(self):
        """Send batched messages."""
        if not self.pending_messages:
            return
        
        # Create batch message
        batch_data = b''
        for message in self.pending_messages:
            batch_data += message.serialize()
        
        batch_message = CompactMessage(
            msg_type=MessageType.DAG_SYNC,  # Use sync type for batches
            payload=batch_data,
            timestamp=int(time.time())
        )
        
        # Send batch (would need connection context)
        # await self.protocol.send_message(writer, batch_message)
        
        # Clear pending messages
        self.pending_messages.clear()
        self.batch_timer = None
    
    async def _delayed_send(self):
        """Send batch after delay."""
        await asyncio.sleep(self.max_wait_time)
        await self._send_batch()

# Utility functions for lightweight networking
def calculate_message_priority(message: CompactMessage) -> int:
    """Calculate message priority for QoS."""
    priority_map = {
        MessageType.PING: 1,
        MessageType.PONG: 1,
        MessageType.TX_BROADCAST: 3,
        MessageType.TX_REQUEST: 2,
        MessageType.TX_RESPONSE: 3,
        MessageType.PEER_LIST: 1,
        MessageType.DAG_SYNC: 2,
        MessageType.ERROR: 3
    }
    return priority_map.get(message.msg_type, 2)

def estimate_bandwidth_usage(message: CompactMessage) -> int:
    """Estimate bandwidth usage for message."""
    return len(message.serialize())

def create_lightweight_client() -> LightweightProtocol:
    """Create a lightweight protocol client optimized for minimal resource usage."""
    return LightweightProtocol(compress_threshold=50)  # Aggressive compression
