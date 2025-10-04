"""
Optimized HTTP Networking for MicroDAG
Reduces HTTP overhead while maintaining firewall-friendly design
"""

import asyncio
import aiohttp
import time
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import json
import gzip
import ssl

logger = logging.getLogger(__name__)


@dataclass
class NetworkMetrics:
    """Network performance metrics"""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    avg_latency_ms: float = 0.0
    min_latency_ms: float = float('inf')
    max_latency_ms: float = 0.0
    total_bytes_sent: int = 0
    total_bytes_received: int = 0
    connection_reuse_rate: float = 0.0
    compression_ratio: float = 0.0


@dataclass
class RegionLatency:
    """Regional latency measurements"""
    region: str
    avg_latency_ms: float
    min_latency_ms: float
    max_latency_ms: float
    packet_loss_rate: float
    sample_count: int


class ConnectionPool:
    """Optimized HTTP connection pool"""
    
    def __init__(self, 
                 max_connections: int = 100,
                 max_connections_per_host: int = 10,
                 keepalive_timeout: int = 30,
                 enable_compression: bool = True):
        """
        Args:
            max_connections: Total connection pool size
            max_connections_per_host: Max connections per host
            keepalive_timeout: Keep-alive timeout in seconds
            enable_compression: Enable gzip compression
        """
        self.max_connections = max_connections
        self.max_connections_per_host = max_connections_per_host
        self.keepalive_timeout = keepalive_timeout
        self.enable_compression = enable_compression
        
        # Connection pool configuration
        self.connector = aiohttp.TCPConnector(
            limit=max_connections,
            limit_per_host=max_connections_per_host,
            keepalive_timeout=keepalive_timeout,
            enable_cleanup_closed=True,
            use_dns_cache=True,
            ttl_dns_cache=300,  # 5 minutes DNS cache
            family=0,  # Allow both IPv4 and IPv6
            ssl=False  # Disable SSL for local network performance
        )
        
        # Session configuration
        self.timeout = aiohttp.ClientTimeout(
            total=5,      # Total timeout
            connect=2,    # Connection timeout
            sock_read=3   # Socket read timeout
        )
        
        self.session = None
        self.metrics = NetworkMetrics()
        self.latency_samples = []
    
    async def get_session(self) -> aiohttp.ClientSession:
        """Get or create HTTP session"""
        if self.session is None or self.session.closed:
            headers = {
                'User-Agent': 'MicroDAG/1.0',
                'Connection': 'keep-alive'
            }
            
            if self.enable_compression:
                headers['Accept-Encoding'] = 'gzip, deflate'
            
            self.session = aiohttp.ClientSession(
                connector=self.connector,
                timeout=self.timeout,
                headers=headers,
                json_serialize=json.dumps,
                raise_for_status=False
            )
        
        return self.session
    
    async def close(self):
        """Close connection pool"""
        if self.session and not self.session.closed:
            await self.session.close()
        await self.connector.close()
    
    def compress_data(self, data: bytes) -> bytes:
        """Compress data if beneficial"""
        if not self.enable_compression or len(data) < 100:
            return data
        
        compressed = gzip.compress(data)
        if len(compressed) < len(data) * 0.8:  # Only if >20% compression
            return compressed
        return data
    
    def update_metrics(self, latency_ms: float, bytes_sent: int, bytes_received: int, success: bool):
        """Update network metrics"""
        self.metrics.total_requests += 1
        
        if success:
            self.metrics.successful_requests += 1
        else:
            self.metrics.failed_requests += 1
        
        # Update latency metrics
        self.latency_samples.append(latency_ms)
        if len(self.latency_samples) > 1000:  # Keep last 1000 samples
            self.latency_samples = self.latency_samples[-1000:]
        
        self.metrics.avg_latency_ms = sum(self.latency_samples) / len(self.latency_samples)
        self.metrics.min_latency_ms = min(self.metrics.min_latency_ms, latency_ms)
        self.metrics.max_latency_ms = max(self.metrics.max_latency_ms, latency_ms)
        
        # Update bandwidth metrics
        self.metrics.total_bytes_sent += bytes_sent
        self.metrics.total_bytes_received += bytes_received


