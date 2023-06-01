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
            id='c8745005-e9d3-4d93-8e03-6f5c388664f6',
        ),
        date_='error',
        deposited_record_refs=[
            shared.InvoiceTo(
                data_type='corporis',
                id='530a2e2a-ed6a-4af8-a3c2-8d040c69a3d9',
            ),
            shared.InvoiceTo(
                data_type='voluptatem',
                id='6f6ebd5a-d7ec-4739-8f25-f634b3730714',
            ),
            shared.InvoiceTo(
                data_type='itaque',
                id='6be8c3e0-9c64-4d34-aac2-99a6e5e7aef1',
            ),
        ],
        description='amet',
        from_=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='402e945f-5374-43ef-9e11-98221f9b1f7d',
                name='Gerard Weimann',
            ),
            amount=4322.15,
            currency='omnis',
        ),
        id='682aceef-b04f-48c5-92ca-abea708ed579',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='rem',
        source_modified_date='facere',
        supplemental_data=shared.SupplementalData(
            content={
                "quas": {
                    "illum": 'labore',
                    "ea": 'aperiam',
                },
            },
        ),
        to=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='599d5c33-4957-46d5-9209-e9a2253b6d76',
                name='Irma Larkin',
            ),
            amount=9345.12,
            currency='similique',
        ),
        tracking_category_refs=[
            shared.TrackingCategoryRef(
                id='5fd4b39f-8a14-4906-b8f1-3c686d839fc9',
                name='Joshua Koelpin',
            ),
            shared.TrackingCategoryRef(
                id='fa906ae5-59b7-42eb-a746-030fe18376c2',
                name='Merle Strosin',
            ),
            shared.TrackingCategoryRef(
                id='76790ed0-c16a-47ba-8784-04489f6770ef',
                name='Ms. Suzanne Lang MD',
            ),
            shared.TrackingCategoryRef(
                id='2ba25ee6-c75a-4f8a-a0a7-ae346e0979e5',
                name='Timmy Trantow V',
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
    transfer_id='impedit',
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
    query='culpa',
)

res = s.transfers.list(req)

if res.transfers is not None:
    # handle response
```
