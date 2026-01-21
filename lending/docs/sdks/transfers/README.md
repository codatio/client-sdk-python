# LoanWriteback.Transfers

## Overview

### Available Operations

* [create](#create) - Create transfer
* [get_create_model](#get_create_model) - Get create transfer model

## create

The *Create transfer* endpoint creates a new [transfer](https://docs.codat.io/lending-api#/schemas/Transfer) for a given company's connection.

[Transfers](https://docs.codat.io/lending-api#/schemas/Transfer) record the movement of money between two bank accounts, or between a bank account and a nominal account.

**Integration-specific behavior**

Required data may vary by integration. To see what data to post, first call [Get create transfer model](https://docs.codat.io/lending-api#/operations/get-create-transfers-model).

### Example Usage

<!-- UsageSnippet language="python" operationID="create-transfer" method="post" path="/companies/{companyId}/connections/{connectionId}/push/transfers" -->
```python
from codat_lending import CodatLending
from codat_lending.models import operations, shared
from decimal import Decimal


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.transfers.create(request=operations.CreateTransferRequest(
        accounting_transfer=shared.AccountingTransfer(
            contact_ref=shared.ContactRef(
                data_type=shared.ContactRefDataType.CUSTOMERS,
                id="80000028-167239230944",
            ),
            date_="2023-01-26T11:51:18.104Z",
            description="test transfers push 20230126 12.08",
            from_=shared.TransferAccount(
                account_ref=shared.AccountingRecordRef(
                    data_type="bankAccounts",
                    id="80000028-1671794219",
                ),
                amount=Decimal("12"),
            ),
            metadata=shared.Metadata(
                is_deleted=True,
            ),
            status=shared.AccountingTransferStatus.UNKNOWN,
            to=shared.TransferAccount(
                account_ref=shared.AccountingRecordRef(
                    data_type="bankAccounts",
                    id="80000004-1671793811",
                ),
                amount=Decimal("12"),
            ),
            tracking_category_refs=[
                shared.TrackingCategoryRef(
                    id="80000001-1674553252",
                    name="Class 1",
                ),
            ],
        ),
        company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
        connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateTransferRequest](../../models/operations/createtransferrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[shared.AccountingCreateTransferResponse](../../models/shared/accountingcreatetransferresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_create_model

The *Get create transfer model* endpoint returns the expected data for the request payload when creating a [transfer](https://docs.codat.io/lending-api#/schemas/Transfer) for a given company and integration.

[Transfers](https://docs.codat.io/lending-api#/schemas/Transfer) record the movement of money between two bank accounts, or between a bank account and a nominal account.

**Integration-specific behavior**

See the *response examples* for integration-specific indicative models.


### Example Usage

<!-- UsageSnippet language="python" operationID="get-create-transfers-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/transfers" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.transfers.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetCreateTransfersModelRequest](../../models/operations/getcreatetransfersmodelrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[shared.PushOption](../../models/shared/pushoption.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |