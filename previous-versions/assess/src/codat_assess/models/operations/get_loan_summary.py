"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_assess.types import BaseModel
from codat_assess.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class GetLoanSummaryQueryParamSourceType(str, Enum):
    r"""Data source type."""

    BANKING = "banking"
    COMMERCE = "commerce"
    ACCOUNTING = "accounting"


class GetLoanSummaryRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    source_type: GetLoanSummaryQueryParamSourceType
    r"""Data source type."""


class GetLoanSummaryRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    source_type: Annotated[
        GetLoanSummaryQueryParamSourceType,
        pydantic.Field(alias="sourceType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Data source type."""