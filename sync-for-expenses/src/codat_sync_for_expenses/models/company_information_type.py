from __future__ import annotations

from enum import Enum


class CompanyInformationType(str, Enum):
    """CompanyInformationType enum (lifted from inline OAS enum)."""
    WEBSITE = 'Website'
    SOCIAL = 'Social'
    UNKNOWN = 'Unknown'
