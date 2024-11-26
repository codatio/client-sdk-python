"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_bankfeeds.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ResultTypedDict(TypedDict):
    error: NotRequired[str]
    r"""The error description for the attempted creation of the source account."""
    status_code: NotRequired[str]
    r"""The error status code for the attempted creation of the source account."""


class Result(BaseModel):
    error: Optional[str] = None
    r"""The error description for the attempted creation of the source account."""

    status_code: Annotated[Optional[str], pydantic.Field(alias="statusCode")] = None
    r"""The error status code for the attempted creation of the source account."""


class SourceAccountBatchErrorResponseTypedDict(TypedDict):
    r"""Describes the error that occured when trying to create the specified source account."""

    result: NotRequired[ResultTypedDict]
    source_account_id: NotRequired[str]
    r"""Unique ID for the source account."""


class SourceAccountBatchErrorResponse(BaseModel):
    r"""Describes the error that occured when trying to create the specified source account."""

    result: Optional[Result] = None

    source_account_id: Annotated[
        Optional[str], pydantic.Field(alias="sourceAccountId")
    ] = None
    r"""Unique ID for the source account."""
