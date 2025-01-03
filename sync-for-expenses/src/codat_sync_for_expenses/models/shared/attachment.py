"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AttachmentTypedDict(TypedDict):
    company_id: NotRequired[str]
    r"""Unique ID of company in Codat"""
    id: NotRequired[str]
    r"""Unique identifier of attachment"""
    transaction_id: NotRequired[str]
    r"""Unique identifier of transaction"""


class Attachment(BaseModel):
    company_id: Annotated[Optional[str], pydantic.Field(alias="companyId")] = None
    r"""Unique ID of company in Codat"""

    id: Optional[str] = None
    r"""Unique identifier of attachment"""

    transaction_id: Annotated[Optional[str], pydantic.Field(alias="transactionId")] = (
        None
    )
    r"""Unique identifier of transaction"""
