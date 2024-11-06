"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetAccountingBalanceSheetRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    period_length: int
    r"""Number of months defining the period of interest."""
    periods_to_compare: int
    r"""Number of periods with `periodLength` to compare."""
    start_month: NotRequired[str]
    r"""The month the report starts from."""


class GetAccountingBalanceSheetRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    period_length: Annotated[
        int,
        pydantic.Field(alias="periodLength"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Number of months defining the period of interest."""

    periods_to_compare: Annotated[
        int,
        pydantic.Field(alias="periodsToCompare"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Number of periods with `periodLength` to compare."""

    start_month: Annotated[
        Optional[str],
        pydantic.Field(alias="startMonth"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The month the report starts from."""
