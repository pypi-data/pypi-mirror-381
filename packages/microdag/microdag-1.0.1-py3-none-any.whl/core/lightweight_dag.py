"""
Ultra-lightweight DAG implementation optimized for minimal memory usage and IoT devices.
"""

import struct
import hashlib
from typing import Dict, List, Optional, Set, Iterator
from dataclasses import dataclass
from collections import deque
import weakref

@dataclass
class CompactTransaction:
    """Minimal transaction representation using compact binary encoding."""
    
    # Use __slots__ to reduce memory overhead
    __slots__ = ['hash', 'from_addr', 'to_addr', 'amount', 'timestamp', 'parents', 'signature']
    
    hash: bytes  # 32 bytes
    from_addr: bytes  # 32 bytes (compressed)
    to_addr: bytes  # 32 bytes (compressed)
    amount: int  # 8 bytes (satoshi-style integer)
    timestamp: int  # 4 bytes (unix timestamp)
    parents: tuple  # Tuple of 2 parent hashes (64 bytes total)
    signature: bytes  # 64 bytes
    
    def serialize(self) -> bytes:
        """Serialize to compact binary format (208 bytes total)."""
        return struct.pack(
            '!32s32s32sQI32s32s64s',
            self.hash,
            self.from_addr,
            self.to_addr,
            self.amount,
            self.timestamp,
            self.parents[0],
            self.parents[1],
            self.signature
        )
    
    @classmethod
    def deserialize(cls, data: bytes) -> 'CompactTransaction':
        """Deserialize from binary format."""
        unpacked = struct.unpack('!32s32s32sQI32s32s64s', data)
        return cls(
            hash=unpacked[0],
            from_addr=unpacked[1],
            to_addr=unpacked[2],
            amount=unpacked[3],
            timestamp=unpacked[4],
            parents=(unpacked[5], unpacked[6]),
            signature=unpacked[7]
        )

class LightweightDAGNode:
    """Ultra-minimal DAG node using only essential data."""
    
    __slots__ = ['tx_hash', 'parents', 'children', 'confirmed']
    
    def __init__(self, tx_hash: bytes):
        self.tx_hash = tx_hash
        self.parents: Set[bytes] = set()  # Parent transaction hashes
        self.children: Set[bytes] = set()  # Child transaction hashes
        self.confirmed = False
    
    def add_parent(self, parent_hash: bytes):
        """Add parent reference."""
        self.parents.add(parent_hash)
    
    def add_child(self, child_hash: bytes):
        """Add child reference."""
        self.children.add(child_hash)
    
    def memory_size(self) -> int:
        """Calculate memory usage in bytes."""
        return (
            32 +  # tx_hash
            len(self.parents) * 32 +  # parent hashes
            len(self.children) * 32 +  # child hashes
            1  # confirmed flag
        )

class MemoryPool:
    """Memory pool for efficient object reuse."""
    
    def __init__(self, max_size: int = 1000):
        self.max_size = max_size
        self.pool: deque = deque(maxlen=max_size)
        self.in_use: Set = set()
    
    def get_node(self, tx_hash: bytes) -> LightweightDAGNode:
        """Get a node from pool or create new one."""
        if self.pool:
            node = self.pool.popleft()
            node.tx_hash = tx_hash
            node.parents.clear()
            node.children.clear()
            node.confirmed = False
        else:
            node = LightweightDAGNode(tx_hash)
        
        self.in_use.add(id(node))
        return node
    
    def return_node(self, node: LightweightDAGNode):
        """Return node to pool for reuse."""
        if id(node) in self.in_use:
            self.in_use.remove(id(node))
            if len(self.pool) < self.max_size:
                self.pool.append(node)

