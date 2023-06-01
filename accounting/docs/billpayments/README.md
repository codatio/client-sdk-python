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

Posts a new bill payment to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create bill payment model](https://docs.codat.io/accounting-api#/operations/get-create-billPayments-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) to see which integrations support this endpoint.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillPaymentRequest(
    bill_payment=shared.BillPayment(
        account_ref=shared.AccountRef(
            id='8502a55e-7f73-4bc8-85e3-20a319f4badf',
            name='Jesus Kreiger',
        ),
        currency='animi',
        currency_rate=5287.42,
        date_='aliquid',
        id='3d5a8e00-d108-4045-8823-7f342676cffa',
        lines=[
            shared.BillPaymentLine(
                allocated_on_date='facilis',
                amount=7594.51,
                links=[
                    shared.BillPaymentLineLink(
                        amount=1782.01,
                        currency_rate=2993.79,
                        id='26665816-ddca-48ef-91fc-b4c593ec12cd',
                        type=shared.BillPaymentLineLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                    shared.BillPaymentLineLink(
                        amount=6615.78,
                        currency_rate=8409.92,
                        id='0ec7afed-bd80-4df4-88a4-7f9390c58880',
                        type=shared.BillPaymentLineLinkType.BILL_PAYMENT,
                    ),
                ],
            ),
            shared.BillPaymentLine(
                allocated_on_date='quas',
                amount=2184.13,
                links=[
                    shared.BillPaymentLineLink(
                        amount=6834.9,
                        currency_rate=7047.32,
                        id='f9ef3ffd-d9f7-4f07-9af4-d35724cdb0f4',
                        type=shared.BillPaymentLineLinkType.MANUAL_JOURNAL,
                    ),
                    shared.BillPaymentLineLink(
                        amount=1776.51,
                        currency_rate=5556.63,
                        id='1187d568-44ed-4ed8-9a90-65e628bdfc20',
                        type=shared.BillPaymentLineLinkType.BILL,
                    ),
                    shared.BillPaymentLineLink(
                        amount=1553.71,
                        currency_rate=6937.24,
                        id='6c879923-b7e1-4358-8f7a-e12c6891f82c',
                        type=shared.BillPaymentLineLinkType.DISCOUNT,
                    ),
                    shared.BillPaymentLineLink(
                        amount=1171.42,
                        currency_rate=810.53,
                        id='57172305-377d-4cfa-89df-975e35668609',
                        type=shared.BillPaymentLineLinkType.UNLINKED,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='itaque',
        note='Bill Payment against bill c13e37b6-dfaa-4894-b3be-9fe97bda9f44',
        payment_method_ref=shared.PaymentMethodRef(
            id='9c3ddc5f-111d-4ea1-826d-541a4d190feb',
            name='Evelyn Kuhlman MD',
        ),
        reference='placeat',
        source_modified_date='quod',
        supplemental_data=shared.SupplementalData(
            content={
                "sit": {
                    "distinctio": 'distinctio',
                    "assumenda": 'illum',
                    "soluta": 'magnam',
                    "laudantium": 'tempora',
                },
                "esse": {
                    "corrupti": 'reiciendis',
                },
                "facilis": {
                    "repudiandae": 'amet',
                    "natus": 'ab',
                },
                "officiis": {
                    "rerum": 'placeat',
                    "ab": 'ad',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='8c4c4e54-599e-4a34-a260-e9b200ce78a1',
            supplier_name='expedita',
        ),
        total_amount=1329.54,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=842921,
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteBillPaymentRequest(
    bill_payment_id='quos',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBillPaymentsRequest(
    bill_payment_id='maiores',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBillPaymentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='quidem',
)

res = s.bill_payments.list(req)

if res.bill_payments is not None:
    # handle response
```
