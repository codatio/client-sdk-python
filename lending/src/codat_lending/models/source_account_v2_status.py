from __future__ import annotations

from enum import Enum


class SourceAccountV2Status(str, Enum):
    """SourceAccountV2Status enum (lifted from inline OAS enum)."""
    PENDING = 'pending'
    CONNECTED = 'connected'
    CONNECTING = 'connecting'
    DISCONNECTED = 'disconnected'
    UNKNOWN = 'unknown'
