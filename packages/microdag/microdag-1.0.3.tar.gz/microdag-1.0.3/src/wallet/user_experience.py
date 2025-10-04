"""
Enhanced User Experience Module for MicroDAG Wallet
Provides user-friendly interfaces and guidance for non-technical users
"""

import json
import time
import hashlib
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger(__name__)


class UserType(Enum):
    """User experience levels"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    DEVELOPER = "developer"


class WalletStep(Enum):
    """Wallet setup steps"""
    WELCOME = "welcome"
    BACKUP_WARNING = "backup_warning"
    GENERATE_KEYS = "generate_keys"
    BACKUP_MNEMONIC = "backup_mnemonic"
    VERIFY_BACKUP = "verify_backup"
    SETUP_COMPLETE = "setup_complete"
    FAUCET_REQUEST = "faucet_request"
    FIRST_TRANSACTION = "first_transaction"


@dataclass
class UserProgress:
    """Track user progress through wallet setup"""
    user_type: UserType = UserType.BEGINNER
    current_step: WalletStep = WalletStep.WELCOME
    completed_steps: List[WalletStep] = field(default_factory=list)
    wallet_created: bool = False
    backup_verified: bool = False
    faucet_received: bool = False
    first_transaction_sent: bool = False
    help_shown: Dict[str, bool] = field(default_factory=dict)


@dataclass
class FaucetRequest:
    """Faucet request tracking"""
    address: str
    timestamp: float
    ip_address: str
    user_agent: str
    status: str = "pending"  # pending, completed, failed, rate_limited
    amount_requested: int = 10000000  # 10 MICRO in base units
    transaction_hash: Optional[str] = None


class UserExperienceGuide:
    """Provides step-by-step guidance for wallet users"""
    
    def __init__(self):
        self.progress_data = {}
        self.help_content = self._load_help_content()
        self.tutorials = self._load_tutorials()
    
    def _load_help_content(self) -> Dict:
        """Load contextual help content"""
        return {
            "welcome": {
                "title": "Welcome to MicroDAG Wallet",
                "content": """
                This is your gateway to the MicroDAG network. This wallet:
                • Runs entirely in your browser (no downloads needed)
                • Stores keys locally (never sent to servers)  
                • Works completely offline after loading
                • Is only 27KB in size with zero dependencies
                
                Choose your experience level to get appropriate guidance.
                """,
                "next_action": "Select your experience level"
            },
            "backup_warning": {
                "title": "⚠️ Important: Backup Your Wallet",
                "content": """
                Your wallet will generate a 12-word recovery phrase (mnemonic).
                
                🔒 CRITICAL SECURITY INFORMATION:
                • These 12 words are the ONLY way to recover your wallet
                • If you lose them, your funds are PERMANENTLY lost
                • Anyone with these words can access your funds
                • MicroDAG cannot help you recover lost words
                
                Please prepare to write down these words on paper.
                """,
                "next_action": "I understand and I'm ready to backup my wallet"
            },
            "mnemonic_backup": {
                "title": "Write Down Your Recovery Phrase",
                "content": """
                Write these 12 words on paper in the exact order shown:
                
                📝 BACKUP CHECKLIST:
                • Use pen and paper (not digital storage)
                • Write clearly and double-check spelling
                • Store in a safe, dry place
                • Consider making multiple copies
                • Never share with anyone
                
                You'll need to verify your backup on the next step.
                """,
                "next_action": "I have written down all 12 words"
            },
            "faucet_help": {
                "title": "Getting Your First MICRO Tokens",
                "content": """
                The faucet provides free MICRO tokens for testing:
                
                💧 FAUCET INFORMATION:
                • Provides 10 MICRO tokens per address
                • Rate limited: 1 request per address per day
                • Testnet tokens (not real money)
                • Used for learning and testing
                
                Simply click "Request from Faucet" and wait for confirmation.
                """,
                "next_action": "Request tokens from faucet"
            },
            "first_transaction": {
                "title": "Sending Your First Transaction",
                "content": """
                Ready to send MICRO tokens? Here's what you need:
                
                📤 TRANSACTION REQUIREMENTS:
                • Recipient address (starts with 'micro_')
                • Amount to send (must be ≤ your balance)
                • Transaction will be confirmed in <2 seconds
                • Zero fees (completely free)
                
                Double-check the recipient address before sending!
                """,
                "next_action": "Send transaction"
            }
        }
    
    def _load_tutorials(self) -> Dict:
        """Load interactive tutorials"""
        return {
            "beginner": [
                {
                    "title": "What is MicroDAG?",
                    "steps": [
                        "MicroDAG is a lightweight cryptocurrency",
                        "Transactions are fast (<2 seconds) and free",
                        "Your wallet works entirely in your browser",
                        "No mining or staking required"
                    ]
                },
                {
                    "title": "Understanding Your Wallet",
                    "steps": [
                        "Your wallet has a unique address (like an email)",
                        "You can receive MICRO tokens at this address",
                        "Your balance shows how many tokens you have",
                        "You can send tokens to other addresses"
                    ]
                },
                {
                    "title": "Security Best Practices",
                    "steps": [
                        "Always backup your 12-word recovery phrase",
                        "Never share your recovery phrase with anyone",
                        "Double-check addresses before sending",
                        "Keep your recovery phrase safe and offline"
                    ]
                }
            ],
            "iot_integrator": [
                {
                    "title": "IoT Integration Overview",
                    "steps": [
                        "MicroDAG is designed for IoT devices",
                        "Minimal resource usage (30MB memory)",
                        "HTTP API for easy integration",
                        "Fixed 141-byte transactions"
                    ]
                },
                {
                    "title": "API Integration",
                    "steps": [
                        "Use HTTP POST to /api/broadcast for transactions",
                        "Monitor /api/account/{address} for balance",
                        "Check /api/health for node status",
                        "All responses are JSON format"
                    ]
                },
                {
                    "title": "Testing Workflow",
                    "steps": [
                        "Get testnet tokens from faucet",
                        "Test sending transactions via API",
                        "Verify balance updates",
                        "Monitor confirmation times"
                    ]
                }
            ]
        }
    
    def get_user_guidance(self, user_type: UserType, current_step: WalletStep) -> Dict:
        """Get contextual guidance for user"""
        guidance = {
            "step": current_step.value,
            "user_type": user_type.value,
            "help": self.help_content.get(current_step.value, {}),
            "tutorials": self.tutorials.get(user_type.value, []),
            "ui_hints": self._get_ui_hints(user_type, current_step)
        }
        
        return guidance
    
    def _get_ui_hints(self, user_type: UserType, current_step: WalletStep) -> List[str]:
        """Get UI hints based on user type and step"""
        hints = []
        
        if user_type == UserType.BEGINNER:
            if current_step == WalletStep.GENERATE_KEYS:
                hints = [
                    "Click 'Generate New Wallet' to create your wallet",
                    "This will create a unique address just for you",
                    "The process takes just a few seconds"
                ]
            elif current_step == WalletStep.BACKUP_MNEMONIC:
                hints = [
                    "Write each word exactly as shown",
                    "Number them 1-12 to keep the order",
                    "Use a pen (pencil can fade over time)"
                ]
            elif current_step == WalletStep.FAUCET_REQUEST:
                hints = [
                    "The faucet gives you free test tokens",
                    "You can only request once per day",
                    "Tokens appear in your balance within 30 seconds"
                ]
        
        elif user_type == UserType.INTERMEDIATE:
            if current_step == WalletStep.GENERATE_KEYS:
                hints = [
                    "Uses Ed25519 cryptography for security",
                    "Keys generated using Web Crypto API",
                    "Entropy sourced from browser's secure random"
                ]
        
        return hints
    
    def validate_user_input(self, input_type: str, value: str) -> Tuple[bool, str]:
        """Validate user input with helpful error messages"""
        if input_type == "address":
            if not value.startswith("micro_"):
                return False, "MicroDAG addresses must start with 'micro_'"
            
            if len(value) != 64:  # micro_ + 59 characters
                return False, "Address must be exactly 64 characters long"
            
            # Check for valid characters (base32-like)
            valid_chars = set("abcdefghijklmnopqrstuvwxyz234567")
            address_part = value[6:]  # Remove 'micro_' prefix
            
            if not all(c in valid_chars for c in address_part):
                return False, "Address contains invalid characters"
            
            return True, "Valid address"
        
        elif input_type == "amount":
            try:
                amount = float(value)
                if amount <= 0:
                    return False, "Amount must be greater than 0"
                if amount > 1000000:  # Reasonable upper limit
                    return False, "Amount seems too large. Please double-check."
                return True, "Valid amount"
            except ValueError:
                return False, "Please enter a valid number"
        
        elif input_type == "mnemonic_word":
            if len(value.strip()) == 0:
                return False, "Word cannot be empty"
            if len(value.split()) > 1:
                return False, "Please enter one word at a time"
            return True, "Valid word"
        
        return False, "Unknown input type"


class FaucetIntegration:
    """Handles faucet integration and user flow"""
    
    def __init__(self, faucet_url: str = "https://faucet.microdag.org"):
        self.faucet_url = faucet_url
        self.request_history = {}
        self.rate_limits = {
            "per_address": 86400,  # 24 hours in seconds
            "per_ip": 3600,        # 1 hour in seconds
            "global_daily": 10000  # Max 10k requests per day
        }
    
    async def request_tokens(self, address: str, user_info: Dict) -> Dict:
        """Request tokens from faucet with user-friendly flow"""
        
        # Validate address first
        ux_guide = UserExperienceGuide()
        is_valid, message = ux_guide.validate_user_input("address", address)
        
        if not is_valid:
            return {
                "success": False,
                "error": message,
                "user_friendly": True,
                "suggestion": "Please check your wallet address and try again"
            }
        
        # Check rate limits
        rate_limit_result = self._check_rate_limits(address, user_info.get("ip", ""))
        if not rate_limit_result["allowed"]:
            return {
                "success": False,
                "error": rate_limit_result["message"],
                "retry_after": rate_limit_result.get("retry_after"),
                "user_friendly": True
            }
        
        # Create faucet request
        request = FaucetRequest(
            address=address,
            timestamp=time.time(),
            ip_address=user_info.get("ip", "unknown"),
            user_agent=user_info.get("user_agent", "unknown")
        )
        
        try:
            # Simulate faucet API call (in real implementation, this would be HTTP request)
            result = await self._call_faucet_api(request)
            
            if result["success"]:
                return {
                    "success": True,
                    "transaction_hash": result["tx_hash"],
                    "amount": "10 MICRO",
                    "estimated_arrival": "30 seconds",
                    "message": "Tokens requested successfully! Check your balance in 30 seconds.",
                    "user_friendly": True
                }
            else:
                return {
                    "success": False,
                    "error": result.get("error", "Faucet request failed"),
                    "user_friendly": True,
                    "suggestion": "Please try again in a few minutes"
                }
        
        except Exception as e:
            logger.error(f"Faucet request failed: {e}")
            return {
                "success": False,
                "error": "Faucet service temporarily unavailable",
                "user_friendly": True,
                "suggestion": "Please try again later or contact support"
            }
    
    def _check_rate_limits(self, address: str, ip: str) -> Dict:
        """Check if request is within rate limits"""
        now = time.time()
        
        # Check address rate limit (24 hours)
        if address in self.request_history:
            last_request = self.request_history[address]
            if now - last_request < self.rate_limits["per_address"]:
                retry_after = self.rate_limits["per_address"] - (now - last_request)
                hours_remaining = int(retry_after / 3600)
                return {
                    "allowed": False,
                    "message": f"You can request tokens once per day. Please try again in {hours_remaining} hours.",
                    "retry_after": retry_after
                }
        
        # Check IP rate limit (1 hour)
        ip_key = f"ip_{ip}"
        if ip_key in self.request_history:
            last_request = self.request_history[ip_key]
            if now - last_request < self.rate_limits["per_ip"]:
                retry_after = self.rate_limits["per_ip"] - (now - last_request)
                minutes_remaining = int(retry_after / 60)
                return {
                    "allowed": False,
                    "message": f"Too many requests from your network. Please try again in {minutes_remaining} minutes.",
                    "retry_after": retry_after
                }
        
        return {"allowed": True}
    
    async def _call_faucet_api(self, request: FaucetRequest) -> Dict:
        """Call faucet API (simulated for testing)"""
        # In real implementation, this would make HTTP request to faucet service
        
        # Simulate API delay
        await asyncio.sleep(0.5)
        
        # Simulate success (90% success rate for testing)
        import random
        if random.random() < 0.9:
            # Record successful request
            self.request_history[request.address] = request.timestamp
            self.request_history[f"ip_{request.ip_address}"] = request.timestamp
            
            # Generate fake transaction hash
            tx_hash = hashlib.sha256(f"{request.address}{request.timestamp}".encode()).hexdigest()
            
            return {
                "success": True,
                "tx_hash": tx_hash,
                "amount": request.amount_requested
            }
        else:
            return {
                "success": False,
                "error": "Faucet temporarily out of funds"
            }
    
    def get_faucet_status(self) -> Dict:
        """Get current faucet status"""
        return {
            "available": True,
            "daily_limit": "10 MICRO per address",
            "current_balance": "50,000 MICRO",
            "requests_today": len(self.request_history),
            "estimated_response_time": "30 seconds"
        }


class WalletTutorialSystem:
    """Interactive tutorial system for wallet features"""
    
    def __init__(self):
        self.tutorials = {
            "first_time_setup": {
                "title": "First Time Wallet Setup",
                "estimated_time": "5 minutes",
                "steps": [
                    {
                        "title": "Welcome",
                        "content": "Let's set up your MicroDAG wallet step by step",
                        "action": "continue",
                        "highlight": None
                    },
                    {
                        "title": "Generate Wallet",
                        "content": "Click the 'Generate New Wallet' button to create your wallet",
                        "action": "click",
                        "highlight": "#generate-wallet-btn"
                    },
                    {
                        "title": "Backup Warning",
                        "content": "Read the backup warning carefully. Your recovery phrase is very important!",
                        "action": "acknowledge",
                        "highlight": ".backup-warning"
                    },
                    {
                        "title": "Write Down Recovery Phrase",
                        "content": "Write down all 12 words on paper. This is your backup!",
                        "action": "complete",
                        "highlight": ".mnemonic-display"
                    },
                    {
                        "title": "Verify Backup",
                        "content": "Enter the requested words to verify your backup",
                        "action": "verify",
                        "highlight": ".mnemonic-verify"
                    },
                    {
                        "title": "Setup Complete",
                        "content": "Great! Your wallet is ready. Let's get some test tokens.",
                        "action": "continue",
                        "highlight": None
                    }
                ]
            },
            "get_test_tokens": {
                "title": "Getting Test Tokens",
                "estimated_time": "2 minutes",
                "steps": [
                    {
                        "title": "Faucet Introduction",
                        "content": "The faucet gives you free test tokens to try MicroDAG",
                        "action": "continue",
                        "highlight": None
                    },
                    {
                        "title": "Request Tokens",
                        "content": "Click 'Request from Faucet' to get 10 MICRO tokens",
                        "action": "click",
                        "highlight": "#faucet-request-btn"
                    },
                    {
                        "title": "Wait for Confirmation",
                        "content": "Wait about 30 seconds for tokens to appear in your balance",
                        "action": "wait",
                        "highlight": ".balance-display"
                    },
                    {
                        "title": "Tokens Received",
                        "content": "Success! You now have MICRO tokens to experiment with",
                        "action": "complete",
                        "highlight": ".balance-display"
                    }
                ]
            },
            "send_transaction": {
                "title": "Sending Your First Transaction",
                "estimated_time": "3 minutes",
                "steps": [
                    {
                        "title": "Transaction Basics",
                        "content": "Sending MICRO is fast, free, and easy",
                        "action": "continue",
                        "highlight": None
                    },
                    {
                        "title": "Enter Recipient",
                        "content": "Enter the recipient's address (starts with 'micro_')",
                        "action": "input",
                        "highlight": "#recipient-address"
                    },
                    {
                        "title": "Enter Amount",
                        "content": "Enter how many MICRO tokens to send",
                        "action": "input",
                        "highlight": "#send-amount"
                    },
                    {
                        "title": "Review Transaction",
                        "content": "Double-check the address and amount before sending",
                        "action": "review",
                        "highlight": ".transaction-preview"
                    },
                    {
                        "title": "Send Transaction",
                        "content": "Click 'Send' to broadcast your transaction",
                        "action": "click",
                        "highlight": "#send-transaction-btn"
                    },
                    {
                        "title": "Transaction Sent",
                        "content": "Your transaction is confirmed! It took less than 2 seconds.",
                        "action": "complete",
                        "highlight": ".transaction-result"
                    }
                ]
            }
        }
    
    def get_tutorial(self, tutorial_name: str) -> Dict:
        """Get tutorial by name"""
        return self.tutorials.get(tutorial_name, {})
    
    def get_available_tutorials(self, user_progress: UserProgress) -> List[Dict]:
        """Get tutorials appropriate for user's progress"""
        available = []
        
        if not user_progress.wallet_created:
            available.append({
                "name": "first_time_setup",
                "title": "First Time Wallet Setup",
                "description": "Create and backup your wallet",
                "estimated_time": "5 minutes",
                "required": True
            })
        
        if user_progress.wallet_created and not user_progress.faucet_received:
            available.append({
                "name": "get_test_tokens", 
                "title": "Getting Test Tokens",
                "description": "Get free MICRO tokens for testing",
                "estimated_time": "2 minutes",
                "required": False
            })
        
        if user_progress.faucet_received and not user_progress.first_transaction_sent:
            available.append({
                "name": "send_transaction",
                "title": "Send Your First Transaction", 
                "description": "Learn how to send MICRO tokens",
                "estimated_time": "3 minutes",
                "required": False
            })
        
        return available


