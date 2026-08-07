from __future__ import annotations

from enum import Enum


class PhoneNumberItemsType(str, Enum):
    """PhoneNumberItemsType enum (lifted from inline OAS enum)."""
    PRIMARY = 'Primary'
    LANDLINE = 'Landline'
    MOBILE = 'Mobile'
    FAX = 'Fax'
    UNKNOWN = 'Unknown'
