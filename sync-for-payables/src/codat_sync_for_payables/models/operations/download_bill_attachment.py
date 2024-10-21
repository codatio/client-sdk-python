"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables.types import BaseModel
from codat_sync_for_payables.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class DownloadBillAttachmentRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    bill_id: str
    r"""Unique identifier for a bill."""
    attachment_id: str
    r"""Unique identifier for an attachment."""


class DownloadBillAttachmentRequest(BaseModel):
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

    bill_id: Annotated[
        str,
        pydantic.Field(alias="billId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a bill."""

    attachment_id: Annotated[
        str,
        pydantic.Field(alias="attachmentId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for an attachment."""
