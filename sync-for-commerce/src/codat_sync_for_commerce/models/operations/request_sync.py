"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_commerce.models.shared import (
    synctolatestargs as shared_synctolatestargs,
)
from codat_sync_for_commerce.types import BaseModel
from codat_sync_for_commerce.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RequestSyncRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    sync_to_latest_args: NotRequired[shared_synctolatestargs.SyncToLatestArgsTypedDict]


class RequestSyncRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    sync_to_latest_args: Annotated[
        Optional[shared_synctolatestargs.SyncToLatestArgs],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None