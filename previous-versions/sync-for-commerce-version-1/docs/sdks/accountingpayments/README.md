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
            id='2f64d1db-1f2c-4431-8661-e96349e1cf9e',
            name='Alma Waters',
        ),
        currency='GBP',
        currency_rate=Decimal('2244.67'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='iusto',
            id='000ae6b6-bc9b-48f7-99ea-c55a9741d311',
        ),
        date_='2022-10-23T00:00:00.000Z',
        id='52965bb8-a720-4261-9435-e139dbc2259b',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=Decimal('6633.18'),
                links=[
                    shared.PaymentLineLink(
                        amount=Decimal('7278.88'),
                        currency_rate=Decimal('8544.6'),
                        id='a8c070e1-084c-4b06-b2d1-ad879eeb9665',
                        type=shared.PaymentLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='corporis',
        payment_method_ref='officiis',
        reference='voluptatibus',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "at": {
                    "alias": 'quia',
                },
            },
        ),
        total_amount=Decimal('6941.58'),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=684126,
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

