"""
Compression manager - lightweight data compression utilities.
"""
import zlib
# No additional imports needed

class CompressionManager:
    """Ultra-lightweight compression manager"""
    
    def __init__(self, level: int = 1):
        """Initialize with compression level (1=fastest, 9=best compression)"""
        self.level = level
    
    def compress(self, data: bytes) -> bytes:
        """Compress data using zlib"""
        try:
            return zlib.compress(data, level=self.level)
        except:
            return data  # Return original if compression fails
    
    def decompress(self, compressed_data: bytes) -> bytes:
        """Decompress data using zlib"""
        try:
            return zlib.decompress(compressed_data)
        except:
            return compressed_data  # Return as-is if decompression fails
    
    def get_compression_ratio(self, original: bytes, compressed: bytes) -> float:
        """Calculate compression ratio"""
        if len(original) == 0:
            return 1.0
        return len(compressed) / len(original)
    
    def should_compress(self, data: bytes, threshold: int = 50) -> bool:
        """Check if data should be compressed based on size threshold"""
        return len(data) > threshold
    
    def compress_if_beneficial(self, data: bytes, threshold: int = 50) -> bytes:
        """Compress only if it reduces size significantly"""
        if not self.should_compress(data, threshold):
            return data
        
        compressed = self.compress(data)
        
        # Only use compression if it saves at least 10% space
        if len(compressed) < len(data) * 0.9:
            return compressed
        else:
            return data
