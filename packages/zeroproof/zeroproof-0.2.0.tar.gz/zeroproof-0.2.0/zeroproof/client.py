"""
Main client for the ZeroProof SDK.
"""

import json
from typing import Any, Dict, Optional
from urllib.parse import urljoin

import requests

from .exceptions import (
    AuthenticationError,
    ExpiredError,
    NotFoundError,
    RateLimitError,
    ValidationError,
    ZeroProofError,
)
from .models import DecryptedMessage, EncryptedMessage


class ZeroProof:
    """
    ZeroProof API client for encrypted messaging.

    Example:
        >>> client = ZeroProof(api_key="zkp_your_key")
        >>> result = client.send_encrypted(
        ...     to_agent_id="agent_456",
        ...     message="Hello, world!",
        ...     ttl_minutes=60
        ... )
        >>> print(result.message_id)
    """

    DEFAULT_BASE_URL = "https://api.zeroproofai.com/v1"

    def __init__(self, api_key: str, base_url: Optional[str] = None):
        """
        Initialize the ZeroProof client.

        Args:
            api_key: Your ZeroProof API key (starts with 'zkp_')
            base_url: Custom API base URL (optional)

        Raises:
            ValueError: If API key is invalid or missing
        """
        if not api_key:
            raise ValueError("API key is required")

        if not api_key.startswith("zkp_"):
            raise ValueError("Invalid API key format. API key must start with 'zkp_'")

        self.api_key = api_key
        self.base_url = base_url or self.DEFAULT_BASE_URL
        self.session = requests.Session()
        self.session.headers.update(
            {
                "X-Api-Key": self.api_key,
                "Content-Type": "application/json",
                "User-Agent": "zeroproof-python/0.2.0",
            }
        )

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def close(self):
        """Close the HTTP session."""
        self.session.close()

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            data: Request body data
            params: Query parameters

        Returns:
            API response as dictionary

        Raises:
            ZeroProofError: If the request fails
        """
        url = urljoin(self.base_url + "/", endpoint.lstrip("/"))

        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                timeout=30,
            )

            # Try to parse response as JSON
            try:
                response_data = response.json()
            except json.JSONDecodeError:
                response_data = {"error": response.text}

            # Handle error responses
            if response.status_code == 401:
                raise AuthenticationError(
                    message=response_data.get("message", "Authentication failed"),
                    status_code=response.status_code,
                    response=response_data,
                )
            elif response.status_code == 400:
                raise ValidationError(
                    message=response_data.get("message", "Validation failed"),
                    status_code=response.status_code,
                    response=response_data,
                )
            elif response.status_code == 404:
                raise NotFoundError(
                    message=response_data.get("message", "Resource not found"),
                    status_code=response.status_code,
                    response=response_data,
                )
            elif response.status_code == 410:
                raise ExpiredError(
                    message=response_data.get("message", "Resource expired"),
                    status_code=response.status_code,
                    response=response_data,
                )
            elif response.status_code == 429:
                raise RateLimitError(
                    message=response_data.get("message", "Rate limit exceeded"),
                    status_code=response.status_code,
                    response=response_data,
                )
            elif response.status_code >= 400:
                raise ZeroProofError(
                    message=response_data.get(
                        "message", f"Request failed with status {response.status_code}"
                    ),
                    status_code=response.status_code,
                    response=response_data,
                )

            return response_data

        except requests.exceptions.Timeout:
            raise ZeroProofError("Request timed out")
        except requests.exceptions.ConnectionError:
            raise ZeroProofError("Failed to connect to API")
        except requests.exceptions.RequestException as e:
            raise ZeroProofError(f"Request failed: {str(e)}")

    def send_encrypted(
        self,
        to_agent_id: str,
        message: Any,
        ttl_minutes: int = 60,
    ) -> EncryptedMessage:
        """
        Send an encrypted message to another agent.

        Args:
            to_agent_id: Target agent identifier
            message: Message content (string, dict, or JSON-serializable data)
            ttl_minutes: Time-to-live in minutes (default: 60, max: 1440)

        Returns:
            EncryptedMessage: Object containing message_id, expires_at, etc.

        Raises:
            ZeroProofError: If the request fails

        Example:
            >>> result = client.send_encrypted(
            ...     to_agent_id="agent_456",
            ...     message={"order_id": "12345", "status": "shipped"},
            ...     ttl_minutes=30
            ... )
            >>> print(result.message_id)
        """
        data = {
            "to_agent_id": to_agent_id,
            "message": message,
            "ttl_minutes": ttl_minutes,
        }

        response = self._make_request("POST", "/encryption/send", data=data)
        return EncryptedMessage.from_dict(response)

    def receive_encrypted(self, message_id: str) -> DecryptedMessage:
        """
        Receive and decrypt an encrypted message.

        Args:
            message_id: The message ID from send_encrypted()

        Returns:
            DecryptedMessage: Object with decrypted message and metadata

        Raises:
            NotFoundError: If message not found
            ExpiredError: If message has expired
            ZeroProofError: If decryption fails

        Example:
            >>> message = client.receive_encrypted(message_id="msg_abc123...")
            >>> print(message.message)
            >>> print(f"Read {message.read_count} times")
        """
        data = {"message_id": message_id}

        response = self._make_request("POST", "/encryption/receive", data=data)
        return DecryptedMessage.from_dict(response)
