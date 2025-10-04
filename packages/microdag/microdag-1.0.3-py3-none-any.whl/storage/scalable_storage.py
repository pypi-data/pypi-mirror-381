"""
Scalable Storage System for MicroDAG
Addresses SQLite bottlenecks and provides horizontal scaling options
"""

import sqlite3
import time
import os
import threading
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json

logger = logging.getLogger(__name__)


@dataclass
class StorageMetrics:
    """Storage performance metrics"""
    total_transactions: int = 0
    write_tps: float = 0.0
    read_tps: float = 0.0
    db_size_mb: float = 0.0
    avg_write_time_ms: float = 0.0
    avg_read_time_ms: float = 0.0
    connection_pool_size: int = 0
    cache_hit_rate: float = 0.0


class ConnectionPool:
    """SQLite connection pool for improved concurrency"""
    
    def __init__(self, db_path: str, pool_size: int = 10):
        self.db_path = db_path
        self.pool_size = pool_size
        self.connections = []
        self.available = threading.Semaphore(pool_size)
        self.lock = threading.Lock()
        
        # Initialize connections
        for _ in range(pool_size):
            conn = self._create_connection()
            self.connections.append(conn)
    
    def _create_connection(self) -> sqlite3.Connection:
        """Create optimized SQLite connection"""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        
        # Performance optimizations
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA cache_size=10000")  # 10MB cache
        conn.execute("PRAGMA temp_store=MEMORY")
        conn.execute("PRAGMA mmap_size=268435456")  # 256MB memory map
        conn.execute("PRAGMA optimize")
        
        return conn
    
    def get_connection(self) -> sqlite3.Connection:
        """Get connection from pool"""
        self.available.acquire()
        with self.lock:
            return self.connections.pop()
    
    def return_connection(self, conn: sqlite3.Connection):
        """Return connection to pool"""
        with self.lock:
            self.connections.append(conn)
        self.available.release()
    
    def close_all(self):
        """Close all connections"""
        with self.lock:
            for conn in self.connections:
                conn.close()
            self.connections.clear()


class TransactionCache:
    """LRU cache for frequently accessed transactions"""
    
    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self.cache = {}
        self.access_order = []
        self.lock = threading.RLock()
        self.hits = 0
        self.misses = 0
    
    def get(self, key: str) -> Optional[Dict]:
        """Get item from cache"""
        with self.lock:
            if key in self.cache:
                # Move to end (most recently used)
                self.access_order.remove(key)
                self.access_order.append(key)
                self.hits += 1
                return self.cache[key]
            
            self.misses += 1
            return None
    
    def put(self, key: str, value: Dict):
        """Put item in cache"""
        with self.lock:
            if key in self.cache:
                # Update existing
                self.access_order.remove(key)
            elif len(self.cache) >= self.max_size:
                # Remove least recently used
                lru_key = self.access_order.pop(0)
                del self.cache[lru_key]
            
            self.cache[key] = value
            self.access_order.append(key)
    
    def get_hit_rate(self) -> float:
        """Get cache hit rate"""
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0


class BatchProcessor:
    """Batch transaction processing for improved throughput"""
    
    def __init__(self, storage, batch_size: int = 1000, flush_interval: float = 1.0):
        self.storage = storage
        self.batch_size = batch_size
        self.flush_interval = flush_interval
        
        self.pending_writes = []
        self.pending_lock = threading.Lock()
        self.last_flush = time.time()
        
        # Start background flush thread
        self.flush_thread = threading.Thread(target=self._flush_loop, daemon=True)
        self.flush_thread.start()
    
    def add_transaction(self, tx_data: Dict):
        """Add transaction to batch"""
        with self.pending_lock:
            self.pending_writes.append(tx_data)
            
            # Flush if batch is full
            if len(self.pending_writes) >= self.batch_size:
                self._flush_batch()
    
    def _flush_loop(self):
        """Background flush loop"""
        while True:
            time.sleep(self.flush_interval)
            
            with self.pending_lock:
                if self.pending_writes and time.time() - self.last_flush > self.flush_interval:
                    self._flush_batch()
    
    def _flush_batch(self):
        """Flush pending transactions to storage"""
        if not self.pending_writes:
            return
        
        batch = self.pending_writes.copy()
        self.pending_writes.clear()
        self.last_flush = time.time()
        
        # Write batch to storage
        try:
            self.storage._write_transaction_batch(batch)
        except Exception as e:
            logger.error(f"Batch flush failed: {e}")
            # Re-add to pending (simple retry)
            with self.pending_lock:
                self.pending_writes.extend(batch)


