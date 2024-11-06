"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dataintegritystatus import DataIntegrityStatus, DataIntegrityStatusTypedDict
from codat_lending.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DataIntegrityStatusesTypedDict(TypedDict):
    metadata: NotRequired[List[DataIntegrityStatusTypedDict]]


class DataIntegrityStatuses(BaseModel):
    metadata: Optional[List[DataIntegrityStatus]] = None
