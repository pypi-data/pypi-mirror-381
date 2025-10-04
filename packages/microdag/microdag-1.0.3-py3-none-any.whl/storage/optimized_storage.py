"""
Optimized Storage System for MicroDAG
Implements batch processing, sharding preparation, and performance optimizations for high-volume scenarios
"""

import sqlite3
import threading
import time
import logging
import hashlib
import json
import os
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor
import queue

logger = logging.getLogger(__name__)


@dataclass
class StorageMetrics:
    """Storage performance metrics"""
    total_writes: int = 0
    total_reads: int = 0
    batch_writes: int = 0
    avg_write_time_ms: float = 0.0
    avg_read_time_ms: float = 0.0
    avg_batch_size: float = 0.0
    database_size_mb: float = 0.0
    index_size_mb: float = 0.0
    write_queue_size: int = 0
    shard_distribution: Dict[str, int] = field(default_factory=dict)


@dataclass
class BatchWrite:
    """Batch write operation"""
    operation_type: str  # 'insert', 'update', 'delete'
    table: str
    data: List[Dict]
    timestamp: float = field(default_factory=time.time)


class ShardManager:
    """Manages database sharding for horizontal scaling"""
    
    def __init__(self, shard_count: int = 16):
        self.shard_count = shard_count
        self.shard_mapping = {}
        self.shard_stats = defaultdict(int)
    
    def get_shard_id(self, account_address: str) -> int:
        """Get shard ID for account address"""
        if not account_address.startswith('micro_'):
            raise ValueError("Invalid MicroDAG address format")
        
        # Use first character after 'micro_' for sharding
        shard_char = account_address[6:7].lower()
        
        # Map characters to shard IDs
        char_to_shard = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3,
            'e': 4, 'f': 5, 'g': 6, 'h': 7,
            'i': 8, 'j': 9, 'k': 10, 'l': 11,
            'm': 12, 'n': 13, 'o': 14, 'p': 15,
            # Fallback for other characters
        }
        
        shard_id = char_to_shard.get(shard_char, hash(shard_char) % self.shard_count)
        self.shard_stats[shard_id] += 1
        
        return shard_id
    
    def get_shard_database_path(self, base_path: str, shard_id: int) -> str:
        """Get database path for specific shard"""
        return f"{base_path}_shard_{shard_id:02d}.db"
    
    def get_shard_distribution(self) -> Dict[int, int]:
        """Get current shard distribution statistics"""
        return dict(self.shard_stats)


class BatchProcessor:
    """Processes database operations in batches for optimal performance"""
    
    def __init__(self, batch_size: int = 100, flush_interval: float = 1.0):
        self.batch_size = batch_size
        self.flush_interval = flush_interval
        self.write_queue = queue.Queue()
        self.batch_buffer = defaultdict(list)
        self.last_flush = time.time()
        self.processing = False
        self.processor_thread = None
        self.metrics = StorageMetrics()
        self._lock = threading.Lock()
    
    def start_processing(self):
        """Start batch processing thread"""
        if not self.processing:
            self.processing = True
            self.processor_thread = threading.Thread(target=self._process_batches, daemon=True)
            self.processor_thread.start()
            logger.info("Batch processor started")
    
    def stop_processing(self):
        """Stop batch processing and flush remaining batches"""
        self.processing = False
        if self.processor_thread:
            self.processor_thread.join(timeout=5)
        self._flush_all_batches()
        logger.info("Batch processor stopped")
    
    def add_write_operation(self, operation_type: str, table: str, data: Dict):
        """Add write operation to batch queue"""
        batch_write = BatchWrite(
            operation_type=operation_type,
            table=table,
            data=[data]
        )
        
        with self._lock:
            self.batch_buffer[f"{operation_type}_{table}"].append(data)
            self.metrics.write_queue_size = sum(len(batch) for batch in self.batch_buffer.values())
            
            # Check if we should flush
            if self._should_flush():
                self._flush_all_batches()
    
    def _should_flush(self) -> bool:
        """Check if batches should be flushed"""
        # Flush if any batch reaches target size
        for batch in self.batch_buffer.values():
            if len(batch) >= self.batch_size:
                return True
        
        # Flush if time interval exceeded
        if time.time() - self.last_flush >= self.flush_interval:
            return True
        
        return False
    
    def _process_batches(self):
        """Main batch processing loop"""
        while self.processing:
            try:
                time.sleep(0.1)  # Small delay to allow batching
                
                with self._lock:
                    if self._should_flush():
                        self._flush_all_batches()
                        
            except Exception as e:
                logger.error(f"Batch processing error: {e}")
    
    def _flush_all_batches(self):
        """Flush all pending batches"""
        if not self.batch_buffer:
            return
        
        flush_start = time.time()
        total_operations = 0
        
        for batch_key, batch_data in self.batch_buffer.items():
            if batch_data:
                operation_type, table = batch_key.split('_', 1)
                self._execute_batch(operation_type, table, batch_data)
                total_operations += len(batch_data)
        
        # Clear buffers
        self.batch_buffer.clear()
        self.last_flush = time.time()
        
        # Update metrics
        flush_time = (time.time() - flush_start) * 1000
        self.metrics.batch_writes += 1
        self.metrics.avg_write_time_ms = (
            (self.metrics.avg_write_time_ms * (self.metrics.batch_writes - 1) + flush_time) /
            self.metrics.batch_writes
        )
        self.metrics.avg_batch_size = (
            (self.metrics.avg_batch_size * (self.metrics.batch_writes - 1) + total_operations) /
            self.metrics.batch_writes
        )
        self.metrics.write_queue_size = 0
        
        logger.debug(f"Flushed {total_operations} operations in {flush_time:.1f}ms")
    
    def _execute_batch(self, operation_type: str, table: str, batch_data: List[Dict]):
        """Execute batch operation - to be implemented by storage backend"""
        # This is a placeholder - actual implementation depends on storage backend
        logger.debug(f"Executing batch {operation_type} on {table}: {len(batch_data)} operations")


