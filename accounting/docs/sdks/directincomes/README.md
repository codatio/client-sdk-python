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
            data_type='totam',
            id='9c8a3263-9da5-4b7b-a902-b881a94f6436',
        ),
        currency='USD',
        currency_rate=2725.62,
        id='a8f0af8c-691d-4732-99fb-af9476a2ae8d',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='50c8a351-2c73-4784-8930-750a00e966ec',
                    name='Florence Keeling',
                ),
                description='neque',
                discount_amount=816.89,
                discount_percentage=6064.72,
                item_ref=shared.ItemRef(
                    id='4398c783-c923-498e-93d3-ab7ca3c5ca86',
                    name='Isabel Okuneva DDS',
                ),
                quantity=9687.73,
                sub_total=8458.89,
                tax_amount=3297,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8638.28,
                    id='6989b720-6451-4077-919e-a83d492ed14b',
                    name='Blake Connelly V',
                ),
                total_amount=3475.83,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='545e955d-cc18-45ea-8901-c7c43ad2daa7',
                        name='Troy Murphy',
                    ),
                    shared.TrackingCategoryRef(
                        id='3d230edf-7381-41a1-9538-2bd7ed565076',
                        name='Christine Sauer',
                    ),
                ],
                unit_amount=9851.55,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='4d739656-4c20-4a07-91a9-61d24a7dbb8f',
                    name='Shannon Cremin',
                ),
                description='perspiciatis',
                discount_amount=1421.56,
                discount_percentage=7540.53,
                item_ref=shared.ItemRef(
                    id='f7812cb5-12c8-4782-80bf-548f88f8f1bf',
                    name='Hannah Schmidt',
                ),
                quantity=1202.57,
                sub_total=9822.77,
                tax_amount=1756.76,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=195.51,
                    id='6d5d831d-0081-4090-b670-6673f3a681c5',
                    name='Vera Kutch',
                ),
                total_amount=9328.07,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='42409a21-5e08-4601-889a-5f63e3af3dd9',
                        name='Marty Nikolaus',
                    ),
                    shared.TrackingCategoryRef(
                        id='dcd63483-e4a7-4a98-a4df-37e45b8955d4',
                        name='Mrs. Tracy Walker',
                    ),
                ],
                unit_amount=2578.35,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='82310907-bd35-44c0-92bd-734f02449d86',
                    name='Edwin Rath',
                ),
                description='eaque',
                discount_amount=9915.63,
                discount_percentage=8906.06,
                item_ref=shared.ItemRef(
                    id='5d911cbf-e749-4caf-85a2-7f69e2c9e6d1',
                    name='Henrietta Moen',
                ),
                quantity=2060.11,
                sub_total=6648.58,
                tax_amount=8344.57,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2719.56,
                    id='c6b03108-d9c3-4374-b308-2b94f2ab1fd5',
                    name='Glenda Boehm',
                ),
                total_amount=7725.66,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='26350a46-7143-4789-8e0e-991594d93a74',
                        name='Jeffrey Dare',
                    ),
                ],
                unit_amount=9545.42,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='e3b4b4db-8b77-48eb-b6e1-d2cf502bafb2',
                    name='Archie Schroeder',
                ),
                description='adipisci',
                discount_amount=3732.03,
                discount_percentage=8526.23,
                item_ref=shared.ItemRef(
                    id='5e65da02-8c3e-4951-a1e3-0fda966489d7',
                    name='Darryl Kuvalis',
                ),
                quantity=2412.36,
                sub_total=8992.58,
                tax_amount=844.51,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2323.42,
                    id='a12a6b99-2494-4594-887f-5c843836b86b',
                    name='Adrienne Stokes',
                ),
                total_amount=2950.58,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5b0449f9-df13-4f4e-adbe-78bf60682589',
                        name='Kelley Nader',
                    ),
                ],
                unit_amount=2274.52,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='corporis',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=4549.34,
                    total_amount=5910.92,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='5b785148-d6d5-449e-9635-b33bc0f970c4',
                        name='Shari Schmeler',
                    ),
                    currency='GBP',
                    currency_rate=5170.23,
                    id='44225e75-b796-4065-80ef-a6f93b90a1b8',
                    note='eligendi',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='veniam',
                    total_amount=7243.07,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=1317.05,
                    total_amount=3572.56,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='4b739f4f-e772-410d-9f65-58c99c722d2b',
                        name='Steven Weimann',
                    ),
                    currency='GBP',
                    currency_rate=5286.46,
                    id='7d9caae0-42dd-47ca-ac9b-4caa1cfe9e15',
                    note='nulla',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='molestias',
                    total_amount=576.67,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=455.46,
                    total_amount=4952.25,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='f3783198-3d42-4e54-a854-66597c50233c',
                        name='Dr. Pauline Koss',
                    ),
                    currency='GBP',
                    currency_rate=6798.99,
                    id='aa6ddf5a-bd64-487c-9fc2-b862a00bef69',
                    note='saepe',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='aperiam',
                    total_amount=617.28,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=4998.83,
                    total_amount=3808.84,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='30bda7af-ded8-44a3-9a41-238e1a735ac2',
                        name='Kristi Turcotte',
                    ),
                    currency='EUR',
                    currency_rate=9305.47,
                    id='f971a8f4-6bca-4110-afe9-65b711d08cf8',
                    note='deleniti',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='cumque',
                    total_amount=6116.3,
                ),
            ),
        ],
        reference='reiciendis',
        source_modified_date='2022-10-23T00:00:00.000Z',
        sub_total=7293.47,
        supplemental_data=shared.SupplementalData(
            content={
                "occaecati": {
                    "nemo": 'quis',
                    "doloremque": 'similique',
                    "eum": 'quis',
                },
                "commodi": {
                    "possimus": 'dolor',
                    "ratione": 'velit',
                    "soluta": 'cum',
                    "accusantium": 'quo',
                },
                "officiis": {
                    "est": 'fuga',
                    "autem": 'quis',
                    "modi": 'consectetur',
                },
            },
        ),
        tax_amount=1844.01,
        total_amount=6424.34,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=585645,
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
    direct_income_id='rem',
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
    direct_income_id='ea',
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
    direct_income_id='debitis',
    timeout_in_minutes=743023,
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
    query='odio',
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
    direct_income_id='eveniet',
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
        content='beatae'.encode(),
        request_body='dolore',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='quisquam',
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

