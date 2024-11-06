"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountingpaymentallocation import (
    AccountingPaymentAllocation,
    AccountingPaymentAllocationTypedDict,
)
from .billcreditnotelineitem import (
    BillCreditNoteLineItem,
    BillCreditNoteLineItemTypedDict,
)
from .billcreditnotestatus import BillCreditNoteStatus
from .items import Items, ItemsTypedDict
from .metadata import Metadata, MetadataTypedDict
from .recordref import RecordRef, RecordRefTypedDict
from .supplementaldata import SupplementalData, SupplementalDataTypedDict
from .supplierref import SupplierRef, SupplierRefTypedDict
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
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountingBillCreditNoteTypedDict(TypedDict):
    r"""> **Bill credit notes or credit notes?**
    >
    > In Codat, bill credit notes represent accounts payable only. For accounts receivable, see [Credit notes](https://docs.codat.io/lending-api#/schemas/CreditNote).

    ## Overview

    A bill credit note is issued by a supplier for the purpose of recording credit. For example, if a supplier was unable to fulfil an order that was placed by a business, or delivered damaged goods, they would issue a bill credit note. A bill credit note reduces the amount a business owes to the supplier. It can be refunded to the business or used to pay off future bills.

    In the Codat API, a bill credit note is an accounts payable record issued by a [supplier](https://docs.codat.io/lending-api#/schemas/Supplier).

    A bill credit note includes details of:
    * The original and remaining credit.
    * Any allocations of the credit against other records, such as [bills](https://docs.codat.io/lending-api#/schemas/Bill).
    * The supplier that issued the bill credit note.
    """

    discount_percentage: Decimal
    r"""Percentage rate of any discount applied to the bill credit note."""
    status: BillCreditNoteStatus
    r"""Current state of the bill credit note"""
    sub_total: Decimal
    r"""Total amount of the bill credit note, including discounts but excluding tax."""
    total_amount: Decimal
    r"""Total amount of credit that has been applied to the business' account with the supplier, including discounts and tax."""
    total_discount: Decimal
    r"""Total value of any discounts applied."""
    total_tax_amount: Decimal
    r"""Amount of tax included in the bill credit note."""
    allocated_on_date: NotRequired[str]
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
    bill_credit_note_number: NotRequired[Nullable[str]]
    r"""Friendly reference for the bill credit note."""
    created_from_refs: NotRequired[Nullable[List[RecordRefTypedDict]]]
    r"""An array of records the credit note was created from."""
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    currency_rate: NotRequired[Nullable[Decimal]]
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting software, it will be available from Codat with the same precision (up to a maximum of 9 decimal places).

    For accounting software which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

    ## Examples with base currency of GBP

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |

    ## Examples with base currency of USD

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, specify a currencyRate in the request body.  |
    """
    id: NotRequired[str]
    r"""Identifier for the bill credit note that is unique to a company in the accounting software."""
    issue_date: NotRequired[str]
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
    line_items: NotRequired[Nullable[List[BillCreditNoteLineItemTypedDict]]]
    r"""An array of line"""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    note: NotRequired[Nullable[str]]
    r"""Any additional information about the bill credit note."""
    payment_allocations: NotRequired[
        Nullable[List[AccountingPaymentAllocationTypedDict]]
    ]
    r"""An array of payment allocations."""
    remaining_credit: NotRequired[Decimal]
    r"""Amount of the bill credit note that is still outstanding."""
    source_modified_date: NotRequired[str]
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    supplier_ref: NotRequired[SupplierRefTypedDict]
    r"""Reference to the supplier the record relates to."""
    withholding_tax: NotRequired[Nullable[List[ItemsTypedDict]]]


class AccountingBillCreditNote(BaseModel):
    r"""> **Bill credit notes or credit notes?**
    >
    > In Codat, bill credit notes represent accounts payable only. For accounts receivable, see [Credit notes](https://docs.codat.io/lending-api#/schemas/CreditNote).

    ## Overview

    A bill credit note is issued by a supplier for the purpose of recording credit. For example, if a supplier was unable to fulfil an order that was placed by a business, or delivered damaged goods, they would issue a bill credit note. A bill credit note reduces the amount a business owes to the supplier. It can be refunded to the business or used to pay off future bills.

    In the Codat API, a bill credit note is an accounts payable record issued by a [supplier](https://docs.codat.io/lending-api#/schemas/Supplier).

    A bill credit note includes details of:
    * The original and remaining credit.
    * Any allocations of the credit against other records, such as [bills](https://docs.codat.io/lending-api#/schemas/Bill).
    * The supplier that issued the bill credit note.
    """

    discount_percentage: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="discountPercentage"),
    ]
    r"""Percentage rate of any discount applied to the bill credit note."""

    status: BillCreditNoteStatus
    r"""Current state of the bill credit note"""

    sub_total: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="subTotal"),
    ]
    r"""Total amount of the bill credit note, including discounts but excluding tax."""

    total_amount: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalAmount"),
    ]
    r"""Total amount of credit that has been applied to the business' account with the supplier, including discounts and tax."""

    total_discount: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalDiscount"),
    ]
    r"""Total value of any discounts applied."""

    total_tax_amount: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalTaxAmount"),
    ]
    r"""Amount of tax included in the bill credit note."""

    allocated_on_date: Annotated[
        Optional[str], pydantic.Field(alias="allocatedOnDate")
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

    bill_credit_note_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="billCreditNoteNumber")
    ] = UNSET
    r"""Friendly reference for the bill credit note."""

    created_from_refs: Annotated[
        OptionalNullable[List[RecordRef]], pydantic.Field(alias="createdFromRefs")
    ] = UNSET
    r"""An array of records the credit note was created from."""

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    currency_rate: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="currencyRate"),
    ] = UNSET
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting software, it will be available from Codat with the same precision (up to a maximum of 9 decimal places).

    For accounting software which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

    ## Examples with base currency of GBP

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **USD**          | $20            | 0.781         | £15.62                     |
    | **EUR**          | €20            | 0.885         | £17.70                     |
    | **RUB**          | ₽20            | 0.011         | £0.22                      |

    ## Examples with base currency of USD

    | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) |
    | :--------------- | :------------- | :------------ | :------------------------- |
    | **GBP**          | £20            | 1.277         | $25.54                     |
    | **EUR**          | €20            | 1.134         | $22.68                     |
    | **RUB**          | ₽20            | 0.015         | $0.30                      |


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, specify a currencyRate in the request body.  |
    """

    id: Optional[str] = None
    r"""Identifier for the bill credit note that is unique to a company in the accounting software."""

    issue_date: Annotated[Optional[str], pydantic.Field(alias="issueDate")] = None
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

    line_items: Annotated[
        OptionalNullable[List[BillCreditNoteLineItem]],
        pydantic.Field(alias="lineItems"),
    ] = UNSET
    r"""An array of line"""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    note: OptionalNullable[str] = UNSET
    r"""Any additional information about the bill credit note."""

    payment_allocations: Annotated[
        OptionalNullable[List[AccountingPaymentAllocation]],
        pydantic.Field(alias="paymentAllocations"),
    ] = UNSET
    r"""An array of payment allocations."""

    remaining_credit: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="remainingCredit"),
    ] = None
    r"""Amount of the bill credit note that is still outstanding."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    supplemental_data: Annotated[
        Optional[SupplementalData], pydantic.Field(alias="supplementalData")
    ] = None
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """

    supplier_ref: Annotated[
        Optional[SupplierRef], pydantic.Field(alias="supplierRef")
    ] = None
    r"""Reference to the supplier the record relates to."""

    withholding_tax: Annotated[
        OptionalNullable[List[Items]], pydantic.Field(alias="withholdingTax")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "allocatedOnDate",
            "billCreditNoteNumber",
            "createdFromRefs",
            "currency",
            "currencyRate",
            "id",
            "issueDate",
            "lineItems",
            "metadata",
            "modifiedDate",
            "note",
            "paymentAllocations",
            "remainingCredit",
            "sourceModifiedDate",
            "supplementalData",
            "supplierRef",
            "withholdingTax",
        ]
        nullable_fields = [
            "billCreditNoteNumber",
            "createdFromRefs",
            "currencyRate",
            "lineItems",
            "note",
            "paymentAllocations",
            "withholdingTax",
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
