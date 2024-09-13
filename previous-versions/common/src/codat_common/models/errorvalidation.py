"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .errorvalidationitem import ErrorValidationItem, ErrorValidationItemTypedDict
from codat_common.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import NotRequired


class ErrorValidationTypedDict(TypedDict):
    r"""A human-readable object describing validation decisions Codat has made. If an operation has failed because of validation errors, they will be detailed here."""

    errors: NotRequired[Nullable[List[ErrorValidationItemTypedDict]]]
    warnings: NotRequired[Nullable[List[ErrorValidationItemTypedDict]]]


class ErrorValidation(BaseModel):
    r"""A human-readable object describing validation decisions Codat has made. If an operation has failed because of validation errors, they will be detailed here."""

    errors: OptionalNullable[List[ErrorValidationItem]] = UNSET

    warnings: OptionalNullable[List[ErrorValidationItem]] = UNSET

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
