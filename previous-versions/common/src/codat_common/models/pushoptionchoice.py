"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pushoptiontype import PushOptionType
from codat_common.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PushOptionChoiceTypedDict(TypedDict):
    description: NotRequired[str]
    r"""A description of the property."""
    display_name: NotRequired[str]
    r"""The property's display name."""
    required: NotRequired[bool]
    r"""The property is required if `True`."""
    type: NotRequired[PushOptionType]
    r"""The option type."""
    value: NotRequired[str]
    r"""Allowed value for field."""


class PushOptionChoice(BaseModel):
    description: Optional[str] = None
    r"""A description of the property."""

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The property's display name."""

    required: Optional[bool] = None
    r"""The property is required if `True`."""

    type: Optional[PushOptionType] = None
    r"""The option type."""

    value: Optional[str] = None
    r"""Allowed value for field."""
