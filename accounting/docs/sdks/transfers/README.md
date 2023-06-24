# transfers

## Overview

Transfers

### Available Operations

* [create](#create) - Create transfer
* [get](#get) - Get transfer
* [get_create_model](#get_create_model) - Get create transfer model
* [list](#list) - List transfers

## create

Posts a new transfer to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create transfer model](https://docs.codat.io/accounting-api#/operations/get-create-transfers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) to see which integrations support this endpoint.

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
            data_type='maiores',
            id='a2795836-7363-4da0-b909-6faeb8648073',
        ),
        date_='2022-10-23T00:00:00.000Z',
        deposited_record_refs=[
            shared.InvoiceTo(
                data_type='laudantium',
                id='f8b89d9c-a607-4565-afc0-ebe67155e2d0',
            ),
            shared.InvoiceTo(
                data_type='autem',
                id='a3070d6e-297f-4581-baba-aa7d80108807',
            ),
            shared.InvoiceTo(
                data_type='laboriosam',
                id='ff5f6ed2-9814-4088-a69b-6a70b0dd82f9',
            ),
            shared.InvoiceTo(
                data_type='numquam',
                id='fffbd1e1-e21d-4dc6-9038-b1d187b51eb5',
            ),
        ],
        description='doloribus',
        from_=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='d30bfe03-490c-4f20-a54a-959043cb462d',
                name='Karla Schimmel',
            ),
            amount=944.75,
            currency='USD',
        ),
        id='f98e4792-b979-4a41-bd6a-8c91683bd861',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "natus": {
                    "quod": 'quo',
                    "repellat": 'voluptatum',
                    "excepturi": 'illum',
                },
                "amet": {
                    "ex": 'quae',
                    "beatae": 'praesentium',
                    "commodi": 'vero',
                },
                "temporibus": {
                    "nisi": 'minus',
                    "eaque": 'consequatur',
                },
                "magni": {
                    "est": 'cumque',
                    "harum": 'dicta',
                    "nesciunt": 'dolorum',
                    "placeat": 'sed',
                },
            },
        ),
        to=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='4c8143b8-66c5-475a-9e26-68730be37b0e',
                name='Terrell Reichert',
            ),
            amount=5391.45,
            currency='EUR',
        ),
        tracking_category_refs=[
            shared.TrackingCategoryRef(
                id='c7e69b53-5105-4050-94dc-a105882484c3',
                name='Raquel Metz',
            ),
            shared.TrackingCategoryRef(
                id='892782d3-4e0b-48fc-8d59-f57b9f9820be',
                name='Ms. Heidi Lind',
            ),
            shared.TrackingCategoryRef(
                id='36c9e2f7-0344-4e00-b478-eb539483f748',
                name='Santiago Windler',
            ),
            shared.TrackingCategoryRef(
                id='b69d541b-4b39-43f3-9666-25bea32201de',
                name='Earl Kiehn',
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

Gets the specified transfer for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetTransferRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    transfer_id='voluptas',
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

Get create transfer model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating transfers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

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
from codataccounting.models import operations

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
    query='error',
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

