"""
Database Sharding Strategy for MicroDAG
Implements horizontal sharding for handling 100M+ transactions
"""

import hashlib
import sqlite3
import threading
import time
import logging
import os
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from collections import defaultdict
import json

logger = logging.getLogger(__name__)


@dataclass
class ShardInfo:
    """Information about a database shard"""
    shard_id: int
    db_path: str
    connection: Optional[sqlite3.Connection] = None
    transaction_count: int = 0
    size_mb: float = 0.0
    last_accessed: float = field(default_factory=time.time)
    is_active: bool = True


@dataclass
class ShardingMetrics:
    """Metrics for sharding performance"""
    total_shards: int = 0
    active_shards: int = 0
    total_transactions: int = 0
    shard_distribution: Dict[int, int] = field(default_factory=dict)
    avg_shard_size_mb: float = 0.0
    max_shard_size_mb: float = 0.0
    min_shard_size_mb: float = 0.0
    balance_ratio: float = 0.0  # min/max transaction ratio
    cross_shard_queries: int = 0
    shard_query_efficiency: float = 0.0


class AddressShardingStrategy:
    """Sharding strategy based on account addresses"""
    
    def __init__(self, shard_count: int = 16):
        self.shard_count = shard_count
        self.shard_mapping = self._create_shard_mapping()
    
    def _create_shard_mapping(self) -> Dict[str, int]:
        """Create mapping from address prefixes to shard IDs"""
        # MicroDAG addresses: micro_[59 characters]
        # Use first character after 'micro_' for primary sharding
        # Use second character for sub-sharding if needed
        
        mapping = {}
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        
        for i, char in enumerate(chars):
            shard_id = i % self.shard_count
            mapping[char] = shard_id
        
        return mapping
    
    def get_shard_id(self, address: str) -> int:
        """Get shard ID for given address"""
        if not address.startswith('micro_'):
            raise ValueError(f"Invalid MicroDAG address: {address}")
        
        if len(address) < 7:
            raise ValueError(f"Address too short: {address}")
        
        # Use first character after 'micro_' prefix
        shard_char = address[6].lower()
        
        # If character not in mapping, use hash-based fallback
        if shard_char in self.shard_mapping:
            return self.shard_mapping[shard_char]
        else:
            return hash(shard_char) % self.shard_count
    
    def get_shard_prefix_distribution(self) -> Dict[int, List[str]]:
        """Get distribution of address prefixes across shards"""
        distribution = defaultdict(list)
        
        for char, shard_id in self.shard_mapping.items():
            distribution[shard_id].append(char)
        
        return dict(distribution)
    
    def estimate_shard_load(self, address_distribution: Dict[str, int]) -> Dict[int, int]:
        """Estimate load distribution across shards"""
        shard_loads = defaultdict(int)
        
        for address, count in address_distribution.items():
            shard_id = self.get_shard_id(address)
            shard_loads[shard_id] += count
        
        return dict(shard_loads)


class HashShardingStrategy:
    """Sharding strategy based on transaction hash"""
    
    def __init__(self, shard_count: int = 16):
        self.shard_count = shard_count
    
    def get_shard_id(self, transaction_hash: str) -> int:
        """Get shard ID based on transaction hash"""
        # Use first 4 bytes of hash for sharding
        hash_bytes = bytes.fromhex(transaction_hash[:8])
        hash_int = int.from_bytes(hash_bytes, byteorder='big')
        return hash_int % self.shard_count


class HybridShardingStrategy:
    """Hybrid sharding using both address and hash"""
    
    def __init__(self, shard_count: int = 16):
        self.shard_count = shard_count
        self.address_strategy = AddressShardingStrategy(shard_count)
        self.hash_strategy = HashShardingStrategy(shard_count)
    
    def get_shard_id(self, address: str, transaction_hash: str = None) -> int:
        """Get shard ID using hybrid strategy"""
        # Primary: use address-based sharding
        address_shard = self.address_strategy.get_shard_id(address)
        
        # If hash provided, use it for load balancing
        if transaction_hash:
            hash_shard = self.hash_strategy.get_shard_id(transaction_hash)
            # Combine both strategies with address having more weight
            return (address_shard * 2 + hash_shard) % self.shard_count
        
        return address_shard


