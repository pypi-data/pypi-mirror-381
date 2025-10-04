"""
Ultra-minimal storage - <1KB, bytes-only, function-based.
"""
import sqlite3
import zlib
import os
import time
from typing import Optional, List, Tuple

# Global storage state
_db_path = None
_connection = None
_stats = {'tx_count': 0, 'compressed_bytes': 0, 'original_bytes': 0}

def init_storage(db_path: str, max_size_kb: int = 1024):
    """Initialize ultra-lightweight storage"""
    global _db_path, _connection
    
    _db_path = db_path
    _connection = sqlite3.connect(db_path, check_same_thread=False)
    
    # Ultra-minimal schema and optimizations
    _connection.executescript(f"""
        PRAGMA journal_mode = MEMORY;
        PRAGMA synchronous = OFF;
        PRAGMA cache_size = -100;
        PRAGMA temp_store = MEMORY;
        
        CREATE TABLE IF NOT EXISTS tx (
            h BLOB PRIMARY KEY,
            d BLOB,
            t INTEGER
        ) WITHOUT ROWID;
        
        CREATE INDEX IF NOT EXISTS tx_t ON tx(t);
    """)

def store_transaction(tx_hash: bytes, tx_data: bytes, timestamp: int = None) -> bool:
    """Store transaction with compression"""
    global _connection, _stats
    
    if not _connection:
        return False
    
    if timestamp is None:
        timestamp = int(time.time())
    
    # Compress data
    compressed = zlib.compress(tx_data, level=1)
    
    try:
        _connection.execute("INSERT OR REPLACE INTO tx (h, d, t) VALUES (?, ?, ?)",
                          (tx_hash, compressed, timestamp))
        
        # Update stats
        _stats['tx_count'] += 1
        _stats['compressed_bytes'] += len(compressed)
        _stats['original_bytes'] += len(tx_data)
        
        return True
    except:
        return False

def get_transaction(tx_hash: bytes) -> Optional[bytes]:
    """Get transaction with decompression"""
    global _connection
    
    if not _connection:
        return None
    
    try:
        cursor = _connection.execute("SELECT d FROM tx WHERE h = ?", (tx_hash,))
        row = cursor.fetchone()
        
        if row:
            return zlib.decompress(row[0])
        return None
    except:
        return None

def has_transaction(tx_hash: bytes) -> bool:
    """Check if transaction exists"""
    global _connection
    
    if not _connection:
        return False
    
    try:
        cursor = _connection.execute("SELECT 1 FROM tx WHERE h = ? LIMIT 1", (tx_hash,))
        return cursor.fetchone() is not None
    except:
        return False

def get_recent_transactions(limit: int = 10) -> List[Tuple[bytes, bytes]]:
    """Get recent transactions"""
    global _connection
    
    if not _connection:
        return []
    
    try:
        cursor = _connection.execute("SELECT h, d FROM tx ORDER BY t DESC LIMIT ?", (limit,))
        results = []
        
        for row in cursor:
            tx_hash, compressed_data = row
            tx_data = zlib.decompress(compressed_data)
            results.append((tx_hash, tx_data))
        
        return results
    except:
        return []

def prune_old_transactions(max_age_hours: int = 24) -> int:
    """Prune transactions older than max_age_hours"""
    global _connection
    
    if not _connection:
        return 0
    
    cutoff_time = int(time.time()) - (max_age_hours * 3600)
    
    try:
        cursor = _connection.execute("DELETE FROM tx WHERE t < ?", (cutoff_time,))
        deleted_count = cursor.rowcount
        
        # Vacuum to reclaim space
        _connection.execute("VACUUM")
        
        return deleted_count
    except:
        return 0

def get_storage_stats() -> dict:
    """Get storage statistics"""
    global _stats, _db_path
    
    stats = _stats.copy()
    
    if _db_path and os.path.exists(_db_path):
        stats['db_size_bytes'] = os.path.getsize(_db_path)
        stats['db_size_kb'] = stats['db_size_bytes'] / 1024
    else:
        stats['db_size_bytes'] = 0
        stats['db_size_kb'] = 0
    
    if stats['original_bytes'] > 0:
        stats['compression_ratio'] = stats['compressed_bytes'] / stats['original_bytes']
        stats['space_saved_bytes'] = stats['original_bytes'] - stats['compressed_bytes']
    else:
        stats['compression_ratio'] = 1.0
        stats['space_saved_bytes'] = 0
    
    return stats

def compact_storage():
    """Compact storage to reclaim space"""
    global _connection
    
    if _connection:
        try:
            _connection.execute("VACUUM")
            return True
        except:
            return False
    return False

def close_storage():
    """Close storage connection"""
    global _connection
    
    if _connection:
        _connection.close()
        _connection = None

# Batch operations for efficiency
def store_transactions_batch(transactions: List[Tuple[bytes, bytes, int]]) -> int:
    """Store multiple transactions in batch"""
    global _connection, _stats
    
    if not _connection:
        return 0
    
    compressed_batch = []
    for tx_hash, tx_data, timestamp in transactions:
        compressed = zlib.compress(tx_data, level=1)
        compressed_batch.append((tx_hash, compressed, timestamp))
        
        # Update stats
        _stats['compressed_bytes'] += len(compressed)
        _stats['original_bytes'] += len(tx_data)
    
    try:
        _connection.execute("BEGIN TRANSACTION")
        _connection.executemany("INSERT OR REPLACE INTO tx (h, d, t) VALUES (?, ?, ?)",
                              compressed_batch)
        _connection.execute("COMMIT")
        
        _stats['tx_count'] += len(transactions)
        return len(transactions)
    except:
        _connection.execute("ROLLBACK")
        return 0

# Memory-mapped access for large queries
def get_transactions_range(start_time: int, end_time: int, limit: int = 100) -> List[Tuple[bytes, bytes]]:
    """Get transactions in time range"""
    global _connection
    
    if not _connection:
        return []
    
    try:
        cursor = _connection.execute(
            "SELECT h, d FROM tx WHERE t BETWEEN ? AND ? ORDER BY t DESC LIMIT ?",
            (start_time, end_time, limit)
        )
        
        results = []
        for row in cursor:
            tx_hash, compressed_data = row
            tx_data = zlib.decompress(compressed_data)
            results.append((tx_hash, tx_data))
        
        return results
    except:
        return []

# Utility functions
def estimate_storage_size(tx_count: int, avg_tx_size: int) -> dict:
    """Estimate storage requirements"""
    original_size = tx_count * avg_tx_size
    compressed_size = int(original_size * 0.7)  # Assume 70% compression
    
    return {
        'tx_count': tx_count,
        'original_kb': original_size / 1024,
        'compressed_kb': compressed_size / 1024,
        'saved_kb': (original_size - compressed_size) / 1024
    }

def check_storage_health() -> dict:
    """Check storage health"""
    global _connection, _db_path
    
    health = {
        'connected': _connection is not None,
        'db_exists': _db_path and os.path.exists(_db_path),
        'writable': False,
        'readable': False
    }
    
    if health['connected']:
        try:
            # Test write
            _connection.execute("SELECT 1")
            health['readable'] = True
            
            # Test write with temp data
            test_hash = b'test' + b'\x00' * 28
            _connection.execute("INSERT OR REPLACE INTO tx (h, d, t) VALUES (?, ?, ?)",
                              (test_hash, b'test', int(time.time())))
            _connection.execute("DELETE FROM tx WHERE h = ?", (test_hash,))
            health['writable'] = True
        except:
            pass
    
    return health
