"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class DataConnectionStatus(str, Enum):
    r"""The current authorization status of the data connection."""
    PENDING_AUTH = "PendingAuth"
    LINKED = "Linked"
    UNLINKED = "Unlinked"
    DEAUTHORIZED = "Deauthorized"
