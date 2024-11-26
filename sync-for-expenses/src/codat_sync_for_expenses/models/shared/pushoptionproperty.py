"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pushoptionchoice import PushOptionChoice, PushOptionChoiceTypedDict
from .pushoptiontype import PushOptionType
from .pushvalidationinfo import PushValidationInfo, PushValidationInfoTypedDict
from codat_sync_for_expenses.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PushOptionPropertyTypedDict(TypedDict):
    description: str
    r"""A description of the property."""
    display_name: str
    r"""The property's display name."""
    required: bool
    r"""The property is required if `True`."""
    type: PushOptionType
    r"""The option type."""
    options: NotRequired[Nullable[List[PushOptionChoiceTypedDict]]]
    properties: NotRequired[Nullable[Dict[str, PushOptionPropertyTypedDict]]]
    validation: NotRequired[PushValidationInfoTypedDict]


class PushOptionProperty(BaseModel):
    description: str
    r"""A description of the property."""

    display_name: Annotated[str, pydantic.Field(alias="displayName")]
    r"""The property's display name."""

    required: bool
    r"""The property is required if `True`."""

    type: PushOptionType
    r"""The option type."""

    options: OptionalNullable[List[PushOptionChoice]] = UNSET

    properties: OptionalNullable[Dict[str, PushOptionProperty]] = UNSET

    validation: Optional[PushValidationInfo] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["options", "properties", "validation"]
        nullable_fields = ["options", "properties"]
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