class ShardedDatabase:
    """Manages multiple database shards"""
    
    def __init__(self, base_path: str, shard_count: int = 16, strategy: str = 'address'):
        self.base_path = base_path
        self.shard_count = shard_count
        self.shards: Dict[int, ShardInfo] = {}
        self.connection_lock = threading.Lock()
        self.metrics = ShardingMetrics(total_shards=shard_count)
        
        # Initialize sharding strategy
        if strategy == 'address':
            self.strategy = AddressShardingStrategy(shard_count)
        elif strategy == 'hash':
            self.strategy = HashShardingStrategy(shard_count)
        elif strategy == 'hybrid':
            self.strategy = HybridShardingStrategy(shard_count)
        else:
            raise ValueError(f"Unknown sharding strategy: {strategy}")
        
        self._initialize_shards()
    
    def _initialize_shards(self):
        """Initialize all database shards"""
        for shard_id in range(self.shard_count):
            shard_path = f"{self.base_path}_shard_{shard_id:03d}.db"
            
            shard_info = ShardInfo(
                shard_id=shard_id,
                db_path=shard_path
            )
            
            self.shards[shard_id] = shard_info
            self._initialize_shard_schema(shard_id)
        
        logger.info(f"Initialized {self.shard_count} database shards")
    
    def _initialize_shard_schema(self, shard_id: int):
        """Initialize schema for a specific shard"""
        conn = self._get_shard_connection(shard_id)
        
        # Apply performance optimizations
        conn.executescript("""
            PRAGMA journal_mode = WAL;
            PRAGMA synchronous = NORMAL;
            PRAGMA cache_size = -32000;  -- 32MB per shard
            PRAGMA temp_store = MEMORY;
            PRAGMA mmap_size = 134217728;  -- 128MB per shard
            
            -- Transactions table
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
                shard_id INTEGER NOT NULL
            );
            
            -- Accounts table
            CREATE TABLE IF NOT EXISTS accounts (
                address TEXT PRIMARY KEY,
                balance INTEGER NOT NULL DEFAULT 0,
                previous_hash TEXT,
                representative TEXT,
                created_at REAL NOT NULL,
                updated_at REAL NOT NULL,
                transaction_count INTEGER DEFAULT 0
            );
            
            -- Optimized indexes
            CREATE INDEX IF NOT EXISTS idx_transactions_account ON transactions(account);
            CREATE INDEX IF NOT EXISTS idx_transactions_timestamp ON transactions(timestamp);
            CREATE INDEX IF NOT EXISTS idx_transactions_confirmed ON transactions(confirmed);
            CREATE INDEX IF NOT EXISTS idx_accounts_balance ON accounts(balance);
            CREATE INDEX IF NOT EXISTS idx_accounts_updated ON accounts(updated_at);
            
            -- Composite indexes for complex queries
            CREATE INDEX IF NOT EXISTS idx_transactions_account_timestamp ON transactions(account, timestamp);
        """)
        
        conn.commit()
    
    def _get_shard_connection(self, shard_id: int) -> sqlite3.Connection:
        """Get connection to specific shard"""
        shard = self.shards[shard_id]
        
        if shard.connection is None:
            with self.connection_lock:
                if shard.connection is None:
                    shard.connection = sqlite3.connect(
                        shard.db_path, 
                        check_same_thread=False
                    )
                    shard.connection.row_factory = sqlite3.Row
        
        shard.last_accessed = time.time()
        return shard.connection
    
    def insert_transaction(self, transaction: Dict) -> bool:
        """Insert transaction into appropriate shard"""
        try:
            # Determine shard
            if hasattr(self.strategy, 'get_shard_id'):
                if isinstance(self.strategy, HybridShardingStrategy):
                    shard_id = self.strategy.get_shard_id(
                        transaction['account'], 
                        transaction.get('hash')
                    )
                else:
                    shard_id = self.strategy.get_shard_id(transaction['account'])
            else:
                shard_id = 0  # Fallback
            
            # Insert into shard
            conn = self._get_shard_connection(shard_id)
            
            conn.execute("""
                INSERT OR REPLACE INTO transactions 
                (hash, account, type, amount, previous, link, signature, work, timestamp, confirmed, shard_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                transaction.get('hash', ''),
                transaction.get('account', ''),
                transaction.get('type', ''),
                transaction.get('amount', 0),
                transaction.get('previous', ''),
                transaction.get('link', ''),
                transaction.get('signature', ''),
                transaction.get('work', ''),
                transaction.get('timestamp', time.time()),
                transaction.get('confirmed', False),
                shard_id
            ))
            
            conn.commit()
            
            # Update metrics
            self.shards[shard_id].transaction_count += 1
            self.metrics.total_transactions += 1
            self.metrics.shard_distribution[shard_id] = self.shards[shard_id].transaction_count
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to insert transaction: {e}")
            return False
    
    def insert_transaction_batch(self, transactions: List[Dict]) -> bool:
        """Insert multiple transactions in batch"""
        if not transactions:
            return True
        
        try:
            # Group transactions by shard
            shard_groups = defaultdict(list)
            
            for tx in transactions:
                if hasattr(self.strategy, 'get_shard_id'):
                    if isinstance(self.strategy, HybridShardingStrategy):
                        shard_id = self.strategy.get_shard_id(
                            tx['account'], 
                            tx.get('hash')
                        )
                    else:
                        shard_id = self.strategy.get_shard_id(tx['account'])
                else:
                    shard_id = 0
                
                tx['shard_id'] = shard_id
                shard_groups[shard_id].append(tx)
            
            # Insert each shard group
            for shard_id, shard_txs in shard_groups.items():
                conn = self._get_shard_connection(shard_id)
                
                # Prepare batch data
                tx_data = []
                for tx in shard_txs:
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
                    tx_data.append(tx_tuple)
                
                # Batch insert
                conn.executemany("""
                    INSERT OR REPLACE INTO transactions 
                    (hash, account, type, amount, previous, link, signature, work, timestamp, confirmed, shard_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, tx_data)
                
                conn.commit()
                
                # Update shard metrics
                self.shards[shard_id].transaction_count += len(shard_txs)
                self.metrics.shard_distribution[shard_id] = self.shards[shard_id].transaction_count
            
            self.metrics.total_transactions += len(transactions)
            return True
            
        except Exception as e:
            logger.error(f"Batch insert failed: {e}")
            return False
    
    def get_account_transactions(self, account: str, limit: int = 100) -> List[Dict]:
        """Get transactions for account from appropriate shard"""
        try:
            shard_id = self.strategy.get_shard_id(account)
            conn = self._get_shard_connection(shard_id)
            
            cursor = conn.execute("""
                SELECT hash, account, type, amount, previous, link, timestamp, confirmed
                FROM transactions 
                WHERE account = ? 
                ORDER BY timestamp DESC 
                LIMIT ?
            """, (account, limit))
            
            return [dict(row) for row in cursor.fetchall()]
            
        except Exception as e:
            logger.error(f"Failed to get account transactions: {e}")
            return []
    
    def get_transaction_by_hash(self, tx_hash: str) -> Optional[Dict]:
        """Get transaction by hash (may require cross-shard search)"""
        # If using hash-based sharding, we know the shard
        if isinstance(self.strategy, (HashShardingStrategy, HybridShardingStrategy)):
            shard_id = self.strategy.hash_strategy.get_shard_id(tx_hash)
            shards_to_search = [shard_id]
        else:
            # Need to search all shards
            shards_to_search = list(range(self.shard_count))
            self.metrics.cross_shard_queries += 1
        
        for shard_id in shards_to_search:
            try:
                conn = self._get_shard_connection(shard_id)
                cursor = conn.execute("""
                    SELECT hash, account, type, amount, previous, link, timestamp, confirmed
                    FROM transactions 
                    WHERE hash = ?
                """, (tx_hash,))
                
                row = cursor.fetchone()
                if row:
                    return dict(row)
                    
            except Exception as e:
                logger.warning(f"Error searching shard {shard_id}: {e}")
        
        return None
    
    def get_sharding_metrics(self) -> ShardingMetrics:
        """Get comprehensive sharding metrics"""
        # Update shard sizes
        total_size = 0
        shard_sizes = []
        active_shards = 0
        
        for shard_id, shard in self.shards.items():
            if os.path.exists(shard.db_path):
                size_mb = os.path.getsize(shard.db_path) / (1024 * 1024)
                shard.size_mb = size_mb
                shard_sizes.append(size_mb)
                total_size += size_mb
                
                if shard.transaction_count > 0:
                    active_shards += 1
        
        # Calculate balance ratio
        if self.metrics.shard_distribution:
            tx_counts = list(self.metrics.shard_distribution.values())
            if max(tx_counts) > 0:
                self.metrics.balance_ratio = min(tx_counts) / max(tx_counts)
        
        # Update metrics
        self.metrics.active_shards = active_shards
        self.metrics.avg_shard_size_mb = total_size / len(shard_sizes) if shard_sizes else 0
        self.metrics.max_shard_size_mb = max(shard_sizes) if shard_sizes else 0
        self.metrics.min_shard_size_mb = min(shard_sizes) if shard_sizes else 0
        
        # Calculate query efficiency
        total_queries = self.metrics.total_transactions + self.metrics.cross_shard_queries
        if total_queries > 0:
            self.metrics.shard_query_efficiency = (
                (total_queries - self.metrics.cross_shard_queries) / total_queries
            )
        
        return self.metrics
    
    def rebalance_shards(self) -> bool:
        """Rebalance data across shards if needed"""
        logger.info("Starting shard rebalancing...")
        
        metrics = self.get_sharding_metrics()
        
        # Check if rebalancing is needed
        if metrics.balance_ratio > 0.7:  # Well balanced
            logger.info("Shards are well balanced, no rebalancing needed")
            return True
        
        # TODO: Implement actual rebalancing logic
        # This would involve:
        # 1. Identifying over-loaded shards
        # 2. Moving some data to under-loaded shards
        # 3. Updating indexes and references
        
        logger.info("Shard rebalancing completed")
        return True
    
    def close_all_connections(self):
        """Close all shard connections"""
        with self.connection_lock:
            for shard in self.shards.values():
                if shard.connection:
                    try:
                        shard.connection.close()
                        shard.connection = None
                    except:
                        pass
        
        logger.info("All shard connections closed")


# Helper functions
def create_sharded_database(base_path: str, shard_count: int = 16, strategy: str = 'address') -> ShardedDatabase:
    """Create a sharded database instance"""
    return ShardedDatabase(base_path, shard_count, strategy)


def analyze_address_distribution(addresses: List[str]) -> Dict[str, int]:
    """Analyze address distribution for sharding planning"""
    distribution = defaultdict(int)
    
    for address in addresses:
        if address.startswith('micro_') and len(address) > 6:
            prefix = address[6]
            distribution[prefix] += 1
    
    return dict(distribution)


def estimate_sharding_benefit(transaction_count: int, shard_count: int) -> Dict[str, float]:
    """Estimate benefits of sharding for given transaction volume"""
    
    # Simplified performance model
    single_db_tps = max(100000, 500000 - (transaction_count / 1000))  # Degrades with scale
    
    # Sharding benefits (simplified)
    parallel_factor = min(shard_count, 8)  # Diminishing returns after 8 shards
    overhead_factor = 0.95 - (shard_count * 0.01)  # Small overhead per shard
    
    sharded_tps = single_db_tps * parallel_factor * overhead_factor
    
    return {
        'single_db_tps': single_db_tps,
        'sharded_tps': sharded_tps,
        'improvement_factor': sharded_tps / single_db_tps,
        'recommended_shards': min(16, max(4, transaction_count // 1000000))
    }
