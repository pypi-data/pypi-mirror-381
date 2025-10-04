"""
Ultra-minimal network protocol - <1KB, bytes-only, function-based.
"""
import struct
import zlib
import time
from typing import Tuple, Optional

# Message types (1 byte)
PING = 0x01
PONG = 0x02
TX_BROADCAST = 0x03
PEER_LIST = 0x04

# Ultra-compact message: 7 byte header + payload
def pack_message(msg_type: int, payload: bytes) -> bytes:
    """Pack message: 1 byte type + 4 bytes timestamp + 2 bytes length + payload"""
    timestamp = int(time.time())
    header = struct.pack('!BIH', msg_type, timestamp, len(payload))
    return header + payload

def unpack_message(data: bytes) -> Optional[Tuple[int, int, bytes]]:
    """Unpack message -> (type, timestamp, payload)"""
    if len(data) < 7:
        return None
    
    msg_type, timestamp, payload_len = struct.unpack('!BIH', data[:7])
    if len(data) < 7 + payload_len:
        return None
    
    payload = data[7:7+payload_len]
    return msg_type, timestamp, payload

# Message creation functions
def create_ping() -> bytes:
    """Create ping message (7 bytes total)"""
    return pack_message(PING, b'')

def create_pong() -> bytes:
    """Create pong message (7 bytes total)"""
    return pack_message(PONG, b'')

def create_tx_broadcast(tx_data: bytes, compress: bool = True) -> bytes:
    """Create transaction broadcast with optional compression"""
    payload = tx_data
    
    # Compress if beneficial (>50 bytes)
    if compress and len(tx_data) > 50:
        compressed = zlib.compress(tx_data, level=1)
        if len(compressed) < len(tx_data):
            payload = b'\x01' + compressed  # Compression flag
        else:
            payload = b'\x00' + tx_data  # No compression
    else:
        payload = b'\x00' + tx_data  # No compression
    
    return pack_message(TX_BROADCAST, payload)

def create_peer_list(peers: list) -> bytes:
    """Create peer list message (max 10 peers)"""
    # Pack up to 10 peers: count (1 byte) + peers (6 bytes each: 4 IP + 2 port)
    peer_data = struct.pack('!B', min(len(peers), 10))
    
    for i, (ip_str, port) in enumerate(peers[:10]):
        # Convert IP string to 4 bytes (simplified)
        ip_parts = ip_str.split('.')
        if len(ip_parts) == 4:
            ip_bytes = struct.pack('!BBBB', *[int(p) for p in ip_parts])
            peer_data += ip_bytes + struct.pack('!H', port)
    
    return pack_message(PEER_LIST, peer_data)

# Message parsing functions
def parse_tx_broadcast(payload: bytes) -> Optional[bytes]:
    """Parse transaction broadcast payload"""
    if len(payload) < 1:
        return None
    
    compression_flag = payload[0]
    data = payload[1:]
    
    if compression_flag == 0x01:  # Compressed
        try:
            return zlib.decompress(data)
        except:
            return None
    else:  # Not compressed
        return data

def parse_peer_list(payload: bytes) -> list:
    """Parse peer list payload"""
    if len(payload) < 1:
        return []
    
    peer_count = payload[0]
    peers = []
    offset = 1
    
    for _ in range(peer_count):
        if offset + 6 <= len(payload):
            ip_bytes = payload[offset:offset+4]
            port_bytes = payload[offset+4:offset+6]
            
            ip_str = '.'.join(str(b) for b in ip_bytes)
            port = struct.unpack('!H', port_bytes)[0]
            
            peers.append((ip_str, port))
            offset += 6
    
    return peers

# Connection management (minimal)
_connections = {}  # peer_id -> (socket, last_seen)
_stats = {'messages_sent': 0, 'messages_received': 0, 'bytes_sent': 0, 'bytes_received': 0}

def add_connection(peer_id: str, socket_obj):
    """Add connection to pool"""
    _connections[peer_id] = (socket_obj, time.time())

def remove_connection(peer_id: str):
    """Remove connection from pool"""
    _connections.pop(peer_id, None)

def get_connection(peer_id: str):
    """Get connection from pool"""
    if peer_id in _connections:
        socket_obj, last_seen = _connections[peer_id]
        # Update last seen
        _connections[peer_id] = (socket_obj, time.time())
        return socket_obj
    return None

def cleanup_old_connections(max_age: int = 300):
    """Remove connections older than max_age seconds"""
    current_time = time.time()
    to_remove = []
    
    for peer_id, (socket_obj, last_seen) in _connections.items():
        if current_time - last_seen > max_age:
            to_remove.append(peer_id)
    
    for peer_id in to_remove:
        remove_connection(peer_id)

def send_message(socket_obj, message: bytes):
    """Send message and update stats"""
    try:
        socket_obj.send(message)
        _stats['messages_sent'] += 1
        _stats['bytes_sent'] += len(message)
        return True
    except:
        return False

def receive_message(socket_obj) -> Optional[bytes]:
    """Receive message and update stats"""
    try:
        # Read header first
        header = socket_obj.recv(7)
        if len(header) != 7:
            return None
        
        _, _, payload_len = struct.unpack('!BIH', header)
        
        # Read payload
        payload = b''
        if payload_len > 0:
            payload = socket_obj.recv(payload_len)
            if len(payload) != payload_len:
                return None
        
        message = header + payload
        _stats['messages_received'] += 1
        _stats['bytes_received'] += len(message)
        
        return message
    except:
        return None

def get_protocol_stats() -> dict:
    """Get protocol statistics"""
    return {
        **_stats,
        'active_connections': len(_connections),
        'avg_message_size': _stats['bytes_sent'] / max(1, _stats['messages_sent'])
    }

# Bandwidth optimization
def estimate_bandwidth(message: bytes) -> int:
    """Estimate bandwidth usage for message"""
    return len(message)

def should_compress(data: bytes, threshold: int = 50) -> bool:
    """Check if data should be compressed"""
    return len(data) > threshold

# Message validation
def validate_message(data: bytes) -> bool:
    """Validate message format"""
    if len(data) < 7:
        return False
    
    try:
        msg_type, timestamp, payload_len = struct.unpack('!BIH', data[:7])
        return (msg_type in [PING, PONG, TX_BROADCAST, PEER_LIST] and 
                len(data) == 7 + payload_len and
                timestamp > 0)
    except:
        return False