class OptimizedHTTPClient:
    """High-performance HTTP client for MicroDAG networking"""
    
    def __init__(self, enable_compression: bool = True, enable_keepalive: bool = True):
        self.enable_compression = enable_compression
        self.enable_keepalive = enable_keepalive
        self.connection_pool = ConnectionPool(
            max_connections=100,
            max_connections_per_host=20,
            keepalive_timeout=30 if enable_keepalive else 0,
            enable_compression=enable_compression
        )
        self.regional_metrics: Dict[str, RegionLatency] = {}
    
    async def post_json(self, url: str, data: dict, timeout: float = 5.0) -> Tuple[bool, int, dict, float]:
        """
        Optimized JSON POST request
        
        Returns:
            (success, status_code, response_data, latency_ms)
        """
        start_time = time.time()
        
        try:
            session = await self.connection_pool.get_session()
            
            # Serialize and optionally compress data
            json_data = json.dumps(data).encode('utf-8')
            original_size = len(json_data)
            
            headers = {'Content-Type': 'application/json'}
            
            if self.enable_compression and original_size > 100:
                compressed_data = self.connection_pool.compress_data(json_data)
                if len(compressed_data) < original_size:
                    json_data = compressed_data
                    headers['Content-Encoding'] = 'gzip'
            
            # Make request
            async with session.post(url, data=json_data, headers=headers) as response:
                latency_ms = (time.time() - start_time) * 1000
                
                # Read response
                response_data = {}
                response_size = 0
                
                if response.status == 200:
                    try:
                        response_text = await response.text()
                        response_size = len(response_text)
                        response_data = json.loads(response_text)
                    except:
                        pass
                
                # Update metrics
                self.connection_pool.update_metrics(
                    latency_ms=latency_ms,
                    bytes_sent=len(json_data),
                    bytes_received=response_size,
                    success=response.status == 200
                )
                
                return response.status == 200, response.status, response_data, latency_ms
        
        except Exception as e:
            latency_ms = (time.time() - start_time) * 1000
            logger.debug(f"HTTP POST failed: {e}")
            
            self.connection_pool.update_metrics(
                latency_ms=latency_ms,
                bytes_sent=0,
                bytes_received=0,
                success=False
            )
            
            return False, 0, {}, latency_ms
    
    async def get_json(self, url: str, timeout: float = 5.0) -> Tuple[bool, int, dict, float]:
        """
        Optimized JSON GET request
        
        Returns:
            (success, status_code, response_data, latency_ms)
        """
        start_time = time.time()
        
        try:
            session = await self.connection_pool.get_session()
            
            async with session.get(url) as response:
                latency_ms = (time.time() - start_time) * 1000
                
                response_data = {}
                response_size = 0
                
                if response.status == 200:
                    try:
                        response_text = await response.text()
                        response_size = len(response_text)
                        response_data = json.loads(response_text)
                    except:
                        pass
                
                # Update metrics
                self.connection_pool.update_metrics(
                    latency_ms=latency_ms,
                    bytes_sent=0,  # GET requests don't send data
                    bytes_received=response_size,
                    success=response.status == 200
                )
                
                return response.status == 200, response.status, response_data, latency_ms
        
        except Exception as e:
            latency_ms = (time.time() - start_time) * 1000
            logger.debug(f"HTTP GET failed: {e}")
            
            self.connection_pool.update_metrics(
                latency_ms=latency_ms,
                bytes_sent=0,
                bytes_received=0,
                success=False
            )
            
            return False, 0, {}, latency_ms
    
    async def broadcast_to_peers(self, peers: List[str], endpoint: str, data: dict) -> Dict:
        """
        Optimized broadcast to multiple peers
        
        Returns:
            Broadcast results and metrics
        """
        if not peers:
            return {'successful': 0, 'failed': 0, 'avg_latency_ms': 0}
        
        start_time = time.time()
        
        # Create concurrent tasks
        tasks = []
        for peer in peers:
            url = f"{peer}{endpoint}"
            task = asyncio.create_task(self.post_json(url, data))
            tasks.append((peer, task))
        
        # Wait for all requests
        results = []
        for peer, task in tasks:
            try:
                success, status, response, latency = await task
                results.append({
                    'peer': peer,
                    'success': success,
                    'status': status,
                    'latency_ms': latency
                })
            except Exception as e:
                results.append({
                    'peer': peer,
                    'success': False,
                    'status': 0,
                    'latency_ms': (time.time() - start_time) * 1000
                })
        
        # Calculate metrics
        successful = sum(1 for r in results if r['success'])
        failed = len(results) - successful
        avg_latency = sum(r['latency_ms'] for r in results) / len(results) if results else 0
        
        return {
            'successful': successful,
            'failed': failed,
            'total': len(results),
            'avg_latency_ms': avg_latency,
            'max_latency_ms': max(r['latency_ms'] for r in results) if results else 0,
            'results': results
        }
    
    async def measure_regional_latency(self, regions: Dict[str, str]) -> Dict[str, RegionLatency]:
        """
        Measure latency to different regions
        
        Args:
            regions: Dict of region_name -> endpoint_url
            
        Returns:
            Regional latency measurements
        """
        regional_results = {}
        
        for region_name, endpoint_url in regions.items():
            latencies = []
            failures = 0
            
            # Take 10 samples per region
            for i in range(10):
                success, status, response, latency = await self.get_json(f"{endpoint_url}/api/health")
                
                if success:
                    latencies.append(latency)
                else:
                    failures += 1
                
                await asyncio.sleep(0.1)  # Brief pause between samples
            
            if latencies:
                regional_results[region_name] = RegionLatency(
                    region=region_name,
                    avg_latency_ms=sum(latencies) / len(latencies),
                    min_latency_ms=min(latencies),
                    max_latency_ms=max(latencies),
                    packet_loss_rate=failures / 10,
                    sample_count=len(latencies)
                )
            else:
                regional_results[region_name] = RegionLatency(
                    region=region_name,
                    avg_latency_ms=float('inf'),
                    min_latency_ms=float('inf'),
                    max_latency_ms=float('inf'),
                    packet_loss_rate=1.0,
                    sample_count=0
                )
        
        self.regional_metrics = regional_results
        return regional_results
    
    def get_network_metrics(self) -> Dict:
        """Get comprehensive network metrics"""
        metrics = self.connection_pool.metrics
        
        success_rate = (metrics.successful_requests / max(1, metrics.total_requests))
        
        return {
            'requests': {
                'total': metrics.total_requests,
                'successful': metrics.successful_requests,
                'failed': metrics.failed_requests,
                'success_rate': success_rate
            },
            'latency': {
                'avg_ms': metrics.avg_latency_ms,
                'min_ms': metrics.min_latency_ms,
                'max_ms': metrics.max_latency_ms,
                'samples': len(self.connection_pool.latency_samples)
            },
            'bandwidth': {
                'bytes_sent': metrics.total_bytes_sent,
                'bytes_received': metrics.total_bytes_received,
                'compression_ratio': metrics.compression_ratio
            },
            'connection_pool': {
                'max_connections': self.connection_pool.max_connections,
                'max_per_host': self.connection_pool.max_connections_per_host,
                'keepalive_timeout': self.connection_pool.keepalive_timeout,
                'compression_enabled': self.connection_pool.enable_compression
            },
            'regional_latency': {
                region: {
                    'avg_ms': data.avg_latency_ms,
                    'min_ms': data.min_latency_ms,
                    'max_ms': data.max_latency_ms,
                    'packet_loss': data.packet_loss_rate,
                    'samples': data.sample_count
                }
                for region, data in self.regional_metrics.items()
            }
        }
    
    async def close(self):
        """Close HTTP client"""
        await self.connection_pool.close()


