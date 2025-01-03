"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetCategorizedBalanceSheetStatementRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    report_date: str
    r"""The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month."""
    number_of_periods: NotRequired[int]
    r"""The number of periods to return. If not provided, 12 periods will be used as the default value."""


class GetCategorizedBalanceSheetStatementRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    report_date: Annotated[
        str,
        pydantic.Field(alias="reportDate"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month."""

    number_of_periods: Annotated[
        Optional[int],
        pydantic.Field(alias="numberOfPeriods"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The number of periods to return. If not provided, 12 periods will be used as the default value."""
