"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ReportComponentMeasureTypedDict(TypedDict):
    index: NotRequired[int]
    r"""The measure's index."""
    measure_display_name: NotRequired[str]
    r"""The measure's display name."""
    value: NotRequired[Decimal]
    r"""The measure's value."""
    

class ReportComponentMeasure(BaseModel):
    index: Optional[int] = None
    r"""The measure's index."""
    measure_display_name: Annotated[Optional[str], pydantic.Field(alias="measureDisplayName")] = None
    r"""The measure's display name."""
    value: Annotated[Optional[Decimal], BeforeValidator(validate_decimal), PlainSerializer(serialize_decimal(False))] = None
    r"""The measure's value."""
    
