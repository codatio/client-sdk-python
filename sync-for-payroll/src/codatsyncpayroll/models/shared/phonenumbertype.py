"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class PhoneNumberType(str, Enum):
    r"""The type of phone number"""
    PRIMARY = 'Primary'
    LANDLINE = 'Landline'
    MOBILE = 'Mobile'
    FAX = 'Fax'
    UNKNOWN = 'Unknown'
