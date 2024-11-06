"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountstatus import AccountStatus
from .accounttype import AccountType
from .datatype import DataType
from .metadata import Metadata, MetadataTypedDict
from .pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
from .pushoperationstatus import PushOperationStatus
from .supplementaldata import SupplementalData, SupplementalDataTypedDict
from .validation import Validation, ValidationTypedDict
from codat_lending.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict, deprecated


class AccountingCreateAccountResponseValidDataTypeLinksTypedDict(TypedDict):
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


class AccountingCreateAccountResponseValidDataTypeLinks(BaseModel):
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


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class AccountingCreateAccountResponseAccountingAccountTypedDict(TypedDict):
    r"""> **Language tip:** Accounts are also referred to as **chart of accounts**, **nominal accounts**, and **general ledger**.

    ## Overview

    Accounts are the categories a business uses to record accounting transactions. From the Accounts endpoints, you can retrieve a list of all accounts for a specified company.

    The categories for an account include:
    * Asset
    * Expense
    * Income
    * Liability
    * Equity.

    The same account may have a different category based on the integration it is used in. For example, a current account (known as checking in the US) should be categorized as `Asset.Current` for Xero, and `Asset.Bank.Checking` for QuickBooks Online.

    At the same time, each integration may have its own requirements to the categories. For example, a Paypal account in Xero is of the `Asset.Bank` category and therefore requires additional properties to be provided.

    To determine the list of allowed categories for a specific integration, you can:
    - Follow our [Create, update, delete data](https://docs.codat.io/using-the-api/push) guide and use the [Get create account model](https://docs.codat.io/lending-api#/operations/get-create-chartOfAccounts-model).
    - Refer to the integration's own documentation.

    > **Accounts with no category**
    >
    > If an account is pulled from the chart of accounts and its nominal code does not lie within the category layout for the company's accounts, then the **type** is `Unknown`. The **fullyQualifiedCategory** and **fullyQualifiedName** fields return `null`.
    >
    > This approach gives a true representation of the company's accounts whilst preventing distorting financials such as a company's profit and loss and balance sheet reports.
    """

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
    id: NotRequired[str]
    r"""Identifier for the account, unique for the company."""
    is_bank_account: NotRequired[bool]
    r"""Confirms whether the account is a bank account or not."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    name: NotRequired[Nullable[str]]
    r"""Name of the account."""
    nominal_code: NotRequired[Nullable[str]]
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""
    source_modified_date: NotRequired[str]
    status: NotRequired[AccountStatus]
    r"""Status of the account"""
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    type: NotRequired[AccountType]
    r"""Type of account"""
    valid_datatype_links: NotRequired[
        Nullable[List[AccountingCreateAccountResponseValidDataTypeLinksTypedDict]]
    ]
    r"""The validDatatypeLinks can be used to determine whether an account can be correctly mapped to another object; for example, accounts with a `type` of `income` might only support being used on an Invoice and Direct Income. For more information, see [Valid Data Type Links](/lending-api#/schemas/ValidDataTypeLinks)."""


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class AccountingCreateAccountResponseAccountingAccount(BaseModel):
    r"""> **Language tip:** Accounts are also referred to as **chart of accounts**, **nominal accounts**, and **general ledger**.

    ## Overview

    Accounts are the categories a business uses to record accounting transactions. From the Accounts endpoints, you can retrieve a list of all accounts for a specified company.

    The categories for an account include:
    * Asset
    * Expense
    * Income
    * Liability
    * Equity.

    The same account may have a different category based on the integration it is used in. For example, a current account (known as checking in the US) should be categorized as `Asset.Current` for Xero, and `Asset.Bank.Checking` for QuickBooks Online.

    At the same time, each integration may have its own requirements to the categories. For example, a Paypal account in Xero is of the `Asset.Bank` category and therefore requires additional properties to be provided.

    To determine the list of allowed categories for a specific integration, you can:
    - Follow our [Create, update, delete data](https://docs.codat.io/using-the-api/push) guide and use the [Get create account model](https://docs.codat.io/lending-api#/operations/get-create-chartOfAccounts-model).
    - Refer to the integration's own documentation.

    > **Accounts with no category**
    >
    > If an account is pulled from the chart of accounts and its nominal code does not lie within the category layout for the company's accounts, then the **type** is `Unknown`. The **fullyQualifiedCategory** and **fullyQualifiedName** fields return `null`.
    >
    > This approach gives a true representation of the company's accounts whilst preventing distorting financials such as a company's profit and loss and balance sheet reports.
    """

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

    id: Optional[str] = None
    r"""Identifier for the account, unique for the company."""

    is_bank_account: Annotated[
        Optional[bool], pydantic.Field(alias="isBankAccount")
    ] = None
    r"""Confirms whether the account is a bank account or not."""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    name: OptionalNullable[str] = UNSET
    r"""Name of the account."""

    nominal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="nominalCode")
    ] = UNSET
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

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
        OptionalNullable[List[AccountingCreateAccountResponseValidDataTypeLinks]],
        pydantic.Field(alias="validDatatypeLinks"),
    ] = UNSET
    r"""The validDatatypeLinks can be used to determine whether an account can be correctly mapped to another object; for example, accounts with a `type` of `income` might only support being used on an Invoice and Direct Income. For more information, see [Valid Data Type Links](/lending-api#/schemas/ValidDataTypeLinks)."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "currency",
            "currentBalance",
            "description",
            "fullyQualifiedCategory",
            "fullyQualifiedName",
            "id",
            "isBankAccount",
            "metadata",
            "modifiedDate",
            "name",
            "nominalCode",
            "sourceModifiedDate",
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


class AccountingCreateAccountResponseTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for your SMB in Codat."""
    data_connection_key: str
    r"""Unique identifier for a company's data connection."""
    push_operation_key: str
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""
    requested_on_utc: str
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
    status: PushOperationStatus
    r"""The current status of the push operation."""
    status_code: int
    r"""Push status code."""
    changes: NotRequired[Nullable[List[PushOperationChangeTypedDict]]]
    r"""Contains a single entry that communicates which record has changed and the manner in which it changed."""
    completed_on_utc: NotRequired[str]
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
    data: NotRequired[
        Nullable[AccountingCreateAccountResponseAccountingAccountTypedDict]
    ]
    data_type: NotRequired[DataType]
    r"""Available data types"""
    error_message: NotRequired[Nullable[str]]
    r"""A message about the error."""
    timeout_in_minutes: NotRequired[Nullable[int]]
    r"""Number of minutes the push operation must complete within before it times out."""
    timeout_in_seconds: NotRequired[Nullable[int]]
    r"""Number of seconds the push operation must complete within before it times out."""
    validation: NotRequired[ValidationTypedDict]
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""


