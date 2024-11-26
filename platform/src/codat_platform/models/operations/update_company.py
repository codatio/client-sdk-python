"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.models.shared import companyrequestbody as shared_companyrequestbody
from codat_platform.types import BaseModel
from codat_platform.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateCompanyRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    company_request_body: NotRequired[
        shared_companyrequestbody.CompanyRequestBodyTypedDict
    ]


class UpdateCompanyRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    company_request_body: Annotated[
        Optional[shared_companyrequestbody.CompanyRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
