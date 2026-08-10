"""NoResponseError — raised when the HTTP client never receives a response (timeout, dropped connection, DNS failure)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class NoResponseError(Exception):
    """Error raised when no HTTP response is received from the server."""

    message: str

    def __init__(self, message: str = "No response received") -> None:
        object.__setattr__(self, "message", message)
        super().__init__(message)

    def __str__(self) -> str:
        return self.message


__all__ = ["NoResponseError"]
