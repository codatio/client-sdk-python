"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .links import Links, LinksTypedDict
from .supplier import Supplier, SupplierTypedDict
from codat_sync_for_payables_version_1.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SuppliersTypedDict(TypedDict):
    links: LinksTypedDict
    page_number: int
    r"""Current page number."""
    page_size: int
    r"""Number of items to return in results array."""
    total_results: int
    r"""Total number of items."""
    results: NotRequired[List[SupplierTypedDict]]


class Suppliers(BaseModel):
    links: Annotated[Links, pydantic.Field(alias="_links")]

    page_number: Annotated[int, pydantic.Field(alias="pageNumber")]
    r"""Current page number."""

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]
    r"""Number of items to return in results array."""

    total_results: Annotated[int, pydantic.Field(alias="totalResults")]
    r"""Total number of items."""

    results: Optional[List[Supplier]] = None
