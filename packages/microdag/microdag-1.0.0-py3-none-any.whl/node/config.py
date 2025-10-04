"""
Node Configuration
Configuration management for MicroDAG nodes
"""

from dataclasses import dataclass
from typing import Optional, List
import os


@dataclass
class NodeConfig:
    """
    Node configuration
    
    All configuration options for running a MicroDAG node.
    
    Attributes:
        data_dir: Directory for database storage
        p2p_port: Port for P2P network (default: 7075)
        api_port: Port for HTTP API (default: 7076)
        p2p_host: Host to bind P2P server (default: 0.0.0.0)
        api_host: Host to bind API server (default: 0.0.0.0)
        max_peers: Maximum number of peers to track (default: 1000)
        target_connections: Target active connections (default: 32)
        seed_nodes: List of seed node addresses
        enable_api: Enable HTTP API server (default: True)
        vote_timeout: Voting timeout in seconds (default: 2.0)
    """
    
    # Storage
    data_dir: str = "./data"
    
    # P2P Network
    p2p_port: int = 7075
    p2p_host: str = "0.0.0.0"
    max_peers: int = 1000
    target_connections: int = 32
    seed_nodes: Optional[List[tuple[str, int]]] = None
    
    # HTTP API
    api_port: int = 7076
    api_host: str = "0.0.0.0"
    enable_api: bool = True
    
    # Consensus
    vote_timeout: float = 2.0
    
    def __post_init__(self):
        """Validate and normalize configuration"""
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Validate ports
        if not (1024 <= self.p2p_port <= 65535):
            raise ValueError(f"Invalid P2P port: {self.p2p_port}")
        if not (1024 <= self.api_port <= 65535):
            raise ValueError(f"Invalid API port: {self.api_port}")
        
        # Validate peer settings
        if self.max_peers < 1:
            raise ValueError(f"max_peers must be >= 1: {self.max_peers}")
        if self.target_connections < 1:
            raise ValueError(f"target_connections must be >= 1: {self.target_connections}")
        if self.target_connections > self.max_peers:
            raise ValueError(
                f"target_connections ({self.target_connections}) "
                f"cannot exceed max_peers ({self.max_peers})"
            )
        
        # Validate vote timeout
        if self.vote_timeout <= 0:
            raise ValueError(f"vote_timeout must be > 0: {self.vote_timeout}")
    
    @classmethod
    def from_env(cls) -> 'NodeConfig':
        """
        Create configuration from environment variables
        
        Environment variables:
        - MICRODAG_DATA_DIR: Data directory
        - MICRODAG_P2P_PORT: P2P port
        - MICRODAG_API_PORT: API port
        - MICRODAG_P2P_HOST: P2P host
        - MICRODAG_API_HOST: API host
        - MICRODAG_MAX_PEERS: Maximum peers
        - MICRODAG_TARGET_CONNECTIONS: Target connections
        - MICRODAG_ENABLE_API: Enable API (true/false)
        - MICRODAG_VOTE_TIMEOUT: Vote timeout
        
        Returns:
            NodeConfig instance
        """
        return cls(
            data_dir=os.getenv('MICRODAG_DATA_DIR', './data'),
            p2p_port=int(os.getenv('MICRODAG_P2P_PORT', '7075')),
            api_port=int(os.getenv('MICRODAG_API_PORT', '7076')),
            p2p_host=os.getenv('MICRODAG_P2P_HOST', '0.0.0.0'),
            api_host=os.getenv('MICRODAG_API_HOST', '0.0.0.0'),
            max_peers=int(os.getenv('MICRODAG_MAX_PEERS', '1000')),
            target_connections=int(os.getenv('MICRODAG_TARGET_CONNECTIONS', '32')),
            enable_api=os.getenv('MICRODAG_ENABLE_API', 'true').lower() == 'true',
            vote_timeout=float(os.getenv('MICRODAG_VOTE_TIMEOUT', '2.0'))
        )
    
    def to_dict(self) -> dict:
        """Convert configuration to dictionary"""
        return {
            'data_dir': self.data_dir,
            'p2p_port': self.p2p_port,
            'api_port': self.api_port,
            'p2p_host': self.p2p_host,
            'api_host': self.api_host,
            'max_peers': self.max_peers,
            'target_connections': self.target_connections,
            'enable_api': self.enable_api,
            'vote_timeout': self.vote_timeout
        }
