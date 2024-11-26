"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import BaseModel
from codat_platform.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetPushOperationRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    push_operation_key: str
    r"""Push operation key."""


class GetPushOperationRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    push_operation_key: Annotated[
        str,
        pydantic.Field(alias="pushOperationKey"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Push operation key."""
