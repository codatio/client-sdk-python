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

[Direct incomes](https://docs.codat.io/accounting-api#/schemas/DirectIncome) are sales of items directly to a customer where payment is received at the point of the sale. For example, cash sales of items to a customer, referral commissions, and service fee refunds are considered direct incomes.

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
            data_type='pariatur',
            id='e0d56d73-b005-4503-a8dc-626ff77c6567',
        ),
        currency='GBP',
        currency_rate=9648.65,
        id='5b70e3e4-cfcc-46a9-9ec5-2624d00014ef',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='cea11ac5-3ebb-4658-bf34-0414c5b9acee',
                    name='Brenda Auer',
                ),
                description='provident',
                discount_amount=9865.72,
                discount_percentage=6009.39,
                item_ref=shared.ItemRef(
                    id='2caf1b02-5f1d-4147-98c6-fa2fad0c06c5',
                    name='Salvador Heller',
                ),
                quantity=1699.37,
                sub_total=7794.77,
                tax_amount=8682.31,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8577.05,
                    id='14fc43b7-0bca-488f-a70c-43351c3dd1eb',
                    name='Elijah Kuhic',
                ),
                total_amount=3643.32,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='4f23f1c0-a586-4c3a-a7d7-b67feef5e142',
                        name='Freddie Heller PhD',
                    ),
                    shared.TrackingCategoryRef(
                        id='beceff7c-4b15-46e9-a782-75eea7681746',
                        name='Frank Huels',
                    ),
                    shared.TrackingCategoryRef(
                        id='799b7956-c0b0-4fa0-bb20-a40e7c4ae640',
                        name='Monica Cronin',
                    ),
                    shared.TrackingCategoryRef(
                        id='657b01a0-7c08-4fd3-921c-257930d6f093',
                        name='Earl Towne',
                    ),
                ],
                unit_amount=3024.13,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='6d366dfa-1011-4a09-9b3e-c8b53862de1a',
                    name='Wilfred Buckridge',
                ),
                description='debitis',
                discount_amount=4416.46,
                discount_percentage=1519.16,
                item_ref=shared.ItemRef(
                    id='e521f903-03df-4c33-8397-fffa6d1d3209',
                    name='Mrs. Ora Sanford',
                ),
                quantity=6484.42,
                sub_total=7648.54,
                tax_amount=5632.6,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9895.78,
                    id='e1961ce9-be41-4c86-9dd7-d9719d07b200',
                    name='Zachary Lakin',
                ),
                total_amount=8385.83,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='967df8fd-882a-48e6-8be6-20cd9c5afdd0',
                        name='Sheri Douglas',
                    ),
                ],
                unit_amount=1353.76,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='quasi',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=6484.91,
                    total_amount=8876.25,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='1d87ecc5-fdce-4a8e-ba88-311662cda6d7',
                        name='Jacquelyn Casper',
                    ),
                    currency='USD',
                    currency_rate=394.9,
                    id='66237d42-2786-46db-8a74-9e3984511cc7',
                    note='corporis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='incidunt',
                    total_amount=9911.81,
                ),
            ),
        ],
        reference='alias',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=380.04,
        supplemental_data=shared.SupplementalData(
            content={
                "non": {
                    "minima": 'tempore',
                    "rerum": 'molestiae',
                    "ipsam": 'quos',
                },
            },
        ),
        tax_amount=7965.25,
        total_amount=7512.82,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=587166,
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
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='tempora',
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
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectIncomeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='exercitationem',
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
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='voluptas',
    timeout_in_minutes=157397,
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
from codataccounting.models import operations, shared

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
from codataccounting.models import operations, shared

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
    query='delectus',
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
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectIncomeAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='alias',
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
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadDirectIncomeAttachmentRequest(
    request_body=operations.UploadDirectIncomeAttachmentRequestBody(
        content='consequatur'.encode(),
        request_body='suscipit',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='occaecati',
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

