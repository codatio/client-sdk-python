"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ReportInfoTypedDict(TypedDict):
    r"""Report additional information, which is specific to Lending API reports."""

    company_name: NotRequired[str]
    r"""The name of the company being queried."""
    generated_date: NotRequired[str]
    r"""Date the report was generated."""
    page_number: NotRequired[int]
    r"""The number of the page queried."""
    page_size: NotRequired[int]
    r"""The number of transactions returned per page."""
    report_name: NotRequired[str]
    r"""Name of the report."""
    total_results: NotRequired[int]
    r"""The total number of transactions available for a company for the period specified in the query string."""


class ReportInfo(BaseModel):
    r"""Report additional information, which is specific to Lending API reports."""

    company_name: Annotated[Optional[str], pydantic.Field(alias="companyName")] = None
    r"""The name of the company being queried."""

    generated_date: Annotated[Optional[str], pydantic.Field(alias="generatedDate")] = (
        None
    )
    r"""Date the report was generated."""

    page_number: Annotated[Optional[int], pydantic.Field(alias="pageNumber")] = None
    r"""The number of the page queried."""

    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = None
    r"""The number of transactions returned per page."""

    report_name: Annotated[Optional[str], pydantic.Field(alias="reportName")] = None
    r"""Name of the report."""

    total_results: Annotated[Optional[int], pydantic.Field(alias="totalResults")] = None
    r"""The total number of transactions available for a company for the period specified in the query string."""
