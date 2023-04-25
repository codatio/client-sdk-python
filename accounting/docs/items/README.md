# items

## Overview

Items

### Available Operations

* [create_item](#create_item) - Create item
* [get_create_items_model](#get_create_items_model) - Get create item model
* [get_item](#get_item) - Get item
* [list_items](#list_items) - List items

## create_item

Posts a new item to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create item model](https://docs.codat.io/accounting-api#/operations/get-create-items-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) for integrations that support creating items.

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
                id="8afabc98-6e24-41e4-bb23-42417d13e3f6",
                name="Hattie Nienow",
            ),
            description="recusandae",
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=2889.02,
                id="ae8ab4a9-c492-4c5e-8ba5-d4aa4a508bd3",
                name="Jose Rowe",
            ),
            unit_price=6567.81,
        ),
        code="deserunt",
        id="8dd71bdd-aa30-4b7b-9144-9ae69c088d41",
        invoice_item=shared.InvoiceItem(
            account_ref=shared.AccountRef(
                id="8bb71804-f423-4d54-b935-f377ac5c9b7e",
                name="Lee Reichert",
            ),
            description="sequi",
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=7621.04,
                id="523105e7-c34c-4ab0-acb8-12a66148944a",
                name="Ms. Clay Mayer",
            ),
            unit_price=106.86,
        ),
        is_bill_item=False,
        is_invoice_item=False,
        item_status="Active",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="exercitationem",
        name="Sylvester Davis",
        source_modified_date="praesentium",
        type="sed",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=346632,
)

res = s.items.create_item(req)

if res.create_item_response is not None:
    # handle response
```

## get_create_items_model

Get create item model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=items) for integrations that support creating items.

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.items.get_create_items_model(req)

if res.push_option is not None:
    # handle response
```

## get_item

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    item_id="ratione",
)

res = s.items.get_item(req)

if res.item is not None:
    # handle response
```

## list_items

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="nesciunt",
)

res = s.items.list_items(req)

if res.items is not None:
    # handle response
```
