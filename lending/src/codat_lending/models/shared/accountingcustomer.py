"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountingaddress import AccountingAddress, AccountingAddressTypedDict
from .contact import Contact, ContactTypedDict
from .customerstatus import CustomerStatus
from .metadata import Metadata, MetadataTypedDict
from .supplementaldata import SupplementalData, SupplementalDataTypedDict
from codat_lending.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountingCustomerTypedDict(TypedDict):
    r"""## Overview

    A customer is a person or organisation that buys goods or services. From the Customers endpoints, you can retrieve a [list of all the customers of a company](https://api.codat.io/swagger/index.html#/Customers/get_companies__companyId__data_customers).

    Customers' data links to accounts receivable [invoices](https://docs.codat.io/lending-api#/schemas/Invoice).

    """

    status: CustomerStatus
    r"""Status of customer."""
    addresses: NotRequired[Nullable[List[AccountingAddressTypedDict]]]
    r"""An array of Addresses."""
    contact_name: NotRequired[Nullable[str]]
    r"""Name of the main contact for the identified customer."""
    contacts: NotRequired[Nullable[List[ContactTypedDict]]]
    r"""An array of Contacts."""
    customer_name: NotRequired[Nullable[str]]
    r"""Name of the customer as recorded in the accounting system, typically the company name."""
    default_currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    email_address: NotRequired[Nullable[str]]
    r"""Email address the customer can be contacted by."""
    id: NotRequired[str]
    r"""Identifier for the customer, unique to the company in the accounting software."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    phone: NotRequired[Nullable[str]]
    r"""Phone number the customer can be contacted by."""
    registration_number: NotRequired[Nullable[str]]
    r"""Company number. In the UK, this is typically the Companies House company registration number."""
    source_modified_date: NotRequired[str]
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    tax_number: NotRequired[Nullable[str]]
    r"""Company tax number."""


class AccountingCustomer(BaseModel):
    r"""## Overview

    A customer is a person or organisation that buys goods or services. From the Customers endpoints, you can retrieve a [list of all the customers of a company](https://api.codat.io/swagger/index.html#/Customers/get_companies__companyId__data_customers).

    Customers' data links to accounts receivable [invoices](https://docs.codat.io/lending-api#/schemas/Invoice).

    """

    status: CustomerStatus
    r"""Status of customer."""

    addresses: OptionalNullable[List[AccountingAddress]] = UNSET
    r"""An array of Addresses."""

    contact_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="contactName")
    ] = UNSET
    r"""Name of the main contact for the identified customer."""

    contacts: OptionalNullable[List[Contact]] = UNSET
    r"""An array of Contacts."""

    customer_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="customerName")
    ] = UNSET
    r"""Name of the customer as recorded in the accounting system, typically the company name."""

    default_currency: Annotated[
        Optional[str], pydantic.Field(alias="defaultCurrency")
    ] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    email_address: Annotated[
        OptionalNullable[str], pydantic.Field(alias="emailAddress")
    ] = UNSET
    r"""Email address the customer can be contacted by."""

    id: Optional[str] = None
    r"""Identifier for the customer, unique to the company in the accounting software."""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    phone: OptionalNullable[str] = UNSET
    r"""Phone number the customer can be contacted by."""

    registration_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="registrationNumber")
    ] = UNSET
    r"""Company number. In the UK, this is typically the Companies House company registration number."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    supplemental_data: Annotated[
        Optional[SupplementalData], pydantic.Field(alias="supplementalData")
    ] = None
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    tax_number: Annotated[OptionalNullable[str], pydantic.Field(alias="taxNumber")] = (
        UNSET
    )
    r"""Company tax number."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "addresses",
            "contactName",
            "contacts",
            "customerName",
            "defaultCurrency",
            "emailAddress",
            "id",
            "metadata",
            "modifiedDate",
            "phone",
            "registrationNumber",
            "sourceModifiedDate",
            "supplementalData",
            "taxNumber",
        ]
        nullable_fields = [
            "addresses",
            "contactName",
            "contacts",
            "customerName",
            "emailAddress",
            "phone",
            "registrationNumber",
            "taxNumber",
        ]
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
