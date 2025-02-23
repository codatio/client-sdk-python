"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RecordRefTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Identifier of linked reference from mapping options."""


class RecordRef(BaseModel):
    id: Optional[str] = None
    r"""Identifier of linked reference from mapping options."""
