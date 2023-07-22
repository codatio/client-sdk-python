# transfers

## Overview

Transfers

### Available Operations

* [create](#create) - Create transfer
* [get](#get) - Get transfer
* [get_create_model](#get_create_model) - Get create transfer model
* [list](#list) - List transfers

## create

The *Create transfer* endpoint creates a new [transfer](https://docs.codat.io/accounting-api#/schemas/Transfer) for a given company's connection.

[Transfers](https://docs.codat.io/accounting-api#/schemas/Transfer) record the movement of money between two bank accounts, or between a bank account and a nominal account.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create transfer model](https://docs.codat.io/accounting-api#/operations/get-create-transfers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateTransferRequest(
    transfer=shared.Transfer(
        contact_ref=shared.TransferContactRef(
            data_type='magni',
            id='b46097ef-a44a-48df-b40c-dd1850bf5a0c',
        ),
        date_='2022-10-23T00:00:00.000Z',
        deposited_record_refs=[
            shared.InvoiceTo(
                data_type='accountTransaction',
                id='b7860afe-a6c6-4351-b2d5-3086c10a856a',
            ),
            shared.InvoiceTo(
                data_type='journalEntry',
                id='9d4665ba-9725-4987-9dc0-cecbc78bd248',
            ),
            shared.InvoiceTo(
                data_type='transfer',
                id='c6e8b240-b1c0-46c9-8064-9d2bdd9e58dd',
            ),
            shared.InvoiceTo(
                data_type='accountTransaction',
                id='1665c312-c7f5-450d-8721-c176292dd787',
            ),
        ],
        description='blanditiis',
        from_=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='e71bf8c1-4184-41fe-9f87-ea103a9806ea',
                name='Tonya Beier',
            ),
            amount=5840.2,
            currency='USD',
        ),
        id='ef17b817-58d4-4ab5-bc80-dea77fd9931e',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "quasi": {
                    "aliquid": 'impedit',
                },
                "tenetur": {
                    "magni": 'quisquam',
                    "dolores": 'aliquid',
                    "culpa": 'distinctio',
                    "corrupti": 'dolore',
                },
                "doloremque": {
                    "quia": 'totam',
                    "repudiandae": 'id',
                    "aperiam": 'commodi',
                },
                "ducimus": {
                    "quibusdam": 'autem',
                },
            },
        ),
        to=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='b73a34ca-434c-4db3-949a-19f252078a18',
                name='Dr. Oscar Renner',
            ),
            amount=8886.44,
            currency='EUR',
        ),
        tracking_category_refs=[
            shared.TrackingCategoryRef(
                id='b5cf0616-ee92-4275-b5bd-60daa0e149cd',
                name='Sadie Schmitt',
            ),
            shared.TrackingCategoryRef(
                id='362bbf92-3900-415f-a689-9cf4ffeb9bec',
                name='Ms. Sarah Douglas',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.transfers.create(req)

if res.create_transfer_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateTransferRequest](../../models/operations/createtransferrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.CreateTransferResponse](../../models/operations/createtransferresponse.md)**


## get

The *Get transfer* endpoint returns a single transfer for a given transferId.

[Transfers](https://docs.codat.io/accounting-api#/schemas/Transfer) record the movement of money between two bank accounts, or between a bank account and a nominal account.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support getting a specific transfer.

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

req = operations.GetTransferRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    transfer_id='voluptatum',
)

res = s.transfers.get(req)

if res.transfer is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetTransferRequest](../../models/operations/gettransferrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.GetTransferResponse](../../models/operations/gettransferresponse.md)**


## get_create_model

The *Get create transfer model* endpoint returns the expected data for the request payload when creating a [transfer](https://docs.codat.io/accounting-api#/schemas/Transfer) for a given company and integration.

[Transfers](https://docs.codat.io/accounting-api#/schemas/Transfer) record the movement of money between two bank accounts, or between a bank account and a nominal account.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating a transfer.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateTransfersModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.transfers.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetCreateTransfersModelRequest](../../models/operations/getcreatetransfersmodelrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.GetCreateTransfersModelResponse](../../models/operations/getcreatetransfersmodelresponse.md)**


## list

The *List transfers* endpoint returns a list of [transfers](https://docs.codat.io/accounting-api#/schemas/Transfer) for a given company's connection.

[Transfers](https://docs.codat.io/accounting-api#/schemas/Transfer) record the movement of money between two bank accounts, or between a bank account and a nominal account.

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

req = operations.ListTransfersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='vitae',
)

res = s.transfers.list(req)

if res.transfers is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListTransfersRequest](../../models/operations/listtransfersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.ListTransfersResponse](../../models/operations/listtransfersresponse.md)**

