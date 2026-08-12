from __future__ import annotations

from enum import Enum


class WebLinkType(str, Enum):
    """WebLinkType enum (lifted from inline OAS enum)."""
    WEBSITE = 'Website'
    SOCIAL = 'Social'
    UNKNOWN = 'Unknown'
