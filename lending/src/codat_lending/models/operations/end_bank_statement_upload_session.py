"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.models.shared import (
    enduploadsessionrequest as shared_enduploadsessionrequest,
)
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class EndBankStatementUploadSessionRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    dataset_id: str
    r"""Unique identifier for the dataset that completed its sync."""
    end_upload_session_request: NotRequired[
        shared_enduploadsessionrequest.EndUploadSessionRequestTypedDict
    ]


class EndBankStatementUploadSessionRequest(BaseModel):
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

    dataset_id: Annotated[
        str,
        pydantic.Field(alias="datasetId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for the dataset that completed its sync."""

    end_upload_session_request: Annotated[
        Optional[shared_enduploadsessionrequest.EndUploadSessionRequest],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
