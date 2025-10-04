"""
Ultra-lightweight database - compressed SQLite storage.
"""
import sqlite3
import time
from typing import Optional, List, Tuple
from .compression import CompressionManager

class Database:
    """Ultra-lightweight compressed database"""
    
    def __init__(self, path: str):
        self.path = path
        self.compression = CompressionManager()
        self._connection: Optional[sqlite3.Connection] = None
        self._stats = {'stored': 0, 'retrieved': 0, 'compressed_bytes': 0, 'original_bytes': 0}
        self._initialize()
    
    def _initialize(self) -> None:
        """Initialize database with optimizations"""
        self._connection = sqlite3.connect(self.path, check_same_thread=False)
        
        # Ultra-lightweight optimizations
        self._connection.executescript("""
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
    
    def store(self, tx_hash: bytes, data: bytes) -> bool:
        """Store data with compression"""
        if not self._connection:
            return False
        
        try:
            compressed = self.compression.compress(data)
            timestamp = int(time.time())
            
            self._connection.execute(
                "INSERT OR REPLACE INTO tx (h, d, t) VALUES (?, ?, ?)",
                (tx_hash, compressed, timestamp)
            )
            
            # Update stats
            self._stats['stored'] += 1
            self._stats['compressed_bytes'] += len(compressed)
            self._stats['original_bytes'] += len(data)
            
            return True
        except:
            return False
    
    def load(self, tx_hash: bytes) -> Optional[bytes]:
        """Load and decompress data"""
        if not self._connection:
            return None
        
        try:
            cursor = self._connection.execute("SELECT d FROM tx WHERE h = ?", (tx_hash,))
            row = cursor.fetchone()
            
            if row:
                decompressed = self.compression.decompress(row[0])
                self._stats['retrieved'] += 1
                return decompressed
            return None
        except:
            return None
    
    def exists(self, tx_hash: bytes) -> bool:
        """Check if transaction exists"""
        if not self._connection:
            return False
        
        try:
            cursor = self._connection.execute("SELECT 1 FROM tx WHERE h = ? LIMIT 1", (tx_hash,))
            return cursor.fetchone() is not None
        except:
            return False
    
    def get_recent(self, limit: int = 10) -> List[Tuple[bytes, bytes]]:
        """Get recent transactions"""
        if not self._connection:
            return []
        
        try:
            cursor = self._connection.execute(
                "SELECT h, d FROM tx ORDER BY t DESC LIMIT ?", (limit,)
            )
            results = []
            
            for row in cursor:
                tx_hash, compressed_data = row
                data = self.compression.decompress(compressed_data)
                results.append((tx_hash, data))
            
            return results
        except:
            return []
    
    def prune_old(self, max_age_hours: int = 24) -> int:
        """Prune old transactions"""
        if not self._connection:
            return 0
        
        try:
            cutoff_time = int(time.time()) - (max_age_hours * 3600)
            cursor = self._connection.execute("DELETE FROM tx WHERE t < ?", (cutoff_time,))
            deleted_count = cursor.rowcount
            
            # Vacuum to reclaim space
            self._connection.execute("VACUUM")
            
            return deleted_count
        except:
            return 0
    
    def get_stats(self) -> dict:
        """Get database statistics"""
        stats = self._stats.copy()
        
        # Add compression ratio
        if stats['original_bytes'] > 0:
            stats['compression_ratio'] = stats['compressed_bytes'] / stats['original_bytes']
            stats['space_saved'] = stats['original_bytes'] - stats['compressed_bytes']
        else:
            stats['compression_ratio'] = 1.0
            stats['space_saved'] = 0
        
        # Add database size
        try:
            import os
            if os.path.exists(self.path):
                stats['db_size_bytes'] = os.path.getsize(self.path)
            else:
                stats['db_size_bytes'] = 0
        except:
            stats['db_size_bytes'] = 0
        
        return stats
    
    def close(self) -> None:
        """Close database connection"""
        if self._connection:
            self._connection.close()
            self._connection = None
