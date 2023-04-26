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

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating payments.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreatePaymentRequest(
    payment=shared.Payment(
        account_ref=shared.AccountRef(
            id="2de7b356-2201-4a6a-ab4a-e7b1a5b908d4",
            name="Jeffery Aufderhar",
        ),
        currency="quae",
        currency_rate=6765.76,
        customer_ref=shared.CustomerRef(
            company_name="fuga",
            id="35d4a839-f03b-4ab7-bb91-8f0313984507",
        ),
        date_="officiis",
        id="0e39c7e2-3ecb-4060-8652-e23a3d6c657e",
        lines=[
            shared.PaymentLine(
                allocated_on_date="quibusdam",
                amount=8936.05,
                links=[
                    shared.PaymentLineLink(
                        amount=9387.2,
                        currency_rate=4758.76,
                        id="f002d198-6aa9-49d3-a1d3-2329e45837e8",
                        type="Discount",
                    ),
                    shared.PaymentLineLink(
                        amount=1859.89,
                        currency_rate=6377.7,
                        id="d6bb10e2-55fd-4c48-8d6e-3308675cbf18",
                        type="CreditNote",
                    ),
                    shared.PaymentLineLink(
                        amount=5604.72,
                        currency_rate=3424.33,
                        id="6a7e82cd-f9d0-4fc2-82c6-66af3c3f5589",
                        type="PaymentOnAccount",
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date="accusamus",
                amount=6668.05,
                links=[
                    shared.PaymentLineLink(
                        amount=8213.45,
                        currency_rate=1736.08,
                        id="64e41e2c-a848-422e-913f-6d9d2ad37c30",
                        type="Payment",
                    ),
                    shared.PaymentLineLink(
                        amount=5821.15,
                        currency_rate=328.36,
                        id="77c10b68-7921-463e-a7d4-8860543c0a30",
                        type="Invoice",
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date="excepturi",
                amount=7879.41,
                links=[
                    shared.PaymentLineLink(
                        amount=8004.56,
                        currency_rate=9757.5,
                        id="6c0276e7-b21b-4ad9-8d27-43fd6c2a10e6",
                        type="ManualJournal",
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="odit",
        note="natus",
        payment_method_ref=shared.PaymentMethodRef(
            id="78ec256a-5b09-4227-bcc4-7996c977bbc5",
            name="Jeannie Dibbert",
        ),
        reference="eos",
        source_modified_date="quos",
        supplemental_data=shared.SupplementalData(
            content={
                "blanditiis": {
                    "ipsa": "eaque",
                    "quo": "ad",
                },
                "atque": {
                    "eum": "iusto",
                    "facere": "ea",
                    "sequi": "voluptates",
                    "tempora": "similique",
                },
                "officia": {
                    "laboriosam": "quos",
                    "aliquam": "vel",
                },
            },
        ),
        total_amount=2546.16,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=321921,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPaymentRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    payment_id="odio",
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
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating payments.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreatePaymentsModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListPaymentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="omnis",
)

res = s.payments.list(req)

if res.payments is not None:
    # handle response
```
