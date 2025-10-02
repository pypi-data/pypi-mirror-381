"""
ZeroProof Client Module

Provides the main ZeroProof class for interacting with the API.
"""

import json
from typing import Any, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

try:
    import requests
except ImportError:
    raise ImportError(
        "The 'requests' library is required. Install it with: pip install requests"
    )


@dataclass
class Challenge:
    """Represents a verification challenge from the API."""
    
    challenge_id: str
    nonce: str
    expires_in: int
    timestamp: int
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Challenge":
        """Create a Challenge from API response data."""
        return cls(
            challenge_id=data["challenge_id"],
            nonce=data["nonce"],
            expires_in=data["expires_in"],
            timestamp=data["timestamp"],
        )


@dataclass
class VerificationResult:
    """Represents the result of a proof verification."""
    
    verified: bool
    agent_id: str
    action: str
    confidence: float
    timestamp: str
    session_id: str
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "VerificationResult":
        """Create a VerificationResult from API response data."""
        return cls(
            verified=data["verified"],
            agent_id=data["agent_id"],
            action=data["action"],
            confidence=data["confidence"],
            timestamp=data["timestamp"],
            session_id=data["session_id"],
        )


class ZeroProofError(Exception):
    """Base exception for ZeroProof SDK errors."""
    
    def __init__(self, message: str, status_code: Optional[int] = None, response: Optional[Dict] = None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)


class ZeroProof:
    """
    ZeroProof API Client
    
    A simple client for interacting with the ZeroProof verification API.
    
    Example:
        >>> from zeroproof import ZeroProof
        >>> client = ZeroProof(api_key="zkp_your_key_here")
        >>> challenge = client.create_challenge("shopping-bot", "add_to_cart")
        >>> result = client.verify_proof(challenge.challenge_id, "proof_data")
    """
    
    DEFAULT_BASE_URL = "https://api.zeroproofai.com/v1"
    
    def __init__(self, api_key: str, base_url: Optional[str] = None):
        """
        Initialize the ZeroProof client.
        
        Args:
            api_key: Your ZeroProof API key (starts with 'zkp_')
            base_url: Optional custom API base URL (defaults to production)
        """
        if not api_key:
            raise ValueError("API key is required")
        
        if not api_key.startswith("zkp_"):
            raise ValueError("Invalid API key format. API key should start with 'zkp_'")
        
        self.api_key = api_key
        self.base_url = base_url or self.DEFAULT_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "X-Api-Key": self.api_key,
            "Content-Type": "application/json",
        })
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
    ) -> Dict[str, Any]:
        """
        Make a request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            data: Optional request body data
            params: Optional query parameters
            
        Returns:
            Parsed JSON response
            
        Raises:
            ZeroProofError: If the request fails
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                timeout=30,
            )
            
            # Try to parse JSON response
            try:
                response_data = response.json()
            except json.JSONDecodeError:
                response_data = {"raw_response": response.text}
            
            # Check for errors
            if response.status_code >= 400:
                error_message = response_data.get("error", "Unknown error")
                if "message" in response_data:
                    error_message = f"{error_message}: {response_data['message']}"
                
                raise ZeroProofError(
                    message=error_message,
                    status_code=response.status_code,
                    response=response_data,
                )
            
            return response_data
            
        except requests.RequestException as e:
            raise ZeroProofError(f"Request failed: {str(e)}") from e
    
    def create_challenge(
        self,
        agent_id: str,
        action: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> Challenge:
        """
        Create a new verification challenge.
        
        Args:
            agent_id: Unique identifier for the AI agent
            action: The action the agent wants to perform (e.g., "add_to_cart")
            context: Optional additional context for the action
            
        Returns:
            Challenge object containing the challenge details
            
        Raises:
            ZeroProofError: If the request fails
            
        Example:
            >>> challenge = client.create_challenge(
            ...     agent_id="shopping-assistant-v1",
            ...     action="add_to_cart",
            ...     context={"item_id": "laptop-123", "price": 999.99}
            ... )
        """
        data = {
            "agent_id": agent_id,
            "action": action,
        }
        
        if context is not None:
            data["context"] = context
        
        response = self._make_request("POST", "/verify/challenge", data=data)
        return Challenge.from_dict(response)
    
    def verify_proof(
        self,
        challenge_id: str,
        proof: str,
        agent_signature: Optional[str] = None,
    ) -> VerificationResult:
        """
        Verify a proof for a given challenge.
        
        Args:
            challenge_id: The challenge ID from create_challenge()
            proof: The cryptographic proof data
            agent_signature: Optional agent signature for additional verification
            
        Returns:
            VerificationResult object with verification details
            
        Raises:
            ZeroProofError: If verification fails or request fails
            
        Example:
            >>> result = client.verify_proof(
            ...     challenge_id=challenge.challenge_id,
            ...     proof="proof_data_here",
            ...     agent_signature="signature_here"
            ... )
            >>> if result.verified:
            ...     print(f"Verified with {result.confidence * 100}% confidence")
        """
        data = {
            "challenge_id": challenge_id,
            "proof": proof,
        }
        
        if agent_signature is not None:
            data["agent_signature"] = agent_signature
        
        response = self._make_request("POST", "/verify/proof", data=data)
        return VerificationResult.from_dict(response)
    
    def get_status(self, session_id: str) -> Dict[str, Any]:
        """
        Get the status of a verification session.
        
        Args:
            session_id: The session/challenge ID to check
            
        Returns:
            Dictionary with session status details
            
        Raises:
            ZeroProofError: If the request fails
            
        Example:
            >>> status = client.get_status(challenge.challenge_id)
            >>> print(f"Status: {status['status']}")
        """
        response = self._make_request("GET", f"/verify/status/{session_id}")
        return response
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close the session."""
        self.session.close()
    
    def close(self):
        """Close the underlying HTTP session."""
        self.session.close()
