"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountingcustomerref import AccountingCustomerRef, AccountingCustomerRefTypedDict
from .billedtotype import BilledToType
from .projectref import ProjectRef, ProjectRefTypedDict
from .trackingcategoryref import TrackingCategoryRef, TrackingCategoryRefTypedDict
from codat_lending.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountsPayableTrackingTypedDict(TypedDict):
    r"""Categories, and a project and customer, against which the item is tracked."""

    category_refs: List[TrackingCategoryRefTypedDict]
    is_billed_to: BilledToType
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""
    is_rebilled_to: BilledToType
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""
    customer_ref: NotRequired[AccountingCustomerRefTypedDict]
    project_ref: NotRequired[ProjectRefTypedDict]


class AccountsPayableTracking(BaseModel):
    r"""Categories, and a project and customer, against which the item is tracked."""

    category_refs: Annotated[
        List[TrackingCategoryRef], pydantic.Field(alias="categoryRefs")
    ]

    is_billed_to: Annotated[BilledToType, pydantic.Field(alias="isBilledTo")]
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""

    is_rebilled_to: Annotated[BilledToType, pydantic.Field(alias="isRebilledTo")]
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""

    customer_ref: Annotated[
        Optional[AccountingCustomerRef], pydantic.Field(alias="customerRef")
    ] = None

    project_ref: Annotated[Optional[ProjectRef], pydantic.Field(alias="projectRef")] = (
        None
    )