# Helper functions for easy integration
def create_user_experience_config(user_type: UserType = UserType.BEGINNER) -> Dict:
    """Create UX configuration for wallet"""
    return {
        "user_type": user_type.value,
        "show_tutorials": user_type in [UserType.BEGINNER, UserType.INTERMEDIATE],
        "show_tooltips": user_type == UserType.BEGINNER,
        "show_advanced_features": user_type in [UserType.ADVANCED, UserType.DEVELOPER],
        "enable_guided_setup": user_type == UserType.BEGINNER,
        "faucet_integration": True,
        "tutorial_system": user_type != UserType.DEVELOPER
    }


def get_user_friendly_error(error_code: str, context: Dict = None) -> str:
    """Convert technical errors to user-friendly messages"""
    error_messages = {
        "invalid_address": "The address you entered is not valid. Please check it and try again.",
        "insufficient_balance": "You don't have enough MICRO tokens for this transaction.",
        "network_error": "Unable to connect to the MicroDAG network. Please check your internet connection.",
        "faucet_rate_limit": "You've already requested tokens today. Please try again tomorrow.",
        "transaction_failed": "Your transaction couldn't be sent. Please try again in a moment.",
        "backup_not_verified": "Please verify your backup before continuing. This keeps your wallet safe.",
        "mnemonic_invalid": "The recovery phrase you entered is not correct. Please check your backup."
    }
    
    return error_messages.get(error_code, "An unexpected error occurred. Please try again.")
