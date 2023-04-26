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
                id="5472cdd1-4fc4-43b7-8bca-88fa70c43351",
                name="Luis Swaniawski PhD",
            ),
            description="harum",
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=5331.06,
                id="f7f75f4f-23f1-4c0a-986c-3ae7d7b67fee",
                name="Mrs. Floyd Torphy",
            ),
            unit_price=8642.28,
        ),
        code="perspiciatis",
        id="5b1dbece-ff7c-44b1-96e9-278275eea768",
        invoice_item=shared.InvoiceItem(
            account_ref=shared.AccountRef(
                id="17468063-f799-4b79-96c0-b0fa0bb20a40",
                name="Roland Ryan",
            ),
            description="accusamus",
            tax_rate_ref=shared.TaxRateRef(
                effective_tax_rate=3996.96,
                id="40642726-57b0-41a0-bc08-fd3921c25793",
                name="Mercedes Kemmer V",
            ),
            unit_price=2095.62,
        ),
        is_bill_item=False,
        is_invoice_item=False,
        item_status="Active",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="sequi",
        name="Dominick Pagac",
        source_modified_date="temporibus",
        type="adipisci",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=420757,
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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    item_id="ea",
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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="nulla",
)

res = s.items.list(req)

if res.items is not None:
    # handle response
```
