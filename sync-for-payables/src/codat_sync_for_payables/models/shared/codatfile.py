# coding: utf-8
"""Speakeasy-compat multipart file helper. Not an OAS schema — Speakeasy emits this
to wrap multipart/form-data file uploads (see AttachmentUpload)."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, model_serializer
from typing import IO, Any, Optional, Union
from typing_extensions import NotRequired, TypedDict


class CodatFile(BaseModel):

    @model_serializer(mode="wrap")
    def _serialize_drop_none(self, handler):
        serialized = handler(self)
        return {k: v for k, v in serialized.items() if v is not None}

    file_name: str = Field(alias="fileName")
    content: Union[bytes, IO[bytes]]
    content_type: Optional[str] = Field(default=None, alias="Content-Type")

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        protected_namespaces=(),
    )


class CodatFileTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, Any]
    content_type: NotRequired[Optional[str]]
