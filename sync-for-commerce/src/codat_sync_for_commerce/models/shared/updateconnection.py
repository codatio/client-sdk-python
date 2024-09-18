"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dataconnectionstatus import DataConnectionStatus
from codat_sync_for_commerce.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UpdateConnectionTypedDict(TypedDict):
    status: NotRequired[DataConnectionStatus]
    r"""The current authorization status of the data connection."""


class UpdateConnection(BaseModel):
    status: Optional[DataConnectionStatus] = None
    r"""The current authorization status of the data connection."""
