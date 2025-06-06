"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AdjustmentTransactionResponseTypedDict(TypedDict):
    sync_id: NotRequired[str]
    r"""Unique id of sync created"""


class AdjustmentTransactionResponse(BaseModel):
    sync_id: Annotated[Optional[str], pydantic.Field(alias="syncId")] = None
    r"""Unique id of sync created"""
