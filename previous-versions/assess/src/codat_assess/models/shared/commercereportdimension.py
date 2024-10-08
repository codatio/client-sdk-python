"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_assess.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ItemsTypedDict(TypedDict):
    index: NotRequired[int]
    r"""The dimension's items index."""


class Items(BaseModel):
    index: Optional[int] = None
    r"""The dimension's items index."""


class CommerceReportDimensionTypedDict(TypedDict):
    display_name: NotRequired[str]
    r"""The dimension's display name."""
    index: NotRequired[int]
    r"""The dimension's index."""
    items: NotRequired[List[ItemsTypedDict]]
    type: NotRequired[str]
    r"""The dimension's type."""


class CommerceReportDimension(BaseModel):
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The dimension's display name."""

    index: Optional[int] = None
    r"""The dimension's index."""

    items: Optional[List[Items]] = None

    type: Optional[str] = None
    r"""The dimension's type."""
