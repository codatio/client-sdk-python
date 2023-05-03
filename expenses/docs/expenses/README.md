# expenses

## Overview

Create expense datasets and upload receipts.

### Available Operations

* [create_expense_dataset](#create_expense_dataset) - Create expense-transactions
* [upload_attachment](#upload_attachment) - Upload attachment

## create_expense_dataset

Create an expense transaction

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateExpenseDatasetRequest(
    create_expense_request=shared.CreateExpenseRequest(
        items=[
            shared.ExpenseTransaction(
                currency='GBP',
                currency_rate=5928.45,
                id='4d7c6929-7770-412b-91bb-44d3bc71d111',
                issue_date='distinctio',
                lines=[
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                ],
                merchant_name='Amazon UK',
                notes='APPLE.COM/BILL - 09001077498 - Card Ending: 4590',
                type=shared.ExpenseTransactionTypeEnum.PAYMENT,
            ),
            shared.ExpenseTransaction(
                currency='GBP',
                currency_rate=4236.55,
                id='4d7c6929-7770-412b-91bb-44d3bc71d111',
                issue_date='error',
                lines=[
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                ],
                merchant_name='Amazon UK',
                notes='APPLE.COM/BILL - 09001077498 - Card Ending: 4590',
                type=shared.ExpenseTransactionTypeEnum.PAYMENT,
            ),
            shared.ExpenseTransaction(
                currency='GBP',
                currency_rate=8917.73,
                id='4d7c6929-7770-412b-91bb-44d3bc71d111',
                issue_date='ipsa',
                lines=[
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        net_amount=110.42,
                        tax_amount=14.43,
                        tax_rate_ref=shared.RecordRef(
                            id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                        ),
                        tracking_refs=[
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                            shared.RecordRef(
                                id='40e3e57c-2322-4898-966c-ca41adfd23fd',
                            ),
                        ],
                    ),
                ],
                merchant_name='Amazon UK',
                notes='APPLE.COM/BILL - 09001077498 - Card Ending: 4590',
                type=shared.ExpenseTransactionTypeEnum.PAYMENT,
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.expenses.create_expense_dataset(req)

if res.create_expense_response is not None:
    # handle response
```

## upload_attachment

Creates an attachment in the accounting software against the given transactionId

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadAttachmentRequest(
    request_body=operations.UploadAttachmentRequestBody(
        content='placeat'.encode(),
        request_body='voluptatum',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002',
    transaction_id='336694d8-2dca-4cb5-a28d-3ccb83e55eee',
)

res = s.expenses.upload_attachment(req)

if res.attachment is not None:
    # handle response
```
