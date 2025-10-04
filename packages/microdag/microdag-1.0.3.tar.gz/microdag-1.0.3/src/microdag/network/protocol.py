"""
Ultra-lightweight message protocol - 7-byte headers.
"""
import struct
import time
import zlib
from typing import Tuple, Optional

class MessageType:
    """Message type constants"""
    PING = 0x01
    PONG = 0x02
    TX_BROADCAST = 0x03
    PEER_LIST = 0x04

class MessageProtocol:
    """Ultra-lightweight message protocol"""
    
    @staticmethod
    def pack_message(msg_type: int, payload: bytes) -> bytes:
        """Pack message: 1 byte type + 4 bytes timestamp + 2 bytes length + payload"""
        timestamp = int(time.time())
        header = struct.pack('!BIH', msg_type, timestamp, len(payload))
        return header + payload
    
    @staticmethod
    def unpack_message(data: bytes) -> Optional[Tuple[int, int, bytes]]:
        """Unpack message -> (type, timestamp, payload)"""
        if len(data) < 7:
            return None
        
        msg_type, timestamp, payload_len = struct.unpack('!BIH', data[:7])
        if len(data) < 7 + payload_len:
            return None
        
        payload = data[7:7+payload_len]
        return msg_type, timestamp, payload
    
    @staticmethod
    def create_ping() -> bytes:
        """Create ping message (7 bytes total)"""
        return MessageProtocol.pack_message(MessageType.PING, b'')
    
    @staticmethod
    def create_pong() -> bytes:
        """Create pong message (7 bytes total)"""
        return MessageProtocol.pack_message(MessageType.PONG, b'')
    
    @staticmethod
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
        
        return MessageProtocol.pack_message(MessageType.TX_BROADCAST, payload)
    
    @staticmethod
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
    
    @staticmethod
    def validate_message(data: bytes) -> bool:
        """Validate message format"""
        if len(data) < 7:
            return False
        
        try:
            msg_type, timestamp, payload_len = struct.unpack('!BIH', data[:7])
            return (msg_type in [MessageType.PING, MessageType.PONG, 
                               MessageType.TX_BROADCAST, MessageType.PEER_LIST] and 
                    len(data) == 7 + payload_len and
                    timestamp > 0)
        except:
            return False
