"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountstatus import AccountStatus
from .accounttype import AccountType
from .supplementaldata import SupplementalData, SupplementalDataTypedDict
from codat_sync_for_expenses.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_sync_for_expenses.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ValidDataTypeLinksTypedDict(TypedDict):
    r"""When querying Codat's data model, some data types return `validDatatypeLinks` metadata in the JSON response. This indicates where that object can be used as a reference—a _valid link_—when creating or updating other data.

    For example, `validDatatypeLinks` might indicate the following references:

    - Which tax rates are valid to use on the line item of a bill.
    - Which items can be used when creating an invoice.

    You can use `validDatatypeLinks` to present your SMB customers with only valid choices when selecting objects from a list, for example.

    ## `validDatatypeLinks` example

    The following example uses the `Accounting.Accounts` data type. It shows that, on the linked integration, this account is valid as the account on a payment or bill payment; and as the account referenced on the line item of a direct income or direct cost. Because there is no valid link to Invoices or Bills, using this account on those data types will result in an error.

    ```json validDatatypeLinks for an account
    {
    \"id\": \"bd9e85e0-0478-433d-ae9f-0b3c4f04bfe4\",
    \"nominalCode\": \"090\",
    \"name\": \"Business Bank Account\",
    #...
    \"validDatatypeLinks\": [
    {
    \"property\": \"Id\",
    \"links\": [
    \"Payment.AccountRef.Id\",
    \"BillPayment.AccountRef.Id\",
    \"DirectIncome.LineItems.AccountRef.Id\",
    \"DirectCost.LineItems.AccountRef.Id\"
    ]
    }
    ]
    }
    ```



    ## Support for `validDatatypeLinks`

    Codat currently supports `validDatatypeLinks` for some data types on our Xero, QuickBooks Online, QuickBooks Desktop, Exact (NL), and Sage Business Cloud integrations.

    If you'd like us to extend support to more data types or integrations, suggest or vote for this on our <a href=\"https://portal.productboard.com/codat/5-product-roadmap\">Product Roadmap</a>.
    """

    links: NotRequired[Nullable[List[str]]]
    r"""Supported `dataTypes` that the record can be linked to."""
    property: NotRequired[Nullable[str]]
    r"""The property from the account that can be linked."""


