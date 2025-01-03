"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_bankfeeds.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class BankAccountCredentialsTypedDict(TypedDict):
    r"""Result of generate credentials"""

    password: NotRequired[str]
    r"""Password to enable the bank feeds platform to securely retrieve transactions."""
    username: NotRequired[str]
    r"""Username used by the bank feeds platform to retrieve transactions"""


class BankAccountCredentials(BaseModel):
    r"""Result of generate credentials"""

    password: Optional[str] = None
    r"""Password to enable the bank feeds platform to securely retrieve transactions."""

    username: Optional[str] = None
    r"""Username used by the bank feeds platform to retrieve transactions"""
