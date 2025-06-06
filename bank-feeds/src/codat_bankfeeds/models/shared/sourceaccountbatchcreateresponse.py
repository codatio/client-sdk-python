"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sourceaccountbatchcreateresult import (
    SourceAccountBatchCreateResult,
    SourceAccountBatchCreateResultTypedDict,
)
from codat_bankfeeds.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SourceAccountBatchCreateResponseTypedDict(TypedDict):
    r"""Account ID and resulting object of the batch `Create source account` request."""

    result: NotRequired[SourceAccountBatchCreateResultTypedDict]
    r"""Status details and corresponding object of the `Create account` operation."""
    source_account_id: NotRequired[str]
    r"""Unique ID for the source account."""


class SourceAccountBatchCreateResponse(BaseModel):
    r"""Account ID and resulting object of the batch `Create source account` request."""

    result: Optional[SourceAccountBatchCreateResult] = None
    r"""Status details and corresponding object of the `Create account` operation."""

    source_account_id: Annotated[
        Optional[str], pydantic.Field(alias="sourceAccountId")
    ] = None
    r"""Unique ID for the source account."""
