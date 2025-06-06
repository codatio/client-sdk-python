"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.types import BaseModel
from codat_sync_for_expenses.utils import FieldMetadata, SecurityMetadata
from typing_extensions import Annotated, TypedDict


class SecurityTypedDict(TypedDict):
    auth_header: str


class Security(BaseModel):
    auth_header: Annotated[
        str,
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="apiKey",
                sub_type="header",
                field_name="Authorization",
            )
        ),
    ]
