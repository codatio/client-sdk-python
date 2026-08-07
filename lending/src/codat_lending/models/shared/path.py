from __future__ import annotations

from enum import Enum


class Path(str, Enum):
    """Shared OAS parameter enum (lifted from components/parameters/path)."""
    AUTH_GET = 'auth/get'
