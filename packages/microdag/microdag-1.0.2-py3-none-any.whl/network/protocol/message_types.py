"""
Network Message Types
Defines the 7 message types from specification
"""

from enum import IntEnum
from dataclasses import dataclass
from typing import Optional


class MessageType(IntEnum):
    """
    Network message types
    
    Specification: Section 4.1 - Node Communication
    
    Message Types:
    0x01 - PUBLISH_TRANSACTION: Broadcast new transaction
    0x02 - REQUEST_ACCOUNT_STATE: Query account state
    0x03 - REQUEST_TRANSACTION: Query transaction by hash
    0x04 - REQUEST_PENDING: Query pending transactions
    0x05 - VOTE: Vote on conflicting transaction
    0x06 - PING: Keep-alive and latency check
    0x07 - REQUEST_PEERS: Peer discovery
    """
    PUBLISH_TRANSACTION = 0x01
    REQUEST_ACCOUNT_STATE = 0x02
    REQUEST_TRANSACTION = 0x03
    REQUEST_PENDING = 0x04
    VOTE = 0x05
    PING = 0x06
    REQUEST_PEERS = 0x07


@dataclass
class Message:
    """
    Network message
    
    Specification: Section 4.1 - Message Format
    
    Format:
    [0]      Message Type (1 byte)
    [1-2]    Payload Length (uint16, little-endian)
    [3-...]  Payload
    
    Attributes:
        msg_type: Message type
        payload: Message payload bytes
    """
    msg_type: MessageType
    payload: bytes
    
    def __post_init__(self):
        """Validate message"""
        if not isinstance(self.msg_type, MessageType):
            raise ValueError(f"Invalid message type: {self.msg_type}")
        if len(self.payload) > 65535:
            raise ValueError(f"Payload too large: {len(self.payload)} bytes")
    
    @property
    def size(self) -> int:
        """Get total message size in bytes"""
        return 3 + len(self.payload)  # 1 byte type + 2 bytes length + payload
    
    def to_bytes(self) -> bytes:
        """
        Serialize message to bytes
        
        Returns:
            Binary message data
        """
        import struct
        
        # Create buffer
        buffer = bytearray(3 + len(self.payload))
        
        # [0] Message type
        buffer[0] = int(self.msg_type)
        
        # [1-2] Payload length (uint16, little-endian)
        struct.pack_into('<H', buffer, 1, len(self.payload))
        
        # [3-...] Payload
        buffer[3:] = self.payload
        
        return bytes(buffer)
    
    @staticmethod
    def from_bytes(data: bytes) -> 'Message':
        """
        Deserialize message from bytes
        
        Args:
            data: Binary message data
            
        Returns:
            Message object
            
        Raises:
            ValueError: If data is invalid
        """
        import struct
        
        if len(data) < 3:
            raise ValueError("Message too short")
        
        # Parse header
        msg_type = MessageType(data[0])
        payload_length = struct.unpack('<H', data[1:3])[0]
        
        # Validate length
        if len(data) < 3 + payload_length:
            raise ValueError(f"Incomplete message: expected {3 + payload_length}, got {len(data)}")
        
        # Extract payload
        payload = data[3:3 + payload_length]
        
        return Message(msg_type=msg_type, payload=payload)


# Message payload helpers

def create_publish_transaction_payload(tx_bytes: bytes) -> bytes:
    """
    Create PUBLISH_TRANSACTION payload
    
    Specification: 0x01 - PUBLISH_TRANSACTION
    Payload: 141 bytes (transaction)
    
    Args:
        tx_bytes: 141-byte transaction
        
    Returns:
        Payload bytes
    """
    if len(tx_bytes) != 141:
        raise ValueError("Transaction must be 141 bytes")
    return tx_bytes


def create_request_account_state_payload(public_key: bytes) -> bytes:
    """
    Create REQUEST_ACCOUNT_STATE payload
    
    Specification: 0x02 - REQUEST_ACCOUNT_STATE
    Payload: 32 bytes (account public key)
    
    Args:
        public_key: 32-byte account public key
        
    Returns:
        Payload bytes
    """
    if len(public_key) != 32:
        raise ValueError("Public key must be 32 bytes")
    return public_key


def create_request_transaction_payload(tx_hash: bytes) -> bytes:
    """
    Create REQUEST_TRANSACTION payload
    
    Specification: 0x03 - REQUEST_TRANSACTION
    Payload: 32 bytes (transaction hash)
    
    Args:
        tx_hash: 32-byte transaction hash
        
    Returns:
        Payload bytes
    """
    if len(tx_hash) != 32:
        raise ValueError("Transaction hash must be 32 bytes")
    return tx_hash


def create_request_pending_payload(public_key: bytes) -> bytes:
    """
    Create REQUEST_PENDING payload
    
    Specification: 0x04 - REQUEST_PENDING
    Payload: 32 bytes (account public key)
    
    Args:
        public_key: 32-byte account public key
        
    Returns:
        Payload bytes
    """
    if len(public_key) != 32:
        raise ValueError("Public key must be 32 bytes")
    return public_key


def create_vote_payload(tx_hash: bytes, voter_pubkey: bytes, signature: bytes) -> bytes:
    """
    Create VOTE payload
    
    Specification: 0x05 - VOTE
    Payload: 65 bytes (tx_hash + voter_pubkey + signature)
    
    Args:
        tx_hash: 32-byte transaction hash
        voter_pubkey: 32-byte voter public key
        signature: 1-byte signature (simplified for now)
        
    Returns:
        Payload bytes (65 bytes)
    """
    if len(tx_hash) != 32:
        raise ValueError("Transaction hash must be 32 bytes")
    if len(voter_pubkey) != 32:
        raise ValueError("Voter public key must be 32 bytes")
    if len(signature) != 1:
        raise ValueError("Signature must be 1 byte")
    
    return tx_hash + voter_pubkey + signature


def create_ping_payload(timestamp: int) -> bytes:
    """
    Create PING payload
    
    Specification: 0x06 - PING
    Payload: 8 bytes (timestamp)
    
    Args:
        timestamp: Unix timestamp
        
    Returns:
        Payload bytes (8 bytes)
    """
    import struct
    return struct.pack('<Q', timestamp)


def create_request_peers_payload() -> bytes:
    """
    Create REQUEST_PEERS payload
    
    Specification: 0x07 - REQUEST_PEERS
    Payload: 0 bytes
    
    Returns:
        Empty payload
    """
    return b''
