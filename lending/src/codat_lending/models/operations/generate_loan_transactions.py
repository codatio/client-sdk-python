"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from typing_extensions import Annotated, TypedDict


class QueryParamSourceType(str, Enum):
    r"""Data source type."""

    BANKING = "banking"
    COMMERCE = "commerce"
    ACCOUNTING = "accounting"


class GenerateLoanTransactionsRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    source_type: QueryParamSourceType
    r"""Data source type."""


class GenerateLoanTransactionsRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    source_type: Annotated[
        QueryParamSourceType,
        pydantic.Field(alias="sourceType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Data source type."""
