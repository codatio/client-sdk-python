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

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

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
            data_type='ratione',
            id='f4eedbe7-8bf6-4068-a589-4ea763d5c727',
        ),
        currency='USD',
        currency_rate=3378.33,
        id='b785148d-6d54-49e5-a35b-33bc0f970c42',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='9f484422-5e75-4b79-a065-c0efa6f93b90',
                    name='Jack Rau',
                ),
                description='unde',
                discount_amount=3331.5,
                discount_percentage=7243.07,
                item_ref=shared.ItemRef(
                    id='e1254b73-9f4f-4e77-a10d-1f6558c99c72',
                    name='Mona Considine',
                ),
                quantity=349.2,
                sub_total=9387.73,
                tax_amount=5669.15,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2568.9,
                    id='087d9caa-e042-4dd7-8aac-9b4caa1cfe9e',
                    name='Joann Stokes',
                ),
                total_amount=576.67,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='amet',
                        id='907f3783-1983-4d42-a54a-85466597c502',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='nesciunt',
                            id='c1471d51-aaa6-4ddf-9abd-6487c5fc2b86',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a00bef69-e100-4157-a30b-da7afded84a3',
                        name='Mr. Sonya Gutmann',
                    ),
                ],
                unit_amount=5454,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='e1a735ac-26ae-433b-af97-1a8f46bca110',
                    name='Marta Torphy',
                ),
                description='ipsam',
                discount_amount=7436.31,
                discount_percentage=4565.91,
                item_ref=shared.ItemRef(
                    id='11d08cf8-8ec9-4f7b-99a5-50a656ed333b',
                    name='Edward Sanford',
                ),
                quantity=6679.43,
                sub_total=6847.08,
                tax_amount=4224.44,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3351.76,
                    id='432a986e-b7e1-44ca-9640-89150097019a',
                    name='Gwendolyn Wintheiser',
                ),
                total_amount=9368.8,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='impedit',
                        id='e7bf904e-0110-45d3-8908-162c6beb68a0',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='vel',
                            id='57b7d03a-1480-4f8d-a30f-069d810618d9',
                        ),
                        shared.InvoiceTo(
                            data_type='voluptate',
                            id='e1522975-10da-4803-9229-2cc61c2a702b',
                        ),
                        shared.InvoiceTo(
                            data_type='soluta',
                            id='97ee102d-a2de-435f-8e01-bf33eaab4540',
                        ),
                        shared.InvoiceTo(
                            data_type='dolores',
                            id='ac1704bf-1cc9-4fc6-9aae-5eb5f0c492b5',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='44d08a22-67aa-4ee7-9e3c-71ad31becb83',
                        name='Martin Fahey',
                    ),
                    shared.TrackingCategoryRef(
                        id='ae3bfc23-d945-40a9-86a4-95bac707f06b',
                        name='Myrtle Walker',
                    ),
                ],
                unit_amount=5431.22,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='6492386f-62c9-469c-8cc6-b78890a3fd3c',
                    name='Jerry Spinka Jr.',
                ),
                description='asperiores',
                discount_amount=5342.04,
                discount_percentage=7596.13,
                item_ref=shared.ItemRef(
                    id='23df931d-a3ed-4b51-bad9-4acc94351377',
                    name='Mrs. Eileen Spinka',
                ),
                quantity=1584.51,
                sub_total=1199.27,
                tax_amount=7214.48,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5545.08,
                    id='32a56d69-180f-4f60-ab9a-6658e69a4b84',
                    name='Desiree Fisher',
                ),
                total_amount=8447.03,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='harum',
                        id='ec75c68c-6065-4946-8ce3-04d8849bf821',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='eligendi',
                            id='337f96bb-0c69-4e37-adb1-344ba9f78a5c',
                        ),
                        shared.InvoiceTo(
                            data_type='accusantium',
                            id='ed7aab62-e972-461f-b0c5-8d27b51996b5',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='4b50eef7-12b7-4a7a-b034-4b1710688dee',
                        name='Santiago Zboncak',
                    ),
                    shared.TrackingCategoryRef(
                        id='7f3dd0cc-d33f-411b-be4e-080aa104186e',
                        name='Darren Herman',
                    ),
                    shared.TrackingCategoryRef(
                        id='02f3702c-5c8e-42d3-8ead-3104fa44707b',
                        name='Johnny Kunze',
                    ),
                ],
                unit_amount=2839.36,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='4282821f-db2f-469e-9926-7c71cc8d3cd4',
                    name='Dolores Lehner I',
                ),
                description='ipsam',
                discount_amount=5378.94,
                discount_percentage=6718.73,
                item_ref=shared.ItemRef(
                    id='82c808fe-2751-4a20-87c0-449e143f9619',
                    name='Bennie Kirlin',
                ),
                quantity=460.36,
                sub_total=8739.01,
                tax_amount=3575.89,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6731.58,
                    id='11fa436e-6259-4233-b95c-9d237397c785',
                    name='Jorge Stokes',
                ),
                total_amount=9792.55,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='quis',
                        id='00183feb-df67-46b7-a06d-ab750052a564',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='officiis',
                            id='dc439ed8-c432-40f4-9240-d4487ac693b9',
                        ),
                        shared.InvoiceTo(
                            data_type='quaerat',
                            id='c3b9d248-8d79-45aa-82fc-405669f69a00',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='d2124945-0819-4d7c-bb1b-41844060e003',
                        name='Mr. Angela Schuppe',
                    ),
                    shared.TrackingCategoryRef(
                        id='dc901f5a-fd2a-46c4-8846-ae9d89253c89',
                        name='Kathryn Windler',
                    ),
                ],
                unit_amount=5683.23,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='rerum',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=9102.24,
                    total_amount=2717.82,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='652d3c34-3d61-4778-af49-1247725e6219',
                        name='Violet Thiel Jr.',
                    ),
                    currency='GBP',
                    currency_rate=2893.22,
                    id='a5de59ac-7706-4670-8f1c-f5932605251e',
                    note='ex',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='harum',
                    total_amount=7414,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=3850.49,
                    total_amount=5336.81,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='97d99a2d-3356-470e-93ee-6cf59f358aae',
                        name='Devin Nienow',
                    ),
                    currency='GBP',
                    currency_rate=2083.1,
                    id='a31bf7ba-1cc9-4771-ac80-2cc9e0c7d9d3',
                    note='dolores',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='repellat',
                    total_amount=647.23,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=4209.27,
                    total_amount=1945.14,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='ed9cf1c8-56bc-4ba5-9ef2-454a47facf11',
                        name='Marianne Steuber',
                    ),
                    currency='GBP',
                    currency_rate=2914.14,
                    id='4a756287-3c7d-4d9e-baf4-3dc623620f31',
                    note='dolor',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='doloribus',
                    total_amount=2021.77,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=9458.52,
                    total_amount=1945.26,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='db022faa-565f-4b8f-a52e-bb9d38383879',
                        name='Beverly Green',
                    ),
                    currency='GBP',
                    currency_rate=6212.3,
                    id='3dab30e9-17f5-40fd-a04c-8b1bb55a292b',
                    note='aut',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='quo',
                    total_amount=2482.32,
                ),
            ),
        ],
        reference='libero',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=4850.26,
        supplemental_data=shared.SupplementalData(
            content={
                "aliquam": {
                    "nisi": 'labore',
                    "accusamus": 'cum',
                },
                "sunt": {
                    "voluptatem": 'non',
                    "ipsum": 'laudantium',
                    "totam": 'facilis',
                    "consequatur": 'assumenda',
                },
            },
        ),
        tax_amount=1042.64,
        total_amount=7272.56,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=697864,
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadDirectCostAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='architecto',
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectCostRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='in',
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectCostAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='fuga',
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
from codataccounting.models import operations

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
from codataccounting.models import operations

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
    query='tenetur',
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

The *List direct cost attachments* endpoint returns a list of attachments avialable to download for given `directCostId`.

[Direct costs](https://docs.codat.io/accounting-api#/schemas/DirectCost) are purchases of items that are paid off at the point of the purchase.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support listing direct cost attachments.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectCostAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='saepe',
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadDirectCostAttachmentRequest(
    request_body=operations.UploadDirectCostAttachmentRequestBody(
        content='eveniet'.encode(),
        request_body='reprehenderit',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='incidunt',
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

