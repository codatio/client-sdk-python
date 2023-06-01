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
                id='e8ab4a9c-492c-45e8-ba5d-4aa4a508bd38',
                name='Kara Cremin',
            ),
            description='deserunt',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=5230.55,
                id='dd71bdda-a30b-47b9-9449-ae69c088d418',
                name='Ms. Wm Kohler II',
            ),
            unit_price=9965.22,
        ),
        code='modi',
        id='23d54393-5f37-47ac-9c9b-7e93b6a3c523',
        invoice_item=shared.InvoiceItem(
            account_ref=shared.AccountRef(
                id='105e7c34-cab0-4ecb-812a-66148944a8e9',
                name='Ms. Jennie Hartmann',
            ),
            description='nam',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=7904.63,
                id='25382533-43fb-40a4-a66e-a47578d171e2',
                name='Frederick Bogan IV',
            ),
            unit_price=9823.15,
        ),
        is_bill_item=False,
        is_invoice_item=False,
        item_status=shared.ItemStatus.ARCHIVED,
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='aliquid',
        name='Shelly Purdy',
        source_modified_date='quia',
        type=shared.ItemType.SERVICE,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=125551,
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
    query='dolorem',
)

res = s.items.list(req)

if res.items is not None:
    # handle response
```
