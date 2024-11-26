"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .locationref import LocationRef, LocationRefTypedDict
from codat_commerce.types import BaseModel
from codat_commerce.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ProductInventoryLocationTypedDict(TypedDict):
    location_ref: NotRequired[LocationRefTypedDict]
    r"""Reference to the geographic location where the order was placed."""
    quantity: NotRequired[Decimal]
    r"""The quantity of stock remaining at location."""


class ProductInventoryLocation(BaseModel):
    location_ref: Annotated[
        Optional[LocationRef], pydantic.Field(alias="locationRef")
    ] = None
    r"""Reference to the geographic location where the order was placed."""

    quantity: Annotated[
        Optional[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = None
    r"""The quantity of stock remaining at location."""