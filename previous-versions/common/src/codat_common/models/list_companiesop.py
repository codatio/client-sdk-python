"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_common.types import BaseModel
from codat_common.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListCompaniesRequestTypedDict(TypedDict):
    order_by: NotRequired[str]
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""
    page: NotRequired[int]
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""
    page_size: NotRequired[int]
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""
    query: NotRequired[str]
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""


class ListCompaniesRequest(BaseModel):
    order_by: Annotated[
        Optional[str],
        pydantic.Field(alias="orderBy"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""

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
