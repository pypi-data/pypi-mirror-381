#!/usr/bin/env python3
"""
MicroDAG Node Entry Point
Main executable for running a MicroDAG full node
"""

import argparse
import logging
import sys

from .node import MicroDAGNode
from .config import NodeConfig


def setup_logging(level: str = "INFO"):
    """Setup logging configuration"""
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {level}')
    
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='MicroDAG Full Node',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run with default configuration
  python -m src.node.main

  # Run with custom data directory
  python -m src.node.main --data-dir /var/lib/microdag

  # Run with custom ports
  python -m src.node.main --p2p-port 7075 --api-port 7076

  # Disable API server
  python -m src.node.main --no-api

  # Use environment variables
  export MICRODAG_DATA_DIR=/var/lib/microdag
  export MICRODAG_P2P_PORT=7075
  python -m src.node.main --from-env
        """
    )
    
    # Configuration options
    parser.add_argument(
        '--data-dir',
        type=str,
        default='./data',
        help='Data directory for database (default: ./data)'
    )
    parser.add_argument(
        '--p2p-port',
        type=int,
        default=7075,
        help='P2P network port (default: 7075)'
    )
    parser.add_argument(
        '--api-port',
        type=int,
        default=7076,
        help='HTTP API port (default: 7076)'
    )
    parser.add_argument(
        '--p2p-host',
        type=str,
        default='0.0.0.0',
        help='P2P host to bind (default: 0.0.0.0)'
    )
    parser.add_argument(
        '--api-host',
        type=str,
        default='0.0.0.0',
        help='API host to bind (default: 0.0.0.0)'
    )
    parser.add_argument(
        '--max-peers',
        type=int,
        default=1000,
        help='Maximum peers to track (default: 1000)'
    )
    parser.add_argument(
        '--target-connections',
        type=int,
        default=32,
        help='Target active connections (default: 32)'
    )
    parser.add_argument(
        '--no-api',
        action='store_true',
        help='Disable HTTP API server'
    )
    parser.add_argument(
        '--vote-timeout',
        type=float,
        default=2.0,
        help='Voting timeout in seconds (default: 2.0)'
    )
    parser.add_argument(
        '--from-env',
        action='store_true',
        help='Load configuration from environment variables'
    )
    parser.add_argument(
        '--log-level',
        type=str,
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Logging level (default: INFO)'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.log_level)
    logger = logging.getLogger(__name__)
    
    try:
        # Create configuration
        if args.from_env:
            logger.info("Loading configuration from environment variables")
            config = NodeConfig.from_env()
        else:
            config = NodeConfig(
                data_dir=args.data_dir,
                p2p_port=args.p2p_port,
                api_port=args.api_port,
                p2p_host=args.p2p_host,
                api_host=args.api_host,
                max_peers=args.max_peers,
                target_connections=args.target_connections,
                enable_api=not args.no_api,
                vote_timeout=args.vote_timeout
            )
        
        # Create and run node
        logger.info("=" * 60)
        logger.info("MicroDAG Full Node")
        logger.info("Ultra-Lightweight Cryptocurrency DAG")
        logger.info("=" * 60)
        
        node = MicroDAGNode(config)
        node.run()
    
    except KeyboardInterrupt:
        logger.info("\nShutdown complete")
        sys.exit(0)
    
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
