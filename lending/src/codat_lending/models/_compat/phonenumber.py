from __future__ import annotations

from enum import Enum


class PhoneNumberType(str, Enum):
    """Speakeasy-name compat for Type (matched by value set)."""
    PRIMARY = 'Primary'
    LANDLINE = 'Landline'
    MOBILE = 'Mobile'
    FAX = 'Fax'
    UNKNOWN = 'Unknown'
