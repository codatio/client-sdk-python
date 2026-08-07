from __future__ import annotations

from enum import Enum


class CommercePaymentMethodStatus(str, Enum):
    """CommercePaymentMethodStatus enum (lifted from inline OAS enum)."""
    UNKNOWN = 'Unknown'
    ACTIVE = 'Active'
    ARCHIVED = 'Archived'
