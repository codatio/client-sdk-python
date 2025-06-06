"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DataTypeWriteWebhookRecordTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The unique identifier of the data type created, updated, deleted, or had an attachment uploaded in the accounting platform."""


class DataTypeWriteWebhookRecord(BaseModel):
    id: Optional[str] = None
    r"""The unique identifier of the data type created, updated, deleted, or had an attachment uploaded in the accounting platform."""
