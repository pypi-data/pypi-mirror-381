"""User related data models and helpers."""

import hashlib


def hash_token(token: str) -> str:
    """Hash the given token."""
    return hashlib.sha256(token.encode()).hexdigest()
