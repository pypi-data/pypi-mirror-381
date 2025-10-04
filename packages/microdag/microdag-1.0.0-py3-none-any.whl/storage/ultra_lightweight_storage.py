"""
Ultra-lightweight storage system optimized for minimal disk usage and IoT devices.
"""

import sqlite3
import zlib
import struct
import os
import time
import threading
from typing import Dict, List, Optional, Tuple, Iterator
from dataclasses import dataclass
from contextlib import contextmanager
import mmap

@dataclass
class StorageConfig:
    """Configuration for ultra-lightweight storage."""
    
    max_db_size_mb: int = 100  # Maximum database size in MB
    compression_level: int = 1  # Fast compression (1-9)
    auto_vacuum: bool = True
    memory_cache_mb: int = 10
    write_batch_size: int = 1000
    pruning_enabled: bool = True
    max_transaction_age_days: int = 30

class CompressedTransaction:
    """Compressed transaction storage format."""
    
    __slots__ = ['hash', 'compressed_data', 'size', 'timestamp']
    
    def __init__(self, hash_bytes: bytes, data: bytes, timestamp: int):
        self.hash = hash_bytes
        self.compressed_data = zlib.compress(data, level=1)
        self.size = len(self.compressed_data)
        self.timestamp = timestamp
    
    def decompress(self) -> bytes:
        """Decompress transaction data."""
        return zlib.decompress(self.compressed_data)
    
    def compression_ratio(self) -> float:
        """Calculate compression ratio."""
        original_size = len(zlib.decompress(self.compressed_data))
        return self.size / original_size if original_size > 0 else 1.0

