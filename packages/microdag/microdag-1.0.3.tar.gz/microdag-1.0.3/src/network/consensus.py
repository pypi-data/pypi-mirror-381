"""
Consensus Engine for MicroDAG
Simple balance-weighted voting with in-memory cache
"""

import asyncio
import aiohttp
import time
import logging
from collections import defaultdict
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class ConsensusEngine:
    """Balance-weighted consensus with vote caching"""
    
    def __init__(self, cache_ttl: int = 10):
        """
        Args:
            cache_ttl: Vote cache time-to-live in seconds
        """
        self.cache_ttl = cache_ttl
        self.vote_cache: Dict[str, Dict] = defaultdict(dict)  # {tx_hash: {peer: vote_data}}
        self.cache_timestamps: Dict[str, float] = {}  # {tx_hash: timestamp}
    
    async def get_consensus(self, tx_hash: str, peers: List[str], timeout: int = 1) -> bool:
        """
        Check if transaction has network consensus
        
        Args:
            tx_hash: Transaction hash
            peers: List of peer URLs
            timeout: Request timeout in seconds
            
        Returns:
            True if >51% of network weight approves
        """
        # Check cache first
        if self._is_cached(tx_hash):
            return self._check_cached_consensus(tx_hash)
        
        # Collect votes from peers
        await self._collect_votes(tx_hash, peers, timeout)
        
        # Check consensus
        return self._check_cached_consensus(tx_hash)
    
    async def _collect_votes(self, tx_hash: str, peers: List[str], timeout: int):
        """Collect votes from peers asynchronously"""
        async with aiohttp.ClientSession() as session:
            tasks = [
                self._get_vote_from_peer(session, peer, tx_hash, timeout)
                for peer in peers[:8]  # Limit to top 8 peers
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Process results
            for peer, result in zip(peers, results):
                if isinstance(result, Exception):
                    logger.debug(f"Failed to get vote from {peer}: {result}")
                    continue
                
                if result:
                    self.vote_cache[tx_hash][peer] = result
            
            # Update cache timestamp
            self.cache_timestamps[tx_hash] = time.time()
    
    async def _get_vote_from_peer(self, session: aiohttp.ClientSession, 
                                   peer: str, tx_hash: str, timeout: int) -> Optional[Dict]:
        """Get vote from a single peer"""
        try:
            async with session.get(
                f"{peer}/api/vote/{tx_hash}",
                timeout=aiohttp.ClientTimeout(total=timeout)
            ) as response:
                if response.status == 200:
                    return await response.json()
        except Exception as e:
            logger.debug(f"Vote request failed for {peer}: {e}")
        
        return None
    
    def _is_cached(self, tx_hash: str) -> bool:
        """Check if votes are cached and fresh"""
        if tx_hash not in self.cache_timestamps:
            return False
        
        age = time.time() - self.cache_timestamps[tx_hash]
        return age < self.cache_ttl
    
    def _check_cached_consensus(self, tx_hash: str) -> bool:
        """Check consensus from cached votes"""
        votes = self.vote_cache.get(tx_hash, {})
        
        if not votes:
            return False
        
        # Calculate weighted votes
        total_approve_weight = 0
        total_reject_weight = 0
        
        for vote_data in votes.values():
            weight = vote_data.get('weight', 0)
            vote = vote_data.get('vote', 'reject')
            
            if vote == 'approve':
                total_approve_weight += weight
            else:
                total_reject_weight += weight
        
        total_weight = total_approve_weight + total_reject_weight
        
        if total_weight == 0:
            return False
        
        # Require >51% approval
        approval_ratio = total_approve_weight / total_weight
        return approval_ratio > 0.51
    
    def add_local_vote(self, tx_hash: str, vote: str, weight: int):
        """Add local node's vote to cache"""
        self.vote_cache[tx_hash]['local'] = {
            'vote': vote,
            'weight': weight,
            'timestamp': time.time()
        }
        self.cache_timestamps[tx_hash] = time.time()
    
    def cleanup_cache(self):
        """Remove old cached votes"""
        now = time.time()
        expired = []
        
        for tx_hash, timestamp in self.cache_timestamps.items():
            if now - timestamp > self.cache_ttl * 2:
                expired.append(tx_hash)
        
        for tx_hash in expired:
            del self.vote_cache[tx_hash]
            del self.cache_timestamps[tx_hash]
        
        if expired:
            logger.debug(f"Cleaned up {len(expired)} expired vote caches")
    
    def get_stats(self) -> Dict:
        """Get consensus engine statistics"""
        return {
            "cached_votes": len(self.vote_cache),
            "cache_ttl": self.cache_ttl,
            "total_votes": sum(len(votes) for votes in self.vote_cache.values())
        }
