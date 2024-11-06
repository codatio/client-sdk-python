"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetAccountingDirectIncomeRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    direct_income_id: str
    r"""Unique identifier for a direct income."""


class GetAccountingDirectIncomeRequest(BaseModel):
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

    direct_income_id: Annotated[
        str,
        pydantic.Field(alias="directIncomeId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a direct income."""
