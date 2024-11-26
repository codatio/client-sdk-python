"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables_version_1.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class HalRefTypedDict(TypedDict):
    href: NotRequired[str]
    r"""Uri hypertext reference."""


class HalRef(BaseModel):
    href: Optional[str] = None
    r"""Uri hypertext reference."""