class ShardedStorage:
    """Sharded storage for horizontal scaling"""
    
    def __init__(self, base_path: str, num_shards: int = 4):
        self.base_path = base_path
        self.num_shards = num_shards
        self.shards = []
        
        # Create shard storages
        for i in range(num_shards):
            shard_path = f"{base_path}_shard_{i}.db"
            shard = ScalableStorage(shard_path, enable_sharding=False)
            self.shards.append(shard)
    
    def _get_shard(self, key: str) -> 'ScalableStorage':
        """Get shard for given key"""
        shard_index = hash(key) % self.num_shards
        return self.shards[shard_index]
    
    def store_transaction(self, tx_data: Dict):
        """Store transaction in appropriate shard"""
        tx_hash = tx_data.get('hash', '')
        shard = self._get_shard(tx_hash)
        shard.store_transaction(tx_data)
    
    def get_transaction(self, tx_hash: str) -> Optional[Dict]:
        """Get transaction from appropriate shard"""
        shard = self._get_shard(tx_hash)
        return shard.get_transaction(tx_hash)
    
    def get_metrics(self) -> Dict:
        """Get combined metrics from all shards"""
        total_metrics = StorageMetrics()
        
        for shard in self.shards:
            shard_metrics = shard.get_metrics()
            total_metrics.total_transactions += shard_metrics.total_transactions
            total_metrics.db_size_mb += shard_metrics.db_size_mb
        
        # Average other metrics
        if self.shards:
            total_metrics.write_tps = sum(s.get_metrics().write_tps for s in self.shards) / len(self.shards)
            total_metrics.read_tps = sum(s.get_metrics().read_tps for s in self.shards) / len(self.shards)
            total_metrics.avg_write_time_ms = sum(s.get_metrics().avg_write_time_ms for s in self.shards) / len(self.shards)
            total_metrics.avg_read_time_ms = sum(s.get_metrics().avg_read_time_ms for s in self.shards) / len(self.shards)
        
        return total_metrics.__dict__


