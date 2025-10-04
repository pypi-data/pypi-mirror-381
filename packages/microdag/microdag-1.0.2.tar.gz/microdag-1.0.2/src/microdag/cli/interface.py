"""
Command line interface - main CLI class.
"""
import sys
import time
from .commands import CLICommands

class CLI:
    """Ultra-lightweight command line interface"""
    
    def __init__(self):
        self.commands = CLICommands()
    
    def run(self, args: list = None):
        """Run CLI with arguments"""
        if args is None:
            args = sys.argv[1:]
        
        if not args:
            self.show_help()
            return
        
        command = args[0]
        command_args = args[1:]
        
        # Route commands
        if command == 'account':
            self.account_command(command_args)
        elif command == 'node':
            self.node_command(command_args)
        elif command == 'start':
            self.start_node(command_args)
        elif command == 'send':
            self.send_transaction(command_args)
        elif command == 'balance':
            self.check_balance(command_args)
        elif command == 'add-peer':
            self.add_peer(command_args)
        elif command == 'stats':
            self.show_stats(command_args)
        elif command == 'help' or command == '--help' or command == '-h':
            self.show_help()
        else:
            print(f"Unknown command: {command}")
            self.show_help()
    
    def show_help(self):
        """Show help message"""
        print("MicroDAG - Ultra-lightweight DAG blockchain")
        print("")
        print("Usage: microdag <command> [args]")
        print("")
        print("Commands:")
        print("  account create         Create new account")
        print("  node start [port]      Start MicroDAG node (default port: 7076)")
        print("  start [port]           Start MicroDAG node (default port: 7076)")
        print("  send <to> <amount>     Send transaction")
        print("  balance [address]      Check balance")
        print("  add-peer <ip:port>     Add network peer")
        print("  stats                  Show system statistics")
        print("  help                   Show this help message")
        print("")
        print("Examples:")
        print("  microdag account create")
        print("  microdag node start")
        print("  microdag start 7077")
        print("  microdag send micro_alice123... 10.5")
        print("  microdag balance")
        print("  microdag add-peer 192.168.1.100:7076")
        print("  microdag stats")
    
    def account_command(self, args: list):
        """Handle account commands"""
        if not args or args[0] != 'create':
            print("Usage: microdag account create")
            return
        
        print("Creating new MicroDAG account...")
        
        try:
            from ..crypto.keys import generate_keypair, derive_address
            
            # Generate new keypair
            private_key, public_key = generate_keypair()
            address = derive_address(private_key)
            
            print(f"✅ Account created successfully!")
            print(f"   Address: {address}")
            print(f"   Private key: {private_key.hex()}")
            print("")
            print("⚠️  IMPORTANT: Save your private key securely!")
            print("   You'll need it to access your account.")
            
        except Exception as e:
            print(f"❌ Failed to create account: {e}")
    
    def node_command(self, args: list):
        """Handle node commands"""
        if not args:
            print("Usage: microdag node <subcommand>")
            print("Subcommands:")
            print("  start [port]    Start MicroDAG node")
            return
        
        subcommand = args[0]
        if subcommand == 'start':
            self.start_node(args[1:])
        else:
            print(f"Unknown node subcommand: {subcommand}")
    
    def start_node(self, args: list):
        """Start MicroDAG node"""
        port = 7076
        if args:
            try:
                port = int(args[0])
            except ValueError:
                print(f"Invalid port: {args[0]}")
                return
        
        print(f"Starting MicroDAG node on port {port}...")
        
        try:
            # Initialize MicroDAG
            from .. import MicroDAG
            dag = MicroDAG()
            
            # Start node
            dag.start(port)
            
            print(f"✅ Node started successfully!")
            print(f"   API: http://localhost:{port}")
            print(f"   P2P: port {port + 1}")
            print(f"   Node ID: microdag_node_{port}")
            print("")
            print("Press Ctrl+C to stop...")
            
            # Keep running
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n\nShutting down...")
                dag.network.stop()
                dag.database.close()
                
        except Exception as e:
            print(f"❌ Failed to start node: {e}")
    
    def send_transaction(self, args: list):
        """Send transaction"""
        if len(args) < 2:
            print("Usage: microdag send <to_address> <amount>")
            return
        
        to_address = args[0]
        try:
            amount = float(args[1])
        except ValueError:
            print(f"Invalid amount: {args[1]}")
            return
        
        print(f"Sending {amount} MICRO to {to_address}...")
        
        try:
            from .. import MicroDAG
            dag = MicroDAG()
            tx_hash = dag.send(to_address, amount)
            print(f"✅ Transaction sent: {tx_hash}")
        except Exception as e:
            print(f"❌ Transaction failed: {e}")
    
    def check_balance(self, args: list):
        """Check balance"""
        address = None
        if args:
            address = args[0]
        
        try:
            from .. import MicroDAG
            dag = MicroDAG()
            balance = dag.balance(address)
            
            if address:
                print(f"Balance for {address}: {balance:.8f} MICRO")
            else:
                print(f"Your balance: {balance:.8f} MICRO")
                
        except Exception as e:
            print(f"❌ Failed to check balance: {e}")
    
    def add_peer(self, args: list):
        """Add network peer"""
        if not args:
            print("Usage: microdag add-peer <ip:port>")
            return
        
        peer = args[0]
        if ':' not in peer:
            print("Invalid peer format. Use ip:port")
            return
        
        try:
            ip, port = peer.split(':')
            port = int(port)
            
            from .. import MicroDAG
            dag = MicroDAG()
            dag.network.add_peer(ip, port)
            
            print(f"✅ Added peer: {ip}:{port}")
            
        except Exception as e:
            print(f"❌ Failed to add peer: {e}")
    
    def show_stats(self, args: list):
        """Show system statistics"""
        try:
            from .. import MicroDAG
            dag = MicroDAG()
            
            dag_stats = dag.dag.get_stats()
            storage_stats = dag.database.get_stats()
            network_stats = dag.network.get_stats()
            
            print("📊 MicroDAG Statistics")
            print("=" * 30)
            print(f"DAG Transactions: {dag_stats['transactions']}")
            print(f"DAG Tips: {dag_stats['tips']}")
            print(f"DAG Memory: {dag_stats['memory_bytes']} bytes")
            print("")
            print(f"Storage Entries: {storage_stats.get('stored', 0)}")
            print(f"Compression Ratio: {storage_stats.get('compression_ratio', 1.0):.2f}")
            print(f"DB Size: {storage_stats.get('db_size_bytes', 0)} bytes")
            print("")
            print(f"Network Peers: {network_stats['peer_stats']['total_peers']}")
            print(f"Active Peers: {network_stats['peer_stats']['active_peers']}")
            print(f"Messages Sent: {network_stats['peer_stats']['messages_sent']}")
            
        except Exception as e:
            print(f"❌ Failed to get stats: {e}")
