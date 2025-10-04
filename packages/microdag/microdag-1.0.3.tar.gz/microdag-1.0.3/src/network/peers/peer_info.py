"""
Peer Information
Data structures for peer management
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional
import time


class PeerStatus(Enum):
    """Peer connection status"""
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    FAILED = "failed"


@dataclass
class PeerInfo:
    """
    Peer information
    
    Tracks connection status, latency, and metadata for a peer.
    
    Attributes:
        host: Peer IP address
        port: Peer port
        status: Connection status
        last_seen: Last successful communication timestamp
        latency_ms: Average latency in milliseconds
        failed_attempts: Number of consecutive failed connection attempts
    """
    host: str
    port: int
    status: PeerStatus = PeerStatus.DISCONNECTED
    last_seen: float = 0.0
    latency_ms: float = 0.0
    failed_attempts: int = 0
    
    def __post_init__(self):
        """Initialize timestamps"""
        if self.last_seen == 0.0:
            self.last_seen = time.time()
    
    @property
    def address(self) -> tuple[str, int]:
        """Get (host, port) tuple"""
        return (self.host, self.port)
    
    @property
    def is_connected(self) -> bool:
        """Check if peer is connected"""
        return self.status == PeerStatus.CONNECTED
    
    @property
    def is_alive(self) -> bool:
        """Check if peer is recently active (within 5 minutes)"""
        return time.time() - self.last_seen < 300
    
    def update_latency(self, latency_ms: float):
        """
        Update latency with exponential moving average
        
        Args:
            latency_ms: New latency measurement
        """
        if self.latency_ms == 0.0:
            self.latency_ms = latency_ms
        else:
            # EMA with alpha=0.3
            self.latency_ms = 0.3 * latency_ms + 0.7 * self.latency_ms
    
    def mark_success(self):
        """Mark successful communication"""
        self.status = PeerStatus.CONNECTED
        self.last_seen = time.time()
        self.failed_attempts = 0
    
    def mark_failure(self):
        """Mark failed communication"""
        self.failed_attempts += 1
        if self.failed_attempts >= 3:
            self.status = PeerStatus.FAILED
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            'host': self.host,
            'port': self.port,
            'status': self.status.value,
            'last_seen': self.last_seen,
            'latency_ms': self.latency_ms,
            'failed_attempts': self.failed_attempts
        }
    
    def __repr__(self) -> str:
        """String representation"""
        return f"Peer({self.host}:{self.port}, {self.status.value}, {self.latency_ms:.1f}ms)"
