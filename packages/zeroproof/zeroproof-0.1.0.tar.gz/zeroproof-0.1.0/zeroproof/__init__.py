"""
ZeroProof Python SDK

A minimal SDK for the ZeroProof AI verification API.
Secure your agentic e-commerce ecosystem with zero-knowledge proofs.
"""

__version__ = "0.1.0"

from .client import ZeroProof, ZeroProofError, Challenge, VerificationResult

__all__ = ["ZeroProof", "ZeroProofError", "Challenge", "VerificationResult"]
