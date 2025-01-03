"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .companyreference import CompanyReference, CompanyReferenceTypedDict
from codat_lending.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ReportGenerationPayloadTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Unique identifier of the report."""
    reference_company: NotRequired[CompanyReferenceTypedDict]


class ReportGenerationPayload(BaseModel):
    id: Optional[str] = None
    r"""Unique identifier of the report."""

    reference_company: Annotated[
        Optional[CompanyReference], pydantic.Field(alias="referenceCompany")
    ] = None
