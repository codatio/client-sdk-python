# Expenses

## Overview

Create expense datasets and upload receipts.

### Available Operations

* [create](#create) - Create expense transaction
* [update](#update) - Update expense-transactions
* [upload_attachment](#upload_attachment) - Upload attachment

## create

Create an expense transaction

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared
from decimal import Decimal

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateExpenseTransactionRequest(
    create_expense_request=shared.CreateExpenseRequest(
        items=[
            shared.ExpenseTransaction(
                bank_account_ref=shared.ExpenseTransactionBankAccountReference(
                    id='787dfb37-5707-4dc0-8a86-8d74e4cc78ea',
                ),
                contact_ref=shared.ContactRef(
                    contact_type=shared.ContactRefContactType.SUPPLIER,
                    id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                ),
                currency='GBP',
                currency_rate=Decimal('9764.05'),
                id='4d7c6929-7770-412b-91bb-44d3bc71d111',
                issue_date='2022-10-23T00:00:00.000Z',
                lines=[
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=Decimal('110.42'),
                        tax_amount=Decimal('14.43'),
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                ],
                merchant_name='Amazon UK',
                notes='APPLE.COM/BILL - 09001077498 - Card Ending: 4590',
                type=shared.ExpenseTransactionType.PAYMENT,
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.expenses.create(req)

if res.create_expense_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateExpenseTransactionRequest](../../models/operations/createexpensetransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |


### Response

**[operations.CreateExpenseTransactionResponse](../../models/operations/createexpensetransactionresponse.md)**


## update

Update an expense transaction

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared
from decimal import Decimal

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateExpenseTransactionRequest(
    update_expense_request=shared.UpdateExpenseRequest(
        bank_account_ref=shared.UpdateExpenseRequestBankAccountReference(
            id='787dfb37-5707-4dc0-8a86-8d74e4cc78ea',
        ),
        contact_ref=shared.ContactRef(
            contact_type=shared.ContactRefContactType.SUPPLIER,
            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
        ),
        currency='GBP',
        currency_rate=Decimal('6176.58'),
        issue_date='2022-06-28T00:00:00.000Z',
        lines=[
            shared.ExpenseTransactionLine(
                account_ref=shared.RecordRef(
                    id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                ),
                net_amount=Decimal('110.42'),
                tax_amount=Decimal('14.43'),
                tax_rate_ref=shared.RecordRef(
                    id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                ),
                tracking_refs=[
                    shared.RecordRef(
                        id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                    ),
                ],
            ),
        ],
        merchant_name='Amazon UK',
        notes='APPLE.COM/BILL - 09001077498 - Card Ending: 4590',
        type='eos',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    transaction_id='336694d8-2dca-4cb5-a28d-3ccb83e55eee',
)

res = s.expenses.update(req)

if res.update_expense_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateExpenseTransactionRequest](../../models/operations/updateexpensetransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |


### Response

**[operations.UpdateExpenseTransactionResponse](../../models/operations/updateexpensetransactionresponse.md)**


## upload_attachment

Creates an attachment in the accounting software against the given transactionId

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadExpenseAttachmentRequest(
    request_body=operations.UploadExpenseAttachmentRequestBody(
        content='atque'.encode(),
        request_body='sit',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002',
    transaction_id='336694d8-2dca-4cb5-a28d-3ccb83e55eee',
)

res = s.expenses.upload_attachment(req)

if res.attachment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UploadExpenseAttachmentRequest](../../models/operations/uploadexpenseattachmentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.UploadExpenseAttachmentResponse](../../models/operations/uploadexpenseattachmentresponse.md)**

