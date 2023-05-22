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

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating transfers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateTransferRequest(
    transfer=shared.Transfer(
        contact_ref=shared.TransferContactRef(
            data_type='explicabo',
            id='1f06d4d1-7852-4d28-be1d-b01d6919f831',
        ),
        date_='nemo',
        deposited_record_refs=[
            shared.InvoiceTo(
                data_type='dolorem',
                id='a84ea7db-15c4-4c15-be6c-d097a675597e',
            ),
            shared.InvoiceTo(
                data_type='cumque',
                id='beb7982b-af9a-47da-ac29-b938e51a7e6e',
            ),
            shared.InvoiceTo(
                data_type='nulla',
                id='6f7ff04f-da04-4669-aae8-182403655aa9',
            ),
        ],
        description='consequuntur',
        from_=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='3c49919e-bd1c-4f77-9538-cbbfcdf4ece9',
                name='Jodi Schamberger',
            ),
            amount=7140.11,
            currency='modi',
        ),
        id='2c330496-17cb-471d-9c25-0b60c751d2ae',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='expedita',
        source_modified_date='necessitatibus',
        supplemental_data=shared.SupplementalData(
            content={
                "tempore": {
                    "rem": 'consequuntur',
                    "molestias": 'officiis',
                    "qui": 'vel',
                },
                "aliquam": {
                    "ab": 'dolorum',
                    "veniam": 'officiis',
                },
                "minus": {
                    "corrupti": 'reprehenderit',
                    "a": 'quam',
                    "cupiditate": 'incidunt',
                },
            },
        ),
        to=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='f04f4144-6f79-43d3-b100-20147cd1b831',
                name='Amy Price',
            ),
            amount=2218.09,
            currency='voluptates',
        ),
        tracking_category_refs=[
            shared.TrackingCategoryRef(
                id='8960a0aa-fc7a-4867-8ba5-00a8f4cb72ed',
                name='Kara Wilderman',
            ),
            shared.TrackingCategoryRef(
                id='25d55615-8803-4212-b7b5-9b7154642b9e',
                name='Stella Schroeder',
            ),
            shared.TrackingCategoryRef(
                id='c3d3ca49-1837-4978-88d1-56f01ae36bb8',
                name='Jose Adams',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetTransferRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    transfer_id='eveniet',
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
        auth_header="YOUR_API_KEY_HERE",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListTransfersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='ratione',
)

res = s.transfers.list(req)

if res.transfers is not None:
    # handle response
```
