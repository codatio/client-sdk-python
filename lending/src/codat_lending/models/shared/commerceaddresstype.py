"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class CommerceAddressType(str, Enum):
    r"""The type of the address"""

    BILLING = "Billing"
    DELIVERY = "Delivery"
    ORDER = "Order"
    INVENTORY = "Inventory"
    UNKNOWN = "Unknown"