class OptimizedSQLiteStorage:
    """High-performance SQLite storage with batching and optimization"""
    
    def __init__(self, db_path: str, enable_sharding: bool = False, shard_count: int = 16):
        self.db_path = db_path
        self.enable_sharding = enable_sharding
        self.shard_manager = ShardManager(shard_count) if enable_sharding else None
        self.batch_processor = BatchProcessor(batch_size=100, flush_interval=1.0)
        self.connections = {}  # Thread-local connections
        self.connection_lock = threading.Lock()
        self.metrics = StorageMetrics()
        
        # Performance optimization settings
        self.pragma_settings = {
            'journal_mode': 'WAL',  # Write-Ahead Logging for better concurrency
            'synchronous': 'NORMAL',  # Balance between safety and performance
            'cache_size': -64000,  # 64MB cache
            'temp_store': 'MEMORY',  # Store temp tables in memory
            'mmap_size': 268435456,  # 256MB memory-mapped I/O
            'page_size': 4096,  # Optimal page size
            'auto_vacuum': 'INCREMENTAL'  # Incremental vacuuming
        }
        
        self._initialize_database()
        self.batch_processor.start_processing()
    
    def _get_connection(self, shard_id: int = 0) -> sqlite3.Connection:
        """Get thread-local database connection"""
        thread_id = threading.get_ident()
        conn_key = f"{thread_id}_{shard_id}"
        
        if conn_key not in self.connections:
            with self.connection_lock:
                if conn_key not in self.connections:
                    if self.enable_sharding:
                        db_path = self.shard_manager.get_shard_database_path(self.db_path, shard_id)
                    else:
                        db_path = self.db_path
                    
                    conn = sqlite3.connect(db_path, check_same_thread=False)
                    conn.row_factory = sqlite3.Row
                    
                    # Apply performance optimizations
                    for pragma, value in self.pragma_settings.items():
                        conn.execute(f"PRAGMA {pragma} = {value}")
                    
                    self.connections[conn_key] = conn
                    logger.debug(f"Created connection for thread {thread_id}, shard {shard_id}")
        
        return self.connections[conn_key]
    
    def _initialize_database(self):
        """Initialize database schema with optimizations"""
        # Initialize main shard or all shards
        if self.enable_sharding:
            for shard_id in range(self.shard_manager.shard_count):
                self._initialize_shard(shard_id)
        else:
            self._initialize_shard(0)
    
    def _initialize_shard(self, shard_id: int):
        """Initialize individual shard database"""
        conn = self._get_connection(shard_id)
        
        # Create optimized schema
        conn.executescript("""
            -- Accounts table with optimized indexes
            CREATE TABLE IF NOT EXISTS accounts (
                address TEXT PRIMARY KEY,
                balance INTEGER NOT NULL DEFAULT 0,
                previous_hash TEXT,
                representative TEXT,
                created_at REAL NOT NULL,
                updated_at REAL NOT NULL
            );
            
            -- Transactions table with partitioning-friendly design
            CREATE TABLE IF NOT EXISTS transactions (
                hash TEXT PRIMARY KEY,
                account TEXT NOT NULL,
                type TEXT NOT NULL,
                amount INTEGER,
                previous TEXT,
                link TEXT,
                signature TEXT,
                work TEXT,
                timestamp REAL NOT NULL,
                confirmed BOOLEAN DEFAULT FALSE,
                shard_id INTEGER
            );
            
            -- Blocks table for DAG structure
            CREATE TABLE IF NOT EXISTS blocks (
                hash TEXT PRIMARY KEY,
                account TEXT NOT NULL,
                previous TEXT,
                representative TEXT,
                balance INTEGER NOT NULL,
                link TEXT,
                signature TEXT,
                work TEXT,
                timestamp REAL NOT NULL,
                height INTEGER,
                shard_id INTEGER
            );
            
            -- Optimized indexes for common queries
            CREATE INDEX IF NOT EXISTS idx_accounts_balance ON accounts(balance);
            CREATE INDEX IF NOT EXISTS idx_accounts_updated ON accounts(updated_at);
            
            CREATE INDEX IF NOT EXISTS idx_transactions_account ON transactions(account);
            CREATE INDEX IF NOT EXISTS idx_transactions_timestamp ON transactions(timestamp);
            CREATE INDEX IF NOT EXISTS idx_transactions_type ON transactions(type);
            CREATE INDEX IF NOT EXISTS idx_transactions_confirmed ON transactions(confirmed);
            
            CREATE INDEX IF NOT EXISTS idx_blocks_account ON blocks(account);
            CREATE INDEX IF NOT EXISTS idx_blocks_timestamp ON blocks(timestamp);
            CREATE INDEX IF NOT EXISTS idx_blocks_height ON blocks(height);
            CREATE INDEX IF NOT EXISTS idx_blocks_previous ON blocks(previous);
            
            -- Composite indexes for complex queries
            CREATE INDEX IF NOT EXISTS idx_transactions_account_timestamp ON transactions(account, timestamp);
            CREATE INDEX IF NOT EXISTS idx_blocks_account_height ON blocks(account, height);
        """)
        
        conn.commit()
        logger.info(f"Initialized shard {shard_id} database")
    
    def insert_transaction_batch(self, transactions: List[Dict]) -> bool:
        """Insert multiple transactions in a single batch"""
        if not transactions:
            return True
        
        start_time = time.time()
        
        try:
            # Group transactions by shard if sharding is enabled
            if self.enable_sharding:
                shard_groups = defaultdict(list)
                for tx in transactions:
                    shard_id = self.shard_manager.get_shard_id(tx['account'])
                    tx['shard_id'] = shard_id
                    shard_groups[shard_id].append(tx)
                
                # Insert each shard group
                for shard_id, shard_txs in shard_groups.items():
                    self._insert_transactions_to_shard(shard_txs, shard_id)
            else:
                self._insert_transactions_to_shard(transactions, 0)
            
            # Update metrics
            write_time = (time.time() - start_time) * 1000
            self.metrics.total_writes += len(transactions)
            self.metrics.avg_write_time_ms = (
                (self.metrics.avg_write_time_ms * (self.metrics.total_writes - len(transactions)) + write_time) /
                self.metrics.total_writes
            )
            
            return True
            
        except Exception as e:
            logger.error(f"Batch transaction insert failed: {e}")
            return False
    
    def _insert_transactions_to_shard(self, transactions: List[Dict], shard_id: int):
        """Insert transactions to specific shard"""
        conn = self._get_connection(shard_id)
        
        # Prepare batch insert
        insert_sql = """
            INSERT OR REPLACE INTO transactions 
            (hash, account, type, amount, previous, link, signature, work, timestamp, confirmed, shard_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        # Convert transactions to tuples for batch insert
        tx_tuples = []
        for tx in transactions:
            tx_tuple = (
                tx.get('hash', ''),
                tx.get('account', ''),
                tx.get('type', ''),
                tx.get('amount', 0),
                tx.get('previous', ''),
                tx.get('link', ''),
                tx.get('signature', ''),
                tx.get('work', ''),
                tx.get('timestamp', time.time()),
                tx.get('confirmed', False),
                shard_id
            )
            tx_tuples.append(tx_tuple)
        
        # Execute batch insert
        conn.executemany(insert_sql, tx_tuples)
        conn.commit()
        
        logger.debug(f"Inserted {len(transactions)} transactions to shard {shard_id}")
    
    def get_account_transactions(self, account: str, limit: int = 100) -> List[Dict]:
        """Get transactions for account with optimized query"""
        start_time = time.time()
        
        try:
            if self.enable_sharding:
                shard_id = self.shard_manager.get_shard_id(account)
                conn = self._get_connection(shard_id)
            else:
                conn = self._get_connection(0)
            
            # Optimized query with proper indexing
            cursor = conn.execute("""
                SELECT hash, account, type, amount, previous, link, timestamp, confirmed
                FROM transactions 
                WHERE account = ? 
                ORDER BY timestamp DESC 
                LIMIT ?
            """, (account, limit))
            
            transactions = [dict(row) for row in cursor.fetchall()]
            
            # Update metrics
            read_time = (time.time() - start_time) * 1000
            self.metrics.total_reads += 1
            self.metrics.avg_read_time_ms = (
                (self.metrics.avg_read_time_ms * (self.metrics.total_reads - 1) + read_time) /
                self.metrics.total_reads
            )
            
            return transactions
            
        except Exception as e:
            logger.error(f"Failed to get account transactions: {e}")
            return []
    
    def get_database_size(self) -> float:
        """Get total database size in MB"""
        total_size = 0
        
        if self.enable_sharding:
            for shard_id in range(self.shard_manager.shard_count):
                db_path = self.shard_manager.get_shard_database_path(self.db_path, shard_id)
                if os.path.exists(db_path):
                    total_size += os.path.getsize(db_path)
        else:
            if os.path.exists(self.db_path):
                total_size = os.path.getsize(self.db_path)
        
        return total_size / (1024 * 1024)  # Convert to MB
    
    def get_storage_metrics(self) -> StorageMetrics:
        """Get comprehensive storage metrics"""
        self.metrics.database_size_mb = self.get_database_size()
        
        if self.enable_sharding:
            self.metrics.shard_distribution = self.shard_manager.get_shard_distribution()
        
        return self.metrics
    
    def optimize_database(self):
        """Run database optimization operations"""
        logger.info("Starting database optimization...")
        
        if self.enable_sharding:
            for shard_id in range(self.shard_manager.shard_count):
                self._optimize_shard(shard_id)
        else:
            self._optimize_shard(0)
        
        logger.info("Database optimization completed")
    
    def _optimize_shard(self, shard_id: int):
        """Optimize individual shard"""
        conn = self._get_connection(shard_id)
        
        # Run optimization commands
        optimization_commands = [
            "PRAGMA optimize",
            "PRAGMA incremental_vacuum(1000)",
            "ANALYZE"
        ]
        
        for command in optimization_commands:
            try:
                conn.execute(command)
                conn.commit()
            except Exception as e:
                logger.warning(f"Optimization command '{command}' failed on shard {shard_id}: {e}")
    
    def close(self):
        """Close all connections and cleanup"""
        self.batch_processor.stop_processing()
        
        with self.connection_lock:
            for conn in self.connections.values():
                try:
                    conn.close()
                except:
                    pass
            self.connections.clear()
        
        logger.info("Storage connections closed")


# Helper functions for easy integration
def create_optimized_storage(db_path: str, enable_sharding: bool = False, shard_count: int = 16) -> OptimizedSQLiteStorage:
    """Create optimized storage instance"""
    return OptimizedSQLiteStorage(db_path, enable_sharding, shard_count)


def benchmark_storage_performance(storage: OptimizedSQLiteStorage, transaction_count: int = 10000) -> Dict:
    """Benchmark storage performance"""
    print(f"🔬 Benchmarking storage with {transaction_count:,} transactions...")
    
    # Generate test transactions
    test_transactions = []
    for i in range(transaction_count):
        tx = {
            'hash': hashlib.sha256(f"test_tx_{i}".encode()).hexdigest(),
            'account': f'micro_{"abcdefghijklmnop"[i % 16]}{"0" * 48}{i:010d}',
            'type': 'send',
            'amount': 1000000 + i,
            'previous': hashlib.sha256(f"prev_{i}".encode()).hexdigest(),
            'link': hashlib.sha256(f"link_{i}".encode()).hexdigest(),
            'timestamp': time.time() + i,
            'confirmed': True
        }
        test_transactions.append(tx)
    
    # Benchmark batch insert
    start_time = time.time()
    success = storage.insert_transaction_batch(test_transactions)
    insert_time = time.time() - start_time
    
    # Benchmark reads
    read_start = time.time()
    for i in range(min(100, transaction_count)):  # Test 100 random reads
        account = test_transactions[i]['account']
        storage.get_account_transactions(account, 10)
    read_time = time.time() - read_start
    
    # Get final metrics
    metrics = storage.get_storage_metrics()
    
    results = {
        'transaction_count': transaction_count,
        'insert_success': success,
        'total_insert_time': insert_time,
        'insert_tps': transaction_count / insert_time if insert_time > 0 else 0,
        'avg_read_time_ms': read_time * 10,  # Per read
        'database_size_mb': metrics.database_size_mb,
        'total_writes': metrics.total_writes,
        'total_reads': metrics.total_reads,
        'shard_distribution': metrics.shard_distribution
    }
    
    print(f"   Insert TPS: {results['insert_tps']:.1f}")
    print(f"   Database size: {results['database_size_mb']:.1f} MB")
    print(f"   Average read time: {results['avg_read_time_ms']:.2f} ms")
    
    return results
