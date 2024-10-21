"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables.types import BaseModel
from codat_sync_for_payables.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListCompaniesRequestTypedDict(TypedDict):
    page: NotRequired[int]
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""
    page_size: NotRequired[int]
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""
    query: NotRequired[str]
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""
    order_by: NotRequired[str]
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""


class ListCompaniesRequest(BaseModel):
    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""

    query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""

    order_by: Annotated[
        Optional[str],
        pydantic.Field(alias="orderBy"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""
