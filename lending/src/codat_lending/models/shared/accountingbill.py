"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountingpaymentallocation import (
    AccountingPaymentAllocation,
    AccountingPaymentAllocationTypedDict,
)
from .billlineitem import BillLineItem, BillLineItemTypedDict
from .billstatus import BillStatus
from .metadata import Metadata, MetadataTypedDict
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


class PurchaseOrderReferenceTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Identifier for the purchase order, unique for the company in the accounting software."""
    purchase_order_number: NotRequired[Nullable[str]]
    r"""Friendly reference for the purchase order, commonly generated by the accounting software."""


class PurchaseOrderReference(BaseModel):
    id: Optional[str] = None
    r"""Identifier for the purchase order, unique for the company in the accounting software."""

    purchase_order_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="purchaseOrderNumber")
    ] = UNSET
    r"""Friendly reference for the purchase order, commonly generated by the accounting software."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "purchaseOrderNumber"]
        nullable_fields = ["purchaseOrderNumber"]
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


class WithholdingTaxTypedDict(TypedDict):
    amount: Decimal
    r"""Amount of tax withheld."""
    name: str
    r"""Name assigned to withheld tax."""


class WithholdingTax(BaseModel):
    amount: Annotated[
        Decimal,
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ]
    r"""Amount of tax withheld."""

    name: str
    r"""Name assigned to withheld tax."""


class AccountingBillTypedDict(TypedDict):
    r"""> **Invoices or bills?**
    >
    > We distinguish between invoices where the company *owes money* vs. *is owed money*. If the company has received an invoice, and owes money to someone else (accounts payable) we call this a Bill.
    >
    > See [Invoices](https://docs.codat.io/lending-api#/schemas/Invoice) for the accounts receivable equivalent of bills.

    ## Overview

    In Codat, a bill contains details of:
    * When the bill was recorded in the accounting system.
    * How much the bill is for and the currency of the amount.
    * Who the bill was received from — the *supplier*.
    * What the bill is for — the *line items*.

    Some accounting software give a separate name to purchases where the payment is made immediately, such as something bought with a credit card or online payment. One example of this would be QuickBooks Online's *expenses*.

    You can find these types of transactions in our [Direct costs](https://docs.codat.io/lending-api#/schemas/DirectCost) data model.
    """

    issue_date: str
    status: BillStatus
    r"""Current state of the bill."""
    sub_total: Decimal
    r"""Total amount of the bill, excluding any taxes."""
    tax_amount: Decimal
    r"""Amount of tax on the bill."""
    total_amount: Decimal
    r"""Amount of the bill, including tax."""
    amount_due: NotRequired[Nullable[Decimal]]
    r"""Amount outstanding on the bill."""
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
    due_date: NotRequired[str]
    id: NotRequired[str]
    r"""Identifier for the bill, unique for the company in the accounting software."""
    line_items: NotRequired[Nullable[List[BillLineItemTypedDict]]]
    r"""Array of Bill line items."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    note: NotRequired[Nullable[str]]
    r"""Any private, company notes about the bill, such as payment information."""
    payment_allocations: NotRequired[
        Nullable[List[AccountingPaymentAllocationTypedDict]]
    ]
    r"""An array of payment allocations."""
    purchase_order_refs: NotRequired[Nullable[List[PurchaseOrderReferenceTypedDict]]]
    reference: NotRequired[Nullable[str]]
    r"""User-friendly reference for the bill."""
    source_modified_date: NotRequired[str]
    supplemental_data: NotRequired[SupplementalDataTypedDict]
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting software. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    supplier_ref: NotRequired[SupplierRefTypedDict]
    r"""Reference to the supplier the record relates to."""
    withholding_tax: NotRequired[Nullable[List[WithholdingTaxTypedDict]]]


class AccountingBill(BaseModel):
    r"""> **Invoices or bills?**
    >
    > We distinguish between invoices where the company *owes money* vs. *is owed money*. If the company has received an invoice, and owes money to someone else (accounts payable) we call this a Bill.
    >
    > See [Invoices](https://docs.codat.io/lending-api#/schemas/Invoice) for the accounts receivable equivalent of bills.

    ## Overview

    In Codat, a bill contains details of:
    * When the bill was recorded in the accounting system.
    * How much the bill is for and the currency of the amount.
    * Who the bill was received from — the *supplier*.
    * What the bill is for — the *line items*.

    Some accounting software give a separate name to purchases where the payment is made immediately, such as something bought with a credit card or online payment. One example of this would be QuickBooks Online's *expenses*.

    You can find these types of transactions in our [Direct costs](https://docs.codat.io/lending-api#/schemas/DirectCost) data model.
    """

    issue_date: Annotated[str, pydantic.Field(alias="issueDate")]

    status: BillStatus
    r"""Current state of the bill."""

    sub_total: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="subTotal"),
    ]
    r"""Total amount of the bill, excluding any taxes."""

    tax_amount: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="taxAmount"),
    ]
    r"""Amount of tax on the bill."""

    total_amount: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalAmount"),
    ]
    r"""Amount of the bill, including tax."""

    amount_due: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="amountDue"),
    ] = UNSET
    r"""Amount outstanding on the bill."""

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

    due_date: Annotated[Optional[str], pydantic.Field(alias="dueDate")] = None

    id: Optional[str] = None
    r"""Identifier for the bill, unique for the company in the accounting software."""

    line_items: Annotated[
        OptionalNullable[List[BillLineItem]], pydantic.Field(alias="lineItems")
    ] = UNSET
    r"""Array of Bill line items."""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    note: OptionalNullable[str] = UNSET
    r"""Any private, company notes about the bill, such as payment information."""

    payment_allocations: Annotated[
        OptionalNullable[List[AccountingPaymentAllocation]],
        pydantic.Field(alias="paymentAllocations"),
    ] = UNSET
    r"""An array of payment allocations."""

    purchase_order_refs: Annotated[
        OptionalNullable[List[PurchaseOrderReference]],
        pydantic.Field(alias="purchaseOrderRefs"),
    ] = UNSET

    reference: OptionalNullable[str] = UNSET
    r"""User-friendly reference for the bill."""

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
        OptionalNullable[List[WithholdingTax]], pydantic.Field(alias="withholdingTax")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "amountDue",
            "currency",
            "currencyRate",
            "dueDate",
            "id",
            "lineItems",
            "metadata",
            "modifiedDate",
            "note",
            "paymentAllocations",
            "purchaseOrderRefs",
            "reference",
            "sourceModifiedDate",
            "supplementalData",
            "supplierRef",
            "withholdingTax",
        ]
        nullable_fields = [
            "amountDue",
            "currencyRate",
            "lineItems",
            "note",
            "paymentAllocations",
            "purchaseOrderRefs",
            "reference",
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