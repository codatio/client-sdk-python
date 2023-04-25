# transfers

## Overview

Transfers

### Available Operations

* [create_transfer](#create_transfer) - Create transfer
* [get_create_transfers_model](#get_create_transfers_model) - Get create transfer model
* [get_transfer](#get_transfer) - Get transfer
* [list_transfers](#list_transfers) - List transfers

## create_transfer

Posts a new transfer to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create transfer model](https://docs.codat.io/accounting-api#/operations/get-create-transfers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating transfers.

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
            data_type="quisquam",
            id="b4bedef3-c127-4c39-8995-528250dcbbcd",
        ),
        date_="velit",
        deposited_record_refs=[
            "architecto",
            "magni",
            "dicta",
        ],
        description="tempore",
        from_=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id="88c1ee5e-7a06-4139-9cc8-fa0b7d176492",
                name="Flora Auer",
            ),
            amount=3249.63,
            currency="recusandae",
        ),
        id="6cb6ebab-e5e0-4b99-b3b1-358d6a87bb7a",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="voluptates",
        source_modified_date="minus",
        supplemental_data=shared.SupplementalData(
            content={
                "recusandae": {
                    "eum": "iste",
                    "at": "voluptate",
                },
                "alias": {
                    "expedita": "consequatur",
                    "suscipit": "cupiditate",
                    "occaecati": "sit",
                    "dignissimos": "maiores",
                },
                "provident": {
                    "omnis": "incidunt",
                    "incidunt": "vitae",
                    "incidunt": "nostrum",
                },
            },
        ),
        to=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id="2a9f01f3-442c-461b-a133-bacde532b652",
                name="Johanna Lang",
            ),
            amount=5511.24,
            currency="corporis",
        ),
        tracking_category_refs=[
            shared.TrackingCategoryRef(
                id="fe2859ce-3222-431f-a666-4c41d2fba5cb",
                name="Daniel Keeling",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.transfers.create_transfer(req)

if res.create_transfer_response is not None:
    # handle response
```

## get_create_transfers_model

Get create transfer model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating transfers.

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.transfers.get_create_transfers_model(req)

if res.push_option is not None:
    # handle response
```

## get_transfer

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    transfer_id="corrupti",
)

res = s.transfers.get_transfer(req)

if res.transfer is not None:
    # handle response
```

## list_transfers

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="at",
)

res = s.transfers.list_transfers(req)

if res.transfers is not None:
    # handle response
```
