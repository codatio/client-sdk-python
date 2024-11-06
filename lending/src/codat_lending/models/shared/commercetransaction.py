"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .supplementaldata import SupplementalData, SupplementalDataTypedDict
from .transactionsourceref import TransactionSourceRef, TransactionSourceRefTypedDict
from .transactiontype import TransactionType
from codat_lending.types import BaseModel
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CommerceTransactionTypedDict(TypedDict):
    r"""Details of all financial transactions recorded in the commerce or point of sale system are added to the Transactions data type. For example, payments, service charges, and fees.

    You can use data from the Transactions endpoints to calculate key metrics, such as:
    - Transaction volumes
    - Average transaction volume
    - Average transaction value
    - Returns
    - Payouts
    """

    id: str
    r"""A unique, persistent identifier for this record"""
    created_date: NotRequired[str]
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
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    modified_date: NotRequired[str]
    source_created_date: NotRequired[str]
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
    source_modified_date: NotRequired[str]
    sub_type: NotRequired[str]
    r"""Non-standardised transaction type data from the commerce software"""
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    total_amount: NotRequired[Decimal]
    r"""The total transaction amount"""
    transaction_source_ref: NotRequired[TransactionSourceRefTypedDict]
    r"""Link to the source event which triggered this transaction"""
    type: NotRequired[TransactionType]
    r"""The type of the platform transaction:
    - `Unknown`
    - `FailedPayout` — Failed transfer of funds from the seller's merchant account to their bank account.
    - `Payment` — Credit and debit card payments.
    - `PaymentFee` — Payment provider's fee on each card payment.
    - `PaymentFeeRefund` — Payment provider's fee that has been refunded to the seller.
    - `Payout` — Transfer of funds from the seller's merchant account to their bank account.
    - `Refund` — Refunds to a customer's credit or debit card.
    - `Transfer` — Secure transfer of funds to the seller's bank account.
    """


class CommerceTransaction(BaseModel):
    r"""Details of all financial transactions recorded in the commerce or point of sale system are added to the Transactions data type. For example, payments, service charges, and fees.

    You can use data from the Transactions endpoints to calculate key metrics, such as:
    - Transaction volumes
    - Average transaction volume
    - Average transaction value
    - Returns
    - Payouts
    """

    id: str
    r"""A unique, persistent identifier for this record"""

    created_date: Annotated[Optional[str], pydantic.Field(alias="createdDate")] = None
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

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    source_created_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceCreatedDate")
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

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    sub_type: Annotated[Optional[str], pydantic.Field(alias="subType")] = None
    r"""Non-standardised transaction type data from the commerce software"""

    supplemental_data: Annotated[
        Optional[SupplementalData], pydantic.Field(alias="supplementalData")
    ] = None
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    total_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalAmount"),
    ] = None
    r"""The total transaction amount"""

    transaction_source_ref: Annotated[
        Optional[TransactionSourceRef], pydantic.Field(alias="transactionSourceRef")
    ] = None
    r"""Link to the source event which triggered this transaction"""

    type: Optional[TransactionType] = None
    r"""The type of the platform transaction:
    - `Unknown`
    - `FailedPayout` — Failed transfer of funds from the seller's merchant account to their bank account.
    - `Payment` — Credit and debit card payments.
    - `PaymentFee` — Payment provider's fee on each card payment.
    - `PaymentFeeRefund` — Payment provider's fee that has been refunded to the seller.
    - `Payout` — Transfer of funds from the seller's merchant account to their bank account.
    - `Refund` — Refunds to a customer's credit or debit card.
    - `Transfer` — Secure transfer of funds to the seller's bank account.
    """