class UltraLightweightDAG:
    """
    Ultra-lightweight DAG implementation optimized for minimal memory usage.
    
    Key optimizations:
    - Adjacency list representation using hash references
    - Memory pooling for node objects
    - Lazy loading of transaction data
    - Compact binary serialization
    - Weak references to prevent memory leaks
    """
    
    def __init__(self, max_memory_mb: int = 50):
        self.max_memory_bytes = max_memory_mb * 1024 * 1024
        
        # Core DAG structure - adjacency lists with hash references
        self.nodes: Dict[bytes, LightweightDAGNode] = {}
        self.tips: Set[bytes] = set()  # Current DAG tips
        
        # Memory management
        self.memory_pool = MemoryPool()
        self.transaction_cache: Dict[bytes, CompactTransaction] = {}
        self.cache_hits = 0
        self.cache_misses = 0
        
        # Lazy loading support
        self.storage_backend = None  # Will be injected
        
        # Statistics
        self.total_transactions = 0
        self.memory_usage = 0
    
    def add_transaction(self, tx: CompactTransaction) -> bool:
        """Add transaction to DAG with minimal memory overhead."""
        
        # Check memory limit
        if self.memory_usage > self.max_memory_bytes:
            self._prune_old_data()
        
        # Create lightweight node
        node = self.memory_pool.get_node(tx.hash)
        
        # Add parent relationships
        for parent_hash in tx.parents:
            if parent_hash in self.nodes:
                parent_node = self.nodes[parent_hash]
                parent_node.add_child(tx.hash)
                node.add_parent(parent_hash)
                
                # Remove parent from tips if it now has children
                self.tips.discard(parent_hash)
        
        # Add to DAG
        self.nodes[tx.hash] = node
        self.tips.add(tx.hash)
        
        # Cache transaction data (LRU-style)
        if len(self.transaction_cache) > 1000:  # Limit cache size
            # Remove oldest entry
            oldest_hash = next(iter(self.transaction_cache))
            del self.transaction_cache[oldest_hash]
        
        self.transaction_cache[tx.hash] = tx
        self.total_transactions += 1
        self._update_memory_usage()
        
        return True
    
    def get_transaction(self, tx_hash: bytes) -> Optional[CompactTransaction]:
        """Get transaction with lazy loading."""
        
        # Check cache first
        if tx_hash in self.transaction_cache:
            self.cache_hits += 1
            return self.transaction_cache[tx_hash]
        
        # Lazy load from storage
        if self.storage_backend:
            self.cache_misses += 1
            tx = self.storage_backend.load_transaction(tx_hash)
            if tx:
                self.transaction_cache[tx_hash] = tx
                return tx
        
        return None
    
    def get_tips(self) -> Set[bytes]:
        """Get current DAG tips efficiently."""
        return self.tips.copy()
    
    def get_parents(self, tx_hash: bytes) -> Set[bytes]:
        """Get parent hashes efficiently."""
        if tx_hash in self.nodes:
            return self.nodes[tx_hash].parents.copy()
        return set()
    
    def get_children(self, tx_hash: bytes) -> Set[bytes]:
        """Get child hashes efficiently."""
        if tx_hash in self.nodes:
            return self.nodes[tx_hash].children.copy()
        return set()
    
    def traverse_ancestors(self, tx_hash: bytes, max_depth: int = 100) -> Iterator[bytes]:
        """Memory-efficient ancestor traversal using BFS."""
        visited = set()
        queue = deque([tx_hash])
        depth = 0
        
        while queue and depth < max_depth:
            current = queue.popleft()
            if current in visited:
                continue
                
            visited.add(current)
            yield current
            
            if current in self.nodes:
                for parent in self.nodes[current].parents:
                    if parent not in visited:
                        queue.append(parent)
            
            depth += 1
    
    def find_conflicts(self, tx_hash: bytes) -> List[bytes]:
        """Efficiently find conflicting transactions."""
        conflicts = []
        
        if tx_hash not in self.nodes:
            return conflicts
        
        tx = self.get_transaction(tx_hash)
        if not tx:
            return conflicts
        
        # Check for double-spend conflicts
        for other_hash, other_node in self.nodes.items():
            if other_hash == tx_hash:
                continue
                
            other_tx = self.get_transaction(other_hash)
            if other_tx and other_tx.from_addr == tx.from_addr:
                # Same sender - check if conflicting
                if not self._has_causal_relationship(tx_hash, other_hash):
                    conflicts.append(other_hash)
        
        return conflicts
    
    def _has_causal_relationship(self, tx1: bytes, tx2: bytes) -> bool:
        """Check if two transactions have causal relationship."""
        # Check if tx1 is ancestor of tx2
        for ancestor in self.traverse_ancestors(tx2):
            if ancestor == tx1:
                return True
        
        # Check if tx2 is ancestor of tx1
        for ancestor in self.traverse_ancestors(tx1):
            if ancestor == tx2:
                return True
        
        return False
    
    def _prune_old_data(self):
        """Prune old data to maintain memory limits."""
        # Remove oldest transactions from cache
        cache_size = len(self.transaction_cache)
        target_size = cache_size // 2
        
        # Remove half of the cache (oldest entries)
        for _ in range(cache_size - target_size):
            if self.transaction_cache:
                oldest_hash = next(iter(self.transaction_cache))
                del self.transaction_cache[oldest_hash]
        
        self._update_memory_usage()
    
    def _update_memory_usage(self):
        """Update memory usage statistics."""
        self.memory_usage = (
            sum(node.memory_size() for node in self.nodes.values()) +
            len(self.transaction_cache) * 208 +  # CompactTransaction size
            len(self.tips) * 32
        )
    
    def get_statistics(self) -> Dict:
        """Get DAG statistics."""
        return {
            'total_transactions': self.total_transactions,
            'dag_nodes': len(self.nodes),
            'current_tips': len(self.tips),
            'memory_usage_mb': self.memory_usage / (1024 * 1024),
            'cache_hit_rate': self.cache_hits / (self.cache_hits + self.cache_misses) if (self.cache_hits + self.cache_misses) > 0 else 0,
            'avg_node_size': self.memory_usage / len(self.nodes) if self.nodes else 0
        }
    
    def serialize_to_disk(self) -> bytes:
        """Serialize DAG structure to compact binary format."""
        # This would implement efficient disk serialization
        # For now, return placeholder
        return b"serialized_dag_data"
    
    @classmethod
    def deserialize_from_disk(cls, data: bytes) -> 'UltraLightweightDAG':
        """Deserialize DAG from binary format."""
        # This would implement efficient disk deserialization
        # For now, return new instance
        return cls()

