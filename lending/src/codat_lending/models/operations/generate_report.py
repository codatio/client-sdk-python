"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.models.shared import reporttype as shared_reporttype
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GenerateReportRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    report_type: shared_reporttype.ReportType
    r"""The type of the report"""


class GenerateReportRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    report_type: Annotated[
        shared_reporttype.ReportType,
        pydantic.Field(alias="reportType"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The type of the report"""
