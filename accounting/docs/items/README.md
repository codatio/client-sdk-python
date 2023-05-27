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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateItemRequest(
    item=shared.Item(
        bill_item=shared.BillItem(
            account_ref=shared.AccountRef(
                id='d9ca6075-656f-4c0e-be67-155e2d06a307',
                name='Janis Kautzer',
            ),
            description='natus',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=4461.28,
                id='f581faba-aa7d-4801-8880-76ff5f6ed298',
                name='Carrie Beer',
            ),
            unit_price=1272.71,
        ),
        code='aliquid',
        id='9b6a70b0-dd82-4f94-bffb-d1e1e21ddc69',
        invoice_item=shared.InvoiceItem(
            account_ref=shared.AccountRef(
                id='038b1d18-7b51-4eb5-bd30-bfe03490cf20',
                name='Annette Hackett',
            ),
            description='ad',
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=6012.27,
                id='043cb462-d6bc-4991-bf98-e4792b979a41',
                name='Eula Hudson',
            ),
            unit_price=7729.87,
        ),
        is_bill_item=False,
        is_invoice_item=False,
        item_status=shared.ItemStatus.ACTIVE,
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='vitae',
        name='Christy Douglas',
        source_modified_date='rem',
        type=shared.ItemType.INVENTORY,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=99209,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetItemRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    item_id='illum',
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
        auth_header="YOUR_API_KEY_HERE",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListItemsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='quae',
)

res = s.items.list(req)

if res.items is not None:
    # handle response
```
