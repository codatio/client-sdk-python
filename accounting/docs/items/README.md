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
                id='3cf6c027-6e7b-421b-ad90-d2743fd6c2a1',
                name='Gwen Jast',
            ),
            description='natus',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=4616.76,
                id='8ec256a5-b092-427f-8c47-996c977bbc57',
                name='Sean Lakin',
            ),
            unit_price=5542.89,
        ),
        code='est',
        id='8600c58d-67d6-43e4-aa56-8464579cfc6c',
        invoice_item=shared.InvoiceItem(
            account_ref=shared.AccountRef(
                id='0e503f56-831f-41d8-ad87-b28e8afabc98',
                name='Jana Cruickshank DVM',
            ),
            description='magnam',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=2124.42,
                id='b2342417-d13e-43f6-aaa9-ae4ae8ab4a9c',
                name='Becky Crona',
            ),
            unit_price=9000.58,
        ),
        is_bill_item=False,
        is_invoice_item=False,
        item_status=shared.ItemStatus.ACTIVE,
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='quidem',
        name='Dan Skiles',
        source_modified_date='culpa',
        type=shared.ItemType.INVENTORY,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=631429,
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
    item_id='veniam',
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
    query='sit',
)

res = s.items.list(req)

if res.items is not None:
    # handle response
```
