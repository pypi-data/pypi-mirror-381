"""
MicroDAG Faucet Server
Provides free testnet tokens with rate limiting and user-friendly interface
"""

import asyncio
import aiohttp
from aiohttp import web
import time
import json
import hashlib
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from collections import defaultdict
import sqlite3
import os

logger = logging.getLogger(__name__)


@dataclass
class FaucetRequest:
    """Faucet request record"""
    address: str
    ip_address: str
    user_agent: str
    timestamp: float
    amount: int = 10000000  # 10 MICRO in base units
    status: str = "pending"  # pending, completed, failed
    transaction_hash: Optional[str] = None
    error_message: Optional[str] = None


@dataclass
class FaucetMetrics:
    """Faucet performance metrics"""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    rate_limited_requests: int = 0
    total_distributed: int = 0
    unique_addresses: int = 0
    avg_response_time_ms: float = 0.0


class FaucetDatabase:
    """SQLite database for faucet requests"""
    
    def __init__(self, db_path: str = "faucet.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize faucet database"""
        conn = sqlite3.connect(self.db_path)
        try:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS faucet_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    address TEXT NOT NULL,
                    ip_address TEXT NOT NULL,
                    user_agent TEXT,
                    timestamp REAL NOT NULL,
                    amount INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    transaction_hash TEXT,
                    error_message TEXT
                );
                
                CREATE INDEX IF NOT EXISTS idx_address ON faucet_requests(address);
                CREATE INDEX IF NOT EXISTS idx_ip_address ON faucet_requests(ip_address);
                CREATE INDEX IF NOT EXISTS idx_timestamp ON faucet_requests(timestamp);
                CREATE INDEX IF NOT EXISTS idx_status ON faucet_requests(status);
            """)
            conn.commit()
        finally:
            conn.close()
    
    def add_request(self, request: FaucetRequest) -> int:
        """Add faucet request to database"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute("""
                INSERT INTO faucet_requests 
                (address, ip_address, user_agent, timestamp, amount, status, transaction_hash, error_message)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                request.address, request.ip_address, request.user_agent,
                request.timestamp, request.amount, request.status,
                request.transaction_hash, request.error_message
            ))
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()
    
    def update_request(self, request_id: int, status: str, tx_hash: str = None, error: str = None):
        """Update faucet request status"""
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("""
                UPDATE faucet_requests 
                SET status = ?, transaction_hash = ?, error_message = ?
                WHERE id = ?
            """, (status, tx_hash, error, request_id))
            conn.commit()
        finally:
            conn.close()
    
    def get_recent_requests(self, address: str = None, ip: str = None, hours: int = 24) -> List[Dict]:
        """Get recent requests for rate limiting"""
        conn = sqlite3.connect(self.db_path)
        try:
            cutoff_time = time.time() - (hours * 3600)
            
            if address:
                cursor = conn.execute("""
                    SELECT * FROM faucet_requests 
                    WHERE address = ? AND timestamp > ?
                    ORDER BY timestamp DESC
                """, (address, cutoff_time))
            elif ip:
                cursor = conn.execute("""
                    SELECT * FROM faucet_requests 
                    WHERE ip_address = ? AND timestamp > ?
                    ORDER BY timestamp DESC
                """, (ip, cutoff_time))
            else:
                cursor = conn.execute("""
                    SELECT * FROM faucet_requests 
                    WHERE timestamp > ?
                    ORDER BY timestamp DESC
                """, (cutoff_time,))
            
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        finally:
            conn.close()
    
    def get_metrics(self) -> FaucetMetrics:
        """Get faucet metrics"""
        conn = sqlite3.connect(self.db_path)
        try:
            # Get basic counts
            cursor = conn.execute("""
                SELECT 
                    COUNT(*) as total,
                    COUNT(CASE WHEN status = 'completed' THEN 1 END) as successful,
                    COUNT(CASE WHEN status = 'failed' THEN 1 END) as failed,
                    COUNT(CASE WHEN status = 'rate_limited' THEN 1 END) as rate_limited,
                    SUM(CASE WHEN status = 'completed' THEN amount ELSE 0 END) as total_distributed,
                    COUNT(DISTINCT address) as unique_addresses
                FROM faucet_requests
            """)
            
            row = cursor.fetchone()
            
            return FaucetMetrics(
                total_requests=row[0] or 0,
                successful_requests=row[1] or 0,
                failed_requests=row[2] or 0,
                rate_limited_requests=row[3] or 0,
                total_distributed=row[4] or 0,
                unique_addresses=row[5] or 0
            )
        finally:
            conn.close()


