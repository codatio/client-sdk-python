"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_commerce.types import BaseModel
from codat_sync_for_commerce.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateConnectionAuthorizationRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    request_body: NotRequired[Dict[str, str]]


class UpdateConnectionAuthorizationRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    connection_id: Annotated[
        str,
        pydantic.Field(alias="connectionId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a connection."""

    request_body: Annotated[
        Optional[Dict[str, str]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
