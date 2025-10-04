"""
Network Partition Recovery System for MicroDAG
Handles network splits, resynchronization, and data consistency
"""

import asyncio
import time
import hashlib
import logging
from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import aiohttp

logger = logging.getLogger(__name__)


@dataclass
class NetworkState:
    """Current network state information"""
    node_id: str
    last_seen: Dict[str, float] = field(default_factory=dict)  # peer_id -> timestamp
    partition_detected: bool = False
    partition_start_time: Optional[float] = None
    missing_transactions: Set[str] = field(default_factory=set)  # tx hashes
    sync_in_progress: bool = False


@dataclass
class SyncRequest:
    """Transaction synchronization request"""
    peer_url: str
    start_timestamp: float
    end_timestamp: float
    transaction_hashes: List[str] = field(default_factory=list)


@dataclass
class PartitionMetrics:
    """Partition recovery metrics"""
    partitions_detected: int = 0
    recovery_attempts: int = 0
    successful_recoveries: int = 0
    transactions_resynced: int = 0
    avg_recovery_time: float = 0.0
    last_partition_duration: float = 0.0


class PartitionDetector:
    """Detects network partitions based on peer connectivity"""
    
    def __init__(self, min_peers: int = 2, detection_threshold: float = 30.0):
        """
        Args:
            min_peers: Minimum peers required to avoid partition detection
            detection_threshold: Seconds without peer contact to trigger detection
        """
        self.min_peers = min_peers
        self.detection_threshold = detection_threshold
        self.peer_last_seen: Dict[str, float] = {}
        self.partition_callbacks = []
    
    def update_peer_activity(self, peer_id: str):
        """Update last seen time for a peer"""
        self.peer_last_seen[peer_id] = time.time()
    
    def check_partition_status(self) -> Tuple[bool, List[str]]:
        """
        Check if we're in a network partition
        
        Returns:
            (is_partitioned, active_peers)
        """
        now = time.time()
        active_peers = []
        
        for peer_id, last_seen in self.peer_last_seen.items():
            if now - last_seen < self.detection_threshold:
                active_peers.append(peer_id)
        
        is_partitioned = len(active_peers) < self.min_peers
        
        if is_partitioned:
            logger.warning(f"Partition detected: only {len(active_peers)} active peers")
        
        return is_partitioned, active_peers
    
    def add_partition_callback(self, callback):
        """Add callback to be called when partition is detected"""
        self.partition_callbacks.append(callback)
    
    def _notify_partition(self, is_partitioned: bool, active_peers: List[str]):
        """Notify callbacks of partition status change"""
        for callback in self.partition_callbacks:
            try:
                callback(is_partitioned, active_peers)
            except Exception as e:
                logger.error(f"Partition callback error: {e}")


