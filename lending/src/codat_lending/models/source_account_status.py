from __future__ import annotations

from enum import Enum


class SourceAccountStatus(str, Enum):
    """SourceAccountStatus enum (lifted from inline OAS enum)."""
    PENDING = 'pending'
    CONNECTED = 'connected'
    CONNECTING = 'connecting'
    DISCONNECTED = 'disconnected'
    UNKNOWN = 'unknown'
