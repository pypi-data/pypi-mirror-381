"""
SQLite Storage Layer for MicroDAG
Ultra-lightweight persistent storage with WAL mode
"""

import sqlite3
import time
import logging
from typing import Optional, List, Dict, Tuple
from pathlib import Path

logger = logging.getLogger(__name__)


class MicroDAGStorage:
    """SQLite-based storage with WAL mode for concurrent writes"""
    
    def __init__(self, db_path: str = "microdag.db"):
        self.db_path = db_path
        
        # Ensure directory exists
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Connect with WAL mode for concurrent writes
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA synchronous=NORMAL")  # Faster writes
        
        self._init_db()
        logger.info(f"Storage initialized: {db_path} (WAL mode)")
    
    def _init_db(self):
        """Initialize database schema"""
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS transactions (
                hash TEXT PRIMARY KEY,
                data BLOB NOT NULL,
                timestamp INTEGER NOT NULL,
                confirmed INTEGER DEFAULT 0
            );
            
            CREATE TABLE IF NOT EXISTS accounts (
                address TEXT PRIMARY KEY,
                balance INTEGER NOT NULL DEFAULT 0,
                frontier BLOB,
                last_updated INTEGER NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS peers (
                url TEXT PRIMARY KEY,
                last_seen INTEGER NOT NULL,
                latency REAL DEFAULT 0.0,
                failures INTEGER DEFAULT 0
            );
            
            CREATE INDEX IF NOT EXISTS idx_tx_timestamp ON transactions(timestamp);
            CREATE INDEX IF NOT EXISTS idx_tx_confirmed ON transactions(confirmed);
            CREATE INDEX IF NOT EXISTS idx_peers_seen ON peers(last_seen);
        """)
        self.conn.commit()
    
    # Transaction operations
    def store_transaction(self, tx_hash: str, tx_data: bytes) -> bool:
        """Store a transaction (141 bytes)"""
        try:
            self.conn.execute(
                "INSERT OR IGNORE INTO transactions (hash, data, timestamp) VALUES (?, ?, ?)",
                (tx_hash, tx_data, int(time.time()))
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to store transaction {tx_hash}: {e}")
            return False
    
    def get_transaction(self, tx_hash: str) -> Optional[bytes]:
        """Retrieve transaction data"""
        cursor = self.conn.execute(
            "SELECT data FROM transactions WHERE hash = ?",
            (tx_hash,)
        )
        row = cursor.fetchone()
        return row[0] if row else None
    
    def has_transaction(self, tx_hash: str) -> bool:
        """Check if transaction exists"""
        cursor = self.conn.execute(
            "SELECT 1 FROM transactions WHERE hash = ? LIMIT 1",
            (tx_hash,)
        )
        return cursor.fetchone() is not None
    
    def confirm_transaction(self, tx_hash: str) -> bool:
        """Mark transaction as confirmed"""
        try:
            self.conn.execute(
                "UPDATE transactions SET confirmed = 1 WHERE hash = ?",
                (tx_hash,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to confirm transaction {tx_hash}: {e}")
            return False
    
    def get_recent_transactions(self, limit: int = 100) -> List[Tuple[str, bytes]]:
        """Get recent transactions"""
        cursor = self.conn.execute(
            "SELECT hash, data FROM transactions ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
        return cursor.fetchall()
    
    # Account operations
    def update_account(self, address: str, balance: int, frontier: bytes) -> bool:
        """Update account state"""
        try:
            self.conn.execute(
                "INSERT OR REPLACE INTO accounts (address, balance, frontier, last_updated) VALUES (?, ?, ?, ?)",
                (address, balance, frontier, int(time.time()))
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to update account {address}: {e}")
            return False
    
    def get_account(self, address: str) -> Optional[Dict]:
        """Get account state"""
        cursor = self.conn.execute(
            "SELECT balance, frontier FROM accounts WHERE address = ?",
            (address,)
        )
        row = cursor.fetchone()
        if row:
            return {
                "address": address,
                "balance": row[0],
                "frontier": row[1].hex() if row[1] else None
            }
        return None
    
    def get_account_count(self) -> int:
        """Get total number of accounts"""
        cursor = self.conn.execute("SELECT COUNT(*) FROM accounts")
        return cursor.fetchone()[0]
    
    # Peer operations
    def add_peer(self, url: str) -> bool:
        """Add or update peer"""
        try:
            self.conn.execute(
                "INSERT OR REPLACE INTO peers (url, last_seen) VALUES (?, ?)",
                (url, int(time.time()))
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add peer {url}: {e}")
            return False
    
    def update_peer_latency(self, url: str, latency: float):
        """Update peer latency"""
        self.conn.execute(
            "UPDATE peers SET latency = ?, last_seen = ? WHERE url = ?",
            (latency, int(time.time()), url)
        )
        self.conn.commit()
    
    def record_peer_failure(self, url: str):
        """Record peer failure"""
        self.conn.execute(
            "UPDATE peers SET failures = failures + 1 WHERE url = ?",
            (url,)
        )
        self.conn.commit()
    
    def get_peers(self, limit: int = 32) -> List[str]:
        """Get active peers (sorted by latency)"""
        cursor = self.conn.execute(
            "SELECT url FROM peers WHERE failures < 10 ORDER BY latency ASC, last_seen DESC LIMIT ?",
            (limit,)
        )
        return [row[0] for row in cursor.fetchall()]
    
    def cleanup_old_peers(self, max_age: int = 86400):
        """Remove peers not seen in max_age seconds"""
        cutoff = int(time.time()) - max_age
        self.conn.execute("DELETE FROM peers WHERE last_seen < ?", (cutoff,))
        self.conn.commit()
    
    # Statistics
    def get_stats(self) -> Dict:
        """Get database statistics"""
        stats = {}
        
        cursor = self.conn.execute("SELECT COUNT(*) FROM transactions")
        stats['total_transactions'] = cursor.fetchone()[0]
        
        cursor = self.conn.execute("SELECT COUNT(*) FROM transactions WHERE confirmed = 1")
        stats['confirmed_transactions'] = cursor.fetchone()[0]
        
        cursor = self.conn.execute("SELECT COUNT(*) FROM accounts")
        stats['total_accounts'] = cursor.fetchone()[0]
        
        cursor = self.conn.execute("SELECT COUNT(*) FROM peers")
        stats['total_peers'] = cursor.fetchone()[0]
        
        return stats
    
    def close(self):
        """Close database connection"""
        self.conn.close()
        logger.info("Storage closed")
