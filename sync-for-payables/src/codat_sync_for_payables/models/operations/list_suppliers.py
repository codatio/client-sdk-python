"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables.types import BaseModel
from codat_sync_for_payables.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListSuppliersRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    continuation_token: NotRequired[str]
    r"""Retrieve the next page of results using the continuation token from the previous response."""
    query: NotRequired[str]
    r"""Codat query string allows you to filter by `sourceModifiedDate` or if a supplier is `Active` or `Archived` in the accounting software. Learn more about Codat's query string [here](https://docs.codat.io/using-the-api/querying)."""


class ListSuppliersRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    connection_id: Annotated[
        str,
        pydantic.Field(alias="connectionId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a connection."""

    continuation_token: Annotated[
        Optional[str],
        pydantic.Field(alias="continuationToken"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Retrieve the next page of results using the continuation token from the previous response."""

    query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Codat query string allows you to filter by `sourceModifiedDate` or if a supplier is `Active` or `Archived` in the accounting software. Learn more about Codat's query string [here](https://docs.codat.io/using-the-api/querying)."""
