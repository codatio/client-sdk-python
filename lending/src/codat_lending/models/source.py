from __future__ import annotations

from enum import Enum


class Source(str, Enum):
    """Source enum (lifted from inline OAS enum)."""
    CODAT = 'codat'
