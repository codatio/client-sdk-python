# direct_incomes

## Overview

Direct incomes

### Available Operations

* [create](#create) - Create direct income
* [download_attachment](#download_attachment) - Download direct income attachment
* [get](#get) - Get direct income
* [get_attachment](#get_attachment) - Get direct income attachment
* [get_create_model](#get_create_model) - Get create direct income model
* [list](#list) - List direct incomes
* [list_attachments](#list_attachments) - List direct income attachments
* [upload_attachment](#upload_attachment) - Create direct income attachment

## create

The *Create direct income* endpoint creates a new [direct income](https://docs.codat.io/accounting-api#/schemas/DirectIncome) for a given company's connection.

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateDirectIncomeRequest(
    direct_income=shared.DirectIncome(
        contact_ref=shared.ContactRef(
            data_type='soluta',
            id='6feb9457-c7ed-4af3-9d16-fbf76fd162b3',
        ),
        currency='GBP',
        currency_rate=2210,
        id='e3023b93-e343-416c-b55b-4313553ccf1c',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='4c4adcc9-904c-4519-9b86-48cefa78f1e2',
                    name='Danny Reinger Sr.',
                ),
                description='saepe',
                discount_amount=289.94,
                discount_percentage=5725.89,
                item_ref=shared.ItemRef(
                    id='52bbb4cb-b19f-4713-995a-4169c1387271',
                    name='Terry Luettgen',
                ),
                quantity=5980.87,
                sub_total=8940.82,
                tax_amount=2501.58,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3333.54,
                    id='118c2cc5-7fbd-460b-9a78-ed29a9d4eea8',
                    name='Alma Hickle',
                ),
                total_amount=1452.42,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='4f4c88be-4f27-48fd-9667-e46c51d2ffaa',
                        name='Carole Smith',
                    ),
                    shared.TrackingCategoryRef(
                        id='f234c955-b9bd-4f21-90ab-d9bbcc2725ec',
                        name='Jeanette Hilpert',
                    ),
                    shared.TrackingCategoryRef(
                        id='e0280840-c69e-4f68-a45c-8addfac75450',
                        name='Miss Michele Douglas',
                    ),
                    shared.TrackingCategoryRef(
                        id='632b4391-fdf0-41c3-a91e-8f7bc69d460a',
                        name='Courtney Trantow',
                    ),
                ],
                unit_amount=7355.86,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='nisi',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=9517.68,
                    total_amount=923.49,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='ef2631c7-c0f0-4f87-bf9d-5c25fd3e0b4a',
                        name='Blanche Gusikowski',
                    ),
                    currency='GBP',
                    currency_rate=8051.65,
                    id='3025711f-42c7-4e7d-8548-be09e41a7a21',
                    note='ipsam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='officia',
                    total_amount=901.86,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=2891.08,
                    total_amount=6905.07,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a9d59988-192c-4fd0-877c-53e7e7d4ee6e',
                        name='Miss Robin Marks',
                    ),
                    currency='EUR',
                    currency_rate=2321.12,
                    id='84e23967-03fe-4c31-8508-24d189a36a6b',
                    note='sunt',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='dolores',
                    total_amount=4465.83,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=4576.32,
                    total_amount=351.52,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='7aa60c8f-e46e-4617-bdb9-db3b70ffbb69',
                        name='Sarah VonRueden',
                    ),
                    currency='USD',
                    currency_rate=580.86,
                    id='e36097ef-7c20-46e6-9b0d-308714c20a3d',
                    note='perspiciatis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='ea',
                    total_amount=1937.94,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=6699.87,
                    total_amount=5213.33,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='5c3fe655-74db-4af9-8a7c-98f13af28db2',
                        name='Timmy Cruickshank',
                    ),
                    currency='GBP',
                    currency_rate=9761.21,
                    id='3ded356d-7e14-4b21-8d98-196d55af69a1',
                    note='quod',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='facilis',
                    total_amount=4962.61,
                ),
            ),
        ],
        reference='natus',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=9064.68,
        supplemental_data=shared.SupplementalData(
            content={
                "non": {
                    "praesentium": 'beatae',
                    "eligendi": 'eos',
                },
            },
        ),
        tax_amount=2240.34,
        total_amount=7581.17,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=211693,
)

