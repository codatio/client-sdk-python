"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables.models.shared import (
    billpaymentprototype as shared_billpaymentprototype,
)
from codat_sync_for_payables.types import BaseModel
from codat_sync_for_payables.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateBillPaymentRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    bill_id: str
    r"""Unique identifier for a bill."""
    idempotency_key: NotRequired[str]
    r"""A unique identifier to ensure idempotent behaviour for subsequent requests."""
    bill_payment_prototype: NotRequired[
        shared_billpaymentprototype.BillPaymentPrototypeTypedDict
    ]


class CreateBillPaymentRequest(BaseModel):
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

    bill_id: Annotated[
        str,
        pydantic.Field(alias="billId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a bill."""

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A unique identifier to ensure idempotent behaviour for subsequent requests."""

    bill_payment_prototype: Annotated[
        Optional[shared_billpaymentprototype.BillPaymentPrototype],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None