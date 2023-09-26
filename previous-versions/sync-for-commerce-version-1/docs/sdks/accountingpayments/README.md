# AccountingPayments

## Overview

Payments

### Available Operations

* [create_accounting_payment](#create_accounting_payment) - Create payment

## create_accounting_payment

The *Create payment* endpoint creates a new [payment](https://docs.codat.io/accounting-api#/schemas/Payment) for a given company's connection.

[Payments](https://docs.codat.io/accounting-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create payment model](https://docs.codat.io/accounting-api#/operations/get-create-payments-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=payments) for integrations that support creating an account.


### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared
from decimal import Decimal

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingPaymentRequest(
    accounting_payment=shared.AccountingPayment(
        account_ref=shared.AccountRef(
            id='e96349e1-cf9e-406e-ba43-7000ae6b6bc9',
            name='Alfredo Wilkinson',
        ),
        currency='USD',
        currency_rate=Decimal('8975.43'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='animi',
            id='c55a9741-d311-4352-965b-b8a720261143',
        ),
        date_='2022-10-23T00:00:00.000Z',
        id='e139dbc2-259b-41ab-9a8c-070e1084cb06',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=Decimal('1729.51'),
                links=[
                    shared.PaymentLineLink(
                        amount=Decimal('8247.98'),
                        currency_rate=Decimal('1072.1'),
                        id='ad879eeb-9665-4b85-afbd-02bae0be2d78',
                        type=shared.PaymentLinkType.UNLINKED,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='corporis',
        payment_method_ref='error',
        reference='earum',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "recusandae": {
                    "similique": 'ut',
                },
            },
        ),
        total_amount=Decimal('6937.46'),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=339631,
)

res = s.accounting_payments.create_accounting_payment(req)

if res.accounting_create_payment_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingPaymentRequest](../../models/operations/createaccountingpaymentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.CreateAccountingPaymentResponse](../../models/operations/createaccountingpaymentresponse.md)**

