"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class LocationRefTypedDict(TypedDict):
    r"""Reference to the geographic location where the order was placed."""

    id: str
    r"""The unique identitifer of the location being referenced."""
    name: NotRequired[str]
    r"""Name of the location being referenced."""


class LocationRef(BaseModel):
    r"""Reference to the geographic location where the order was placed."""

    id: str
    r"""The unique identitifer of the location being referenced."""

    name: Optional[str] = None
    r"""Name of the location being referenced."""
