"""
Data models for the ZeroProof SDK.
"""

from typing import Any
from dataclasses import dataclass


@dataclass
class EncryptedMessage:
    """Represents an encrypted message response."""

    message_id: str
    expires_at: str
    status: str
    ttl_minutes: int

    @classmethod
    def from_dict(cls, data: dict) -> "EncryptedMessage":
        """Create an EncryptedMessage from API response data."""
        return cls(
            message_id=data["message_id"],
            expires_at=data["expires_at"],
            status=data["status"],
            ttl_minutes=data["ttl_minutes"],
        )


@dataclass
class DecryptedMessage:
    """Represents a decrypted message."""

    message_id: str
    from_agent_id: str
    to_agent_id: str
    message: Any
    read_count: int
    created_at: str
    expires_at: str

    @classmethod
    def from_dict(cls, data: dict) -> "DecryptedMessage":
        """Create a DecryptedMessage from API response data."""
        return cls(
            message_id=data["message_id"],
            from_agent_id=data["from_agent_id"],
            to_agent_id=data["to_agent_id"],
            message=data["message"],
            read_count=data["read_count"],
            created_at=data["created_at"],
            expires_at=data["expires_at"],
        )