class ValidDataTypeLinks(BaseModel):
    r"""When querying Codat's data model, some data types return `validDatatypeLinks` metadata in the JSON response. This indicates where that object can be used as a reference—a _valid link_—when creating or updating other data.

    For example, `validDatatypeLinks` might indicate the following references:

    - Which tax rates are valid to use on the line item of a bill.
    - Which items can be used when creating an invoice.

    You can use `validDatatypeLinks` to present your SMB customers with only valid choices when selecting objects from a list, for example.

    ## `validDatatypeLinks` example

    The following example uses the `Accounting.Accounts` data type. It shows that, on the linked integration, this account is valid as the account on a payment or bill payment; and as the account referenced on the line item of a direct income or direct cost. Because there is no valid link to Invoices or Bills, using this account on those data types will result in an error.

    ```json validDatatypeLinks for an account
    {
    \"id\": \"bd9e85e0-0478-433d-ae9f-0b3c4f04bfe4\",
    \"nominalCode\": \"090\",
    \"name\": \"Business Bank Account\",
    #...
    \"validDatatypeLinks\": [
    {
    \"property\": \"Id\",
    \"links\": [
    \"Payment.AccountRef.Id\",
    \"BillPayment.AccountRef.Id\",
    \"DirectIncome.LineItems.AccountRef.Id\",
    \"DirectCost.LineItems.AccountRef.Id\"
    ]
    }
    ]
    }
    ```



    ## Support for `validDatatypeLinks`

    Codat currently supports `validDatatypeLinks` for some data types on our Xero, QuickBooks Online, QuickBooks Desktop, Exact (NL), and Sage Business Cloud integrations.

    If you'd like us to extend support to more data types or integrations, suggest or vote for this on our <a href=\"https://portal.productboard.com/codat/5-product-roadmap\">Product Roadmap</a>.
    """

    links: OptionalNullable[List[str]] = UNSET
    r"""Supported `dataTypes` that the record can be linked to."""

    property: OptionalNullable[str] = UNSET
    r"""The property from the account that can be linked."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["links", "property"]
        nullable_fields = ["links", "property"]
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


class AccountPrototypeTypedDict(TypedDict):
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    current_balance: NotRequired[Nullable[Decimal]]
    r"""Current balance in the account."""
    description: NotRequired[Nullable[str]]
    r"""Description for the account."""
    fully_qualified_category: NotRequired[Nullable[str]]
    r"""Full category of the account.

    For example, `Liability.Current` or `Income.Revenue`. To determine a list of possible categories for each integration, see our examples, follow our [Create, update, delete data](https://docs.codat.io/using-the-api/push) guide, or refer to the integration's own documentation.
    """
    fully_qualified_name: NotRequired[Nullable[str]]
    r"""Full name of the account, for example:
    - `Cash On Hand`
    - `Rents Held In Trust`
    - `Fixed Asset`
    """
    is_bank_account: NotRequired[bool]
    r"""Confirms whether the account is a bank account or not."""
    name: NotRequired[Nullable[str]]
    r"""Name of the account."""
    nominal_code: NotRequired[Nullable[str]]
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""
    status: NotRequired[AccountStatus]
    r"""Status of the account"""
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    type: NotRequired[AccountType]
    r"""Type of account"""
    valid_datatype_links: NotRequired[Nullable[List[ValidDataTypeLinksTypedDict]]]
    r"""The validDatatypeLinks can be used to determine whether an account can be correctly mapped to another object; for example, accounts with a `type` of `income` might only support being used on an Invoice and Direct Income. For more information, see [Valid Data Type Links](/sync-for-expenses-api#/schemas/ValidDataTypeLinks)."""


class AccountPrototype(BaseModel):
    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    current_balance: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="currentBalance"),
    ] = UNSET
    r"""Current balance in the account."""

    description: OptionalNullable[str] = UNSET
    r"""Description for the account."""

    fully_qualified_category: Annotated[
        OptionalNullable[str], pydantic.Field(alias="fullyQualifiedCategory")
    ] = UNSET
    r"""Full category of the account.

    For example, `Liability.Current` or `Income.Revenue`. To determine a list of possible categories for each integration, see our examples, follow our [Create, update, delete data](https://docs.codat.io/using-the-api/push) guide, or refer to the integration's own documentation.
    """

    fully_qualified_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="fullyQualifiedName")
    ] = UNSET
    r"""Full name of the account, for example:
    - `Cash On Hand`
    - `Rents Held In Trust`
    - `Fixed Asset`
    """

    is_bank_account: Annotated[
        Optional[bool], pydantic.Field(alias="isBankAccount")
    ] = None
    r"""Confirms whether the account is a bank account or not."""

    name: OptionalNullable[str] = UNSET
    r"""Name of the account."""

    nominal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="nominalCode")
    ] = UNSET
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""

    status: Optional[AccountStatus] = None
    r"""Status of the account"""

    supplemental_data: Annotated[
        Optional[SupplementalData], pydantic.Field(alias="supplementalData")
    ] = None
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    type: Optional[AccountType] = None
    r"""Type of account"""

    valid_datatype_links: Annotated[
        OptionalNullable[List[ValidDataTypeLinks]],
        pydantic.Field(alias="validDatatypeLinks"),
    ] = UNSET
    r"""The validDatatypeLinks can be used to determine whether an account can be correctly mapped to another object; for example, accounts with a `type` of `income` might only support being used on an Invoice and Direct Income. For more information, see [Valid Data Type Links](/sync-for-expenses-api#/schemas/ValidDataTypeLinks)."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "currency",
            "currentBalance",
            "description",
            "fullyQualifiedCategory",
            "fullyQualifiedName",
            "isBankAccount",
            "name",
            "nominalCode",
            "status",
            "supplementalData",
            "type",
            "validDatatypeLinks",
        ]
        nullable_fields = [
            "currentBalance",
            "description",
            "fullyQualifiedCategory",
            "fullyQualifiedName",
            "name",
            "nominalCode",
            "validDatatypeLinks",
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
