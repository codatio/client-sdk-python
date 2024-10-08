"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_assess.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class DataIntegrityConnectionIDTypedDict(TypedDict):
    source: NotRequired[List[str]]
    r"""An array of strings. The connection IDs for the type specified in the url."""
    target: NotRequired[List[str]]
    r"""An array of strings. The connection IDs for the type being matched to."""


class DataIntegrityConnectionID(BaseModel):
    source: Optional[List[str]] = None
    r"""An array of strings. The connection IDs for the type specified in the url."""

    target: Optional[List[str]] = None
    r"""An array of strings. The connection IDs for the type being matched to."""
