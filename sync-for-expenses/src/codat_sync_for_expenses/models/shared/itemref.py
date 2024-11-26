"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ItemRefTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Unique identifier for the item associated with the transaction. The `itemRef` object is currently supported only for QuickBooks Desktop. You can specify either `itemRef` or `accountRef`, but not both."""


class ItemRef(BaseModel):
    id: Optional[str] = None
    r"""Unique identifier for the item associated with the transaction. The `itemRef` object is currently supported only for QuickBooks Desktop. You can specify either `itemRef` or `accountRef`, but not both."""
