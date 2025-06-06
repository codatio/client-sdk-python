"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .commerceaddresstype import CommerceAddressType
from codat_lending.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CommerceAddressTypedDict(TypedDict):
    city: NotRequired[str]
    r"""The third line of the address, or city"""
    country: NotRequired[str]
    r"""The country for the address"""
    line1: NotRequired[str]
    r"""The first line of the address"""
    line2: NotRequired[str]
    r"""The second line of the address"""
    postal_code: NotRequired[str]
    r"""The postal (or zip) code for the address"""
    region: NotRequired[str]
    r"""The fourth line of the address, or region"""
    type: NotRequired[CommerceAddressType]
    r"""The type of the address"""


class CommerceAddress(BaseModel):
    city: Optional[str] = None
    r"""The third line of the address, or city"""

    country: Optional[str] = None
    r"""The country for the address"""

    line1: Optional[str] = None
    r"""The first line of the address"""

    line2: Optional[str] = None
    r"""The second line of the address"""

    postal_code: Annotated[Optional[str], pydantic.Field(alias="postalCode")] = None
    r"""The postal (or zip) code for the address"""

    region: Optional[str] = None
    r"""The fourth line of the address, or region"""

    type: Optional[CommerceAddressType] = None
    r"""The type of the address"""
