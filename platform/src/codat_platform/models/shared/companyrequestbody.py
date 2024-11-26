"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import BaseModel
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class CompanyRequestBodyTypedDict(TypedDict):
    name: str
    r"""Name of company being connected."""
    description: NotRequired[str]
    r"""Additional information about the company. This can be used to store foreign IDs, references, etc."""
    tags: NotRequired[Dict[str, str]]
    r"""A collection of user-defined key-value pairs that store custom metadata against the company."""


class CompanyRequestBody(BaseModel):
    name: str
    r"""Name of company being connected."""

    description: Optional[str] = None
    r"""Additional information about the company. This can be used to store foreign IDs, references, etc."""

    tags: Optional[Dict[str, str]] = None
    r"""A collection of user-defined key-value pairs that store custom metadata against the company."""
