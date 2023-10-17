"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class BilledToType(str, Enum):
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""
    UNKNOWN = 'Unknown'
    NOT_APPLICABLE = 'NotApplicable'
    CUSTOMER = 'Customer'
    PROJECT = 'Project'
