from __future__ import annotations

from enum import Enum


class Type(str, Enum):
    """Type enum (lifted from inline OAS enum)."""
    FAX = 'Fax'
    LANDLINE = 'Landline'
    MOBILE = 'Mobile'
    PRIMARY = 'Primary'
    UNKNOWN = 'Unknown'
