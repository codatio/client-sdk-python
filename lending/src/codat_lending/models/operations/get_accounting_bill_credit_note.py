"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class GetAccountingBillCreditNoteRequestTypedDict(TypedDict):
    bill_credit_note_id: str
    r"""Unique identifier for a bill credit note."""
    company_id: str
    r"""Unique identifier for a company."""


class GetAccountingBillCreditNoteRequest(BaseModel):
    bill_credit_note_id: Annotated[
        str,
        pydantic.Field(alias="billCreditNoteId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a bill credit note."""

    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""
