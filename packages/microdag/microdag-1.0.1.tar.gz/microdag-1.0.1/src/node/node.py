"""
MicroDAG Full Node
Complete node implementation integrating all components
"""

import logging
import signal
import sys
import time
from typing import Optional

from .config import NodeConfig
from ..storage.leveldb import LevelDBStorage
from ..core.processing import TransactionProcessor
from ..core.consensus import ConflictResolver
from ..core.genesis import initialize_genesis
from ..network.protocol import NetworkServer, MessageHandler
from ..network.peers import PeerManager
from ..network.propagation import TransactionPropagator
from ..api import APIServer


logger = logging.getLogger(__name__)


class MicroDAGNode:
    """
    Complete MicroDAG full node
    
    Integrates all components:
    - LevelDB storage
    - Transaction processing
    - Conflict resolution
    - P2P networking
    - HTTP API
    
    Example:
        >>> # Create node with default config
        >>> node = MicroDAGNode()
        >>> node.start()
        >>> 
        >>> # Node is running...
        >>> 
        >>> node.stop()
    """
    
    def __init__(self, config: Optional[NodeConfig] = None):
        """
        Initialize MicroDAG node
        
        Args:
            config: Node configuration (uses defaults if None)
        """
        self.config = config or NodeConfig()
        self.running = False
        
        # Components (initialized in start())
        self.storage: Optional[LevelDBStorage] = None
        self.processor: Optional[TransactionProcessor] = None
        self.resolver: Optional[ConflictResolver] = None
        self.peer_manager: Optional[PeerManager] = None
        self.propagator: Optional[TransactionPropagator] = None
        self.network_server: Optional[NetworkServer] = None
        self.api_server: Optional[APIServer] = None
        
        logger.info("MicroDAG node initialized")
    
    def start(self):
        """
        Start node and all components
        
        Startup sequence:
        1. Open database
        2. Initialize genesis (if needed)
        3. Create components
        4. Start P2P server
        5. Start API server
        6. Bootstrap network
        """
        if self.running:
            logger.warning("Node already running")
            return
        
        logger.info("Starting MicroDAG node...")
        logger.info(f"Configuration: {self.config.to_dict()}")
        
        try:
            # 1. Open database
            logger.info(f"Opening database: {self.config.data_dir}")
            db_path = f"{self.config.data_dir}/microdag.db"
            self.storage = LevelDBStorage(db_path)
            self.storage.open()
            
            # 2. Initialize genesis (if needed)
            logger.info("Checking genesis...")
            try:
                genesis_keypair = initialize_genesis(self.storage)
                logger.info(f"Genesis initialized: {genesis_keypair.public_key.hex()[:16]}...")
            except ValueError as e:
                # Genesis already exists
                logger.info("Genesis already exists")
            
            # 3. Create components
            logger.info("Creating components...")
            
            # Transaction processor
            self.processor = TransactionProcessor(self.storage)
            
            # Conflict resolver
            self.resolver = ConflictResolver(
                self.storage,
                self.processor,
                vote_timeout=self.config.vote_timeout
            )
            
            # Peer manager
            self.peer_manager = PeerManager(
                max_peers=self.config.max_peers,
                target_connections=self.config.target_connections,
                seed_nodes=self.config.seed_nodes
            )
            
            # Transaction propagator
            self.propagator = TransactionPropagator(self.peer_manager)
            
            # Message handler
            message_handler = MessageHandler(
                storage=self.storage,
                processor=self.processor,
                get_peers=lambda: [
                    (p.host, p.port) for p in self.peer_manager.get_active_peers()
                ]
            )
            
            # 4. Start P2P server
            logger.info(f"Starting P2P server on {self.config.p2p_host}:{self.config.p2p_port}")
            self.network_server = NetworkServer(
                port=self.config.p2p_port,
                handler=message_handler,
                host=self.config.p2p_host,
                max_connections=self.config.target_connections
            )
            self.network_server.start()
            
            # 5. Start API server (if enabled)
            if self.config.enable_api:
                logger.info(f"Starting API server on {self.config.api_host}:{self.config.api_port}")
                self.api_server = APIServer(
                    port=self.config.api_port,
                    storage=self.storage,
                    propagator=self.propagator,
                    peer_manager=self.peer_manager,
                    host=self.config.api_host
                )
                self.api_server.start()
            
            # 6. Bootstrap network
            logger.info("Bootstrapping network...")
            self.peer_manager.bootstrap()
            
            self.running = True
            logger.info("✅ MicroDAG node started successfully!")
            logger.info(f"P2P: {self.config.p2p_host}:{self.config.p2p_port}")
            if self.config.enable_api:
                logger.info(f"API: http://{self.config.api_host}:{self.config.api_port}")
            
        except Exception as e:
            logger.error(f"Failed to start node: {e}")
            self.stop()
            raise
    
    def stop(self):
        """
        Stop node and all components
        
        Shutdown sequence:
        1. Stop API server
        2. Stop P2P server
        3. Close database
        """
        if not self.running:
            return
        
        logger.info("Stopping MicroDAG node...")
        
        # Stop API server
        if self.api_server:
            logger.info("Stopping API server...")
            self.api_server.stop()
        
        # Stop P2P server
        if self.network_server:
            logger.info("Stopping P2P server...")
            self.network_server.stop()
        
        # Close database
        if self.storage:
            logger.info("Closing database...")
            self.storage.close()
        
        self.running = False
        logger.info("✅ MicroDAG node stopped")
    
    def run(self):
        """
        Run node until interrupted
        
        Starts node and runs until SIGINT (Ctrl+C) or SIGTERM.
        """
        # Setup signal handlers
        def signal_handler(sig, frame):
            logger.info("\nReceived interrupt signal, shutting down...")
            self.stop()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        # Start node
        self.start()
        
        # Run forever
        logger.info("Node running. Press Ctrl+C to stop.")
        try:
            while self.running:
                # Maintain peer connections
                self.peer_manager.maintain_connections()
                
                # Sleep for a bit
                time.sleep(10)
        
        except KeyboardInterrupt:
            logger.info("\nShutting down...")
        
        finally:
            self.stop()
    
    def get_stats(self) -> dict:
        """
        Get node statistics
        
        Returns:
            Dictionary with node statistics
        """
        if not self.running:
            return {'status': 'stopped'}
        
        stats = {
            'status': 'running',
            'config': self.config.to_dict()
        }
        
        # Storage stats
        if self.storage:
            stats['storage'] = self.storage.get_stats()
        
        # Peer stats
        if self.peer_manager:
            stats['peers'] = self.peer_manager.get_stats()
        
        # Propagation stats
        if self.propagator:
            stats['propagation'] = self.propagator.get_stats()
        
        # Consensus stats
        if self.resolver:
            stats['consensus'] = {
                'conflicts': self.resolver.detector.get_conflict_count(),
                'voting': self.resolver.vote_collector.get_stats()
            }
        
        return stats
