"""Decimal validators and serializers matching Speakeasy's money-field handling."""
from __future__ import annotations
from decimal import Decimal
from codat_lending.types import Unset


def serialize_decimal(as_str: bool):
    def serialize(d):
        if d is None:
            return None
        if isinstance(d, Unset):
            return d
        if not isinstance(d, Decimal):
            raise ValueError("Expected Decimal object")
        return str(d) if as_str else float(d)
    return serialize


def validate_decimal(d):
    if d is None:
        return None
    if isinstance(d, (Decimal, Unset)):
        return d
    if not isinstance(d, (str, int, float)):
        raise ValueError("Expected string, int or float")
    return Decimal(str(d))
