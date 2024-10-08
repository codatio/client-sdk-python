"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_assess.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class AccountRefTypedDict(TypedDict):
    r"""An account reference containing the account id and name."""

    id: NotRequired[str]
    r"""The id of the account."""
    name: NotRequired[str]
    r"""The name of the account."""


class AccountRef(BaseModel):
    r"""An account reference containing the account id and name."""

    id: Optional[str] = None
    r"""The id of the account."""

    name: Optional[str] = None
    r"""The name of the account."""
