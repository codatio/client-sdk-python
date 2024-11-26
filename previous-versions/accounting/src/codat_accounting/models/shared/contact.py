"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customerstatus import CustomerStatus
from .items import Items, ItemsTypedDict
from .phonenumber_items import PhoneNumberItems, PhoneNumberItemsTypedDict
from codat_accounting.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ContactTypedDict(TypedDict):
    status: CustomerStatus
    r"""Status of customer."""
    address: NotRequired[ItemsTypedDict]
    email: NotRequired[Nullable[str]]
    r"""Email of a contact for a customer."""
    modified_date: NotRequired[str]
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    >
    > Not all dates from Codat will contain information about time zones.
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """
    name: NotRequired[Nullable[str]]
    r"""Name of a contact for a customer."""
    phone: NotRequired[Nullable[List[PhoneNumberItemsTypedDict]]]
    r"""An array of Phone numbers."""


class Contact(BaseModel):
    status: CustomerStatus
    r"""Status of customer."""

    address: Optional[Items] = None

    email: OptionalNullable[str] = UNSET
    r"""Email of a contact for a customer."""

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    >
    > Not all dates from Codat will contain information about time zones.
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """

    name: OptionalNullable[str] = UNSET
    r"""Name of a contact for a customer."""

    phone: OptionalNullable[List[PhoneNumberItems]] = UNSET
    r"""An array of Phone numbers."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["address", "email", "modifiedDate", "name", "phone"]
        nullable_fields = ["email", "name", "phone"]
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