class ScalableStorage:
    """Enhanced storage system with performance optimizations"""
    
    def __init__(self, db_path: str, enable_sharding: bool = False, shard_count: int = 4):
        self.db_path = db_path
        self.enable_sharding = enable_sharding
        
        # Initialize storage backend
        if enable_sharding:
            self.storage = ShardedStorage(db_path, shard_count)
        else:
            # Single database with optimizations
            self.connection_pool = ConnectionPool(db_path, pool_size=20)
            self.cache = TransactionCache(max_size=50000)
            self.batch_processor = BatchProcessor(self, batch_size=500, flush_interval=0.5)
            self._init_database()
        
        # Metrics
        self.metrics = StorageMetrics()
        self.write_times = []
        self.read_times = []
        self.metrics_lock = threading.Lock()
    
    def _init_database(self):
        """Initialize database schema with optimizations"""
        conn = self.connection_pool.get_connection()
        try:
            # Create optimized schema
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS transactions (
                    hash TEXT PRIMARY KEY,
                    data BLOB NOT NULL,
                    timestamp INTEGER NOT NULL,
                    account TEXT NOT NULL,
                    amount INTEGER,
                    confirmed INTEGER DEFAULT 0
                );
                
                CREATE INDEX IF NOT EXISTS idx_timestamp ON transactions(timestamp);
                CREATE INDEX IF NOT EXISTS idx_account ON transactions(account);
                CREATE INDEX IF NOT EXISTS idx_confirmed ON transactions(confirmed);
                
                CREATE TABLE IF NOT EXISTS accounts (
                    address TEXT PRIMARY KEY,
                    balance INTEGER NOT NULL DEFAULT 0,
                    frontier BLOB,
                    last_updated INTEGER NOT NULL
                );
                
                CREATE INDEX IF NOT EXISTS idx_balance ON accounts(balance);
                CREATE INDEX IF NOT EXISTS idx_last_updated ON accounts(last_updated);
                
                -- Optimize database
                ANALYZE;
            """)
            conn.commit()
        finally:
            self.connection_pool.return_connection(conn)
    
    def store_transaction(self, tx_data: Dict):
        """Store transaction with optimizations"""
        if self.enable_sharding:
            self.storage.store_transaction(tx_data)
            return
        
        # Use batch processing for better throughput
        self.batch_processor.add_transaction(tx_data)
    
    def _write_transaction_batch(self, batch: List[Dict]):
        """Write batch of transactions"""
        start_time = time.time()
        
        conn = self.connection_pool.get_connection()
        try:
            # Prepare batch insert
            tx_records = []
            for tx_data in batch:
                tx_records.append((
                    tx_data.get('hash', ''),
                    json.dumps(tx_data).encode(),
                    tx_data.get('timestamp', int(time.time())),
                    tx_data.get('account', ''),
                    tx_data.get('amount', 0),
                    1 if tx_data.get('confirmed') else 0
                ))
            
            # Batch insert
            conn.executemany(
                "INSERT OR REPLACE INTO transactions (hash, data, timestamp, account, amount, confirmed) VALUES (?, ?, ?, ?, ?, ?)",
                tx_records
            )
            conn.commit()
            
            # Update cache
            for tx_data in batch:
                tx_hash = tx_data.get('hash', '')
                if tx_hash:
                    self.cache.put(tx_hash, tx_data)
            
            # Update metrics
            write_time = (time.time() - start_time) * 1000  # ms
            with self.metrics_lock:
                self.write_times.append(write_time)
                self.metrics.total_transactions += len(batch)
                
                # Keep only recent times for average calculation
                if len(self.write_times) > 1000:
                    self.write_times = self.write_times[-1000:]
                
                if self.write_times:
                    self.metrics.avg_write_time_ms = sum(self.write_times) / len(self.write_times)
                    self.metrics.write_tps = len(batch) / (write_time / 1000) if write_time > 0 else 0
        
        finally:
            self.connection_pool.return_connection(conn)
    
    def get_transaction(self, tx_hash: str) -> Optional[Dict]:
        """Get transaction with caching"""
        if self.enable_sharding:
            return self.storage.get_transaction(tx_hash)
        
        start_time = time.time()
        
        # Check cache first
        cached = self.cache.get(tx_hash)
        if cached:
            return cached
        
        # Query database
        conn = self.connection_pool.get_connection()
        try:
            cursor = conn.execute("SELECT data FROM transactions WHERE hash = ?", (tx_hash,))
            row = cursor.fetchone()
            
            if row:
                tx_data = json.loads(row[0].decode())
                self.cache.put(tx_hash, tx_data)
                
                # Update metrics
                read_time = (time.time() - start_time) * 1000
                with self.metrics_lock:
                    self.read_times.append(read_time)
                    if len(self.read_times) > 1000:
                        self.read_times = self.read_times[-1000:]
                    
                    if self.read_times:
                        self.metrics.avg_read_time_ms = sum(self.read_times) / len(self.read_times)
                
                return tx_data
            
            return None
            
        finally:
            self.connection_pool.return_connection(conn)
    
    def get_transactions_since(self, timestamp: int, limit: int = 1000) -> List[Dict]:
        """Get transactions since timestamp"""
        if self.enable_sharding:
            # Aggregate from all shards
            all_transactions = []
            for shard in self.storage.shards:
                shard_txs = shard.get_transactions_since(timestamp, limit // len(self.storage.shards))
                all_transactions.extend(shard_txs)
            
            # Sort by timestamp and limit
            all_transactions.sort(key=lambda x: x.get('timestamp', 0))
            return all_transactions[:limit]
        
        conn = self.connection_pool.get_connection()
        try:
            cursor = conn.execute(
                "SELECT data FROM transactions WHERE timestamp >= ? ORDER BY timestamp LIMIT ?",
                (timestamp, limit)
            )
            
            transactions = []
            for row in cursor.fetchall():
                tx_data = json.loads(row[0].decode())
                transactions.append(tx_data)
            
            return transactions
            
        finally:
            self.connection_pool.return_connection(conn)
    
    def get_recent_transaction_hashes(self, limit: int = 1000) -> List[str]:
        """Get recent transaction hashes"""
        if self.enable_sharding:
            all_hashes = []
            for shard in self.storage.shards:
                shard_hashes = shard.get_recent_transaction_hashes(limit // len(self.storage.shards))
                all_hashes.extend(shard_hashes)
            return all_hashes[:limit]
        
        conn = self.connection_pool.get_connection()
        try:
            cursor = conn.execute(
                "SELECT hash FROM transactions ORDER BY timestamp DESC LIMIT ?",
                (limit,)
            )
            
            return [row[0] for row in cursor.fetchall()]
            
        finally:
            self.connection_pool.return_connection(conn)
    
    def get_metrics(self) -> StorageMetrics:
        """Get storage performance metrics"""
        if self.enable_sharding:
            return self.storage.get_metrics()
        
        with self.metrics_lock:
            # Update database size
            if os.path.exists(self.db_path):
                self.metrics.db_size_mb = os.path.getsize(self.db_path) / 1024 / 1024
            
            # Update cache metrics
            self.metrics.cache_hit_rate = self.cache.get_hit_rate()
            self.metrics.connection_pool_size = self.connection_pool.pool_size
            
            return self.metrics
    
    def optimize_database(self):
        """Run database optimization"""
        if self.enable_sharding:
            for shard in self.storage.shards:
                shard.optimize_database()
            return
        
        conn = self.connection_pool.get_connection()
        try:
            # Run optimization commands
            conn.execute("VACUUM")
            conn.execute("ANALYZE")
            conn.execute("PRAGMA optimize")
            conn.commit()
            
            logger.info("Database optimization completed")
            
        finally:
            self.connection_pool.return_connection(conn)
    
    def close(self):
        """Close storage system"""
        if self.enable_sharding:
            for shard in self.storage.shards:
                shard.close()
        else:
            self.connection_pool.close_all()


# Factory function for creating optimized storage
def create_scalable_storage(db_path: str, expected_volume: int = 1000000) -> ScalableStorage:
    """
    Create optimized storage based on expected transaction volume
    
    Args:
        db_path: Database file path
        expected_volume: Expected number of transactions
        
    Returns:
        Configured ScalableStorage instance
    """
    if expected_volume > 5000000:  # >5M transactions - use sharding
        return ScalableStorage(db_path, enable_sharding=True, shard_count=8)
    elif expected_volume > 1000000:  # >1M transactions - use optimized single DB
        return ScalableStorage(db_path, enable_sharding=False)
    else:  # <1M transactions - standard configuration
        return ScalableStorage(db_path, enable_sharding=False)
