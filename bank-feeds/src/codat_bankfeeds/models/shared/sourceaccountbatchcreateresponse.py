"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sourceaccount import SourceAccount, SourceAccountTypedDict
from codat_bankfeeds.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SourceAccountBatchCreateResponseTypedDict(TypedDict):
    r"""The account ID and source account object of the successfully created source account."""

    result: NotRequired[SourceAccountTypedDict]
    r"""The target bank account in a supported accounting software for ingestion into a bank feed."""
    source_account_id: NotRequired[str]
    r"""Unique ID for the source account."""


class SourceAccountBatchCreateResponse(BaseModel):
    r"""The account ID and source account object of the successfully created source account."""

    result: Optional[SourceAccount] = None
    r"""The target bank account in a supported accounting software for ingestion into a bank feed."""

    source_account_id: Annotated[
        Optional[str], pydantic.Field(alias="sourceAccountId")
    ] = None
    r"""Unique ID for the source account."""
