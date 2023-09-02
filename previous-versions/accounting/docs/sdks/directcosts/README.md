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
            data_type='enim',
            id='2a5647ed-c439-4ed8-8432-0f41240d4487',
        ),
        currency='USD',
        currency_rate=7842.87,
        id='693b94c3-b9d2-4488-9795-aa42fc405669',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='9a006d21-2494-4508-99d7-c3b1b4184406',
                    name='Mr. Jenna Bashirian Jr.',
                ),
                description='possimus',
                discount_amount=168.83,
                discount_percentage=1861.03,
                item_ref=shared.ItemRef(
                    id='3dc901f5-afd2-4a6c-8484-6ae9d89253c8',
                    name='Angel Crooks',
                ),
                quantity=5528.22,
                sub_total=5683.23,
                tax_amount=4317.12,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6999.62,
                    id='f51e4652-d3c3-443d-a177-8af491247725',
                    name='Miss Leslie Cummings V',
                ),
                total_amount=8776.13,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='accountTransaction',
                        id='1044a5de-59ac-4770-a670-cf1cf5932605',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='invoice',
                            id='1e66bb42-6897-4d99-a2d3-35670e93ee6c',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='59f358aa-eaca-4e32-ba31-bf7ba1cc9771',
                        name='Mr. Kendra Leuschke',
                    ),
                    shared.TrackingCategoryRef(
                        id='c9e0c7d9-d323-4f1a-a63e-d9cf1c856bcb',
                        name='Jon Blick',
                    ),
                    shared.TrackingCategoryRef(
                        id='2454a47f-acf1-416c-9d54-44a7562873c7',
                        name='Irving Morissette',
                    ),
                    shared.TrackingCategoryRef(
                        id='af43dc62-3620-4f31-b8f3-0df3db022faa',
                        name='Lucy Heaney',
                    ),
                ],
                unit_amount=5240.51,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='f652ebb9-d383-4838-b902-43b293dab30e',
                    name='Samuel Kessler',
                ),
                description='alias',
                discount_amount=9923.82,
                discount_percentage=8438.75,
                item_ref=shared.ItemRef(
                    id='a04c8b1b-b55a-4292-b0bc-3bb744664eb1',
                    name='Donald Franey',
                ),
                quantity=5206.86,
                sub_total=7056.22,
                tax_amount=76.82,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8245.36,
                    id='1bb17afe-e74b-46fe-b945-7c7edaf39d16',
                    name='Jean Ziemann',
                ),
                total_amount=9408.65,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='transfer',
                        id='162b303e-3023-4b93-a343-16cf55b43135',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='journalEntry',
                            id='ccf1c204-c4ad-4cc9-904c-5195b8648cef',
                        ),
                        shared.InvoiceTo(
                            data_type='accountTransaction',
                            id='78f1e2d3-b901-4e09-92bb-b4cbb19f713d',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5a4169c1-3872-471e-98ea-9e45118c2cc5',
                        name='Essie Reinger',
                    ),
                    shared.TrackingCategoryRef(
                        id='0b1a78ed-29a9-4d4e-aa85-658c2d4f4c88',
                        name='Pat Grant',
                    ),
                    shared.TrackingCategoryRef(
                        id='78fd9667-e46c-451d-affa-a58dcef234c9',
                        name='Sally Renner',
                    ),
                ],
                unit_amount=8272.2,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='odit',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=6633.77,
                    total_amount=7477.85,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='d9bbcc27-25ec-4265-9ce0-280840c69ef6',
                        name='Pat Gleason',
                    ),
                    currency='USD',
                    currency_rate=6575.51,
                    id='ddfac754-5004-430c-a632-b4391fdf01c3',
                    note='itaque',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='beatae',
                    total_amount=9120.57,
                ),
            ),
        ],
        reference='quas',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=4517.27,
        supplemental_data=shared.SupplementalData(
            content={
                "quod": {
                    "error": 'at',
                    "incidunt": 'autem',
                },
                "alias": {
                    "iusto": 'dignissimos',
                    "debitis": 'quo',
                    "saepe": 'tempore',
                },
                "sunt": {
                    "nulla": 'architecto',
                    "accusantium": 'a',
                },
            },
        ),
        tax_amount=923.49,
        total_amount=9186.1,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=966221,
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
    direct_cost_id='qui',
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
    direct_cost_id='laboriosam',
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
    direct_cost_id='neque',
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
    query='ab',
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
    direct_cost_id='quisquam',
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
        content='nihil'.encode(),
        request_body='quisquam',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='aperiam',
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

