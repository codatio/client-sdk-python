"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.types import BaseModel
from codat_sync_for_expenses.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetLastSuccessfulSyncRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""


class GetLastSuccessfulSyncRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""
