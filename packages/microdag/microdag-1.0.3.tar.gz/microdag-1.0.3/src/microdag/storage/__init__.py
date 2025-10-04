"""
Storage layer - compressed data persistence and database management.
"""

from .database import Database
from .compression import CompressionManager

__all__ = ['Database', 'CompressionManager']
