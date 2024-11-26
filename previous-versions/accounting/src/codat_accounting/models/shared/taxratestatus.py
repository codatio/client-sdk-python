"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class TaxRateStatus(str, Enum):
    r"""Status of the tax rate in the accounting software.
    - `Active` - An active tax rate in use by a company.
    - `Archived` - A tax rate that has been archived or is inactive in the accounting software.
    - `Unknown` - Where the status of the tax rate cannot be determined from the underlying platform.
    """

    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"