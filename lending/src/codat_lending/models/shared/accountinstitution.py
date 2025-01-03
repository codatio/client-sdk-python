"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AccountInstitutionTypedDict(TypedDict):
    r"""The bank or other financial institution providing the account."""

    id: NotRequired[str]
    r"""The institution's ID, according to the provider."""
    name: NotRequired[str]
    r"""The institution's name, according to the underlying provider."""


class AccountInstitution(BaseModel):
    r"""The bank or other financial institution providing the account."""

    id: Optional[str] = None
    r"""The institution's ID, according to the provider."""

    name: Optional[str] = None
    r"""The institution's name, according to the underlying provider."""
