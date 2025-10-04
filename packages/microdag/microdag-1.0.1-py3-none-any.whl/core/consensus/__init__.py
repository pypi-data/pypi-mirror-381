"""
Consensus Module
Implements conflict resolution and voting mechanism
"""

from .conflict_detector import ConflictDetector, ConflictPair
from .voter import VoteCollector, Vote, VoteResult
from .resolver import ConflictResolver

__all__ = [
    'ConflictDetector',
    'ConflictPair',
    'VoteCollector',
    'Vote',
    'VoteResult',
    'ConflictResolver'
]