class HTTPLatencyOptimizer:
    """Optimize HTTP performance for low-latency requirements"""
    
    def __init__(self):
        self.client = OptimizedHTTPClient(enable_compression=True, enable_keepalive=True)
        self.baseline_latency = {}
        self.optimization_results = {}
    
    async def benchmark_baseline(self, test_endpoints: List[str]) -> Dict:
        """Benchmark baseline HTTP performance"""
        print("🔍 Benchmarking baseline HTTP performance...")
        
        results = {}
        
        for endpoint in test_endpoints:
            latencies = []
            
            # Take 20 samples
            for i in range(20):
                success, status, response, latency = await self.client.get_json(f"{endpoint}/api/health")
                if success:
                    latencies.append(latency)
                await asyncio.sleep(0.05)
            
            if latencies:
                results[endpoint] = {
                    'avg_latency_ms': sum(latencies) / len(latencies),
                    'min_latency_ms': min(latencies),
                    'max_latency_ms': max(latencies),
                    'samples': len(latencies)
                }
                
                print(f"   {endpoint}: {results[endpoint]['avg_latency_ms']:.1f}ms avg")
        
        self.baseline_latency = results
        return results
    
    async def test_optimization_techniques(self, test_endpoints: List[str]) -> Dict:
        """Test various HTTP optimization techniques"""
        print("⚡ Testing HTTP optimization techniques...")
        
        optimizations = {
            'keepalive_disabled': OptimizedHTTPClient(enable_keepalive=False),
            'compression_disabled': OptimizedHTTPClient(enable_compression=False),
            'both_disabled': OptimizedHTTPClient(enable_keepalive=False, enable_compression=False),
            'optimized': OptimizedHTTPClient(enable_keepalive=True, enable_compression=True)
        }
        
        results = {}
        
        for opt_name, client in optimizations.items():
            print(f"   Testing {opt_name}...")
            
            endpoint_results = {}
            
            for endpoint in test_endpoints:
                latencies = []
                
                # Take 10 samples per optimization
                for i in range(10):
                    success, status, response, latency = await client.get_json(f"{endpoint}/api/health")
                    if success:
                        latencies.append(latency)
                    await asyncio.sleep(0.05)
                
                if latencies:
                    endpoint_results[endpoint] = {
                        'avg_latency_ms': sum(latencies) / len(latencies),
                        'min_latency_ms': min(latencies),
                        'max_latency_ms': max(latencies)
                    }
            
            results[opt_name] = endpoint_results
            await client.close()
        
        self.optimization_results = results
        return results
    
    async def analyze_confirmation_time_impact(self, test_endpoints: List[str]) -> Dict:
        """Analyze impact on <0.1s confirmation time goal"""
        print("⏱️  Analyzing confirmation time impact...")
        
        # Simulate transaction confirmation process
        confirmation_results = {}
        
        for endpoint in test_endpoints:
            # Simulate: broadcast -> vote collection -> confirmation
            steps = []
            
            # Step 1: Broadcast transaction
            start_time = time.time()
            success, status, response, broadcast_latency = await self.client.post_json(
                f"{endpoint}/api/broadcast",
                {'test': 'transaction', 'timestamp': time.time()}
            )
            steps.append(('broadcast', broadcast_latency))
            
            # Step 2: Collect votes (simulate 3 peers)
            vote_latencies = []
            for i in range(3):
                success, status, response, vote_latency = await self.client.get_json(
                    f"{endpoint}/api/health"  # Simulate vote endpoint
                )
                if success:
                    vote_latencies.append(vote_latency)
            
            avg_vote_latency = sum(vote_latencies) / len(vote_latencies) if vote_latencies else 0
            steps.append(('vote_collection', avg_vote_latency))
            
            # Step 3: Confirmation processing (local)
            processing_time = 1.0  # Assume 1ms local processing
            steps.append(('local_processing', processing_time))
            
            # Calculate total confirmation time
            total_confirmation_time = sum(step[1] for step in steps)
            
            confirmation_results[endpoint] = {
                'steps': steps,
                'total_confirmation_time_ms': total_confirmation_time,
                'meets_100ms_goal': total_confirmation_time < 100,
                'breakdown': {
                    'broadcast_ms': steps[0][1],
                    'vote_collection_ms': steps[1][1],
                    'processing_ms': steps[2][1]
                }
            }
            
            print(f"   {endpoint}: {total_confirmation_time:.1f}ms total")
            print(f"     Broadcast: {steps[0][1]:.1f}ms")
            print(f"     Vote collection: {steps[1][1]:.1f}ms")
            print(f"     Processing: {steps[2][1]:.1f}ms")
            print(f"     Meets <100ms goal: {total_confirmation_time < 100}")
        
        return confirmation_results
    
    def generate_optimization_report(self) -> Dict:
        """Generate comprehensive optimization report"""
        return {
            'baseline_performance': self.baseline_latency,
            'optimization_comparison': self.optimization_results,
            'network_metrics': self.client.get_network_metrics(),
            'recommendations': self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate optimization recommendations"""
        recommendations = []
        
        # Analyze results and generate recommendations
        if self.baseline_latency:
            avg_baseline = sum(
                data['avg_latency_ms'] 
                for data in self.baseline_latency.values()
            ) / len(self.baseline_latency)
            
            if avg_baseline > 50:
                recommendations.append("Consider regional deployment to reduce latency")
            
            if avg_baseline > 100:
                recommendations.append("HTTP overhead may impact <100ms confirmation goal")
                recommendations.append("Consider WebSocket upgrade for high-frequency operations")
        
        recommendations.extend([
            "Enable HTTP keep-alive for connection reuse",
            "Enable gzip compression for large payloads",
            "Use connection pooling with appropriate limits",
            "Implement regional clustering for geographic distribution",
            "Monitor latency continuously in production"
        ])
        
        return recommendations
    
    async def close(self):
        """Close optimizer"""
        await self.client.close()


# Helper functions for easy integration
async def measure_http_latency(endpoints: List[str]) -> Dict:
    """Quick HTTP latency measurement"""
    optimizer = HTTPLatencyOptimizer()
    try:
        results = await optimizer.benchmark_baseline(endpoints)
        return results
    finally:
        await optimizer.close()


async def optimize_http_performance(endpoints: List[str]) -> Dict:
    """Comprehensive HTTP performance optimization"""
    optimizer = HTTPLatencyOptimizer()
    try:
        await optimizer.benchmark_baseline(endpoints)
        await optimizer.test_optimization_techniques(endpoints)
        confirmation_analysis = await optimizer.analyze_confirmation_time_impact(endpoints)
        
        report = optimizer.generate_optimization_report()
        report['confirmation_analysis'] = confirmation_analysis
        
        return report
    finally:
        await optimizer.close()
