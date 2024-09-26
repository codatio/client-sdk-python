"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class CommerceCustomerRefTypedDict(TypedDict):
    r"""Reference to the customer that placed the order."""

    id: str
    r"""The unique identitifer of the customer being referenced"""
    name: NotRequired[str]
    r"""Name of the customer being referenced."""


class CommerceCustomerRef(BaseModel):
    r"""Reference to the customer that placed the order."""

    id: str
    r"""The unique identitifer of the customer being referenced"""

    name: Optional[str] = None
    r"""Name of the customer being referenced."""