class AccountingCreateAccountResponse(BaseModel):
    company_id: Annotated[str, pydantic.Field(alias="companyId")]
    r"""Unique identifier for your SMB in Codat."""

    data_connection_key: Annotated[str, pydantic.Field(alias="dataConnectionKey")]
    r"""Unique identifier for a company's data connection."""

    push_operation_key: Annotated[str, pydantic.Field(alias="pushOperationKey")]
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""

    requested_on_utc: Annotated[str, pydantic.Field(alias="requestedOnUtc")]
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

    status: PushOperationStatus
    r"""The current status of the push operation."""

    status_code: Annotated[int, pydantic.Field(alias="statusCode")]
    r"""Push status code."""

    changes: OptionalNullable[List[PushOperationChange]] = UNSET
    r"""Contains a single entry that communicates which record has changed and the manner in which it changed."""

    completed_on_utc: Annotated[
        Optional[str], pydantic.Field(alias="completedOnUtc")
    ] = None
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

    data: OptionalNullable[AccountingCreateAccountResponseAccountingAccount] = UNSET

    data_type: Annotated[Optional[DataType], pydantic.Field(alias="dataType")] = None
    r"""Available data types"""

    error_message: Annotated[
        OptionalNullable[str], pydantic.Field(alias="errorMessage")
    ] = UNSET
    r"""A message about the error."""

    timeout_in_minutes: Annotated[
        OptionalNullable[int], pydantic.Field(alias="timeoutInMinutes")
    ] = UNSET
    r"""Number of minutes the push operation must complete within before it times out."""

    timeout_in_seconds: Annotated[
        OptionalNullable[int],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="timeoutInSeconds",
        ),
    ] = UNSET
    r"""Number of seconds the push operation must complete within before it times out."""

    validation: Optional[Validation] = None
    r"""A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "changes",
            "completedOnUtc",
            "data",
            "dataType",
            "errorMessage",
            "timeoutInMinutes",
            "timeoutInSeconds",
            "validation",
        ]
        nullable_fields = [
            "changes",
            "data",
            "errorMessage",
            "timeoutInMinutes",
            "timeoutInSeconds",
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
