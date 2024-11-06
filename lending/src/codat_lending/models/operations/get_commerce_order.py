"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetCommerceOrderRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    order_id: str
    r"""Unique identifier for an order."""


class GetCommerceOrderRequest(BaseModel):
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

    order_id: Annotated[
        str,
        pydantic.Field(alias="orderId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for an order."""
