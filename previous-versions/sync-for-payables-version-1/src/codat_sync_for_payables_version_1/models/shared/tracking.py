"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .billedtotype import BilledToType
from .trackingcategoryref import TrackingCategoryRef, TrackingCategoryRefTypedDict
from codat_sync_for_payables_version_1.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CustomerRefTypedDict(TypedDict):
    id: str
    r"""`id` from the Customers data type"""
    company_name: NotRequired[Nullable[str]]
    r"""`customerName` from the Customer data type"""


class CustomerRef(BaseModel):
    id: str
    r"""`id` from the Customers data type"""

    company_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="companyName")
    ] = UNSET
    r"""`customerName` from the Customer data type"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["companyName"]
        nullable_fields = ["companyName"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class AccountingProjectReferenceTypedDict(TypedDict):
    id: str
    r"""Unique identifier to the project reference."""
    name: NotRequired[Nullable[str]]
    r"""The project's name."""


class AccountingProjectReference(BaseModel):
    id: str
    r"""Unique identifier to the project reference."""

    name: OptionalNullable[str] = UNSET
    r"""The project's name."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name"]
        nullable_fields = ["name"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class TrackingTypedDict(TypedDict):
    r"""Categories, and a project and customer, against which the item is tracked."""

    category_refs: List[TrackingCategoryRefTypedDict]
    is_billed_to: BilledToType
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""
    is_rebilled_to: BilledToType
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""
    customer_ref: NotRequired[CustomerRefTypedDict]
    project_ref: NotRequired[AccountingProjectReferenceTypedDict]


class Tracking(BaseModel):
    r"""Categories, and a project and customer, against which the item is tracked."""

    category_refs: Annotated[
        List[TrackingCategoryRef], pydantic.Field(alias="categoryRefs")
    ]

    is_billed_to: Annotated[BilledToType, pydantic.Field(alias="isBilledTo")]
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""

    is_rebilled_to: Annotated[BilledToType, pydantic.Field(alias="isRebilledTo")]
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""

    customer_ref: Annotated[
        Optional[CustomerRef], pydantic.Field(alias="customerRef")
    ] = None

    project_ref: Annotated[
        Optional[AccountingProjectReference], pydantic.Field(alias="projectRef")
    ] = None
