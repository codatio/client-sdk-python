# direct_costs

## Overview

Direct costs

### Available Operations

* [create](#create) - Create direct cost
* [download_attachment](#download_attachment) - Download direct cost attachment
* [get](#get) - Get direct cost
* [get_attachment](#get_attachment) - Get direct cost attachment
* [get_create_model](#get_create_model) - Get create direct cost model
* [list](#list) - List direct costs
* [list_attachments](#list_attachments) - List direct cost attachments
* [upload_attachment](#upload_attachment) - Upload direct cost attachment

## create

The *Create direct cost* endpoint creates a new [direct cost](https://docs.codat.io/accounting-api#/schemas/DirectCost) for a given company's connection.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are the expenses associated with a business' operations. For example, purchases of raw materials that are paid off at the point of the purchase and service fees are considered direct costs.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create direct cost model](https://docs.codat.io/accounting-api#/operations/get-create-directCosts-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateDirectCostRequest(
    direct_cost=shared.DirectCost(
        contact_ref=shared.ContactRef(
            data_type='inventore',
            id='fdf01c3e-91e8-4f7b-869d-460a77eceb26',
        ),
        currency='EUR',
        currency_rate=1008.13,
        id='0f1ef263-1c7c-40f0-b873-f9d5c25fd3e0',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='a4a4253c-3025-4711-b42c-7e7dc548be09',
                    name='Bradley Boyle',
                ),
                description='culpa',
                discount_amount=1734.29,
                discount_percentage=816.73,
                item_ref=shared.ItemRef(
                    id='5ca12a4b-a9d5-4998-8192-cfd0c77c53e7',
                    name='Julio Schulist',
                ),
                quantity=8787.52,
                sub_total=3952.6,
                tax_amount=9251.57,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5344.54,
                    id='b90bac38-4e23-4967-83fe-c31c50824d18',
                    name='Kenny Fadel',
                ),
                total_amount=4356.32,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='accountTransaction',
                        id='2d27eb70-7aa6-40c8-be46-e6177db9db3b',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='journalEntry',
                            id='ffbb6970-ee77-40e3-a097-ef7c206e61b0',
                        ),
                        shared.InvoiceTo(
                            data_type='transfer',
                            id='308714c2-0a3d-4986-b7ca-85c3fe65574d',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='af94a7c9-8f13-4af2-8db2-cf2bf4f3ded3',
                        name='Terri Stehr',
                    ),
                    shared.TrackingCategoryRef(
                        id='14b21cd9-8196-4d55-af69-a1c4b79ae336',
                        name='Albert Roob',
                    ),
                    shared.TrackingCategoryRef(
                        id='c39a7c0e-17cb-412c-9ba8-25fe22cd5cba',
                        name='May Rogahn',
                    ),
                ],
                unit_amount=7892.35,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='932af681-3d65-4bfe-8ec2-dd6916f7fc7d',
                    name='Dr. Matt Kreiger',
                ),
                description='aliquid',
                discount_amount=257.44,
                discount_percentage=8786.54,
                item_ref=shared.ItemRef(
                    id='6075894d-61c1-44cd-9022-7e37c0d977f1',
                    name='Greg Gerlach V',
                ),
                quantity=6973.14,
                sub_total=8869.03,
                tax_amount=5900.02,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4925.06,
                    id='51b106d2-3e03-4e69-815a-ae99fcde9e72',
                    name='Colin Mueller',
                ),
                total_amount=9831.05,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='journalEntry',
                        id='d8a44640-ca60-4db7-ba2f-93f467dc0d8d',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='invoice',
                            id='6122026a-b8f2-4774-85c1-976af980da7a',
                        ),
                        shared.InvoiceTo(
                            data_type='journalEntry',
                            id='89fc44db-2745-430e-9cc7-c6d0cbcfdcd3',
                        ),
                        shared.InvoiceTo(
                            data_type='journalEntry',
                            id='4b6f623b-ceca-4b50-aee5-e0da8b9af6ad',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5486e7b4-13cb-4e2d-976d-c1c43d40f61d',
                        name='Mrs. Melinda Borer',
                    ),
                ],
                unit_amount=7638.37,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='debitis',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=2524.07,
                    total_amount=9407.97,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='72118407-72f3-42e3-b49d-be0f23b7b6d9',
                        name='Theodore Lynch',
                    ),
                    currency='EUR',
                    currency_rate=8165.56,
                    id='ed477680-fc7a-417a-82e5-e82fd28d1040',
                    note='harum',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='debitis',
                    total_amount=5723.68,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=6096.53,
                    total_amount=1850.41,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='ab44cb18-3500-48f4-a1ce-53e914498a9b',
                        name='Miss Theodore Huel',
                    ),
                    currency='EUR',
                    currency_rate=9692.94,
                    id='de410c37-daa9-4182-a49d-9625d3caffc1',
                    note='cupiditate',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='voluptates',
                    total_amount=9025.46,
                ),
            ),
        ],
        reference='animi',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=3101.3,
        supplemental_data=shared.SupplementalData(
            content={
                "dolores": {
                    "unde": 'odit',
                    "tempore": 'maxime',
                },
                "possimus": {
                    "ut": 'ipsa',
                    "saepe": 'id',
                },
            },
        ),
        tax_amount=5779.71,
        total_amount=5452.98,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=723093,
)

