# Expenses
(*expenses*)

## Overview

Create expense datasets and upload receipts.

### Available Operations

* [create_expense_dataset](#create_expense_dataset) - Create expense-transactions
* [update_expense_dataset](#update_expense_dataset) - Update expense transactions
* [upload_attachment](#upload_attachment) - Upload attachment

## create_expense_dataset

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

req = operations.CreateExpenseDatasetRequest(
    create_expense_request=shared.CreateExpenseRequest(
        items=[
            shared.ExpenseTransaction(
                contact_ref=shared.ContactRef(
                    contact_type=shared.ContactRefContactType.SUPPLIER,
                    id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                ),
                currency='GBP',
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

res = s.expenses.create_expense_dataset(req)

if res.create_expense_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateExpenseDatasetRequest](../../models/operations/createexpensedatasetrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.CreateExpenseDatasetResponse](../../models/operations/createexpensedatasetresponse.md)**


## update_expense_dataset

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

req = operations.UpdateExpenseDatasetRequest(
    update_expense_request=shared.UpdateExpenseRequest(
        contact_ref=shared.ContactRef(
            contact_type=shared.ContactRefContactType.SUPPLIER,
            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
        ),
        currency='GBP',
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
        type='Technetium',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    transaction_id='336694d8-2dca-4cb5-a28d-3ccb83e55eee',
)

res = s.expenses.update_expense_dataset(req)

if res.update_expense_dataset_202_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateExpenseDatasetRequest](../../models/operations/updateexpensedatasetrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.UpdateExpenseDatasetResponse](../../models/operations/updateexpensedatasetresponse.md)**


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

req = operations.UploadAttachmentRequest(
    request_body=operations.UploadAttachmentRequestBody(
        content='v/ghW&IC$x'.encode(),
        request_body='Elegant Producer Electric',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002',
    transaction_id='336694d8-2dca-4cb5-a28d-3ccb83e55eee',
)

res = s.expenses.upload_attachment(req)

if res.attachment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UploadAttachmentRequest](../../models/operations/uploadattachmentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.UploadAttachmentResponse](../../models/operations/uploadattachmentresponse.md)**

