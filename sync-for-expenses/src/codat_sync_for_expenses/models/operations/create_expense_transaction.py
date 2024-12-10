"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.models.shared import (
    expensetransaction as shared_expensetransaction,
)
from codat_sync_for_expenses.types import BaseModel
from codat_sync_for_expenses.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateExpenseTransactionRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    request_body: NotRequired[
        List[shared_expensetransaction.ExpenseTransactionTypedDict]
    ]


class CreateExpenseTransactionRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    request_body: Annotated[
        Optional[List[shared_expensetransaction.ExpenseTransaction]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None