# LoanWriteback.Transfers

### Available Operations

* [create](#create) - Create transfer
* [get_create_model](#get_create_model) - Get create transfer model

## create

The *Create transfer* endpoint creates a new [transfer](https://docs.codat.io/lending-api#/schemas/Transfer) for a given company's connection.

[Transfers](https://docs.codat.io/lending-api#/schemas/Transfer) record the movement of money between two bank accounts, or between a bank account and a nominal account.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create transfer model](https://docs.codat.io/lending-api#/operations/get-create-transfers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating an account.


### Example Usage

```python
import codatlending
from codatlending.models import operations, shared
from decimal import Decimal

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateTransferRequest(
    accounting_transfer=shared.AccountingTransfer(
        contact_ref=shared.AccountingTransferContactRef(
            data_type=shared.DataType.INVOICES,
            id='ac366c8d-d6b1-4442-9074-74778a7bd466',
        ),
        date_='2022-10-23T00:00:00.000Z',
        deposited_record_refs=[
            shared.RecordRef(
                data_type='journalEntry',
                id='8c10ab3c-dca4-4251-904e-523c7e0bc717',
            ),
        ],
        description='totam',
        from_=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='e4796f2a-70c6-4882-82aa-482562f222e9',
                name='Carl Koch',
            ),
            amount=Decimal('829.71'),
            currency='USD',
        ),
        id='cbe61e6b-7b95-4bc0-ab3c-20c4f3789fd8',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "a": {
                    "error": 'sint',
                },
            },
        ),
        to=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id='dd2efd12-1aa6-4f1e-a74b-db04f1575608',
                name='Rosemarie Jacobs',
            ),
            amount=Decimal('6802.7'),
            currency='GBP',
        ),
        tracking_category_refs=[
            shared.TrackingCategoryRef(
                id='9f1d1705-1339-4d08-886a-1840394c2607',
                name='Elisa Mosciski',
            ),
        ],
    ),
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=374323,
)

res = s.loan_writeback.transfers.create(req)

if res.accounting_create_transfer_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateTransferRequest](../../models/operations/createtransferrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.CreateTransferResponse](../../models/operations/createtransferresponse.md)**


## get_create_model

The *Get create transfer model* endpoint returns the expected data for the request payload when creating a [transfer](https://docs.codat.io/lending-api#/schemas/Transfer) for a given company and integration.

[Transfers](https://docs.codat.io/lending-api#/schemas/Transfer) record the movement of money between two bank accounts, or between a bank account and a nominal account.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating a transfer.


### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateTransfersModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.loan_writeback.transfers.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetCreateTransfersModelRequest](../../models/operations/getcreatetransfersmodelrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.GetCreateTransfersModelResponse](../../models/operations/getcreatetransfersmodelresponse.md)**

