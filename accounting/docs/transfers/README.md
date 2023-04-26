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
            data_type="laborum",
            id="9ffc5619-29cc-4a95-a0a1-395918da1d48",
        ),
        date_="recusandae",
        deposited_record_refs=[
            "quas",
            "officiis",
        ],
        description="ipsum",
        from_=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id="cf8e1143-da93-408b-a7a0-8af22184439b",
                name="Desiree Walsh",
            ),
            amount=3395.66,
            currency="eum",
        ),
        id="ccce470c-d214-47b6-a615-2cf01d0d8c3a",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="magnam",
        source_modified_date="facilis",
        supplemental_data=shared.SupplementalData(
            content={
                "laborum": {
                    "quidem": "repellat",
                    "molestias": "amet",
                },
                "veniam": {
                    "voluptatibus": "vero",
                    "provident": "iure",
                    "incidunt": "repellat",
                    "similique": "ut",
                },
                "tempore": {
                    "voluptates": "excepturi",
                },
            },
        ),
        to=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id="c097eda6-2344-42e1-a923-7e9984c80b47",
                name="Bert Lind V",
            ),
            amount=1752.16,
            currency="dolorem",
        ),
        tracking_category_refs=[
            shared.TrackingCategoryRef(
                id="18ca8d69-c568-4921-8fa2-0207e4fae038",
                name="Carroll Klocko DDS",
            ),
            shared.TrackingCategoryRef(
                id="c2cabaf7-fc2c-4cba-8bef-0df68eaedb2e",
                name="Darryl Altenwerth",
            ),
            shared.TrackingCategoryRef(
                id="069fb36a-dd70-4408-8e0a-3fc73a5a034b",
                name="Rebecca Graham",
            ),
            shared.TrackingCategoryRef(
                id="243afa69-87a4-472b-b09a-153e22301068",
                name="Tracy Monahan",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    transfer_id="ipsa",
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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="perspiciatis",
)

res = s.transfers.list(req)

if res.transfers is not None:
    # handle response
```
