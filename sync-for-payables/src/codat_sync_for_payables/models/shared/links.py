"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .halref import HalRef, HalRefTypedDict
from codat_sync_for_payables.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LinksTypedDict(TypedDict):
    self_: HalRefTypedDict
    current: HalRefTypedDict
    next: NotRequired[HalRefTypedDict]
    previous: NotRequired[HalRefTypedDict]


class Links(BaseModel):
    self_: Annotated[HalRef, pydantic.Field(alias="self")]

    current: HalRef

    next: Optional[HalRef] = None

    previous: Optional[HalRef] = None
