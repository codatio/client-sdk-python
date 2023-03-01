from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any, Optional


@dataclasses.dataclass
class PostPaymentPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PostPaymentQueryParams:
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPaymentSourceModifiedDateAccountRef:
    r"""PostPaymentSourceModifiedDateAccountRef
    Account the payment is recorded against in the accounting platform.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPaymentSourceModifiedDateCustomerRef:
    r"""PostPaymentSourceModifiedDateCustomerRef
    Customer the payment is recorded against in the accounting platform.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName'), 'exclude': lambda f: f is None }})
    
class PostPaymentSourceModifiedDateLinesLinksTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    UNLINKED = "Unlinked"
    INVOICE = "Invoice"
    CREDIT_NOTE = "CreditNote"
    OTHER = "Other"
    REFUND = "Refund"
    PAYMENT = "Payment"
    PAYMENT_ON_ACCOUNT = "PaymentOnAccount"
    MANUAL_JOURNAL = "ManualJournal"
    DISCOUNT = "Discount"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPaymentSourceModifiedDateLinesLinks:
    type: PostPaymentSourceModifiedDateLinesLinksTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPaymentSourceModifiedDateLines:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    allocated_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allocatedOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    links: Optional[list[PostPaymentSourceModifiedDateLinesLinks]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('links'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPaymentSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPaymentSourceModifiedDatePaymentMethodRef:
    r"""PostPaymentSourceModifiedDatePaymentMethodRef
    The Payment Method to which the payment is linked in the accounting platform.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPaymentSourceModifiedDateSupplementalData:
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPaymentSourceModifiedDate:
    r"""PostPaymentSourceModifiedDate
    > **Payments or bill payments?**  
    > 
    >  In Codat, payments represent accounts receivable only. For accounts payable, see [bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment). These include [bills](https://docs.codat.io/accounting-api#/schemas/Bill) and credit notes against bills.
    
    > View the coverage for payments in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    Payments include all accounts receivable transaction data. This includes [invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) and [credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote).
    
    A payment in Codat usually represents an allocation of money within any customer accounts receivable account. This includes, but is not strictly limited to: 
    
    - A payment made against an invoice, like a credit card, cheque, or cash payment.
    - An allocation of a customer's credit note, either to an invoice or maybe a refund.
    - A payment made directly to that accounts receivable account. This might be an overpayment or a prepayment. It might also be the refund of a payment made directly to an accounts receivable account.
    
    Depending on the payments allowed by the underlying accounting package, some payment types may be combined. Please see the [Example data](#section-example-data) below for more details.
    
    In Codat, a payment contains details of:
    
    - When the payment was recorded in the accounting system.
    - How much it is for and in what currency that amount is in.
    - Who the payment was _paid by_ – the _customer_.
    - The payment method used.
    - The breakdown of the types of payments – the _line items_.
    
    Payments is a child data type of [account transactions](https://docs.codat.io/accounting-api#/schemas/AccountTransaction).
    
    ## Payment types
    
    ## Payment of an invoice
    
    A payment paying a single invoice has one entry in its `lines` array. This **line** has the following properties:
    
    - An _amount_ that indicates the amount of the invoice that was paid. This is always positive.
    - A **links** array containing one element with the following properties:
      - A **type** that indicates the type of **link**, in this case an `Invoice`.
      - An **id** that contains the ID of the invoice that was paid.
      - An **amount** for the link. The sum of the **line.amount** and the **links.amount** must equal `0`.
    
    The **amount** field on the **line** equals the **totalAmount** on the payment.
    
    ## Payment of multiple invoices
    
    A single payment can pay multiple invoices. This can be represented in one of two formats depending on how the customer keeps their books:
    
    - The payment has multiple entries in its **lines** array, one for each invoice that is paid. Each line follows the example and rules described in [Payment of an invoice](#payment-of-an-invoice).
    - The payment has a line with multiple links to each invoice. This occurs when the proportion of the original payment allocated to each invoice is not available.
    
    Each **line** has the same properties as those described in [Payment of an invoice](#payment-of-an-invoice), with the **amount** indicating how much of the payment was allocated to the invoice. The sum of line amounts equals the **totalAmount** on the payment.
    
    ## Payments and refunds on account
    
    A payment on account, that is a payment that doesn’t pay a specific invoice, has one entry in its lines array. The **line** has the following properties:
    
    - A **totalAmount** that indicates the amount paid by a customer or refunded to them by a company. A payment to the customer is always negative. A refund is always positive.
    - A **links** array containing one element with the following properties:
    - A **type** that indicates the type of link. For a payment this is `PaymentOnAccount`. For a refund this is `Refund`.
    - The **id** containing the ID of the customer.
    - The **amount** for the link is `0` – the **totalAmount** _or_ the amount of the payment or refund.
    
    It is possible to have a payment that is part _on account_ and part _allocated_ to an invoice. Each line should follow the examples above.
    
    ## Using a credit note to pay an invoice
    
    The payment of an invoice using a credit note has one entry in its **lines** array. This **line** has the following properties:
    
    - An **amount** that indicates the amount of money moved, which in this case is `0`, as the credit note and invoice allocation must balance each other.
    - A **links** array containing two elements:
      - The first **link** has:
        - A **type** that indicates the type of **link**, in this case an `Invoice`.
        - An **id** that contains the ID of the invoice that was paid.
      - The second **link** has:
        - A **type** that indicates the type of **link**, in this case a `CreditNote`.
        - An **id** that contains the ID of the credit note used by this payment.
    
    The **amount** field on the **line** equals the **totalAmount** on the payment.
    
    ## Refunding a credit note
    
    A payment refunding a credit note has one entry in its **lines** array. This **line** has the following properties:
    
    - An **amount** that indicates the amount of the credit note that was refunded. This is always negative for a refund.
    - A **links** array that contains one element with the following properties:
      - A **type** that indicates the type of **link**, in this case a `CreditNote`.
      - An **id** that contains the ID of the credit note that was refunded.
    
    The **totalAmount** field on the payment equals the **amount** field of the **line**. These are both negative, as this is money leaving accounts receivable.
    
    ## Refunding a payment
    
    If a payment is refunded, for example, if a customer overpaid an invoice and the overpayment is returned to the customer, there are two payment records: 
    
    - One for the incoming over payment.
    - Another for the outgoing refund.
    
    The payment issuing the refund has a negative **totalAmount**. This payment also has one entry in its lines array with the following properties:
    
    - An **amount** that indicates the amount that was refunded. This is always negative.
    - A **links** array that contains one element with the following properties:
      - A **type** that indicates the type of **link**, in this case a `Payment`.
      - An **id** that contains the ID of the payment that was refunded.
    
    The **amount** field on the **line** equals the **totalAmount** on the payment and is negative, as this is money leaving accounts receivable.
    
    The payment that was refunded has a line where the **amount** is positive and the type of the link is `Refund`. This payment may have several entries in its **lines** array if it was used to partly pay an invoice. 
    
    For example: A £1,050 payment on a £1,000 invoice with a refund of £50 has two lines: 
    
    - One for £1,000 linked to the invoice that was paid.
    - Another for £50 linked to the payment that refunded the overpayment with a** type** of `Refund` and an ID that corresponds to the payment.
    
    The **line** linked to the payment has the following properties:
    
    - An **amount** that indicates the amount that was refunded. This is positive as its money that was added to accounts receivable. It's balanced out by the negative amount of the refund.
    - A **links** array containing one element with the following properties:
      - A **type** that indicates the type of **link**, in this case a `Refund`.
      - An **id** that contains the ID of the payment that refunded this line.
    
    > 📘 Support for linked payments
    > 
    > Not all accounting packages support linking payments in this way. In some platforms, you may see a payment on account and a refund on account.
    
    ## Foreign currencies
    
    There are two types of currency rate that are included in the payments data type: 
    
    Payment currency rate: 
    
    - Base currency of the accounts receivable account.
    - Foreign currency of the payment.
    
    Payment line link currency rate: 
    
    - Base currency of the item the link represents.
    - Foreign currency of the payment.
    
    These two rates allow the calculation of currency loss or gain for any of the transactions affected by the payment lines. The second rate is used when a payment is applied to an item in a currency that doesn't match either:
    
    - The base currency for the accounts receivable account. 
    - The currency of the item.
    
    ```json Currency rate example
    {
        \"id\": \"123\",
        \"note\": \"\"
        \"totalAmount\": 99.99,
        \"currency\": \"GBP\",
        \"lines\": [
            {
                \"amount\": 99.99,
                \"links\": [
                    {
                        \"type\": \"Invoice\",
                        \"id\": \"178\",
                        \"amount\": -50,
                        \"currencyRate\":  1.9998,
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ## Example data
    
    > 📘 Object properties
    > 
    > For the sake of brevity, the examples here may omit properties from objects. For the full object definition, see [Payments](https://api.codat.io/swagger/index.html#/Payments).
    
    ## Simple examples
    
    ```json Payment for invoice
    {
        \"totalAmount\": 1000,
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Allocation of credit note
    {
        \"totalAmount\": 0,
        \"lines\": [
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Payment of invoice and payment on account
    {
        \"totalAmount\": 2000,
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"y\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Refund of credit note
    {
        \"totalAmount\": -1000,
        \"lines\": [
            {
                \"amount\" : -1000,
                \"links\" : [
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Refund on accounts receivable account
    {
        \"totalAmount\": -1000,
        \"lines\": [
            {
                \"amount\" : -1000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Linked refund on accounts receivable account
    {
        \"id\" : \"payment-001\",
        \"totalAmount\": 1000,
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Refund\",
                        \"id\" : \"refund-001\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    {
        \"id\" : \"refund-001\",
        \"totalAmount\": -1000,
        \"lines\": [
            {
                \"amount\" : -1000,
                \"links\" : [
                    {
                        \"type\" : \"Payment\",
                        \"id\" : \"payment-001\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Using a credit note and cash to pay an invoice
    {
        \"totalAmount\": 250,
        \"lines\": [
            {
                \"amount\": 0,
                \"links\": [
                    {
                        \"type\": \"Invoice\",
                        \"id\": \"x\",
                        \"amount\": -750
                    }, 
                    {
                        \"type\": \"CreditNote\",
                        \"id\": \"y\",
                        \"amount\": 750
                    }
                ]
            },
            {
                \"amount\": 250,
                \"links\": [
                    {
                        \"type\": \"Invoice\",
                        \"id\": \"x\",
                        \"amount\": -250
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ## Complex examples
    
    ```json Use two credit notes and 1000 in to \"bank\" (cash, cheque etc.) to pay invoice
    {
        \"totalAmount\": 1000,
        \"lines\": [
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"z\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Pay an invoice with two credit notes and cash, with 1000 left \"on account\"
    {
        \"totalAmount\": 2000,
        \"lines\": [
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"z\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"customer-001\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Two credit notes pay two invoices with no allocation amount specified
    {
        \"totalAmount\": 0,
        \"lines\": [
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"w\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"z\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Two credit notes and cash pay three invoices with no allocation amount specified, and refund cash
    {
        \"totalAmount\": 2000,
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"w\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"u\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"z\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Refund\",
                        \"id\" : \"refund-001\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    {
        \"id\" : \"refund-001\",
        \"totalAmount\": -1000,
        \"lines\": [
            {
                \"amount\" : -1000,
                \"links\" : [
                    {
                        \"type\" : \"Payment\",
                        \"id\" : \"payment-001\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    In this example, a payment on account is used to pay the same invoice in January and again in February.
    
    ```json January
    {
        \"id\": \"001\",
        \"totalAmount\": 5000,
        \"date\" : \"1901-01-01\",
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"Invoice-x\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 4000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"PaymentOnAccount-y\",
                        \"amount\" : -4000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json February
    {
        \"id\": \"001\",
        \"totalAmount\": 5000,
        \"date\" : \"1901-02-01\",
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"Invoice-x\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"Invoice-y\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 3000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"PaymentOnAccount-y\",
                        \"amount\" : -3000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Two credit notes and some cash pay two invoices with no allocations specified
    {
        \"totalAmount\": 500,
        \"lines\": [
            {
                \"amount\": 500,
                \"links\": [{
                        \"type\": \"Invoice\",
                        \"id\": \"a\",
                        \"amount\": -1000
                    }, {
                        \"type\": \"Invoice\",
                        \"id\": \"b\",
                        \"amount\": -1000
                    }, {
                        \"type\": \"CreditNote\",
                        \"id\": \"y\",
                        \"amount\": 750
                    },{
                        \"type\": \"CreditNote\",
                        \"id\": \"z\",
                        \"amount\": 750
                    }
                ]
            }
        ]
    }
    ```
    """
    
    date_: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    account_ref: Optional[PostPaymentSourceModifiedDateAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    customer_ref: Optional[PostPaymentSourceModifiedDateCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerRef'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    lines: Optional[list[PostPaymentSourceModifiedDateLines]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lines'), 'exclude': lambda f: f is None }})
    metadata: Optional[PostPaymentSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    payment_method_ref: Optional[PostPaymentSourceModifiedDatePaymentMethodRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paymentMethodRef'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[PostPaymentSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplementalData'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostPaymentSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class PostPaymentRequest:
    path_params: PostPaymentPathParams = dataclasses.field()
    query_params: PostPaymentQueryParams = dataclasses.field()
    security: PostPaymentSecurity = dataclasses.field()
    request: Optional[PostPaymentSourceModifiedDate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONChangesPushOperationRecordRef:
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    
class PostPayment200ApplicationJSONChangesTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CREATED = "Created"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    ATTACHMENT_UPLOADED = "AttachmentUploaded"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONChanges:
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attachmentId'), 'exclude': lambda f: f is None }})
    record_ref: Optional[PostPayment200ApplicationJSONChangesPushOperationRecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('recordRef'), 'exclude': lambda f: f is None }})
    type: Optional[PostPayment200ApplicationJSONChangesTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONSourceModifiedDateAccountRef:
    r"""PostPayment200ApplicationJSONSourceModifiedDateAccountRef
    Account the payment is recorded against in the accounting platform.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONSourceModifiedDateCustomerRef:
    r"""PostPayment200ApplicationJSONSourceModifiedDateCustomerRef
    Customer the payment is recorded against in the accounting platform.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyName'), 'exclude': lambda f: f is None }})
    
class PostPayment200ApplicationJSONSourceModifiedDateLinesLinksTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    UNLINKED = "Unlinked"
    INVOICE = "Invoice"
    CREDIT_NOTE = "CreditNote"
    OTHER = "Other"
    REFUND = "Refund"
    PAYMENT = "Payment"
    PAYMENT_ON_ACCOUNT = "PaymentOnAccount"
    MANUAL_JOURNAL = "ManualJournal"
    DISCOUNT = "Discount"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONSourceModifiedDateLinesLinks:
    type: PostPayment200ApplicationJSONSourceModifiedDateLinesLinksTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONSourceModifiedDateLines:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    allocated_on_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allocatedOnDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    links: Optional[list[PostPayment200ApplicationJSONSourceModifiedDateLinesLinks]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('links'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONSourceModifiedDatePaymentMethodRef:
    r"""PostPayment200ApplicationJSONSourceModifiedDatePaymentMethodRef
    The Payment Method to which the payment is linked in the accounting platform.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONSourceModifiedDateSupplementalData:
    content: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONSourceModifiedDate:
    r"""PostPayment200ApplicationJSONSourceModifiedDate
    > **Payments or bill payments?**  
    > 
    >  In Codat, payments represent accounts receivable only. For accounts payable, see [bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment). These include [bills](https://docs.codat.io/accounting-api#/schemas/Bill) and credit notes against bills.
    
    > View the coverage for payments in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    Payments include all accounts receivable transaction data. This includes [invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) and [credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote).
    
    A payment in Codat usually represents an allocation of money within any customer accounts receivable account. This includes, but is not strictly limited to: 
    
    - A payment made against an invoice, like a credit card, cheque, or cash payment.
    - An allocation of a customer's credit note, either to an invoice or maybe a refund.
    - A payment made directly to that accounts receivable account. This might be an overpayment or a prepayment. It might also be the refund of a payment made directly to an accounts receivable account.
    
    Depending on the payments allowed by the underlying accounting package, some payment types may be combined. Please see the [Example data](#section-example-data) below for more details.
    
    In Codat, a payment contains details of:
    
    - When the payment was recorded in the accounting system.
    - How much it is for and in what currency that amount is in.
    - Who the payment was _paid by_ – the _customer_.
    - The payment method used.
    - The breakdown of the types of payments – the _line items_.
    
    Payments is a child data type of [account transactions](https://docs.codat.io/accounting-api#/schemas/AccountTransaction).
    
    ## Payment types
    
    ## Payment of an invoice
    
    A payment paying a single invoice has one entry in its `lines` array. This **line** has the following properties:
    
    - An _amount_ that indicates the amount of the invoice that was paid. This is always positive.
    - A **links** array containing one element with the following properties:
      - A **type** that indicates the type of **link**, in this case an `Invoice`.
      - An **id** that contains the ID of the invoice that was paid.
      - An **amount** for the link. The sum of the **line.amount** and the **links.amount** must equal `0`.
    
    The **amount** field on the **line** equals the **totalAmount** on the payment.
    
    ## Payment of multiple invoices
    
    A single payment can pay multiple invoices. This can be represented in one of two formats depending on how the customer keeps their books:
    
    - The payment has multiple entries in its **lines** array, one for each invoice that is paid. Each line follows the example and rules described in [Payment of an invoice](#payment-of-an-invoice).
    - The payment has a line with multiple links to each invoice. This occurs when the proportion of the original payment allocated to each invoice is not available.
    
    Each **line** has the same properties as those described in [Payment of an invoice](#payment-of-an-invoice), with the **amount** indicating how much of the payment was allocated to the invoice. The sum of line amounts equals the **totalAmount** on the payment.
    
    ## Payments and refunds on account
    
    A payment on account, that is a payment that doesn’t pay a specific invoice, has one entry in its lines array. The **line** has the following properties:
    
    - A **totalAmount** that indicates the amount paid by a customer or refunded to them by a company. A payment to the customer is always negative. A refund is always positive.
    - A **links** array containing one element with the following properties:
    - A **type** that indicates the type of link. For a payment this is `PaymentOnAccount`. For a refund this is `Refund`.
    - The **id** containing the ID of the customer.
    - The **amount** for the link is `0` – the **totalAmount** _or_ the amount of the payment or refund.
    
    It is possible to have a payment that is part _on account_ and part _allocated_ to an invoice. Each line should follow the examples above.
    
    ## Using a credit note to pay an invoice
    
    The payment of an invoice using a credit note has one entry in its **lines** array. This **line** has the following properties:
    
    - An **amount** that indicates the amount of money moved, which in this case is `0`, as the credit note and invoice allocation must balance each other.
    - A **links** array containing two elements:
      - The first **link** has:
        - A **type** that indicates the type of **link**, in this case an `Invoice`.
        - An **id** that contains the ID of the invoice that was paid.
      - The second **link** has:
        - A **type** that indicates the type of **link**, in this case a `CreditNote`.
        - An **id** that contains the ID of the credit note used by this payment.
    
    The **amount** field on the **line** equals the **totalAmount** on the payment.
    
    ## Refunding a credit note
    
    A payment refunding a credit note has one entry in its **lines** array. This **line** has the following properties:
    
    - An **amount** that indicates the amount of the credit note that was refunded. This is always negative for a refund.
    - A **links** array that contains one element with the following properties:
      - A **type** that indicates the type of **link**, in this case a `CreditNote`.
      - An **id** that contains the ID of the credit note that was refunded.
    
    The **totalAmount** field on the payment equals the **amount** field of the **line**. These are both negative, as this is money leaving accounts receivable.
    
    ## Refunding a payment
    
    If a payment is refunded, for example, if a customer overpaid an invoice and the overpayment is returned to the customer, there are two payment records: 
    
    - One for the incoming over payment.
    - Another for the outgoing refund.
    
    The payment issuing the refund has a negative **totalAmount**. This payment also has one entry in its lines array with the following properties:
    
    - An **amount** that indicates the amount that was refunded. This is always negative.
    - A **links** array that contains one element with the following properties:
      - A **type** that indicates the type of **link**, in this case a `Payment`.
      - An **id** that contains the ID of the payment that was refunded.
    
    The **amount** field on the **line** equals the **totalAmount** on the payment and is negative, as this is money leaving accounts receivable.
    
    The payment that was refunded has a line where the **amount** is positive and the type of the link is `Refund`. This payment may have several entries in its **lines** array if it was used to partly pay an invoice. 
    
    For example: A £1,050 payment on a £1,000 invoice with a refund of £50 has two lines: 
    
    - One for £1,000 linked to the invoice that was paid.
    - Another for £50 linked to the payment that refunded the overpayment with a** type** of `Refund` and an ID that corresponds to the payment.
    
    The **line** linked to the payment has the following properties:
    
    - An **amount** that indicates the amount that was refunded. This is positive as its money that was added to accounts receivable. It's balanced out by the negative amount of the refund.
    - A **links** array containing one element with the following properties:
      - A **type** that indicates the type of **link**, in this case a `Refund`.
      - An **id** that contains the ID of the payment that refunded this line.
    
    > 📘 Support for linked payments
    > 
    > Not all accounting packages support linking payments in this way. In some platforms, you may see a payment on account and a refund on account.
    
    ## Foreign currencies
    
    There are two types of currency rate that are included in the payments data type: 
    
    Payment currency rate: 
    
    - Base currency of the accounts receivable account.
    - Foreign currency of the payment.
    
    Payment line link currency rate: 
    
    - Base currency of the item the link represents.
    - Foreign currency of the payment.
    
    These two rates allow the calculation of currency loss or gain for any of the transactions affected by the payment lines. The second rate is used when a payment is applied to an item in a currency that doesn't match either:
    
    - The base currency for the accounts receivable account. 
    - The currency of the item.
    
    ```json Currency rate example
    {
        \"id\": \"123\",
        \"note\": \"\"
        \"totalAmount\": 99.99,
        \"currency\": \"GBP\",
        \"lines\": [
            {
                \"amount\": 99.99,
                \"links\": [
                    {
                        \"type\": \"Invoice\",
                        \"id\": \"178\",
                        \"amount\": -50,
                        \"currencyRate\":  1.9998,
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ## Example data
    
    > 📘 Object properties
    > 
    > For the sake of brevity, the examples here may omit properties from objects. For the full object definition, see [Payments](https://api.codat.io/swagger/index.html#/Payments).
    
    ## Simple examples
    
    ```json Payment for invoice
    {
        \"totalAmount\": 1000,
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Allocation of credit note
    {
        \"totalAmount\": 0,
        \"lines\": [
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Payment of invoice and payment on account
    {
        \"totalAmount\": 2000,
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"y\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Refund of credit note
    {
        \"totalAmount\": -1000,
        \"lines\": [
            {
                \"amount\" : -1000,
                \"links\" : [
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Refund on accounts receivable account
    {
        \"totalAmount\": -1000,
        \"lines\": [
            {
                \"amount\" : -1000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Linked refund on accounts receivable account
    {
        \"id\" : \"payment-001\",
        \"totalAmount\": 1000,
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Refund\",
                        \"id\" : \"refund-001\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    {
        \"id\" : \"refund-001\",
        \"totalAmount\": -1000,
        \"lines\": [
            {
                \"amount\" : -1000,
                \"links\" : [
                    {
                        \"type\" : \"Payment\",
                        \"id\" : \"payment-001\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Using a credit note and cash to pay an invoice
    {
        \"totalAmount\": 250,
        \"lines\": [
            {
                \"amount\": 0,
                \"links\": [
                    {
                        \"type\": \"Invoice\",
                        \"id\": \"x\",
                        \"amount\": -750
                    }, 
                    {
                        \"type\": \"CreditNote\",
                        \"id\": \"y\",
                        \"amount\": 750
                    }
                ]
            },
            {
                \"amount\": 250,
                \"links\": [
                    {
                        \"type\": \"Invoice\",
                        \"id\": \"x\",
                        \"amount\": -250
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ## Complex examples
    
    ```json Use two credit notes and 1000 in to \"bank\" (cash, cheque etc.) to pay invoice
    {
        \"totalAmount\": 1000,
        \"lines\": [
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"z\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Pay an invoice with two credit notes and cash, with 1000 left \"on account\"
    {
        \"totalAmount\": 2000,
        \"lines\": [
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"z\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"customer-001\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Two credit notes pay two invoices with no allocation amount specified
    {
        \"totalAmount\": 0,
        \"lines\": [
            {
                \"amount\" : 0,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"w\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"z\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Two credit notes and cash pay three invoices with no allocation amount specified, and refund cash
    {
        \"totalAmount\": 2000,
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"w\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"x\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"u\",
                        \"amount\" : -1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"y\",
                        \"amount\" : 1000
                    },
                    {
                        \"type\" : \"CreditNote\",
                        \"id\" : \"z\",
                        \"amount\" : 1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Refund\",
                        \"id\" : \"refund-001\",
                        \"amount\" : -1000
                    }
                ]
            }
        ]
    }
    {
        \"id\" : \"refund-001\",
        \"totalAmount\": -1000,
        \"lines\": [
            {
                \"amount\" : -1000,
                \"links\" : [
                    {
                        \"type\" : \"Payment\",
                        \"id\" : \"payment-001\",
                        \"amount\" : 1000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    In this example, a payment on account is used to pay the same invoice in January and again in February.
    
    ```json January
    {
        \"id\": \"001\",
        \"totalAmount\": 5000,
        \"date\" : \"1901-01-01\",
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"Invoice-x\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 4000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"PaymentOnAccount-y\",
                        \"amount\" : -4000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json February
    {
        \"id\": \"001\",
        \"totalAmount\": 5000,
        \"date\" : \"1901-02-01\",
        \"lines\": [
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"Invoice-x\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 1000,
                \"links\" : [
                    {
                        \"type\" : \"Invoice\",
                        \"id\" : \"Invoice-y\",
                        \"amount\" : -1000
                    }
                ]
            },
            {
                \"amount\" : 3000,
                \"links\" : [
                    {
                        \"type\" : \"PaymentOnAccount\",
                        \"id\" : \"PaymentOnAccount-y\",
                        \"amount\" : -3000
                    }
                ]
            }
        ]
    }
    ```
    
    
    
    ```json Two credit notes and some cash pay two invoices with no allocations specified
    {
        \"totalAmount\": 500,
        \"lines\": [
            {
                \"amount\": 500,
                \"links\": [{
                        \"type\": \"Invoice\",
                        \"id\": \"a\",
                        \"amount\": -1000
                    }, {
                        \"type\": \"Invoice\",
                        \"id\": \"b\",
                        \"amount\": -1000
                    }, {
                        \"type\": \"CreditNote\",
                        \"id\": \"y\",
                        \"amount\": 750
                    },{
                        \"type\": \"CreditNote\",
                        \"id\": \"z\",
                        \"amount\": 750
                    }
                ]
            }
        ]
    }
    ```
    """
    
    date_: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    account_ref: Optional[PostPayment200ApplicationJSONSourceModifiedDateAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountRef'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency'), 'exclude': lambda f: f is None }})
    currency_rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currencyRate'), 'exclude': lambda f: f is None }})
    customer_ref: Optional[PostPayment200ApplicationJSONSourceModifiedDateCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerRef'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    lines: Optional[list[PostPayment200ApplicationJSONSourceModifiedDateLines]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lines'), 'exclude': lambda f: f is None }})
    metadata: Optional[PostPayment200ApplicationJSONSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata'), 'exclude': lambda f: f is None }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('note'), 'exclude': lambda f: f is None }})
    payment_method_ref: Optional[PostPayment200ApplicationJSONSourceModifiedDatePaymentMethodRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('paymentMethodRef'), 'exclude': lambda f: f is None }})
    reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reference'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    supplemental_data: Optional[PostPayment200ApplicationJSONSourceModifiedDateSupplementalData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplementalData'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalAmount'), 'exclude': lambda f: f is None }})
    
class PostPayment200ApplicationJSONStatusEnum(str, Enum):
    PENDING = "Pending"
    FAILED = "Failed"
    SUCCESS = "Success"
    TIMED_OUT = "TimedOut"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONValidationValidationItem:
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('itemId'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    validator_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validatorName'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSONValidation:
    r"""PostPayment200ApplicationJSONValidation
    A human-readable object describing validation decisions Codat has made when pushing data into the platform. If a push has failed because of validation errors, they will be detailed here.
    """
    
    errors: Optional[list[PostPayment200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors'), 'exclude': lambda f: f is None }})
    warnings: Optional[list[PostPayment200ApplicationJSONValidationValidationItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('warnings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPayment200ApplicationJSON:
    company_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    data_connection_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionKey') }})
    push_operation_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pushOperationKey') }})
    requested_on_utc: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('requestedOnUtc'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: PostPayment200ApplicationJSONStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    status_code: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode') }})
    changes: Optional[list[PostPayment200ApplicationJSONChanges]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('changes'), 'exclude': lambda f: f is None }})
    completed_on_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('completedOnUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    data: Optional[PostPayment200ApplicationJSONSourceModifiedDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeoutInMinutes'), 'exclude': lambda f: f is None }})
    timeout_in_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeoutInSeconds'), 'exclude': lambda f: f is None }})
    validation: Optional[PostPayment200ApplicationJSONValidation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('validation'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostPaymentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_payment_200_application_json_object: Optional[PostPayment200ApplicationJSON] = dataclasses.field(default=None)
    