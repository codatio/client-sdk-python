# payments

## Overview

Payments

### Available Operations

* [create](#create) - Create payment
* [get](#get) - Get payment
* [get_create_model](#get_create_model) - Get create payment model
* [list](#list) - List payments

## create

Posts a new payment to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create payment model](https://docs.codat.io/accounting-api#/operations/get-create-payments-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) to see which integrations support this endpoint.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreatePaymentRequest(
    payment=shared.Payment(
        account_ref=shared.AccountRef(
            id='aa558a65-e208-4301-aca3-4bb87d4f6212',
            name='Ms. Kristi Jast',
        ),
        currency='architecto',
        currency_rate=3766.39,
        customer_ref=shared.CustomerRef(
            company_name='voluptatem',
            id='6294514c-3db9-4ca9-b38b-d2be87870349',
        ),
        date_='adipisci',
        id='f49aa846-5a32-4832-b9b7-19d1cea673d8',
        lines=[
            shared.PaymentLine(
                allocated_on_date='itaque',
                amount=1984.56,
                links=[
                    shared.PaymentLineLink(
                        amount=1976.2,
                        currency_rate=3400.87,
                        id='e49a3135-778c-4e54-8acb-0e3ea975045b',
                        type=shared.PaymentLinkType.PAYMENT,
                    ),
                    shared.PaymentLineLink(
                        amount=7977.88,
                        currency_rate=9916.87,
                        id='63b21518-6ab5-4e3a-8226-14315d156829',
                        type=shared.PaymentLinkType.REFUND,
                    ),
                    shared.PaymentLineLink(
                        amount=9207.5,
                        currency_rate=3778.77,
                        id='1afc7186-ff20-4b7a-b3df-40ca0d7657c1',
                        type=shared.PaymentLinkType.OTHER,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='eius',
                amount=698.78,
                links=[
                    shared.PaymentLineLink(
                        amount=7083.87,
                        currency_rate=9823,
                        id='055271b2-511d-4d60-add1-b28272bc9c32',
                        type=shared.PaymentLinkType.UNLINKED,
                    ),
                    shared.PaymentLineLink(
                        amount=1125.17,
                        currency_rate=4058.4,
                        id='97b1880f-cbb2-4b93-815f-670bd1784831',
                        type=shared.PaymentLinkType.OTHER,
                    ),
                    shared.PaymentLineLink(
                        amount=3516.07,
                        currency_rate=2234.48,
                        id='eeb3b6e2-41c3-4109-9836-63c66dcbb7df',
                        type=shared.PaymentLinkType.CREDIT_NOTE,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='porro',
        note='soluta',
        payment_method_ref=shared.PaymentMethodRef(
            id='09c8b408-e071-4377-8de4-fee101d9780a',
            name='Laura Schimmel',
        ),
        reference='rerum',
        source_modified_date='provident',
        supplemental_data=shared.SupplementalData(
            content={
                "perferendis": {
                    "accusantium": 'possimus',
                    "vel": 'minus',
                },
                "blanditiis": {
                    "quia": 'similique',
                    "ipsam": 'a',
                    "alias": 'perferendis',
                },
            },
        ),
        total_amount=1333.46,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=152643,
)

res = s.payments.create(req)

if res.create_payment_response is not None:
    # handle response
```

## get

Get payment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetPaymentRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    payment_id='sit',
)

res = s.payments.get(req)

if res.payment is not None:
    # handle response
```

## get_create_model

Get create payment model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating payments.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreatePaymentsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.payments.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

Gets the latest payments for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListPaymentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='esse',
)

res = s.payments.list(req)

if res.payments is not None:
    # handle response
```