class TransactionSynchronizer:
    """Handles transaction synchronization after partition recovery"""
    
    def __init__(self, storage, max_concurrent_syncs: int = 5):
        self.storage = storage
        self.max_concurrent_syncs = max_concurrent_syncs
        self.sync_semaphore = asyncio.Semaphore(max_concurrent_syncs)
        self.synced_hashes: Set[str] = set()
    
    async def sync_with_peer(self, peer_url: str, since_timestamp: float) -> List[str]:
        """
        Synchronize transactions with a peer since given timestamp
        
        Returns:
            List of synchronized transaction hashes
        """
        async with self.sync_semaphore:
            try:
                # Request transactions since timestamp
                async with aiohttp.ClientSession() as session:
                    params = {
                        'since': int(since_timestamp),
                        'limit': 1000  # Reasonable batch size
                    }
                    
                    async with session.get(
                        f"{peer_url}/api/transactions/since",
                        params=params,
                        timeout=aiohttp.ClientTimeout(total=30)
                    ) as response:
                        
                        if response.status != 200:
                            logger.warning(f"Sync failed with {peer_url}: {response.status}")
                            return []
                        
                        data = await response.json()
                        transactions = data.get('transactions', [])
                        
                        synced_hashes = []
                        for tx_data in transactions:
                            tx_hash = tx_data.get('hash')
                            if tx_hash and tx_hash not in self.synced_hashes:
                                # Store transaction if we don't have it
                                if not self.storage.has_transaction(tx_hash):
                                    self.storage.store_transaction(tx_data)
                                    synced_hashes.append(tx_hash)
                                    self.synced_hashes.add(tx_hash)
                        
                        logger.info(f"Synced {len(synced_hashes)} transactions from {peer_url}")
                        return synced_hashes
                        
            except Exception as e:
                logger.error(f"Sync error with {peer_url}: {e}")
                return []
    
    async def sync_missing_transactions(self, peer_urls: List[str], missing_hashes: List[str]) -> int:
        """
        Sync specific missing transactions from available peers
        
        Returns:
            Number of transactions successfully synced
        """
        if not missing_hashes:
            return 0
        
        synced_count = 0
        
        for peer_url in peer_urls:
            if synced_count >= len(missing_hashes):
                break
                
            try:
                async with aiohttp.ClientSession() as session:
                    # Request specific transactions
                    payload = {'hashes': missing_hashes}
                    
                    async with session.post(
                        f"{peer_url}/api/transactions/batch",
                        json=payload,
                        timeout=aiohttp.ClientTimeout(total=30)
                    ) as response:
                        
                        if response.status == 200:
                            data = await response.json()
                            transactions = data.get('transactions', [])
                            
                            for tx_data in transactions:
                                tx_hash = tx_data.get('hash')
                                if tx_hash in missing_hashes:
                                    self.storage.store_transaction(tx_data)
                                    synced_count += 1
                                    
            except Exception as e:
                logger.error(f"Batch sync error with {peer_url}: {e}")
        
        return synced_count


