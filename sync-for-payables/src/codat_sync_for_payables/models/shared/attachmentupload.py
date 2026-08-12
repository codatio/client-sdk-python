# coding: utf-8
"""Multipart attachment-upload body — Speakeasy wraps the uploaded file in this
shape (`attachment_upload.file` is a CodatFile)."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, model_serializer
from typing_extensions import NotRequired, TypedDict

from codat_sync_for_payables.models.shared.codatfile import CodatFile, CodatFileTypedDict


class AttachmentUpload(BaseModel):

    @model_serializer(mode="wrap")
    def _serialize_drop_none(self, handler):
        serialized = handler(self)
        return {k: v for k, v in serialized.items() if v is not None}

    file: CodatFile = Field(description="The file to be uploaded as an attachment.")

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        protected_namespaces=(),
    )


class AttachmentUploadTypedDict(TypedDict):
    file: CodatFileTypedDict
