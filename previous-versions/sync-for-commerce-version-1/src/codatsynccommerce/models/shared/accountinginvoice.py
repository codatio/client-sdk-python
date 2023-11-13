"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountingcustomerref import AccountingCustomerRef
from .datatype import DataType
from .invoicelineitem import InvoiceLineItem
from .invoicestatus import InvoiceStatus
from .metadata import Metadata
from .paymentallocationpayment import PaymentAllocationPayment
from .supplementaldata import SupplementalData
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountingInvoiceAllocation:
    allocated_on_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allocatedOnDate'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

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
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    currency_rate: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyRate'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.  

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places). 

    For accounting platforms which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

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
    """
    total_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""The total amount that has been allocated."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountingPaymentAllocation:
    allocation: AccountingInvoiceAllocation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allocation') }})
    payment: PaymentAllocationPayment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SalesOrderReference:
    data_type: Optional[DataType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Available Data types"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier to a record in `dataType`."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WithholdingTax:
    amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of tax withheld."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name assigned to withheld tax."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountingInvoice:
    r"""> **Invoices or bills?**
    >
    > We distinguish between invoices where the company *owes money* vs. *is owed money*. If the company issued an invoice, and is owed money (accounts receivable) we call this an Invoice.
    >
    > See [Bills](https://docs.codat.io/accounting-api#/schemas/Bill) for the accounts payable equivalent of bills.

    View the coverage for invoices in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    An invoice is an itemized record of goods sold or services provided to a [customer](https://docs.codat.io/accounting-api#/schemas/Customer).

    In Codat, an invoice contains details of:

    - The timeline of the invoice—when it was raised, marked as paid, last edited, and so on.
    - How much the invoice is for, what portion of the invoice is tax or discounts, and what currency the amounts are represented in. 
    - Who the invoice has been raised to; the _customer_.
    - The breakdown of what the invoice is for; the _line items_.
    - Any [payments](https://docs.codat.io/accounting-api#/schemas/Payment) assigned to the invoice; the _payment allocations_.

    > **Invoice PDF downloads**  
    >
    > You can <a className=\"external\" href=\"https://docs.codat.io/accounting-api#/operations/get-invoice-pdf\" target=\"_blank\">download a PDF version</a> of an invoice for supported integrations.
    > 
    > The filename will be invoice-{number}.pdf.

    > **Referencing an invoice in Sage 50 and ClearBooks**
    >
    > In Sage 50 and ClearBooks, you may prefer to use the **invoiceNumber** to identify an invoice rather than the invoice **id**. Each time a draft invoice is submitted or printed, the draft **id** becomes void and a submitted invoice with a new **id** exists in its place. In both platforms, the **invoiceNumber** should remain the same.
    """
    amount_due: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amountDue'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Amount outstanding on the invoice."""
    issue_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issueDate') }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

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
    status: InvoiceStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Current state of the invoice:

    - `Draft` - Invoice hasn't been submitted to the supplier. It may be in a pending state or is scheduled for future submission, for example by email.
    - `Submitted` - Invoice is no longer a draft. It has been processed and, or, sent to the customer. In this state, it will impact the ledger. It also has no payments made against it (amountDue == totalAmount).
    - `PartiallyPaid` - The balance paid against the invoice is positive, but less than the total invoice amount (0 < amountDue < totalAmount).
    - `Paid` - Invoice is paid in full. This includes if the invoice has been credited or overpaid (amountDue == 0).
    - `Void` - An invoice can become Void when it's deleted, refunded, written off, or cancelled. A voided invoice may still be PartiallyPaid, and so all outstanding amounts on voided invoices are removed from the accounts receivable account.
    """
    total_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of the invoice, inclusive of tax."""
    total_tax_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalTaxAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of tax on the invoice."""
    additional_tax_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalTaxAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Additional tax amount applied to invoice."""
    additional_tax_percentage: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalTaxPercentage'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Percentage rate of any additional tax applied to the invoice."""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    currency_rate: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currencyRate'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.

    Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.  

    It is not possible to perform the currency conversion with two or more non-base currencies participating in the transaction. For example, if a company's base currency is USD, and it has a bill issued in EUR, then the bill payment must happen in USD or EUR.

    Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places). 

    For accounting platforms which do not provide an explicit currency rate, it is calculated as `baseCurrency / foreignCurrency` and will be returned to 9 decimal places.

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
    """
    customer_ref: Optional[AccountingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    discount_percentage: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Percentage rate (from 0 to 100) of discounts applied to the invoice. For example: A 5% discount will return a value of `5`, not `0.05`."""
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

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
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the invoice, unique to the company in the accounting platform."""
    invoice_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNumber') }})
    r"""Friendly reference for the invoice. If available, this appears in the file name of invoice attachments."""
    line_items: Optional[List[InvoiceLineItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    r"""An array of line items."""
    metadata: Optional[Metadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('note') }})
    r"""Any additional information about the invoice. Where possible, Codat links to a data field in the accounting platform that is publicly available. This means that the contents of the note field are included when an invoice is emailed from the accounting platform to the customer."""
    paid_on_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paidOnDate'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

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
    payment_allocations: Optional[List[AccountingPaymentAllocation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentAllocations') }})
    r"""An array of payment allocations."""
    sales_order_refs: Optional[List[SalesOrderReference]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('salesOrderRefs') }})
    r"""List of references to related Sales orders."""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    sub_total: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Total amount of the invoice excluding any taxes."""
    supplemental_data: Optional[SupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting platform. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    total_discount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalDiscount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Numerical value of discounts applied to the invoice."""
    withholding_tax: Optional[List[WithholdingTax]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('withholdingTax') }})
    

