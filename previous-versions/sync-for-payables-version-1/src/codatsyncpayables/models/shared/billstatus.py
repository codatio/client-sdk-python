"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class BillStatus(str, Enum):
    r"""Current state of the bill."""
    UNKNOWN = 'Unknown'
    OPEN = 'Open'
    PARTIALLY_PAID = 'PartiallyPaid'
    PAID = 'Paid'
    VOID = 'Void'
    DRAFT = 'Draft'
