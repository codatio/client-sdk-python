"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import BaseModel
import pydantic
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ContentTypedDict(TypedDict):
    pass


class Content(BaseModel):
    pass


class ModifiedDateTypedDict(TypedDict):
    modified_date: NotRequired[str]


class ModifiedDate(BaseModel):
    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None


class CustomDataTypeRecordTypedDict(TypedDict):
    content: NotRequired[Dict[str, ContentTypedDict]]
    r"""Values from the source system for the properties defined in the custom data type configuration."""
    id: NotRequired[str]
    r"""Unique identifier of the record."""
    modified_date: NotRequired[ModifiedDateTypedDict]


class CustomDataTypeRecord(BaseModel):
    content: Optional[Dict[str, Content]] = None
    r"""Values from the source system for the properties defined in the custom data type configuration."""

    id: Optional[str] = None
    r"""Unique identifier of the record."""

    modified_date: Annotated[
        Optional[ModifiedDate], pydantic.Field(alias="modifiedDate")
    ] = None
