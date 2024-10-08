"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_assess.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SourceRefTypedDict(TypedDict):
    r"""A source reference containing the `sourceType` object \"Banking\"."""

    source_type: NotRequired[str]
    r"""The data source type."""


class SourceRef(BaseModel):
    r"""A source reference containing the `sourceType` object \"Banking\"."""

    source_type: Annotated[Optional[str], pydantic.Field(alias="sourceType")] = None
    r"""The data source type."""
