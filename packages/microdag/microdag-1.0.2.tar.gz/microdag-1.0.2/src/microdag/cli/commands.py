"""
CLI command implementations - individual command handlers.
"""
import json
from typing import List, Dict, Any

class CLICommands:
    """Command implementations for CLI"""
    
    def __init__(self):
        pass
    
    def format_transaction_output(self, tx_data: Dict[str, Any]) -> str:
        """Format transaction data for display"""
        lines = [
            f"Hash: {tx_data.get('hash', 'N/A')}",
            f"From: {tx_data.get('from_address', 'N/A')}",
            f"To: {tx_data.get('to_address', 'N/A')}",
            f"Amount: {tx_data.get('amount', 0):.8f} MICRO",
            f"Timestamp: {tx_data.get('timestamp', 0)}"
        ]
        
        parents = tx_data.get('parents', [])
        if any(parents):
            lines.append(f"Parents: {', '.join(p for p in parents if p)}")
        
        return '\n'.join(lines)
    
    def format_stats_output(self, stats: Dict[str, Any]) -> str:
        """Format statistics for display"""
        lines = ["📊 System Statistics", "=" * 40]
        
        # DAG stats
        if 'dag' in stats:
            dag = stats['dag']
            lines.extend([
                "",
                "🧬 DAG:",
                f"  Transactions: {dag.get('transactions', 0)}",
                f"  Tips: {dag.get('tips', 0)}",
                f"  Memory: {dag.get('memory_bytes', 0)} bytes"
            ])
        
        # Storage stats
        if 'storage' in stats:
            storage = stats['storage']
            lines.extend([
                "",
                "💾 Storage:",
                f"  Stored: {storage.get('stored', 0)} items",
                f"  Compression: {storage.get('compression_ratio', 1.0):.2f}",
                f"  DB Size: {storage.get('db_size_bytes', 0)} bytes"
            ])
        
        # Network stats
        if 'network' in stats:
            network = stats['network']
            peer_stats = network.get('peer_stats', {})
            lines.extend([
                "",
                "🌐 Network:",
                f"  Total Peers: {peer_stats.get('total_peers', 0)}",
                f"  Active Peers: {peer_stats.get('active_peers', 0)}",
                f"  Messages Sent: {peer_stats.get('messages_sent', 0)}",
                f"  Messages Received: {peer_stats.get('messages_received', 0)}"
            ])
        
        return '\n'.join(lines)
    
    def format_peer_list(self, peers: List[Dict[str, Any]]) -> str:
        """Format peer list for display"""
        if not peers:
            return "No peers connected"
        
        lines = [f"📡 Connected Peers ({len(peers)}):"]
        for i, peer in enumerate(peers, 1):
            lines.append(f"  {i}. {peer['ip']}:{peer['port']}")
        
        return '\n'.join(lines)
    
    def format_tips_output(self, tips: List[str]) -> str:
        """Format DAG tips for display"""
        if not tips:
            return "No tips in DAG"
        
        lines = [f"🔗 DAG Tips ({len(tips)}):"]
        for i, tip in enumerate(tips, 1):
            lines.append(f"  {i}. {tip}")
        
        return '\n'.join(lines)
    
    def validate_address_format(self, address: str) -> bool:
        """Validate address format"""
        return address.startswith('micro_') and len(address) >= 22
    
    def validate_amount_format(self, amount_str: str) -> tuple:
        """Validate and parse amount"""
        try:
            amount = float(amount_str)
            if amount <= 0:
                return False, "Amount must be positive"
            if amount > 1000000000:  # 1 billion max
                return False, "Amount too large"
            return True, amount
        except ValueError:
            return False, "Invalid amount format"
    
    def validate_peer_format(self, peer_str: str) -> tuple:
        """Validate and parse peer string"""
        if ':' not in peer_str:
            return False, "Peer format must be ip:port"
        
        try:
            ip, port_str = peer_str.split(':', 1)
            port = int(port_str)
            
            if not (1024 <= port <= 65535):
                return False, "Port must be between 1024 and 65535"
            
            # Basic IP validation
            octets = ip.split('.')
            if len(octets) != 4:
                return False, "Invalid IP address format"
            
            for octet in octets:
                if not (0 <= int(octet) <= 255):
                    return False, "Invalid IP address"
            
            return True, (ip, port)
            
        except ValueError:
            return False, "Invalid peer format"
    
    def format_error(self, message: str) -> str:
        """Format error message"""
        return f"❌ Error: {message}"
    
    def format_success(self, message: str) -> str:
        """Format success message"""
        return f"✅ {message}"
    
    def format_info(self, message: str) -> str:
        """Format info message"""
        return f"ℹ️  {message}"