class MicroDAGFaucet:
    """MicroDAG Faucet Server"""
    
    def __init__(self, 
                 node_url: str = "http://localhost:7076",
                 faucet_address: str = None,
                 faucet_private_key: str = None):
        """
        Initialize faucet server
        
        Args:
            node_url: MicroDAG node API URL
            faucet_address: Faucet wallet address
            faucet_private_key: Faucet private key for signing transactions
        """
        self.node_url = node_url
        self.faucet_address = faucet_address or "micro_faucet123456789012345678901234567890123456789012345678"
        self.faucet_private_key = faucet_private_key
        
        # Configuration
        self.amount_per_request = 10000000  # 10 MICRO in base units
        self.rate_limits = {
            "per_address_hours": 24,    # 24 hours between requests per address
            "per_ip_hours": 1,          # 1 hour between requests per IP
            "daily_global_limit": 10000 # Max 10k requests per day
        }
        
        # Database and metrics
        self.db = FaucetDatabase()
        self.metrics = FaucetMetrics()
        
        # In-memory cache for rate limiting
        self.request_cache = defaultdict(list)
    
    def validate_address(self, address: str) -> tuple[bool, str]:
        """Validate MicroDAG address"""
        if not address:
            return False, "Address is required"
        
        if not address.startswith("micro_"):
            return False, "Address must start with 'micro_'"
        
        if len(address) != 64:  # micro_ + 59 characters
            return False, "Address must be exactly 64 characters long"
        
        # Check for valid characters
        valid_chars = set("abcdefghijklmnopqrstuvwxyz234567")
        address_part = address[6:]  # Remove 'micro_' prefix
        
        if not all(c in valid_chars for c in address_part):
            return False, "Address contains invalid characters"
        
        return True, "Valid address"
    
    def check_rate_limits(self, address: str, ip_address: str) -> tuple[bool, str, int]:
        """
        Check if request is within rate limits
        
        Returns:
            (allowed, message, retry_after_seconds)
        """
        now = time.time()
        
        # Check address rate limit
        address_requests = self.db.get_recent_requests(
            address=address, 
            hours=self.rate_limits["per_address_hours"]
        )
        
        if address_requests:
            last_request = max(req["timestamp"] for req in address_requests)
            time_since_last = now - last_request
            required_wait = self.rate_limits["per_address_hours"] * 3600
            
            if time_since_last < required_wait:
                retry_after = int(required_wait - time_since_last)
                hours_remaining = retry_after // 3600
                return False, f"You can request tokens once per day. Please try again in {hours_remaining} hours.", retry_after
        
        # Check IP rate limit
        ip_requests = self.db.get_recent_requests(
            ip=ip_address,
            hours=self.rate_limits["per_ip_hours"]
        )
        
        if ip_requests:
            last_request = max(req["timestamp"] for req in ip_requests)
            time_since_last = now - last_request
            required_wait = self.rate_limits["per_ip_hours"] * 3600
            
            if time_since_last < required_wait:
                retry_after = int(required_wait - time_since_last)
                minutes_remaining = retry_after // 60
                return False, f"Too many requests from your network. Please try again in {minutes_remaining} minutes.", retry_after
        
        # Check daily global limit
        daily_requests = self.db.get_recent_requests(hours=24)
        if len(daily_requests) >= self.rate_limits["daily_global_limit"]:
            return False, "Daily faucet limit reached. Please try again tomorrow.", 86400
        
        return True, "Request allowed", 0
    
    async def send_tokens(self, recipient_address: str, amount: int) -> tuple[bool, str, str]:
        """
        Send tokens to recipient address
        
        Returns:
            (success, transaction_hash_or_error, message)
        """
        try:
            # Create transaction
            transaction = {
                "type": "send",
                "account": recipient_address,
                "amount": str(amount),
                "previous": "0" * 64,  # Simplified for faucet
                "link": "0" * 64,
                "timestamp": int(time.time())
            }
            
            # Send to node
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.node_url}/api/broadcast",
                    json=transaction,
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    
                    if response.status in [200, 201, 202]:
                        # Generate transaction hash (simplified)
                        tx_hash = hashlib.sha256(
                            json.dumps(transaction, sort_keys=True).encode()
                        ).hexdigest()
                        
                        return True, tx_hash, "Tokens sent successfully"
                    else:
                        error_text = await response.text()
                        return False, f"HTTP {response.status}", f"Node error: {error_text}"
        
        except asyncio.TimeoutError:
            return False, "timeout", "Request timed out. Please try again."
        except Exception as e:
            logger.error(f"Token send error: {e}")
            return False, "network_error", "Network error. Please try again later."
    
    async def handle_faucet_request(self, request):
        """Handle faucet token request"""
        start_time = time.time()
        
        try:
            # Get request data
            data = await request.json()
            address = data.get("address", "").strip()
            
            # Get client info
            ip_address = request.remote
            user_agent = request.headers.get("User-Agent", "")
            
            # Validate address
            is_valid, validation_message = self.validate_address(address)
            if not is_valid:
                return web.json_response({
                    "success": False,
                    "error": validation_message,
                    "user_friendly": True
                }, status=400)
            
            # Check rate limits
            allowed, rate_message, retry_after = self.check_rate_limits(address, ip_address)
            if not allowed:
                # Record rate limited request
                rate_limited_request = FaucetRequest(
                    address=address,
                    ip_address=ip_address,
                    user_agent=user_agent,
                    timestamp=time.time(),
                    status="rate_limited",
                    error_message=rate_message
                )
                self.db.add_request(rate_limited_request)
                
                return web.json_response({
                    "success": False,
                    "error": rate_message,
                    "retry_after": retry_after,
                    "user_friendly": True
                }, status=429)
            
            # Create request record
            faucet_request = FaucetRequest(
                address=address,
                ip_address=ip_address,
                user_agent=user_agent,
                timestamp=time.time(),
                amount=self.amount_per_request
            )
            
            request_id = self.db.add_request(faucet_request)
            
            # Send tokens
            success, tx_hash_or_error, message = await self.send_tokens(address, self.amount_per_request)
            
            # Update request status
            if success:
                self.db.update_request(request_id, "completed", tx_hash_or_error)
                
                response_time = (time.time() - start_time) * 1000
                
                return web.json_response({
                    "success": True,
                    "transaction_hash": tx_hash_or_error,
                    "amount": f"{self.amount_per_request / 1000000:.1f} MICRO",
                    "message": "Tokens sent successfully! Check your balance in 30 seconds.",
                    "estimated_arrival": "30 seconds",
                    "response_time_ms": response_time,
                    "user_friendly": True
                })
            else:
                self.db.update_request(request_id, "failed", None, message)
                
                return web.json_response({
                    "success": False,
                    "error": message,
                    "technical_error": tx_hash_or_error,
                    "suggestion": "Please try again in a few minutes",
                    "user_friendly": True
                }, status=500)
        
        except json.JSONDecodeError:
            return web.json_response({
                "success": False,
                "error": "Invalid request format",
                "user_friendly": True
            }, status=400)
        
        except Exception as e:
            logger.error(f"Faucet request error: {e}")
            return web.json_response({
                "success": False,
                "error": "Internal server error",
                "suggestion": "Please try again later",
                "user_friendly": True
            }, status=500)
    
    async def handle_faucet_status(self, request):
        """Handle faucet status request"""
        try:
            metrics = self.db.get_metrics()
            
            # Calculate success rate
            success_rate = 0
            if metrics.total_requests > 0:
                success_rate = metrics.successful_requests / metrics.total_requests
            
            # Get faucet balance (simplified - would query actual balance)
            faucet_balance = 50000 * 1000000  # 50,000 MICRO in base units
            
            return web.json_response({
                "status": "operational",
                "faucet_address": self.faucet_address,
                "amount_per_request": f"{self.amount_per_request / 1000000:.1f} MICRO",
                "rate_limits": {
                    "per_address": f"{self.rate_limits['per_address_hours']} hours",
                    "per_ip": f"{self.rate_limits['per_ip_hours']} hour",
                    "daily_global": self.rate_limits['daily_global_limit']
                },
                "metrics": {
                    "total_requests": metrics.total_requests,
                    "successful_requests": metrics.successful_requests,
                    "success_rate": f"{success_rate:.1%}",
                    "total_distributed": f"{metrics.total_distributed / 1000000:.1f} MICRO",
                    "unique_addresses": metrics.unique_addresses
                },
                "estimated_balance": f"{faucet_balance / 1000000:.0f} MICRO",
                "estimated_response_time": "2-5 seconds"
            })
        
        except Exception as e:
            logger.error(f"Status request error: {e}")
            return web.json_response({
                "status": "error",
                "error": "Unable to get faucet status"
            }, status=500)
    
    async def handle_faucet_page(self, request):
        """Serve faucet web interface"""
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MicroDAG Faucet</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #000;
            color: #fff;
            font-family: 'Courier New', monospace;
            padding: 20px;
            line-height: 1.6;
        }
        .container { max-width: 600px; margin: 0 auto; }
        h1 { color: #00ff00; margin-bottom: 20px; text-align: center; }
        .info-box {
            border: 1px solid #333;
            padding: 20px;
            margin: 20px 0;
            background: #0a0a0a;
        }
        input {
            width: 100%;
            background: #000;
            border: 1px solid #00ff00;
            color: #fff;
            padding: 10px;
            font-family: 'Courier New', monospace;
            margin: 10px 0;
        }
        button {
            background: #000;
            border: 1px solid #00ff00;
            color: #00ff00;
            padding: 15px 30px;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            width: 100%;
            margin: 10px 0;
        }
        button:hover { background: #00ff00; color: #000; }
        button:disabled { 
            border-color: #666; 
            color: #666; 
            cursor: not-allowed; 
        }
        .result {
            margin: 20px 0;
            padding: 15px;
            border: 1px solid #333;
        }
        .success { border-color: #00ff00; color: #00ff00; }
        .error { border-color: #ff0000; color: #ff0000; }
        .loading { border-color: #ffff00; color: #ffff00; }
    </style>
</head>
<body>
    <div class="container">
        <h1>💧 MicroDAG Faucet</h1>
        
        <div class="info-box">
            <h3>Get Free MICRO Tokens</h3>
            <p>• Receive 10 MICRO tokens for testing</p>
            <p>• One request per address per day</p>
            <p>• Testnet tokens (not real money)</p>
            <p>• Tokens arrive in ~30 seconds</p>
        </div>
        
        <div class="info-box">
            <label for="address">Your MicroDAG Address:</label>
            <input type="text" id="address" placeholder="micro_..." maxlength="64">
            <button onclick="requestTokens()" id="requestBtn">Request 10 MICRO Tokens</button>
        </div>
        
        <div id="result" class="result" style="display: none;"></div>
        
        <div class="info-box">
            <h3>Need Help?</h3>
            <p>• Get your address from the <a href="/wallet.html" style="color: #00ff00;">MicroDAG Wallet</a></p>
            <p>• Address must start with 'micro_' and be 64 characters long</p>
            <p>• Having issues? Check the <a href="/docs.html" style="color: #00ff00;">documentation</a></p>
        </div>
    </div>
    
    <script>
        async function requestTokens() {
            const address = document.getElementById('address').value.trim();
            const resultDiv = document.getElementById('result');
            const button = document.getElementById('requestBtn');
            
            if (!address) {
                showResult('Please enter your MicroDAG address', 'error');
                return;
            }
            
            if (!address.startsWith('micro_') || address.length !== 64) {
                showResult('Invalid address format. Must start with "micro_" and be 64 characters long.', 'error');
                return;
            }
            
            button.disabled = true;
            button.textContent = 'Requesting...';
            showResult('Requesting tokens...', 'loading');
            
            try {
                const response = await fetch('/api/faucet', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ address: address })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    showResult(`Success! ${data.amount} sent to your address. Transaction: ${data.transaction_hash}. ${data.message}`, 'success');
                } else {
                    showResult(`Error: ${data.error}${data.suggestion ? ' ' + data.suggestion : ''}`, 'error');
                    
                    if (data.retry_after) {
                        const hours = Math.floor(data.retry_after / 3600);
                        const minutes = Math.floor((data.retry_after % 3600) / 60);
                        if (hours > 0) {
                            showResult(`Please try again in ${hours} hours.`, 'error');
                        } else if (minutes > 0) {
                            showResult(`Please try again in ${minutes} minutes.`, 'error');
                        }
                    }
                }
            } catch (error) {
                showResult('Network error. Please check your connection and try again.', 'error');
            }
            
            button.disabled = false;
            button.textContent = 'Request 10 MICRO Tokens';
        }
        
        function showResult(message, type) {
            const resultDiv = document.getElementById('result');
            resultDiv.textContent = message;
            resultDiv.className = `result ${type}`;
            resultDiv.style.display = 'block';
        }
        
        // Allow Enter key to submit
        document.getElementById('address').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                requestTokens();
            }
        });
    </script>
