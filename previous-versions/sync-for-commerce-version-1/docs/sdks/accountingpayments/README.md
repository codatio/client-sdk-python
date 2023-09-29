# AccountingPayments
(*accounting_payments*)

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
            id='<ID>',
            name='female Romaguera property',
        ),
        currency='GBP',
        currency_rate=Decimal('2253.13'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='Rohan - Stoltenberg',
            id='<ID>',
        ),
        date_='2022-10-23T00:00:00.000Z',
        id='<ID>',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=Decimal('2946.18'),
                links=[
                    shared.PaymentLineLink(
                        amount=Decimal('7256.22'),
                        currency_rate=Decimal('9866.42'),
                        id='<ID>',
                        type=shared.PaymentLinkType.PAYMENT,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='East HDD',
        payment_method_ref='Diesel',
        reference='lumen',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "ab": {
                    "eligendi": 'nimble',
                },
            },
        ),
        total_amount=Decimal('4535.25'),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=324249,
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

