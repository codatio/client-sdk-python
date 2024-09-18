"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountconfiguration import AccountConfiguration, AccountConfigurationTypedDict
from codat_sync_for_commerce.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Dict, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PaymentsConfigurationTypedDict(TypedDict):
    accounts: NotRequired[Nullable[Dict[str, AccountConfigurationTypedDict]]]
    sync_payments: NotRequired[bool]
    r"""Boolean indicator for syncing sales."""


class PaymentsConfiguration(BaseModel):
    accounts: OptionalNullable[Dict[str, AccountConfiguration]] = UNSET

    sync_payments: Annotated[Optional[bool], pydantic.Field(alias="syncPayments")] = (
        None
    )
    r"""Boolean indicator for syncing sales."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["accounts", "syncPayments"]
        nullable_fields = ["accounts"]
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