res = s.direct_incomes.create(req)

if res.create_direct_income_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateDirectIncomeRequest](../../models/operations/createdirectincomerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.CreateDirectIncomeResponse](../../models/operations/createdirectincomeresponse.md)**


## download_attachment

The *Download direct income attachment* endpoint downloads a specific attachment for a given `directIncomeId` and `attachmentId`.

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support downloading a direct income attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='omnis',
)

res = s.direct_incomes.download_attachment(req)

if res.data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DownloadDirectIncomeAttachmentRequest](../../models/operations/downloaddirectincomeattachmentrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.DownloadDirectIncomeAttachmentResponse](../../models/operations/downloaddirectincomeattachmentresponse.md)**


## get

The *Get direct income* endpoint returns a single direct income for a given directIncomeId.

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support getting a specific direct income.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectIncomeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='fuga',
)

res = s.direct_incomes.get(req)

if res.direct_income is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetDirectIncomeRequest](../../models/operations/getdirectincomerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.GetDirectIncomeResponse](../../models/operations/getdirectincomeresponse.md)**


## get_attachment

The *Get direct income attachment* endpoint returns a specific attachment for a given `directIncomeId` and `attachmentId`.

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support getting a direct income attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='voluptate',
    timeout_in_minutes=780639,
)

res = s.direct_incomes.get_attachment(req)

if res.attachment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetDirectIncomeAttachmentRequest](../../models/operations/getdirectincomeattachmentrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetDirectIncomeAttachmentResponse](../../models/operations/getdirectincomeattachmentresponse.md)**


## get_create_model

The *Get create direct income model* endpoint returns the expected data for the request payload when creating a [direct income](https://docs.codat.io/accounting-api#/schemas/DirectIncome) for a given company and integration.

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating a direct income.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateDirectIncomesModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.direct_incomes.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetCreateDirectIncomesModelRequest](../../models/operations/getcreatedirectincomesmodelrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |


### Response

**[operations.GetCreateDirectIncomesModelResponse](../../models/operations/getcreatedirectincomesmodelresponse.md)**


## list

The *List direct incomes* endpoint returns a list of [direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) for a given company's connection.

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectIncomesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='consequatur',
)

res = s.direct_incomes.list(req)

if res.direct_incomes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListDirectIncomesRequest](../../models/operations/listdirectincomesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |


### Response

**[operations.ListDirectIncomesResponse](../../models/operations/listdirectincomesresponse.md)**


## list_attachments

The *List direct income attachments* endpoint returns a list of attachments available to download for given `directIncomeId`.

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support listing direct income attachments.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectIncomeAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='officiis',
)

res = s.direct_incomes.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListDirectIncomeAttachmentsRequest](../../models/operations/listdirectincomeattachmentsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |


### Response

**[operations.ListDirectIncomeAttachmentsResponse](../../models/operations/listdirectincomeattachmentsresponse.md)**


## upload_attachment

The *Upload direct income attachment* endpoint uploads an attachment and assigns it against a specific `directIncomeId`.

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale.

**Integration-specific behaviour**

For more details on supported file types by integration see [Attachments](https://docs.codat.io/accounting-api#/schemas/Attachment).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support uploading a direct income attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadDirectIncomeAttachmentRequest(
    request_body=operations.UploadDirectIncomeAttachmentRequestBody(
        content='ab'.encode(),
        request_body='in',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='optio',
)

res = s.direct_incomes.upload_attachment(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.UploadDirectIncomeAttachmentRequest](../../models/operations/uploaddirectincomeattachmentrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |


### Response

**[operations.UploadDirectIncomeAttachmentResponse](../../models/operations/uploaddirectincomeattachmentresponse.md)**