res = s.direct_costs.create(req)

if res.create_direct_cost_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateDirectCostRequest](../../models/operations/createdirectcostrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.CreateDirectCostResponse](../../models/operations/createdirectcostresponse.md)**


## download_attachment

The *Download direct cost attachment* endpoint downloads a specific attachment for a given `directCostId` and `attachmentId`.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support downloading a direct cost attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadDirectCostAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='itaque',
)

res = s.direct_costs.download_attachment(req)

if res.data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.DownloadDirectCostAttachmentRequest](../../models/operations/downloaddirectcostattachmentrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |


### Response

**[operations.DownloadDirectCostAttachmentResponse](../../models/operations/downloaddirectcostattachmentresponse.md)**


## get

The *Get direct cost* endpoint returns a single direct cost for a given directCostId.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support getting a specific direct cost.

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

req = operations.GetDirectCostRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='placeat',
)

res = s.direct_costs.get(req)

if res.direct_cost is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetDirectCostRequest](../../models/operations/getdirectcostrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.GetDirectCostResponse](../../models/operations/getdirectcostresponse.md)**


## get_attachment

The *Get direct cost attachment* endpoint returns a specific attachment for a given `directCostId` and `attachmentId`.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support getting a direct cost attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectCostAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='porro',
)

res = s.direct_costs.get_attachment(req)

if res.attachment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetDirectCostAttachmentRequest](../../models/operations/getdirectcostattachmentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.GetDirectCostAttachmentResponse](../../models/operations/getdirectcostattachmentresponse.md)**


## get_create_model

The *Get create direct cost model* endpoint returns the expected data for the request payload when creating a [direct cost](https://docs.codat.io/accounting-api#/schemas/DirectCost) for a given company and integration.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating a direct cost.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateDirectCostsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.direct_costs.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCreateDirectCostsModelRequest](../../models/operations/getcreatedirectcostsmodelrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetCreateDirectCostsModelResponse](../../models/operations/getcreatedirectcostsmodelresponse.md)**


## list

The *List direct costs* endpoint returns a list of [direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) for a given company's connection.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

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

req = operations.ListDirectCostsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='itaque',
)

res = s.direct_costs.list(req)

if res.direct_costs is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListDirectCostsRequest](../../models/operations/listdirectcostsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.ListDirectCostsResponse](../../models/operations/listdirectcostsresponse.md)**


## list_attachments

The *List direct cost attachments* endpoint returns a list of attachments available to download for given `directCostId`.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support listing direct cost attachments.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectCostAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='accusantium',
)

res = s.direct_costs.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListDirectCostAttachmentsRequest](../../models/operations/listdirectcostattachmentsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.ListDirectCostAttachmentsResponse](../../models/operations/listdirectcostattachmentsresponse.md)**


## upload_attachment

The *Upload direct cost attachment* endpoint uploads an attachment and assigns it against a specific `directCostId`.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

**Integration-specific behaviour**

For more details on supported file types by integration see [Attachments](https://docs.codat.io/accounting-api#/schemas/Attachment).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support uploading a direct cost attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadDirectCostAttachmentRequest(
    request_body=operations.UploadDirectCostAttachmentRequestBody(
        content='labore'.encode(),
        request_body='voluptatum',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='nisi',
)

res = s.direct_costs.upload_attachment(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UploadDirectCostAttachmentRequest](../../models/operations/uploaddirectcostattachmentrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[operations.UploadDirectCostAttachmentResponse](../../models/operations/uploaddirectcostattachmentresponse.md)**

