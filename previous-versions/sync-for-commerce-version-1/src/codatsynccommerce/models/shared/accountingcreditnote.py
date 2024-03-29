"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountingcustomerref import AccountingCustomerRef
from .creditnotelineitem import CreditNoteLineItem
from .creditnotestatus import CreditNoteStatus
from .metadata import Metadata
from .paymentallocation_items import PaymentAllocationItems
from .supplementaldata import SupplementalData
from .withholdingtax_items import WithholdingTaxItems
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountingCreditNote:
    r"""> View the coverage for credit notes in the <a className=\\"external\\" href=\\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes\\" target=\\"_blank\\">Data coverage explorer</a>.

    ## Overview

    Think of a credit note as a voucher issued to a customer. It is a reduction that can be applied against one or multiple invoices. A credit note can either reduce the amount owed or cancel out an invoice entirely.

    In the Codat system a credit note is issued to a [customer's](https://docs.codat.io/accounting-api#/schemas/Customer) accounts receivable. 

    It contains details of:
    * The amount of credit remaining and its status.
    * Payment allocations against the payments type, in this case an invoice.
    * Which customers the credit notes have been issued to.
    """
    discount_percentage: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Percentage rate (from 0 to 100) of discounts applied to the credit note."""
    remaining_credit: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remainingCredit'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Unused balance of totalAmount originally raised."""
    status: CreditNoteStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Current state of the credit note."""
    sub_total: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Value of the credit note, including discounts and excluding tax."""
    total_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Total amount of credit that has been applied to the customer's accounts receivable"""
    total_discount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalDiscount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Any discounts applied to the credit note amount."""
    total_tax_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalTaxAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Any tax applied to the credit note amount."""
    additional_tax_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalTaxAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Additional tax amount applied to credit note."""
    additional_tax_percentage: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalTaxPercentage'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Percentage rate of any additional tax applied to the credit note."""
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
    credit_note_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditNoteNumber') }})
    r"""Friendly reference for the credit note."""
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


    ### Integration-specific details

    | Integration       | Scenario                                        | System behavior                                                                                                                                                      |
    |-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | QuickBooks Online | Transaction currency differs from base currency | If currency rate value is left `null`, a rate of 1 will be used by QBO by default. To override this, include the required currency rate in the expense transaction.  |
    """
    customer_ref: Optional[AccountingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier for the credit note, unique to the company in the accounting platform."""
    issue_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issueDate'), 'exclude': lambda f: f is None }})
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
    line_items: Optional[List[CreditNoteLineItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    metadata: Optional[Metadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('note') }})
    r"""Any additional information about the credit note. Where possible, Codat links to a data field in the accounting platform that is publicly available. This means that the contents of the note field are included when a credit note is emailed from the accounting platform to the customer."""
    payment_allocations: Optional[List[PaymentAllocationItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentAllocations') }})
    r"""An array of payment allocations."""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[SupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalData'), 'exclude': lambda f: f is None }})
    r"""Supplemental data is additional data you can include in our standard data types.

    It is referenced as a configured dynamic key value pair that is unique to the accounting platform. [Learn more](https://docs.codat.io/using-the-api/supplemental-data/overview) about supplemental data.
    """
    withholding_tax: Optional[List[WithholdingTaxItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('withholdingTax') }})
    

