"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dataintegritydetails import DataIntegrityDetails, DataIntegrityDetailsTypedDict
from .links import Links, LinksTypedDict
from codat_assess.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DetailsTypedDict(TypedDict):
    links: LinksTypedDict
    page_number: int
    r"""Current page number."""
    page_size: int
    r"""Number of items to return in results array."""
    total_results: int
    r"""Total number of items."""
    results: NotRequired[List[DataIntegrityDetailsTypedDict]]


class Details(BaseModel):
    links: Annotated[Links, pydantic.Field(alias="_links")]

    page_number: Annotated[int, pydantic.Field(alias="pageNumber")]
    r"""Current page number."""

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]
    r"""Number of items to return in results array."""

    total_results: Annotated[int, pydantic.Field(alias="totalResults")]
    r"""Total number of items."""

    results: Optional[List[DataIntegrityDetails]] = None
