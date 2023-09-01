# accounting_payments

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

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingPaymentRequest(
    accounting_payment=shared.AccountingPayment(
        account_ref=shared.AccountRef(
            id='7d56844e-ded8-45a9-865e-628bdfc2032b',
            name='Angelica Langworth',
        ),
        currency='USD',
        currency_rate=1443.97,
        customer_ref=shared.AccountingCustomerRef(
            company_name='dolorem',
            id='b7e13584-f7ae-412c-a891-f82ce1157172',
        ),
        date_='2022-10-23T00:00:00.000Z',
        id='05377dcf-a89d-4f97-9e35-6686092e9c3d',
        lines=[
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=3269.42,
                links=[
                    shared.PaymentLineLink(
                        amount=1048.34,
                        currency_rate=1142.12,
                        id='1dea1026-d541-4a4d-990f-eb21780bccc0',
                        type=shared.PaymentLinkType.MANUAL_JOURNAL,
                    ),
                    shared.PaymentLineLink(
                        amount=7188.79,
                        currency_rate=7148.35,
                        id='ddb48470-8fb4-4e39-9e6b-c158c4c4e545',
                        type=shared.PaymentLinkType.REFUND,
                    ),
                    shared.PaymentLineLink(
                        amount=5786.1,
                        currency_rate=9294.43,
                        id='a342260e-9b20-40ce-b8a1-bd8fb7a0a116',
                        type=shared.PaymentLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=8855.23,
                        currency_rate=4909.56,
                        id='23d4097f-a30e-49af-b25b-29122030d83f',
                        type=shared.PaymentLinkType.CREDIT_NOTE,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=9319.53,
                links=[
                    shared.PaymentLineLink(
                        amount=4802.95,
                        currency_rate=4938.65,
                        id='99d22e8c-1f84-4938-a5fd-c42c876c2c2d',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=6908.71,
                        currency_rate=3049.64,
                        id='cfc1c762-30f8-441f-b1bd-23fdb14db6be',
                        type=shared.PaymentLinkType.CREDIT_NOTE,
                    ),
                    shared.PaymentLineLink(
                        amount=6422.79,
                        currency_rate=3755.88,
                        id='85998e22-ae20-4da1-afc2-b271a289c57e',
                        type=shared.PaymentLinkType.REFUND,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=2505.2,
                links=[
                    shared.PaymentLineLink(
                        amount=6050.43,
                        currency_rate=585.67,
                        id='439d2224-6569-4462-8070-84f7ab37cef0',
                        type=shared.PaymentLinkType.UNLINKED,
                    ),
                    shared.PaymentLineLink(
                        amount=1806.6,
                        currency_rate=1622.51,
                        id='5194db55-410a-4dc6-a9af-90a26c7cdc98',
                        type=shared.PaymentLinkType.UNKNOWN,
                    ),
                    shared.PaymentLineLink(
                        amount=9788.57,
                        currency_rate=298.53,
                        id='68981d6b-b33c-4faa-b48c-31bf407ee4fc',
                        type=shared.PaymentLinkType.DISCOUNT,
                    ),
                    shared.PaymentLineLink(
                        amount=0.73,
                        currency_rate=7704.67,
                        id='42b78f15-6263-498a-8dc7-66324ccb06c8',
                        type=shared.PaymentLinkType.PAYMENT_ON_ACCOUNT,
                    ),
                ],
            ),
            shared.PaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=815.41,
                links=[
                    shared.PaymentLineLink(
                        amount=8310.37,
                        currency_rate=271.97,
                        id='2529270b-8d57-422d-9895-b8bcf24db959',
                        type=shared.PaymentLinkType.CREDIT_NOTE,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='amet',
        payment_method_ref='dolor',
        reference='nostrum',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "molestiae": {
                    "ullam": 'velit',
                    "adipisci": 'cupiditate',
                },
                "occaecati": {
                    "fugiat": 'molestiae',
                    "quas": 'repellendus',
                },
                "saepe": {
                    "distinctio": 'vel',
                },
                "necessitatibus": {
                    "nesciunt": 'corrupti',
                    "cupiditate": 'voluptatibus',
                    "ullam": 'dolorum',
                },
            },
        ),
        total_amount=7437.05,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=739946,
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

