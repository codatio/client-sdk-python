# items

## Overview

Items

### Available Operations

* [create](#create) - Create item
* [get](#get) - Get item
* [get_create_model](#get_create_model) - Get create item model
* [list](#list) - List items

## create

Posts a new item to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create item model](https://docs.codat.io/accounting-api#/operations/get-create-items-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) to see which integrations support this endpoint.

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
                id='d64161e9-1500-4323-b2c0-9b924771f566',
                name='Pat Hickle',
            ),
            description='saepe',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=7828.51,
                id='7626649d-84eb-49e4-8fd2-276e0b88fb87',
                name='Gilbert Zboncak',
            ),
            unit_price=7370.08,
        ),
        code='vel',
        id='e8dbf812-f83b-41ca-aa9f-fc561929cca9',
        invoice_item=shared.InvoiceItem(
            account_ref=shared.AccountRef(
                id='560a1395-918d-4a1d-88e7-8e3cf8e1143d',
                name='Ms. Wendell Dooley',
            ),
            description='magni',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=4682.52,
                id='a08af221-8443-49b3-9e87-56ccce470cd2',
                name='Elaine Kihn',
            ),
            unit_price=9267.48,
        ),
        is_bill_item=False,
        is_invoice_item=False,
        item_status=shared.ItemStatus.ACTIVE,
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        name='Nicole Schowalter Sr.',
        source_modified_date='2022-10-23T00:00:00.000Z',
        type=shared.ItemType.UNKNOWN,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=873982,
)

res = s.items.create(req)

if res.create_item_response is not None:
    # handle response
```

## get

Gets the specified item for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetItemRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    item_id='voluptatum',
)

res = s.items.get(req)

if res.item is not None:
    # handle response
```

## get_create_model

Get create item model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) for integrations that support creating items.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

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

## list

Gets the items for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

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
    query='eligendi',
)

res = s.items.list(req)

if res.items is not None:
    # handle response
```