</body>
</html>
        """
        
        return web.Response(text=html_content, content_type='text/html')
    
    def create_app(self):
        """Create aiohttp application"""
        app = web.Application()
        
        # API routes
        app.router.add_post('/api/faucet', self.handle_faucet_request)
        app.router.add_get('/api/faucet/status', self.handle_faucet_status)
        
        # Web interface
        app.router.add_get('/', self.handle_faucet_page)
        app.router.add_get('/faucet', self.handle_faucet_page)
        
        # CORS middleware for web wallet integration
        async def cors_middleware(request, handler):
            response = await handler(request)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
            return response
        
        app.middlewares.append(cors_middleware)
        
        return app
    
    async def start_server(self, host: str = "0.0.0.0", port: int = 8080):
        """Start faucet server"""
        app = self.create_app()
        
        runner = web.AppRunner(app)
        await runner.setup()
        
        site = web.TCPSite(runner, host, port)
        await site.start()
        
        logger.info(f"MicroDAG Faucet started on http://{host}:{port}")
        print(f"🚀 MicroDAG Faucet running on http://{host}:{port}")
        print(f"💧 Distributing {self.amount_per_request / 1000000:.1f} MICRO per request")
        print(f"📊 Rate limits: {self.rate_limits['per_address_hours']}h per address, {self.rate_limits['per_ip_hours']}h per IP")


async def main():
    """Main function to run faucet server"""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create and start faucet
    faucet = MicroDAGFaucet(
        node_url="http://localhost:7076",  # Default MicroDAG node
        faucet_address="micro_faucet123456789012345678901234567890123456789012345678"
    )
    
    await faucet.start_server(host="0.0.0.0", port=8080)
    
    # Keep server running
    try:
        while True:
            await asyncio.sleep(3600)  # Sleep for 1 hour
    except KeyboardInterrupt:
        print("\n👋 Shutting down faucet server...")


if __name__ == "__main__":
    asyncio.run(main())
