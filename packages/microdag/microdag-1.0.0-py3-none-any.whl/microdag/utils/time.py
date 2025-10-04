"""
Time utilities - timestamp handling and formatting.
"""
import time
from datetime import datetime

def get_timestamp() -> int:
    """Get current Unix timestamp"""
    return int(time.time())

def format_timestamp(timestamp: int) -> str:
    """Format timestamp as human-readable string"""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def is_timestamp_valid(timestamp: int, max_drift: int = 3600) -> bool:
    """Check if timestamp is within acceptable drift (default 1 hour)"""
    current_time = get_timestamp()
    return abs(timestamp - current_time) <= max_drift

def timestamp_to_datetime(timestamp: int) -> datetime:
    """Convert timestamp to datetime object"""
    return datetime.fromtimestamp(timestamp)