class UltraLightweightStorage:
    """
    Ultra-lightweight storage system with aggressive optimizations:
    
    - Data compression (zlib level 1 for speed)
    - Automatic pruning of old data
    - Memory-mapped file access for large datasets
    - Write batching to reduce I/O
    - Minimal SQLite schema
    - Automatic database optimization
    """
    
    def __init__(self, db_path: str, config: StorageConfig = None):
        self.db_path = db_path
        self.config = config or StorageConfig()
        self.connection = None
        self.write_buffer: List[Tuple] = []
        self.buffer_lock = threading.Lock()
        self.last_optimization = 0
        
        # Statistics
        self.stats = {
            'total_transactions': 0,
            'compressed_size': 0,
            'original_size': 0,
            'compression_ratio': 0.0,
            'pruned_transactions': 0,
            'cache_hits': 0,
            'cache_misses': 0
        }
        
        # Memory cache for frequently accessed data
        self.memory_cache: Dict[bytes, CompressedTransaction] = {}
        self.cache_access_times: Dict[bytes, float] = {}
        
        self._initialize_database()
    
    def _initialize_database(self):
        """Initialize database with optimal settings for lightweight operation."""
        self.connection = sqlite3.connect(
            self.db_path,
            check_same_thread=False,
            isolation_level=None  # Autocommit mode
        )
        
        # Optimize SQLite for minimal resource usage
        self.connection.executescript(f"""
            -- Performance optimizations
            PRAGMA journal_mode = WAL;
            PRAGMA synchronous = NORMAL;
            PRAGMA cache_size = -{self.config.memory_cache_mb * 1024};
            PRAGMA temp_store = MEMORY;
            PRAGMA mmap_size = {64 * 1024 * 1024};  -- 64MB memory mapping
            
            -- Space optimizations
            PRAGMA auto_vacuum = {'INCREMENTAL' if self.config.auto_vacuum else 'NONE'};
            PRAGMA page_size = 4096;
            
            -- Create minimal schema
            CREATE TABLE IF NOT EXISTS transactions (
                hash BLOB PRIMARY KEY,
                data BLOB NOT NULL,
                size INTEGER NOT NULL,
                timestamp INTEGER NOT NULL,
                compressed INTEGER DEFAULT 1
            ) WITHOUT ROWID;
            
            CREATE INDEX IF NOT EXISTS idx_timestamp ON transactions(timestamp);
            
            -- Metadata table for storage statistics
            CREATE TABLE IF NOT EXISTS storage_meta (
                key TEXT PRIMARY KEY,
                value TEXT
            );
        """)
        
        # Load existing statistics
        self._load_statistics()
    
    def store_transaction(self, tx_hash: bytes, tx_data: bytes, timestamp: int = None) -> bool:
        """Store transaction with compression and batching."""
        if timestamp is None:
            timestamp = int(time.time())
        
        # Create compressed transaction
        compressed_tx = CompressedTransaction(tx_hash, tx_data, timestamp)
        
        # Add to memory cache
        self._add_to_cache(tx_hash, compressed_tx)
        
        # Add to write buffer
        with self.buffer_lock:
            self.write_buffer.append((
                tx_hash,
                compressed_tx.compressed_data,
                compressed_tx.size,
                timestamp
            ))
            
            # Flush buffer if it's full
            if len(self.write_buffer) >= self.config.write_batch_size:
                self._flush_write_buffer()
        
        # Update statistics
        self.stats['total_transactions'] += 1
        self.stats['compressed_size'] += compressed_tx.size
        self.stats['original_size'] += len(tx_data)
        self.stats['compression_ratio'] = (
            self.stats['compressed_size'] / self.stats['original_size']
            if self.stats['original_size'] > 0 else 1.0
        )
        
        # Periodic maintenance
        if self.stats['total_transactions'] % 10000 == 0:
            self._perform_maintenance()
        
        return True
    
    def get_transaction(self, tx_hash: bytes) -> Optional[bytes]:
        """Retrieve transaction with caching and decompression."""
        
        # Check memory cache first
        if tx_hash in self.memory_cache:
            self.stats['cache_hits'] += 1
            self.cache_access_times[tx_hash] = time.time()
            return self.memory_cache[tx_hash].decompress()
        
        self.stats['cache_misses'] += 1
        
        # Query database
        cursor = self.connection.execute(
            "SELECT data, timestamp FROM transactions WHERE hash = ?",
            (tx_hash,)
        )
        
        row = cursor.fetchone()
        if row:
            compressed_data, timestamp = row
            
            # Create compressed transaction object
            compressed_tx = CompressedTransaction.__new__(CompressedTransaction)
            compressed_tx.hash = tx_hash
            compressed_tx.compressed_data = compressed_data
            compressed_tx.size = len(compressed_data)
            compressed_tx.timestamp = timestamp
            
            # Add to cache
            self._add_to_cache(tx_hash, compressed_tx)
            
            return compressed_tx.decompress()
        
        return None
    
    def get_transactions_by_timerange(self, start_time: int, end_time: int) -> Iterator[Tuple[bytes, bytes]]:
        """Get transactions in time range with minimal memory usage."""
        cursor = self.connection.execute(
            "SELECT hash, data FROM transactions WHERE timestamp BETWEEN ? AND ? ORDER BY timestamp",
            (start_time, end_time)
        )
        
        for row in cursor:
            tx_hash, compressed_data = row
            decompressed_data = zlib.decompress(compressed_data)
            yield tx_hash, decompressed_data
    
    def get_recent_transactions(self, limit: int = 100) -> List[Tuple[bytes, bytes]]:
        """Get most recent transactions efficiently."""
        cursor = self.connection.execute(
            "SELECT hash, data FROM transactions ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
        
        results = []
        for row in cursor:
            tx_hash, compressed_data = row
            decompressed_data = zlib.decompress(compressed_data)
            results.append((tx_hash, decompressed_data))
        
        return results
    
    def prune_old_transactions(self, max_age_days: int = None) -> int:
        """Prune old transactions to maintain storage limits."""
        if not self.config.pruning_enabled:
            return 0
        
        max_age = max_age_days or self.config.max_transaction_age_days
        cutoff_time = int(time.time()) - (max_age * 24 * 60 * 60)
        
        # Count transactions to be pruned
        cursor = self.connection.execute(
            "SELECT COUNT(*) FROM transactions WHERE timestamp < ?",
            (cutoff_time,)
        )
        count_to_prune = cursor.fetchone()[0]
        
        if count_to_prune > 0:
            # Remove old transactions
            self.connection.execute(
                "DELETE FROM transactions WHERE timestamp < ?",
                (cutoff_time,)
            )
            
            # Update statistics
            self.stats['pruned_transactions'] += count_to_prune
            
            # Clean up memory cache
            self._cleanup_cache()
            
            # Vacuum database to reclaim space
            if self.config.auto_vacuum:
                self.connection.execute("PRAGMA incremental_vacuum")
        
        return count_to_prune
    
    def _add_to_cache(self, tx_hash: bytes, compressed_tx: CompressedTransaction):
        """Add transaction to memory cache with LRU eviction."""
        current_time = time.time()
        
        # Check cache size limit
        max_cache_size = (self.config.memory_cache_mb * 1024 * 1024) // 1000  # Rough estimate
        
        if len(self.memory_cache) >= max_cache_size:
            # Evict least recently used item
            oldest_hash = min(self.cache_access_times.keys(), key=self.cache_access_times.get)
            del self.memory_cache[oldest_hash]
            del self.cache_access_times[oldest_hash]
        
        self.memory_cache[tx_hash] = compressed_tx
        self.cache_access_times[tx_hash] = current_time
    
    def _cleanup_cache(self):
        """Clean up memory cache by removing old entries."""
        current_time = time.time()
        max_age = 3600  # 1 hour
        
        expired_hashes = [
            tx_hash for tx_hash, access_time in self.cache_access_times.items()
            if current_time - access_time > max_age
        ]
        
        for tx_hash in expired_hashes:
            self.memory_cache.pop(tx_hash, None)
            self.cache_access_times.pop(tx_hash, None)
    
    def _flush_write_buffer(self):
        """Flush write buffer to database in batch."""
        if not self.write_buffer:
            return
        
        self.connection.execute("BEGIN TRANSACTION")
        try:
            self.connection.executemany(
                "INSERT OR REPLACE INTO transactions (hash, data, size, timestamp) VALUES (?, ?, ?, ?)",
                self.write_buffer
            )
            self.connection.execute("COMMIT")
            self.write_buffer.clear()
        except Exception:
            self.connection.execute("ROLLBACK")
            raise
    
    def _perform_maintenance(self):
        """Perform periodic maintenance tasks."""
        current_time = time.time()
        
        # Skip if maintenance was performed recently
        if current_time - self.last_optimization < 3600:  # 1 hour
            return
        
        # Flush any pending writes
        with self.buffer_lock:
            self._flush_write_buffer()
        
        # Prune old transactions
        if self.config.pruning_enabled:
            pruned = self.prune_old_transactions()
            if pruned > 0:
                print(f"Pruned {pruned} old transactions")
        
        # Check database size
        db_size_mb = os.path.getsize(self.db_path) / (1024 * 1024)
        if db_size_mb > self.config.max_db_size_mb:
            print(f"Warning: Database size ({db_size_mb:.1f}MB) exceeds limit ({self.config.max_db_size_mb}MB)")
        
        # Optimize database
        self.connection.execute("PRAGMA optimize")
        
        # Update statistics
        self._save_statistics()
        
        self.last_optimization = current_time
    
    def _load_statistics(self):
        """Load statistics from database."""
        cursor = self.connection.execute("SELECT key, value FROM storage_meta")
        for key, value in cursor:
            if key in self.stats:
                try:
                    self.stats[key] = float(value) if '.' in value else int(value)
                except ValueError:
                    pass
    
    def _save_statistics(self):
        """Save statistics to database."""
        for key, value in self.stats.items():
            self.connection.execute(
                "INSERT OR REPLACE INTO storage_meta (key, value) VALUES (?, ?)",
                (key, str(value))
            )
    
    def get_storage_statistics(self) -> Dict:
        """Get comprehensive storage statistics."""
        # Get database file size
        db_size_bytes = os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0
        
        # Get transaction count from database
        cursor = self.connection.execute("SELECT COUNT(*) FROM transactions")
        db_transaction_count = cursor.fetchone()[0]
        
        return {
            **self.stats,
            'db_size_mb': db_size_bytes / (1024 * 1024),
            'db_transaction_count': db_transaction_count,
            'cache_size': len(self.memory_cache),
            'write_buffer_size': len(self.write_buffer),
            'avg_compression_ratio': self.stats['compression_ratio'],
            'space_saved_mb': (self.stats['original_size'] - self.stats['compressed_size']) / (1024 * 1024)
        }
    
    def compact_database(self):
        """Compact database to reclaim space."""
        with self.buffer_lock:
            self._flush_write_buffer()
        
        self.connection.execute("VACUUM")
        print("Database compacted successfully")
    
    def close(self):
        """Close storage and cleanup resources."""
        with self.buffer_lock:
            self._flush_write_buffer()
        
        self._save_statistics()
        
        if self.connection:
            self.connection.close()
        
        self.memory_cache.clear()
        self.cache_access_times.clear()

@contextmanager
def lightweight_storage(db_path: str, config: StorageConfig = None):
    """Context manager for lightweight storage."""
    storage = UltraLightweightStorage(db_path, config)
    try:
        yield storage
    finally:
        storage.close()

# Utility functions for storage optimization
def estimate_storage_requirements(transaction_count: int, avg_tx_size: int, compression_ratio: float = 0.7) -> Dict:
    """Estimate storage requirements for given transaction volume."""
    original_size = transaction_count * avg_tx_size
    compressed_size = original_size * compression_ratio
    
    return {
        'transaction_count': transaction_count,
        'original_size_mb': original_size / (1024 * 1024),
        'compressed_size_mb': compressed_size / (1024 * 1024),
        'space_saved_mb': (original_size - compressed_size) / (1024 * 1024),
        'compression_ratio': compression_ratio
    }

def create_iot_optimized_config() -> StorageConfig:
    """Create storage configuration optimized for IoT devices."""
    return StorageConfig(
        max_db_size_mb=50,  # Very small for IoT
        compression_level=1,  # Fast compression
        auto_vacuum=True,
        memory_cache_mb=5,  # Minimal cache
        write_batch_size=100,  # Small batches
        pruning_enabled=True,
        max_transaction_age_days=7  # Aggressive pruning
    )

def create_server_optimized_config() -> StorageConfig:
    """Create storage configuration optimized for server deployment."""
    return StorageConfig(
        max_db_size_mb=1000,  # Larger for servers
        compression_level=3,  # Better compression
        auto_vacuum=True,
        memory_cache_mb=50,  # Larger cache
        write_batch_size=5000,  # Larger batches
        pruning_enabled=True,
        max_transaction_age_days=90  # Keep data longer
    )
