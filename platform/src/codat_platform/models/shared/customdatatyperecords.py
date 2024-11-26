"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customdatatyperecord import CustomDataTypeRecord, CustomDataTypeRecordTypedDict
from codat_platform.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CustomDataTypeRecordsTypedDict(TypedDict):
    r"""Resulting records pulled from the source platform for a specific custom data type."""

    page_number: NotRequired[int]
    r"""Current page number."""
    page_size: NotRequired[int]
    r"""Number of items to return in results array."""
    results: NotRequired[List[CustomDataTypeRecordTypedDict]]
    total_results: NotRequired[int]
    r"""Total number of items."""


class CustomDataTypeRecords(BaseModel):
    r"""Resulting records pulled from the source platform for a specific custom data type."""

    page_number: Annotated[Optional[int], pydantic.Field(alias="pageNumber")] = None
    r"""Current page number."""

    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = None
    r"""Number of items to return in results array."""

    results: Optional[List[CustomDataTypeRecord]] = None

    total_results: Annotated[Optional[int], pydantic.Field(alias="totalResults")] = None
    r"""Total number of items."""
