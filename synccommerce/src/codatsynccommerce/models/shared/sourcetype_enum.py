"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class SourceTypeEnum(str, Enum):
    r"""The type of platform of the connection."""
    ACCOUNTING = 'Accounting'
    BANKING = 'Banking'
    COMMERCE = 'Commerce'
    OTHER = 'Other'
    UNKNOWN = 'Unknown'