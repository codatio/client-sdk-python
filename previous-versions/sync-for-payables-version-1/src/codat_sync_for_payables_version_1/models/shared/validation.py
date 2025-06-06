"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .validationitem import ValidationItem, ValidationItemTypedDict
from codat_sync_for_payables_version_1.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class ValidationTypedDict(TypedDict):
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""

    errors: NotRequired[Nullable[List[ValidationItemTypedDict]]]
    warnings: NotRequired[Nullable[List[ValidationItemTypedDict]]]


class Validation(BaseModel):
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""

    errors: OptionalNullable[List[ValidationItem]] = UNSET

    warnings: OptionalNullable[List[ValidationItem]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["errors", "warnings"]
        nullable_fields = ["errors", "warnings"]
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
