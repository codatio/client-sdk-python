<!-- Start SDK Example Usage -->
```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBankTransactionsRequest(
    bank_transactions=shared.BankTransactions(
        account_id='corrupti',
        amount=5928.45,
        balance=7151.9,
        cleared_on_date='quibusdam',
        description='unde',
        id='d8d69a67-4e0f-4467-8c87-96ed151a05df',
        modified_date='quo',
        reconciled=False,
        source_modified_date='odit',
        transaction_type=shared.BankTransactionType.DIRECT_DEBIT,
    ),
    account_id='at',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=978619,
)

res = s.bank_account_transactions.create(req)

if res.create_bank_transactions_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->