"""
Ultra-minimal DAG implementation - <2KB total, bytes-only, function-based.
"""
import struct
import hashlib
from typing import Dict, Set, Tuple, Optional

# Ultra-compact transaction: 208 bytes total
def pack_transaction(from_addr: bytes, to_addr: bytes, amount: int, 
                    timestamp: int, parent1: bytes, parent2: bytes, 
                    signature: bytes) -> bytes:
    """Pack transaction into 208 bytes: 32+32+8+4+32+32+64+4 (hash at end)"""
    data = struct.pack('!32s32sQI32s32s64s', from_addr, to_addr, amount, 
                      timestamp, parent1, parent2, signature)
    tx_hash = hashlib.blake2b(data, digest_size=32).digest()
    return data + tx_hash

def unpack_transaction(data: bytes) -> Tuple[bytes, bytes, int, int, bytes, bytes, bytes, bytes]:
    """Unpack 208-byte transaction"""
    unpacked = struct.unpack('!32s32sQI32s32s64s32s', data)
    return unpacked  # from, to, amount, time, p1, p2, sig, hash

# Minimal DAG node: 97 bytes (32 hash + 1 byte parent count + 32*2 parents + 0 children initially)
def create_node(tx_hash: bytes, parents: Set[bytes]) -> bytes:
    """Create minimal node representation"""
    parent_list = list(parents)[:2]  # Max 2 parents
    while len(parent_list) < 2:
        parent_list.append(b'\x00' * 32)  # Pad with zeros
    
    return struct.pack('!32sB32s32s', tx_hash, len(parents), 
                      parent_list[0], parent_list[1])

def unpack_node(data: bytes) -> Tuple[bytes, Set[bytes]]:
    """Unpack node data"""
    tx_hash, parent_count, p1, p2 = struct.unpack('!32sB32s32s', data)
    parents = set()
    if parent_count > 0 and p1 != b'\x00' * 32:
        parents.add(p1)
    if parent_count > 1 and p2 != b'\x00' * 32:
        parents.add(p2)
    return tx_hash, parents

# Ultra-lightweight DAG: function-based, no classes
_dag_nodes: Dict[bytes, bytes] = {}  # hash -> packed_node
_dag_tips: Set[bytes] = set()
_dag_stats = {'tx_count': 0, 'memory_bytes': 0}

def add_transaction(tx_data: bytes) -> bool:
    """Add transaction to DAG - 208 bytes input"""
    global _dag_nodes, _dag_tips, _dag_stats
    
    # Unpack transaction
    from_addr, to_addr, amount, timestamp, p1, p2, signature, tx_hash = unpack_transaction(tx_data)
    
    # Create parents set
    parents = set()
    if p1 != b'\x00' * 32:
        parents.add(p1)
    if p2 != b'\x00' * 32:
        parents.add(p2)
    
    # Remove parents from tips
    _dag_tips.discard(p1)
    _dag_tips.discard(p2)
    
    # Add new node
    node_data = create_node(tx_hash, parents)
    _dag_nodes[tx_hash] = node_data
    _dag_tips.add(tx_hash)
    
    # Update stats
    _dag_stats['tx_count'] += 1
    _dag_stats['memory_bytes'] = len(_dag_nodes) * 97 + len(_dag_tips) * 32
    
    return True

def get_tips() -> Set[bytes]:
    """Get current DAG tips"""
    return _dag_tips.copy()

def get_parents(tx_hash: bytes) -> Set[bytes]:
    """Get transaction parents"""
    if tx_hash not in _dag_nodes:
        return set()
    _, parents = unpack_node(_dag_nodes[tx_hash])
    return parents

def has_transaction(tx_hash: bytes) -> bool:
    """Check if transaction exists"""
    return tx_hash in _dag_nodes

def get_stats() -> Dict:
    """Get DAG statistics"""
    return _dag_stats.copy()

def clear_dag():
    """Clear entire DAG"""
    global _dag_nodes, _dag_tips, _dag_stats
    _dag_nodes.clear()
    _dag_tips.clear()
    _dag_stats = {'tx_count': 0, 'memory_bytes': 0}

# Conflict detection: function-based
def find_conflicts(tx_hash: bytes, check_limit: int = 100) -> Set[bytes]:
    """Find conflicting transactions (same sender)"""
    if tx_hash not in _dag_nodes:
        return set()
    
    conflicts = set()
    checked = 0
    
    # Simple conflict check - would need transaction data to check sender
    # This is a placeholder for the actual conflict detection logic
    for other_hash in _dag_nodes:
        if checked >= check_limit:
            break
        if other_hash != tx_hash:
            # Would check if same sender and no causal relationship
            pass
        checked += 1
    
    return conflicts

# Traversal: memory-efficient
def traverse_ancestors(tx_hash: bytes, max_depth: int = 50) -> Set[bytes]:
    """Traverse ancestors efficiently"""
    visited = set()
    to_visit = [tx_hash]
    depth = 0
    
    while to_visit and depth < max_depth:
        current = to_visit.pop()
        if current in visited or current not in _dag_nodes:
            continue
            
        visited.add(current)
        parents = get_parents(current)
        to_visit.extend(parents)
        depth += 1
    
    return visited

# Utility functions
def compress_address(addr_str: str) -> bytes:
    """Compress address string to 32 bytes"""
    if addr_str.startswith('micro_'):
        addr_str = addr_str[6:]
    return hashlib.blake2b(addr_str.encode(), digest_size=32).digest()

def create_micro_transaction(from_addr: str, to_addr: str, amount: float,
                           timestamp: int, parents: Tuple[bytes, bytes],
                           private_key: bytes) -> bytes:
    """Create minimal transaction"""
    # Convert to bytes
    from_bytes = compress_address(from_addr)
    to_bytes = compress_address(to_addr)
    amount_int = int(amount * 100000000)  # 8 decimal places
    
    # Create signature (simplified - would use proper Ed25519)
    data_to_sign = struct.pack('!32s32sQI32s32s', from_bytes, to_bytes, 
                              amount_int, timestamp, parents[0], parents[1])
    signature = hashlib.blake2b(data_to_sign + private_key, digest_size=64).digest()
    
    return pack_transaction(from_bytes, to_bytes, amount_int, timestamp,
                          parents[0], parents[1], signature)

# Memory optimization
def get_memory_usage() -> int:
    """Get current memory usage in bytes"""
    return _dag_stats['memory_bytes']

def prune_old_tips(max_tips: int = 10):
    """Keep only recent tips to limit memory"""
    global _dag_tips
    if len(_dag_tips) > max_tips:
        # Keep only the first max_tips (would use better selection in practice)
        tips_list = list(_dag_tips)
        _dag_tips = set(tips_list[:max_tips])