class NetworkPartitionRecovery:
    """Main partition recovery coordinator"""
    
    def __init__(self, node_id: str, storage, peer_manager):
        self.node_id = node_id
        self.storage = storage
        self.peer_manager = peer_manager
        
        # Components
        self.detector = PartitionDetector()
        self.synchronizer = TransactionSynchronizer(storage)
        
        # State
        self.network_state = NetworkState(node_id)
        self.metrics = PartitionMetrics()
        
        # Configuration
        self.recovery_timeout = 300.0  # 5 minutes max recovery time
        self.sync_batch_size = 100
        self.heartbeat_interval = 10.0  # Send heartbeat every 10s
        
        # Setup callbacks
        self.detector.add_partition_callback(self._on_partition_change)
        
        # Background tasks
        self._monitoring_task = None
        self._heartbeat_task = None
    
    async def start(self):
        """Start partition monitoring and recovery"""
        logger.info("Starting network partition recovery system")
        
        self._monitoring_task = asyncio.create_task(self._monitor_network())
        self._heartbeat_task = asyncio.create_task(self._send_heartbeats())
    
    async def stop(self):
        """Stop partition recovery system"""
        if self._monitoring_task:
            self._monitoring_task.cancel()
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
    
    async def _monitor_network(self):
        """Monitor network for partitions and trigger recovery"""
        while True:
            try:
                # Check partition status
                is_partitioned, active_peers = self.detector.check_partition_status()
                
                # Update network state
                if is_partitioned and not self.network_state.partition_detected:
                    # Partition just detected
                    self.network_state.partition_detected = True
                    self.network_state.partition_start_time = time.time()
                    self.metrics.partitions_detected += 1
                    logger.warning("Network partition detected")
                
                elif not is_partitioned and self.network_state.partition_detected:
                    # Partition resolved - trigger recovery
                    await self._trigger_recovery()
                
                # Update peer activity
                for peer_id in active_peers:
                    self.network_state.last_seen[peer_id] = time.time()
                
                await asyncio.sleep(5.0)  # Check every 5 seconds
                
            except Exception as e:
                logger.error(f"Network monitoring error: {e}")
                await asyncio.sleep(10.0)
    
    async def _send_heartbeats(self):
        """Send periodic heartbeats to peers"""
        while True:
            try:
                peers = self.peer_manager.get_active_peers()
                
                for peer_url in peers:
                    try:
                        async with aiohttp.ClientSession() as session:
                            heartbeat_data = {
                                'node_id': self.node_id,
                                'timestamp': time.time(),
                                'last_tx_hash': self.storage.get_latest_transaction_hash()
                            }
                            
                            async with session.post(
                                f"{peer_url}/api/heartbeat",
                                json=heartbeat_data,
                                timeout=aiohttp.ClientTimeout(total=5)
                            ) as response:
                                
                                if response.status == 200:
                                    # Update peer activity
                                    peer_id = self._extract_peer_id(peer_url)
                                    self.detector.update_peer_activity(peer_id)
                                    
                    except Exception as e:
                        logger.debug(f"Heartbeat failed to {peer_url}: {e}")
                
                await asyncio.sleep(self.heartbeat_interval)
                
            except Exception as e:
                logger.error(f"Heartbeat error: {e}")
                await asyncio.sleep(self.heartbeat_interval)
    
    async def _trigger_recovery(self):
        """Trigger partition recovery process"""
        if self.network_state.sync_in_progress:
            logger.info("Recovery already in progress")
            return
        
        logger.info("Starting partition recovery")
        self.network_state.sync_in_progress = True
        self.metrics.recovery_attempts += 1
        
        recovery_start = time.time()
        
        try:
            # Calculate partition duration
            if self.network_state.partition_start_time:
                partition_duration = recovery_start - self.network_state.partition_start_time
                self.metrics.last_partition_duration = partition_duration
                logger.info(f"Partition lasted {partition_duration:.1f} seconds")
            
            # Get available peers
            peers = self.peer_manager.get_active_peers()
            if not peers:
                logger.warning("No peers available for recovery")
                return
            
            # Determine sync start time (from partition start or last known good state)
            sync_start_time = self.network_state.partition_start_time or (recovery_start - 3600)
            
            # Sync transactions from all available peers
            total_synced = 0
            for peer_url in peers[:3]:  # Limit to 3 peers for efficiency
                synced_hashes = await self.synchronizer.sync_with_peer(peer_url, sync_start_time)
                total_synced += len(synced_hashes)
            
            # Detect and sync missing transactions
            missing_hashes = await self._detect_missing_transactions(peers)
            if missing_hashes:
                synced_missing = await self.synchronizer.sync_missing_transactions(peers, missing_hashes)
                total_synced += synced_missing
            
            # Update metrics
            self.metrics.transactions_resynced += total_synced
            self.metrics.successful_recoveries += 1
            
            recovery_time = time.time() - recovery_start
            self.metrics.avg_recovery_time = (
                (self.metrics.avg_recovery_time * (self.metrics.successful_recoveries - 1) + recovery_time)
                / self.metrics.successful_recoveries
            )
            
            logger.info(f"Recovery completed: {total_synced} transactions synced in {recovery_time:.1f}s")
            
        except Exception as e:
            logger.error(f"Recovery failed: {e}")
        
        finally:
            # Reset partition state
            self.network_state.partition_detected = False
            self.network_state.partition_start_time = None
            self.network_state.sync_in_progress = False
    
    async def _detect_missing_transactions(self, peer_urls: List[str]) -> List[str]:
        """Detect transactions we're missing compared to peers"""
        missing_hashes = []
        
        try:
            # Get our latest transactions
            our_hashes = set(self.storage.get_recent_transaction_hashes(1000))
            
            # Compare with each peer
            for peer_url in peer_urls[:2]:  # Check 2 peers max
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(
                            f"{peer_url}/api/transactions/hashes",
                            params={'limit': 1000},
                            timeout=aiohttp.ClientTimeout(total=10)
                        ) as response:
                            
                            if response.status == 200:
                                data = await response.json()
                                peer_hashes = set(data.get('hashes', []))
                                
                                # Find hashes they have that we don't
                                missing = peer_hashes - our_hashes
                                missing_hashes.extend(list(missing))
                                
                except Exception as e:
                    logger.debug(f"Missing transaction detection failed for {peer_url}: {e}")
            
            # Remove duplicates
            missing_hashes = list(set(missing_hashes))
            
            if missing_hashes:
                logger.info(f"Detected {len(missing_hashes)} missing transactions")
            
            return missing_hashes
            
        except Exception as e:
            logger.error(f"Missing transaction detection error: {e}")
            return []
    
    def _extract_peer_id(self, peer_url: str) -> str:
        """Extract peer ID from URL"""
        # Simple implementation - could be more sophisticated
        return hashlib.md5(peer_url.encode()).hexdigest()[:8]
    
    def _on_partition_change(self, is_partitioned: bool, active_peers: List[str]):
        """Handle partition status change"""
        if is_partitioned:
            logger.warning(f"Partition detected with {len(active_peers)} active peers")
        else:
            logger.info(f"Partition resolved, {len(active_peers)} peers available")
    
    def get_recovery_stats(self) -> Dict:
        """Get partition recovery statistics"""
        return {
            'partitions_detected': self.metrics.partitions_detected,
            'recovery_attempts': self.metrics.recovery_attempts,
            'successful_recoveries': self.metrics.successful_recoveries,
            'success_rate': (
                self.metrics.successful_recoveries / max(1, self.metrics.recovery_attempts)
            ),
            'transactions_resynced': self.metrics.transactions_resynced,
            'avg_recovery_time': self.metrics.avg_recovery_time,
            'last_partition_duration': self.metrics.last_partition_duration,
            'current_state': {
                'partition_detected': self.network_state.partition_detected,
                'sync_in_progress': self.network_state.sync_in_progress,
                'active_peers': len(self.network_state.last_seen)
            }
        }