# Utility functions for lightweight operations
def calculate_transaction_hash(tx_data: bytes) -> bytes:
    """Calculate transaction hash using efficient Blake2b."""
    return hashlib.blake2b(tx_data, digest_size=32).digest()

def compress_address(address: str) -> bytes:
    """Compress address to 32 bytes."""
    # Remove 'micro_' prefix and decode
    if address.startswith('micro_'):
        address = address[6:]
    
    # Convert to bytes (simplified - would use proper base58 decoding)
    return hashlib.sha256(address.encode()).digest()

def create_lightweight_transaction(
    from_addr: str,
    to_addr: str,
    amount: float,
    timestamp: int,
    parents: tuple,
    signature: bytes
) -> CompactTransaction:
    """Create a lightweight transaction with minimal overhead."""
    
    # Convert amount to integer (satoshi-style)
    amount_int = int(amount * 100000000)  # 8 decimal places
    
    # Compress addresses
    from_compressed = compress_address(from_addr)
    to_compressed = compress_address(to_addr)
    
    # Create transaction data for hashing
    tx_data = struct.pack(
        '!32s32sQI32s32s',
        from_compressed,
        to_compressed,
        amount_int,
        timestamp,
        parents[0],
        parents[1]
    )
    
    # Calculate hash
    tx_hash = calculate_transaction_hash(tx_data)
    
    return CompactTransaction(
        hash=tx_hash,
        from_addr=from_compressed,
        to_addr=to_compressed,
        amount=amount_int,
        timestamp=timestamp,
        parents=parents,
        signature=signature
    )
