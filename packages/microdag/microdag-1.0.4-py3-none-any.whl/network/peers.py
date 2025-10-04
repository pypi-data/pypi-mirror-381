"""
Peer Manager for MicroDAG
Handles peer discovery with DNS fallback
"""

import asyncio
import aiohttp
import time
import logging
from typing import List, Set
import random

logger = logging.getLogger(__name__)


class PeerManager:
    """Manages peer discovery and connections"""
    
    # Hardcoded seed nodes
    SEED_NODES = [
        "http://localhost:7076",  # Local seed for testing
        "http://localhost:7176",  # Local seed 2
        "http://localhost:7276",  # Local seed 3
    ]
    
    def __init__(self, storage, max_peers: int = 32):
        """
        Args:
            storage: MicroDAGStorage instance
            max_peers: Maximum number of active peers
        """
        self.storage = storage
        self.max_peers = max_peers
        self.known_peers: Set[str] = set(self.SEED_NODES)
        
        # Initialize with seeds
        for seed in self.SEED_NODES:
            self.storage.add_peer(seed)
    
    async def discover_peers(self) -> List[str]:
        """
        Discover peers from seeds and DNS
        
        Returns:
            List of discovered peer URLs
        """
        discovered = set()
        
        # Try DNS fallback first (if available)
        try:
            dns_peers = await self._discover_from_dns()
            discovered.update(dns_peers)
        except Exception as e:
            logger.debug(f"DNS discovery failed: {e}")
        
        # Discover from seed nodes
        for seed in self.SEED_NODES:
            try:
                peers = await self._get_peers_from(seed)
                discovered.update(peers)
            except Exception as e:
                logger.debug(f"Failed to discover from {seed}: {e}")
        
        # Add to known peers
        self.known_peers.update(discovered)
        
        # Store in database
        for peer in discovered:
            self.storage.add_peer(peer)
        
        logger.info(f"Discovered {len(discovered)} peers")
        return list(discovered)
    
    async def _discover_from_dns(self) -> List[str]:
        """
        Discover peers from DNS TXT records
        Format: seeds.microdag.org TXT "http://node1.microdag.org:7075"
        """
        try:
            import dns.resolver
            answers = dns.resolver.resolve('seeds.microdag.org', 'TXT')
            peers = []
            for txt in answers:
                peer_url = txt.to_text().strip('"')
                if peer_url.startswith('http'):
                    peers.append(peer_url)
            return peers
        except ImportError:
            logger.debug("dnspython not available, skipping DNS discovery")
            return []
        except Exception as e:
            logger.debug(f"DNS lookup failed: {e}")
            return []
    
    async def _get_peers_from(self, peer_url: str, timeout: int = 2) -> List[str]:
        """Get peer list from a specific peer"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{peer_url}/api/peers",
                    timeout=aiohttp.ClientTimeout(total=timeout)
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get('peers', [])
        except Exception as e:
            logger.debug(f"Failed to get peers from {peer_url}: {e}")
        
        return []
    
    def get_active_peers(self, limit: int = None) -> List[str]:
        """
        Get active peers from database
        
        Args:
            limit: Maximum number of peers to return (default: max_peers)
            
        Returns:
            List of peer URLs sorted by latency
        """
        if limit is None:
            limit = self.max_peers
        
        peers = self.storage.get_peers(limit=limit)
        return peers
    
    def get_random_peers(self, count: int = 8) -> List[str]:
        """Get random subset of active peers"""
        peers = self.get_active_peers()
        return random.sample(peers, min(count, len(peers)))
    
    async def broadcast_to_peers(self, endpoint: str, data: dict, 
                                 peers: List[str] = None, timeout: int = 2):
        """
        Broadcast data to peers asynchronously
        
        Args:
            endpoint: API endpoint (e.g., "/api/broadcast")
            data: JSON data to send
            peers: List of peers (default: random 8)
            timeout: Request timeout
        """
        if peers is None:
            peers = self.get_random_peers(8)
        
        async with aiohttp.ClientSession() as session:
            tasks = [
                self._post_to_peer(session, peer, endpoint, data, timeout)
                for peer in peers
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Update peer statistics
            for peer, result in zip(peers, results):
                if isinstance(result, Exception):
                    self.storage.record_peer_failure(peer)
                elif result:
                    # Success - could update latency here
                    pass
    
    async def _post_to_peer(self, session: aiohttp.ClientSession, 
                            peer: str, endpoint: str, data: dict, timeout: int) -> bool:
        """Post data to a single peer"""
        try:
            start = time.time()
            async with session.post(
                f"{peer}{endpoint}",
                json=data,
                timeout=aiohttp.ClientTimeout(total=timeout)
            ) as response:
                latency = time.time() - start
                
                if response.status == 200:
                    self.storage.update_peer_latency(peer, latency)
                    return True
                else:
                    self.storage.record_peer_failure(peer)
                    return False
        except Exception as e:
            logger.debug(f"Failed to post to {peer}: {e}")
            self.storage.record_peer_failure(peer)
            return False
    
    def cleanup_old_peers(self, max_age: int = 86400):
        """Remove peers not seen in max_age seconds"""
        self.storage.cleanup_old_peers(max_age)
    
    def get_stats(self) -> dict:
        """Get peer manager statistics"""
        return {
            "known_peers": len(self.known_peers),
            "active_peers": len(self.get_active_peers()),
            "seed_nodes": len(self.SEED_NODES)
        }
