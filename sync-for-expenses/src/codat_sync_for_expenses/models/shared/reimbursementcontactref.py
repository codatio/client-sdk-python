"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.types import BaseModel
from typing_extensions import TypedDict


class ReimbursementContactRefTypedDict(TypedDict):
    id: str
    r"""Identifier of contact."""


class ReimbursementContactRef(BaseModel):
    id: str
    r"""Identifier of contact."""
