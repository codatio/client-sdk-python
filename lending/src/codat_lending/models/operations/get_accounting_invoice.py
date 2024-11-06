"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing_extensions import Annotated, TypedDict


class GetAccountingInvoiceRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    invoice_id: str
    r"""Unique identifier for an invoice."""


class GetAccountingInvoiceRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    invoice_id: Annotated[
        str,
        pydantic.Field(alias="invoiceId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for an invoice."""
