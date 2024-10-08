"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_accounting.models.shared import attachmentupload as shared_attachmentupload
from codat_accounting.types import BaseModel
from codat_accounting.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UploadDirectCostAttachmentRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    direct_cost_id: str
    r"""Unique identifier for a direct cost."""
    attachment_upload: NotRequired[shared_attachmentupload.AttachmentUploadTypedDict]


class UploadDirectCostAttachmentRequest(BaseModel):
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

    direct_cost_id: Annotated[
        str,
        pydantic.Field(alias="directCostId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a direct cost."""

    attachment_upload: Annotated[
        Optional[shared_attachmentupload.AttachmentUpload],
        FieldMetadata(request=RequestMetadata(media_type="multipart/form-data")),
    ] = None
