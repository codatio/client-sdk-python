"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.models.shared import (
    updateconnectionstatus as shared_updateconnectionstatus,
)
from codat_platform.types import BaseModel
from codat_platform.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UnlinkConnectionRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    update_connection_status: NotRequired[
        shared_updateconnectionstatus.UpdateConnectionStatusTypedDict
    ]


class UnlinkConnectionRequest(BaseModel):
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

    update_connection_status: Annotated[
        Optional[shared_updateconnectionstatus.UpdateConnectionStatus],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
