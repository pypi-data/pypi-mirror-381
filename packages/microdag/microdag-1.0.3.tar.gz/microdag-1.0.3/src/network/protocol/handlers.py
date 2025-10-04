"""
Message Handlers
Processes incoming network messages
"""

import struct
from typing import Optional, Callable

from .message_types import MessageType, Message
from ...core.types.transaction import deserialize_transaction
from ...core.types.account import AccountState


class MessageHandler:
    """
    Handles incoming network messages
    
    Specification: Section 4.1 - Node Communication
    
    Processes all 7 message types and generates appropriate responses.
    
    Example:
        >>> handler = MessageHandler(storage, processor)
        >>> 
        >>> # Handle incoming message
        >>> response = handler.handle(message)
        >>> if response:
        ...     send_to_peer(response)
    """
    
    def __init__(
        self,
        storage,
        processor,
        get_peers: Optional[Callable[[], list[tuple[str, int]]]] = None
    ):
        """
        Initialize message handler
        
        Args:
            storage: LevelDBStorage instance
            processor: TransactionProcessor instance
            get_peers: Function to get peer list (optional)
        """
        self.storage = storage
        self.processor = processor
        self.get_peers = get_peers or (lambda: [])
    
    def handle(self, message: Message) -> Optional[Message]:
        """
        Handle incoming message
        
        Args:
            message: Incoming message
            
        Returns:
            Response message or None
        """
        handlers = {
            MessageType.PUBLISH_TRANSACTION: self._handle_publish_transaction,
            MessageType.REQUEST_ACCOUNT_STATE: self._handle_request_account_state,
            MessageType.REQUEST_TRANSACTION: self._handle_request_transaction,
            MessageType.REQUEST_PENDING: self._handle_request_pending,
            MessageType.VOTE: self._handle_vote,
            MessageType.PING: self._handle_ping,
            MessageType.REQUEST_PEERS: self._handle_request_peers
        }
        
        handler = handlers.get(message.msg_type)
        if handler:
            return handler(message)
        
        return None
    
    def _handle_publish_transaction(self, message: Message) -> Optional[Message]:
        """
        Handle PUBLISH_TRANSACTION
        
        Specification: 0x01 - PUBLISH_TRANSACTION
        Payload: 141 bytes (transaction)
        Response: None
        """
        try:
            # Deserialize transaction
            tx = deserialize_transaction(message.payload)
            
            # Process transaction
            result = self.processor.process(tx)
            
            if result.valid:
                # Transaction processed successfully
                # No response needed (fire and forget)
                pass
            else:
                # Transaction invalid - log but don't respond
                pass
            
        except Exception as e:
            # Invalid transaction format - ignore
            pass
        
        return None
    
    def _handle_request_account_state(self, message: Message) -> Optional[Message]:
        """
        Handle REQUEST_ACCOUNT_STATE
        
        Specification: 0x02 - REQUEST_ACCOUNT_STATE
        Payload: 32 bytes (account public key)
        Response: 40 bytes (account state) or 0 bytes if not found
        """
        if len(message.payload) != 32:
            return Message(MessageType.REQUEST_ACCOUNT_STATE, b'')
        
        public_key = message.payload
        
        # Get account state
        state = self.storage.get_account(public_key)
        
        if state is None:
            # Account not found - return empty response
            return Message(MessageType.REQUEST_ACCOUNT_STATE, b'')
        
        # Return account state
        return Message(MessageType.REQUEST_ACCOUNT_STATE, state.to_bytes())
    
    def _handle_request_transaction(self, message: Message) -> Optional[Message]:
        """
        Handle REQUEST_TRANSACTION
        
        Specification: 0x03 - REQUEST_TRANSACTION
        Payload: 32 bytes (transaction hash)
        Response: 141 bytes (transaction) or 0 bytes if not found
        """
        if len(message.payload) != 32:
            return Message(MessageType.REQUEST_TRANSACTION, b'')
        
        tx_hash = message.payload
        
        # Get transaction
        tx = self.storage.get_transaction(tx_hash)
        
        if tx is None:
            # Transaction not found - return empty response
            return Message(MessageType.REQUEST_TRANSACTION, b'')
        
        # Return transaction
        from ...core.types.transaction import serialize_transaction
        return Message(MessageType.REQUEST_TRANSACTION, serialize_transaction(tx))
    
    def _handle_request_pending(self, message: Message) -> Optional[Message]:
        """
        Handle REQUEST_PENDING
        
        Specification: 0x04 - REQUEST_PENDING
        Payload: 32 bytes (account public key)
        Response: N * 32 bytes (hashes of pending SEND transactions)
        """
        if len(message.payload) != 32:
            return Message(MessageType.REQUEST_PENDING, b'')
        
        public_key = message.payload
        
        # Get pending transactions
        pending = self.storage.get_pending(public_key)
        
        # Serialize pending hashes
        payload = b''.join(pending)
        
        return Message(MessageType.REQUEST_PENDING, payload)
    
    def _handle_vote(self, message: Message) -> Optional[Message]:
        """
        Handle VOTE
        
        Specification: 0x05 - VOTE
        Payload: 65 bytes (tx_hash + voter_pubkey + signature)
        Response: None
        """
        if len(message.payload) != 65:
            return None
        
        # Parse vote
        tx_hash = message.payload[0:32]
        voter_pubkey = message.payload[32:64]
        signature = message.payload[64:65]
        
        # TODO: Process vote for conflict resolution
        # For now, just acknowledge receipt
        
        return None
    
    def _handle_ping(self, message: Message) -> Optional[Message]:
        """
        Handle PING
        
        Specification: 0x06 - PING
        Payload: 8 bytes (timestamp)
        Response: 8 bytes (timestamp echoed back)
        """
        if len(message.payload) != 8:
            return None
        
        # Echo timestamp back
        return Message(MessageType.PING, message.payload)
    
    def _handle_request_peers(self, message: Message) -> Optional[Message]:
        """
        Handle REQUEST_PEERS
        
        Specification: 0x07 - REQUEST_PEERS
        Payload: 0 bytes
        Response: N * 6 bytes (IPv4 + port) up to 100 peers
        """
        # Get peer list
        peers = self.get_peers()
        
        # Limit to 100 peers
        peers = peers[:100]
        
        # Serialize peers (IPv4 + port)
        payload = bytearray()
        for ip, port in peers:
            # Convert IP string to 4 bytes
            ip_parts = ip.split('.')
            if len(ip_parts) == 4:
                ip_bytes = bytes([int(p) for p in ip_parts])
                port_bytes = struct.pack('<H', port)
                payload.extend(ip_bytes + port_bytes)
        
        return Message(MessageType.REQUEST_PEERS, bytes(payload))
