"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_files.types import BaseModel
from codat_files.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DownloadFilesRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    date_: NotRequired[str]
    r"""Only download files uploaded on this date."""


class DownloadFilesRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    date_: Annotated[
        Optional[str],
        pydantic.Field(alias="date"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Only download files uploaded on this date."""