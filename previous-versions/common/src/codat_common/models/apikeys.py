"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .apikeydetails import APIKeyDetails, APIKeyDetailsTypedDict
from codat_common.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class APIKeysTypedDict(TypedDict):
    results: NotRequired[List[APIKeyDetailsTypedDict]]


class APIKeys(BaseModel):
    results: Optional[List[APIKeyDetails]] = None