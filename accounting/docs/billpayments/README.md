# bill_payments

## Overview

Bill payments

### Available Operations

* [create](#create) - Create bill payments
* [delete](#delete) - Delete bill payment
* [get](#get) - Get bill payment
* [get_create_model](#get_create_model) - Get create bill payment model
* [list](#list) - List bill payments

## create

﻿Posts a new bill payment to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create bill payment model](https://docs.codat.io/accounting-api#/operations/get-create-billPayments-model).

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating bill payments.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateBillPaymentRequest(
    bill_payment=shared.BillPayment(
        account_ref=shared.AccountRef(
            id='2af03102-d514-4f4c-86f1-8bf9621a6a4f',
            name='Tamara O'Kon',
        ),
        currency='eveniet',
        currency_rate=9351.61,
        date_='velit',
        id='3d5a8e00-d108-4045-8823-7f342676cffa',
        lines=[
            shared.BillPaymentLine(
                allocated_on_date='eius',
                amount=7019.78,
                links=[
                    shared.BillPaymentLineLink(
                        amount=4896.85,
                        currency_rate=3734.49,
                        id='2c65b344-18e3-4bb9-9c8d-975e0e8419d8',
                        type=shared.BillPaymentLineLinkType.DISCOUNT,
                    ),
                    shared.BillPaymentLineLink(
                        amount=5379.46,
                        currency_rate=2649.58,
                        id='f144f3e0-7edc-4c4a-a5f3-cabd905a972e',
                        type=shared.BillPaymentLineLinkType.UNKNOWN,
                    ),
                    shared.BillPaymentLineLink(
                        amount=3214.73,
                        currency_rate=3927.52,
                        id='728227b2-d309-4470-bf7a-4fa87cf535a6',
                        type=shared.BillPaymentLineLinkType.DISCOUNT,
                    ),
                    shared.BillPaymentLineLink(
                        amount=6578.62,
                        currency_rate=9259.94,
                        id='54ebf60c-321f-4023-b75d-2367fe1a0cc8',
                        type=shared.BillPaymentLineLinkType.MANUAL_JOURNAL,
                    ),
                ],
            ),
            shared.BillPaymentLine(
                allocated_on_date='maiores',
                amount=4857.95,
                links=[
                    shared.BillPaymentLineLink(
                        amount=9609.33,
                        currency_rate=455.1,
                        id='a396d90c-364b-47c1-9dfb-ace188b1c4ee',
                        type=shared.BillPaymentLineLinkType.UNLINKED,
                    ),
                    shared.BillPaymentLineLink(
                        amount=7726.28,
                        currency_rate=5582.83,
                        id='c6ce611f-eeb1-4c7c-bdb6-eec74378ba25',
                        type=shared.BillPaymentLineLinkType.UNLINKED,
                    ),
                    shared.BillPaymentLineLink(
                        amount=1068.06,
                        currency_rate=4810.42,
                        id='747dc915-ad2c-4af5-9d67-23dc0f5ae2f3',
                        type=shared.BillPaymentLineLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                ],
            ),
            shared.BillPaymentLine(
                allocated_on_date='suscipit',
                amount=6886.49,
                links=[
                    shared.BillPaymentLineLink(
                        amount=424.54,
                        currency_rate=201.41,
                        id='87875614-3f5a-46c9-8b55-554080d40bca',
                        type=shared.BillPaymentLineLinkType.REFUND,
                    ),
                    shared.BillPaymentLineLink(
                        amount=7697.89,
                        currency_rate=3947.24,
                        id='cbd6b5f3-ec90-4930-8f92-6bad2553819b',
                        type=shared.BillPaymentLineLinkType.BILL,
                    ),
                ],
            ),
            shared.BillPaymentLine(
                allocated_on_date='voluptate',
                amount=2611.7,
                links=[
                    shared.BillPaymentLineLink(
                        amount=463.84,
                        currency_rate=9154.08,
                        id='d20e5624-8fff-4639-a910-abdcab626766',
                        type=shared.BillPaymentLineLinkType.BILL_PAYMENT,
                    ),
                    shared.BillPaymentLineLink(
                        amount=3857.6,
                        currency_rate=8815.68,
                        id='1ec00221-b335-4d89-acb3-ecfda8d0c549',
                        type=shared.BillPaymentLineLinkType.MANUAL_JOURNAL,
                    ),
                    shared.BillPaymentLineLink(
                        amount=9380.94,
                        currency_rate=427.63,
                        id='3004978a-61fa-41cf-a068-8f77c1ffc71d',
                        type=shared.BillPaymentLineLinkType.MANUAL_JOURNAL,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='fuga',
        note='Bill Payment against bill c13e37b6-dfaa-4894-b3be-9fe97bda9f44',
        payment_method_ref=shared.PaymentMethodRef(
            id='163f2a3c-80a9-47ff-b34c-ddf857a9e618',
            name='Tonya Sauer',
        ),
        reference='quidem',
        source_modified_date='explicabo',
        supplemental_data=shared.SupplementalData(
            content={
                "nulla": {
                    "natus": 'illum',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='fc94d6fe-cd79-4939-8066-a6d2d0003553',
            supplier_name='ratione',
        ),
        total_amount=1329.54,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=555386,
)

res = s.bill_payments.create(req)

if res.create_bill_payment_response is not None:
    # handle response
```

## delete

﻿The _Delete Bill Payments_ endpoint allows you to delete a specified Bill Payment from an accounting platform.

### Process
1. Pass the `{billPaymentId}` to the _Delete Bill Payments_ endpoint and store the `pushOperationKey` returned.
2. Check the status of the delete operation by checking the status of push operation either via
    1. [Push operation webhook](/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),
    2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).

   A `Success` status indicates that the Bill Payment object was deleted from the accounting platform.
3. (Optional) Check that the Bill Payment was deleted from the accounting platform.

### Effect on related objects
Be aware that deleting a Bill Payment from an accounting platform might cause related objects to be modified.

## Integration specifics
Integrations that support soft delete do not permanently delete the object in the accounting platform.

| Integration | Soft Delete | Details                                                                                             |  
|-------------|-------------|-----------------------------------------------------------------------------------------------------|
| Oracle NetSuite   | No          | See [here](/integrations/accounting/netsuite/how-deleting-bill-payments-works) to learn more. |

> **Supported Integrations**
>
> This functionality is currently only supported for our QuickBooks Online abd Oracle NetSuite integrations. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DeleteBillPaymentRequest(
    bill_payment_id='maxime',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_payments.delete(req)

if res.push_operation_summary is not None:
    # handle response
```

## get

﻿Get a bill payment.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetBillPaymentsRequest(
    bill_payment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.bill_payments.get(req)

if res.bill_payment is not None:
    # handle response
```

## get_create_model

﻿Get create bill payment model.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating and deleting bill payments.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetCreateBillPaymentsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_payments.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

﻿Gets the latest billPayments for a company, with pagination.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListBillPaymentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='recusandae',
)

res = s.bill_payments.list(req)

if res.bill_payments is not None:
    # handle response
```
