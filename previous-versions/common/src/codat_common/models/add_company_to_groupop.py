"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .companygroupassignment import (
    CompanyGroupAssignment,
    CompanyGroupAssignmentTypedDict,
)
from codat_common.types import BaseModel
from codat_common.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AddCompanyToGroupRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    company_group_assignment: NotRequired[CompanyGroupAssignmentTypedDict]


class AddCompanyToGroupRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    company_group_assignment: Annotated[
        Optional[CompanyGroupAssignment],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
