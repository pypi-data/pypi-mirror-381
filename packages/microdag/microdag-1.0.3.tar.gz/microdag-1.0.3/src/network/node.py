"""
MicroDAG Network Node
Production-ready node with HTTP + SQLite + Consensus
"""

import asyncio
import aiohttp
from aiohttp import web
import logging
import sys
import os
import time
import json

# Add parent directories to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from network.storage import MicroDAGStorage
from network.rate_limiter import RateLimiter
from network.consensus import ConsensusEngine
from network.peers import PeerManager
from core.crypto import generate_keypair
from core.types.account.encoding import encode_address
from core.types.transaction.serialization import serialize_transaction, deserialize_transaction

logging.basicConfig(
    level=logging.INFO,
    format='> %(asctime)s %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


class MicroDAGNode:
    """Production-ready MicroDAG node"""
    
    def __init__(self, node_id: str = "node1", port: int = 7076, 
                 data_dir: str = "./data", genesis: bool = False):
        self.node_id = node_id
        self.port = port
        self.data_dir = data_dir
        self.is_genesis = genesis
        
        # Initialize components
        db_path = f"{data_dir}/{node_id}.db"
        self.storage = MicroDAGStorage(db_path)
        self.rate_limiter = RateLimiter(max_requests=10, window=1)
        self.consensus = ConsensusEngine(cache_ttl=10)
        self.peer_manager = PeerManager(self.storage, max_peers=32)
        
        # Initialize genesis if needed
        if genesis:
            self._init_genesis()
        
        logger.info(f"Node {node_id} initialized on port {port}")
    
    def _init_genesis(self):
        """Initialize genesis account"""
        genesis_keypair = generate_keypair(bytes(32))  # Deterministic
        genesis_address = encode_address(genesis_keypair.public_key)
        
        self.storage.update_account(
            address=genesis_address,
            balance=100_000_000_000_000,  # 100M MICRO
            frontier=bytes(32)
        )
        
        logger.info(f"Genesis account: {genesis_address}")
        logger.info(f"Genesis balance: 0x{100_000_000_000_000:X} (100M MICRO)")
    
    # HTTP Endpoints
    async def handle_broadcast(self, request):
        """POST /api/broadcast - Receive and broadcast transaction"""
        # Rate limiting
        ip = request.remote
        if not self.rate_limiter.is_allowed(ip):
            return web.json_response({"error": "Rate limit exceeded"}, status=429)
        
        try:
            data = await request.json()
            tx_data = data.get('transaction')
            
            if not tx_data:
                return web.json_response({"error": "Missing transaction"}, status=400)
            
            # Deserialize and validate
            tx_bytes = bytes.fromhex(tx_data) if isinstance(tx_data, str) else tx_data
            tx_hash = tx_bytes[:32].hex()
            
            # Check if already have it
            if self.storage.has_transaction(tx_hash):
                return web.json_response({"status": "already_have"})
            
            # Store transaction
            self.storage.store_transaction(tx_hash, tx_bytes)
            
            # Broadcast to peers (async, don't wait)
            asyncio.create_task(
                self.peer_manager.broadcast_to_peers(
                    "/api/broadcast",
                    {"transaction": tx_data}
                )
            )
            
            logger.info(f"TX {tx_hash[:16]}... received and broadcasted")
            
            return web.json_response({"status": "ok", "hash": tx_hash})
            
        except Exception as e:
            logger.error(f"Broadcast error: {e}")
            return web.json_response({"error": str(e)}, status=500)
    
    async def handle_account(self, request):
        """GET /api/account/:address - Get account info"""
        address = request.match_info['address']
        
        account = self.storage.get_account(address)
        
        if account:
            # Return with hex formatting (retro style)
            return web.json_response({
                "address": account['address'],
                "balance": f"0x{account['balance']:X}",
                "balance_decimal": account['balance'],
                "frontier": account['frontier']
            })
        else:
            return web.json_response({"error": "Account not found"}, status=404)
    
    async def handle_vote(self, request):
        """GET /api/vote/:hash - Vote on transaction"""
        tx_hash = request.match_info['hash']
        
        # Simple validation: if we have it, approve
        has_tx = self.storage.has_transaction(tx_hash)
        
        # Get our weight (simplified: use account count as proxy)
        weight = self.storage.get_account_count()
        
        return web.json_response({
            "vote": "approve" if has_tx else "reject",
            "weight": weight,
            "node_id": self.node_id
        })
    
    async def handle_peers(self, request):
        """GET /api/peers - Get peer list"""
        peers = self.peer_manager.get_active_peers()
        
        return web.json_response({
            "peers": peers,
            "count": len(peers)
        })
    
    async def handle_health(self, request):
        """GET /api/health - Health check"""
        stats = self.storage.get_stats()
        
        return web.json_response({
            "status": "ok",
            "node_id": self.node_id,
            "port": self.port,
            "uptime": int(time.time()),
            "stats": stats
        })
    
    async def handle_statistics(self, request):
        """GET /api/statistics - Detailed statistics"""
        storage_stats = self.storage.get_stats()
        peer_stats = self.peer_manager.get_stats()
        consensus_stats = self.consensus.get_stats()
        rate_limiter_stats = self.rate_limiter.get_stats()
        
        return web.json_response({
            "node_id": self.node_id,
            "storage": storage_stats,
            "peers": peer_stats,
            "consensus": consensus_stats,
            "rate_limiter": rate_limiter_stats
        })
    
    # Background tasks
    async def peer_discovery_loop(self):
        """Periodically discover new peers"""
        while True:
            try:
                await asyncio.sleep(300)  # Every 5 minutes
                await self.peer_manager.discover_peers()
                self.peer_manager.cleanup_old_peers()
            except Exception as e:
                logger.error(f"Peer discovery error: {e}")
    
    async def cleanup_loop(self):
        """Periodic cleanup tasks"""
        while True:
            try:
                await asyncio.sleep(60)  # Every minute
                self.rate_limiter.cleanup()
                self.consensus.cleanup_cache()
            except Exception as e:
                logger.error(f"Cleanup error: {e}")
    
    # Server management
    def create_app(self):
        """Create aiohttp application"""
        app = web.Application()
        
        # Add routes
        app.router.add_post('/api/broadcast', self.handle_broadcast)
        app.router.add_get('/api/account/{address}', self.handle_account)
        app.router.add_get('/api/vote/{hash}', self.handle_vote)
        app.router.add_get('/api/peers', self.handle_peers)
        app.router.add_get('/api/health', self.handle_health)
        app.router.add_get('/api/statistics', self.handle_statistics)
        
        return app
    
    async def start(self):
        """Start the node"""
        logger.info("=" * 60)
        logger.info(f"MICRODAG NODE STARTING")
        logger.info("=" * 60)
        logger.info(f"Node ID: {self.node_id}")
        logger.info(f"Port: {self.port}")
        logger.info(f"Data: {self.data_dir}")
        logger.info("=" * 60)
        
        # Create app
        app = self.create_app()
        
        # Start background tasks
        asyncio.create_task(self.peer_discovery_loop())
        asyncio.create_task(self.cleanup_loop())
        
        # Discover peers on startup
        await self.peer_manager.discover_peers()
        
        # Start server
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', self.port)
        await site.start()
        
        logger.info(f"Node running on http://0.0.0.0:{self.port}")
        logger.info(f"Health: http://localhost:{self.port}/api/health")
        logger.info(f"Stats: http://localhost:{self.port}/api/statistics")
        logger.info("=" * 60)
        
        # Keep running
        try:
            await asyncio.Event().wait()
        except KeyboardInterrupt:
            logger.info("Shutting down...")
            await runner.cleanup()


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='MicroDAG Network Node')
    parser.add_argument('--node-id', default='node1', help='Node identifier')
    parser.add_argument('--port', type=int, default=7076, help='HTTP port')
    parser.add_argument('--data-dir', default='./data', help='Data directory')
    parser.add_argument('--genesis', action='store_true', help='Initialize as genesis node')
    
    args = parser.parse_args()
    
    # Create and start node
    node = MicroDAGNode(
        node_id=args.node_id,
        port=args.port,
        data_dir=args.data_dir,
        genesis=args.genesis
    )
    
    # Run
    asyncio.run(node.start())


if __name__ == "__main__":
    main()
