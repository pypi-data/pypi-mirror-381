"""
Validation utilities - input validation and sanitization.
"""
import re

def validate_address(address: str) -> bool:
    """Validate MicroDAG address format"""
    # MicroDAG addresses start with 'micro_' followed by hex
    pattern = r'^micro_[a-fA-F0-9]{16,64}$'
    return bool(re.match(pattern, address))

def validate_amount(amount: float) -> bool:
    """Validate transaction amount"""
    # Must be positive and within reasonable bounds
    return 0 < amount <= 1000000000  # Max 1 billion MICRO

def validate_port(port: int) -> bool:
    """Validate network port number"""
    return 1024 <= port <= 65535

def validate_ip_address(ip: str) -> bool:
    """Validate IPv4 address"""
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    
    # Check each octet is 0-255
    octets = ip.split('.')
    return all(0 <= int(octet) <= 255 for octet in octets)

def sanitize_string(text: str, max_length: int = 256) -> str:
    """Sanitize string input"""
    # Remove control characters and limit length
    sanitized = ''.join(char for char in text if ord(char) >= 32)
    return sanitized[:max_length]

def validate_hex_string(hex_str: str, expected_length: int = None) -> bool:
    """Validate hexadecimal string"""
    pattern = r'^[a-fA-F0-9]+$'
    if not re.match(pattern, hex_str):
        return False
    
    if expected_length and len(hex_str) != expected_length:
        return False
    
    return True
