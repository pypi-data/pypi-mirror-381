"""
Rate Limiter for MicroDAG
Prevents DoS attacks with simple IP-based rate limiting
"""

import time
from collections import defaultdict
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)


class RateLimiter:
    """Simple IP-based rate limiter"""
    
    def __init__(self, max_requests: int = 10, window: int = 1):
        """
        Args:
            max_requests: Maximum requests per window
            window: Time window in seconds
        """
        self.max_requests = max_requests
        self.window = window
        self.requests: Dict[str, List[float]] = defaultdict(list)
        self.blocked_ips: Dict[str, float] = {}  # IP -> block_until_timestamp
    
    def is_allowed(self, ip: str) -> bool:
        """Check if request from IP is allowed"""
        now = time.time()
        
        # Check if IP is blocked
        if ip in self.blocked_ips:
            if now < self.blocked_ips[ip]:
                return False
            else:
                # Unblock
                del self.blocked_ips[ip]
        
        # Clean old requests
        self.requests[ip] = [t for t in self.requests[ip] 
                            if now - t < self.window]
        
        # Check rate limit
        if len(self.requests[ip]) < self.max_requests:
            self.requests[ip].append(now)
            return True
        
        # Rate limit exceeded
        logger.warning(f"Rate limit exceeded for {ip}")
        return False
    
    def block_ip(self, ip: str, duration: int = 60):
        """Temporarily block an IP"""
        self.blocked_ips[ip] = time.time() + duration
        logger.warning(f"Blocked {ip} for {duration}s")
    
    def cleanup(self):
        """Clean up old data"""
        now = time.time()
        
        # Remove old requests
        for ip in list(self.requests.keys()):
            self.requests[ip] = [t for t in self.requests[ip] 
                                if now - t < self.window]
            if not self.requests[ip]:
                del self.requests[ip]
        
        # Remove expired blocks
        for ip in list(self.blocked_ips.keys()):
            if now >= self.blocked_ips[ip]:
                del self.blocked_ips[ip]
    
    def get_stats(self) -> Dict:
        """Get rate limiter statistics"""
        return {
            "tracked_ips": len(self.requests),
            "blocked_ips": len(self.blocked_ips),
            "max_requests": self.max_requests,
            "window": self.window
        }
