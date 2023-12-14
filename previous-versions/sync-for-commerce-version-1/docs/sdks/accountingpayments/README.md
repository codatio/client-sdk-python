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
        account_ref=shared.AccountRef(),
        currency='EUR',
        customer_ref=shared.AccountingCustomerRef(
            id='<ID>',
        ),
        date_='2022-10-23T00:00:00Z',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00Z',
                amount=Decimal('9211.94'),
                links=[
                    shared.PaymentLineLink(
                        type=shared.PaymentLinkType.UNLINKED,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00Z',
        payment_method_ref=shared.PaymentMethodRef(
            id='<ID>',
        ),
        source_modified_date='2022-10-23T00:00:00Z',
        supplemental_data=shared.SupplementalData(
            content={
                'key': {
                    'key': 'string',
                },
            },
        ),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounting_payments.create_accounting_payment(req)

if res.accounting_create_payment_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingPaymentRequest](../../models/operations/createaccountingpaymentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.CreateAccountingPaymentResponse](../../models/operations/createaccountingpaymentresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |
