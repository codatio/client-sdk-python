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
            data_type='magni',
            id='73caa911-8b38-4f1b-a1a3-31a54dc10294',
        ),
        date_='reiciendis',
        deposited_record_refs=[
            shared.InvoiceTo(
                data_type='eos',
                id='fed939ba-8f71-4e29-92c2-0ee1228ac3ad',
            ),
            shared.InvoiceTo(
                data_type='optio',
                id='647d240b-c11e-4a48-a824-ccc6a2f0f5b9',
            ),
            shared.InvoiceTo(
                data_type='quibusdam',
                id='3cb11a76-87d3-4100-a8e2-b9b0d746d2a7',
            ),
        ],
        description='quisquam',
        from_=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='7d1ea0e7-9fa9-4bbe-9f17-9f650b1e707e',
                name='Rochelle Grimes',
            ),
            amount=4097.14,
            currency='odio',
        ),
        id='13bacce0-72ab-4d61-918d-279c10c18516',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='doloribus',
        source_modified_date='repellendus',
        supplemental_data=shared.SupplementalData(
            content={
                "praesentium": {
                    "repudiandae": 'fugit',
                    "vel": 'fugit',
                    "ab": 'quia',
                },
                "esse": {
                    "ea": 'odit',
                },
            },
        ),
        to=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='8fa50396-2867-4e72-b3a6-5024b157f9bb',
                name='Delia Zulauf',
            ),
            amount=6278.1,
            currency='ad',
        ),
        tracking_category_refs=[
            shared.TrackingCategoryRef(
                id='871d99b6-61a7-4def-968b-6ccb2822b4a9',
                name='Roberto Abshire',
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
    transfer_id='magni',
)

res = s.transfers.get(req)

if res.transfer is not None:
    # handle response
```

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

## list

Gets the transfers for a given company.

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
    query='doloribus',
)

res = s.transfers.list(req)

if res.transfers is not None:
    # handle response
```
