"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_commerce.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SyncFlowURLTypedDict(TypedDict):
    url: NotRequired[str]
    r"""Sync flow URL."""


class SyncFlowURL(BaseModel):
    url: Optional[str] = None
    r"""Sync flow URL."""
