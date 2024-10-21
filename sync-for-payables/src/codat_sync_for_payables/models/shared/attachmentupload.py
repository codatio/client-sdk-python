"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .codatfile import CodatFile, CodatFileTypedDict
from codat_sync_for_payables.types import BaseModel
from codat_sync_for_payables.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class AttachmentUploadTypedDict(TypedDict):
    file: CodatFileTypedDict
    r"""The file to be uploaded as an attachment."""


class AttachmentUpload(BaseModel):
    file: Annotated[
        CodatFile,
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(file=True)),
    ]
    r"""The file to be uploaded as an attachment."""
