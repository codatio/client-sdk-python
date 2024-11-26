"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dataintegritysummary import DataIntegritySummary, DataIntegritySummaryTypedDict
from codat_lending.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DataIntegritySummariesTypedDict(TypedDict):
    summaries: NotRequired[List[DataIntegritySummaryTypedDict]]


class DataIntegritySummaries(BaseModel):
    summaries: Optional[List[DataIntegritySummary]] = None