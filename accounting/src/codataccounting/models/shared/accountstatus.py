"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class AccountStatus(str, Enum):
    r"""Status of the account"""
    UNKNOWN = 'Unknown'
    ACTIVE = 'Active'
    ARCHIVED = 'Archived'
    PENDING = 'Pending'
