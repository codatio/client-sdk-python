"""Sentinel / type-alias helpers — matches Speakeasy SDK surface."""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, TypeVar, Union
from typing_extensions import Literal, TypeAlias, TypeAliasType

from pydantic import BaseModel as BaseModel, ConfigDict, model_serializer

# Speakeasy exposes UnrecognizedInt/UnrecognizedStr as the fallback types for open
# (extensible) enums. POC keeps the plain scalar, so these alias to int/str — a
# consumer annotating with them type-checks and runs identically.
UnrecognizedInt: TypeAlias = int
UnrecognizedStr: TypeAlias = str

UNSET_SENTINEL = "~?~unset~?~sentinel~?~"


class Unset(BaseModel):
    """Sentinel distinguishing "not provided" (UNSET) from "explicit None". As a
    pydantic model it serializes to UNSET_SENTINEL, so a model serializer can drop
    UNSET fields from the wire payload while still emitting explicit nulls."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @model_serializer(mode="plain")
    def serialize_model(self):
        return UNSET_SENTINEL

    def __bool__(self) -> Literal[False]:
        return False

    def __repr__(self) -> str:
        return "UNSET"


UNSET = Unset()
_Unset = Unset  # backwards-compat alias for the class name

T = TypeVar("T")

if TYPE_CHECKING:
    Nullable: TypeAlias = Union[T, None]
    OptionalNullable: TypeAlias = Union[Optional[Nullable[T]], _Unset]
else:
    Nullable = TypeAliasType("Nullable", Union[T, None], type_params=(T,))
    OptionalNullable = TypeAliasType(
        "OptionalNullable", Union[Optional[T], _Unset], type_params=(T,)
    )


__all__ = ["BaseModel", "UNSET", "UNSET_SENTINEL", "Unset", "Nullable", "OptionalNullable", "UnrecognizedInt", "UnrecognizedStr"]

from .base64fileinput import Base64EncodedString, Base64FileInput

__all__ += ["Base64EncodedString", "Base64FileInput"]