# API endpoint handlers for partition recovery
async def handle_heartbeat(request, recovery_system):
    """Handle heartbeat from peer"""
    try:
        data = await request.json()
        peer_id = data.get('node_id')
        
        if peer_id:
            recovery_system.detector.update_peer_activity(peer_id)
        
        # Return our status
        return {
            'node_id': recovery_system.node_id,
            'timestamp': time.time(),
            'status': 'healthy'
        }
        
    except Exception as e:
        logger.error(f"Heartbeat handler error: {e}")
        return {'error': str(e)}, 400


async def handle_transactions_since(request, storage):
    """Handle request for transactions since timestamp"""
    try:
        since = int(request.query.get('since', 0))
        limit = int(request.query.get('limit', 1000))
        
        transactions = storage.get_transactions_since(since, limit)
        
        return {
            'transactions': transactions,
            'count': len(transactions),
            'timestamp': time.time()
        }
        
    except Exception as e:
        logger.error(f"Transactions since handler error: {e}")
        return {'error': str(e)}, 400


async def handle_transaction_hashes(request, storage):
    """Handle request for transaction hashes"""
    try:
        limit = int(request.query.get('limit', 1000))
        
        hashes = storage.get_recent_transaction_hashes(limit)
        
        return {
            'hashes': hashes,
            'count': len(hashes),
            'timestamp': time.time()
        }
        
    except Exception as e:
        logger.error(f"Transaction hashes handler error: {e}")
        return {'error': str(e)}, 400


async def handle_batch_transactions(request, storage):
    """Handle batch transaction request"""
    try:
        data = await request.json()
        requested_hashes = data.get('hashes', [])
        
        transactions = []
        for tx_hash in requested_hashes:
            tx_data = storage.get_transaction(tx_hash)
            if tx_data:
                transactions.append(tx_data)
        
        return {
            'transactions': transactions,
            'requested': len(requested_hashes),
            'found': len(transactions)
        }
        
    except Exception as e:
        logger.error(f"Batch transactions handler error: {e}")
        return {'error': str(e)}, 400
