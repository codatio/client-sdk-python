# bill_payments

## Overview

Bill payments

### Available Operations

* [create](#create) - Create bill payments
* [get](#get) - Get bill payment
* [get_create_model](#get_create_model) - Get create bill payment model
* [list](#list) - List bill payments

## create

The *Create bill payment* endpoint creates a new [bill payment](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) for a given company's connection.

[Bill payments](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create bill payment model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-billPayments-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating a bill payment.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillPaymentRequest(
    bill_payment=shared.BillPayment(
        account_ref=shared.AccountRef(
            id='18544ec4-2def-4cce-8f19-77773e63562a',
            name='Ms. Verna Gislason',
        ),
        currency='GBP',
        currency_rate=3314.52,
        date_='2022-10-23T00:00:00.000Z',
        id='3d5a8e00-d108-4045-8823-7f342676cffa',
        lines=[
            shared.BillPaymentLine(
                allocated_on_date='2022-10-23T00:00:00.000Z',
                amount=3071.73,
                links=[
                    shared.BillPaymentLineLink(
                        amount=9847.73,
                        currency_rate=8518.09,
                        id='af313a1f-5fd9-4425-9c0b-36f25ea944f3',
                        type=shared.BillPaymentLineLinkType.REFUND,
                    ),
                    shared.BillPaymentLineLink(
                        amount=4483.86,
                        currency_rate=3296.51,
                        id='6c11f6c3-7a51-4262-8383-5bbc05a23a45',
                        type=shared.BillPaymentLineLinkType.MANUAL_JOURNAL,
                    ),
                    shared.BillPaymentLineLink(
                        amount=9322.5,
                        currency_rate=9555.69,
                        id='c5fde10a-0ce2-4169-a510-019c6dc5e347',
                        type=shared.BillPaymentLineLinkType.OTHER,
                    ),
                ],
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Bill Payment against bill c13e37b6-dfaa-4894-b3be-9fe97bda9f44',
        payment_method_ref='odio',
        reference='natus',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "doloribus": {
                    "quidem": 'itaque',
                    "laboriosam": 'unde',
                    "modi": 'perspiciatis',
                },
                "hic": {
                    "aspernatur": 'libero',
                    "nam": 'incidunt',
                    "recusandae": 'quod',
                },
                "id": {
                    "autem": 'quo',
                    "nesciunt": 'illum',
                    "nemo": 'illum',
                    "facilis": 'non',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='adebd5da-ea4c-4506-a8aa-94c02644cf5e',
            supplier_name='unde',
        ),
        total_amount=1329.54,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=860311,
)

res = s.bill_payments.create(req)

if res.create_bill_payment_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateBillPaymentRequest](../../models/operations/createbillpaymentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |


### Response

**[operations.CreateBillPaymentResponse](../../models/operations/createbillpaymentresponse.md)**


## get

The *Get bill payment* endpoint returns a single bill payment for a given `billPaymentId`.

[Bill payments](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support getting a specific bill payment.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBillPaymentsRequest(
    bill_payment_id='error',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.bill_payments.get(req)

if res.bill_payment is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetBillPaymentsRequest](../../models/operations/getbillpaymentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.GetBillPaymentsResponse](../../models/operations/getbillpaymentsresponse.md)**


## get_create_model

The *Get create bill payment model* endpoint returns the expected data for the request payload when creating a [bill payment](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) for a given company and integration.

[Bill payments](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating a bill payment.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateBillPaymentModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_payments.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCreateBillPaymentModelRequest](../../models/operations/getcreatebillpaymentmodelrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetCreateBillPaymentModelResponse](../../models/operations/getcreatebillpaymentmodelresponse.md)**


## list

The *List bill payments* endpoint returns a list of [bill payments](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) for a given company's connection.

[Bill payments](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBillPaymentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='mollitia',
)

res = s.bill_payments.list(req)

if res.bill_payments is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListBillPaymentsRequest](../../models/operations/listbillpaymentsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.ListBillPaymentsResponse](../../models/operations/listbillpaymentsresponse.md)**
