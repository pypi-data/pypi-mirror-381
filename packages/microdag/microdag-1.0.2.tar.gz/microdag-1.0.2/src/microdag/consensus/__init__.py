"""
Consensus layer - proof of work and validation mechanisms.
"""

from .pow import ProofOfWork
from .validator import ConsensusValidator

__all__ = ['ProofOfWork', 'ConsensusValidator']
