# items

## Overview

Items

### Available Operations

* [create](#create) - Create item
* [get](#get) - Get item
* [get_create_model](#get_create_model) - Get create item model
* [list](#list) - List items

## create

The *Create item* endpoint creates a new [item](https://docs.codat.io/accounting-api#/schemas/Item) for a given company's connection.

[Items](https://docs.codat.io/accounting-api#/schemas/Item) allow your customers to save and track details of the products and services that they buy and sell.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create item model](https://docs.codat.io/accounting-api#/operations/get-create-items-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateItemRequest(
    item=shared.Item(
        bill_item=shared.BillItem(
            account_ref=shared.AccountRef(
                id='b7a73df4-0ca0-4d76-97c1-641bbf055271',
                name='Mr. Alan Haley',
            ),
            description='assumenda',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=3834.21,
                id='06dd1b28-272b-4c9c-b221-697b1880fcbb',
                name='Verna Marks',
            ),
            unit_price=702.82,
        ),
        code='nostrum',
        id='f670bd17-8483-4165-beeb-3b6e241c3109',
        invoice_item=shared.InvoiceItem(
            account_ref=shared.AccountRef(
                id='983663c6-6dcb-4b7d-b6cb-09c8b408e071',
                name='Minnie Kirlin',
            ),
            description='saepe',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=2505.06,
                id='fee101d9-780a-410c-87b9-5040d6c8b2a5',
                name='John Aufderhar',
            ),
            unit_price=249.94,
        ),
        is_bill_item=False,
        is_invoice_item=False,
        item_status=shared.ItemStatus.ACTIVE,
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        name='Brenda Greenholt',
        source_modified_date='2022-10-23T00:00:00.000Z',
        type=shared.ItemType.UNKNOWN,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=4409,
)

res = s.items.create(req)

if res.create_item_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.CreateItemRequest](../../models/operations/createitemrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.CreateItemResponse](../../models/operations/createitemresponse.md)**


## get

The *Get item* endpoint returns a single item for a given itemId.

[Items](https://docs.codat.io/accounting-api#/schemas/Item) allow your customers to save and track details of the products and services that they buy and sell.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) for integrations that support getting a specific item.

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

req = operations.GetItemRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    item_id='sit',
)

res = s.items.get(req)

if res.item is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetItemRequest](../../models/operations/getitemrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |


### Response

**[operations.GetItemResponse](../../models/operations/getitemresponse.md)**


## get_create_model

The *Get create item model* endpoint returns the expected data for the request payload when creating an [item](https://docs.codat.io/accounting-api#/schemas/Item) for a given company and integration.

[Items](https://docs.codat.io/accounting-api#/schemas/Item) allow your customers to save and track details of the products and services that they buy and sell.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) for integrations that support creating an item.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateItemsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.items.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetCreateItemsModelRequest](../../models/operations/getcreateitemsmodelrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.GetCreateItemsModelResponse](../../models/operations/getcreateitemsmodelresponse.md)**


## list

The *List items* endpoint returns a list of [items](https://docs.codat.io/accounting-api#/schemas/Item) for a given company's connection.

[Items](https://docs.codat.io/accounting-api#/schemas/Item) allow your customers to save and track details of the products and services that they buy and sell.

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

req = operations.ListItemsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='iste',
)

res = s.items.list(req)

if res.items is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListItemsRequest](../../models/operations/listitemsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |


### Response

**[operations.ListItemsResponse](../../models/operations/listitemsresponse.md)**

