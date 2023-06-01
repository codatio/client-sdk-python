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
        transactions=[
            shared.BankTransactionLine(
                amount=7151.9,
                balance=8442.66,
                cleared_on_date='unde',
                counterparty='nulla',
                description='corrupti',
                id='d69a674e-0f46-47cc-8796-ed151a05dfc2',
                modified_date='at',
                reconciled=False,
                reference='at',
                source_modified_date='maiores',
                transaction_type=shared.BankTransactionType.ATM,
            ),
            shared.BankTransactionLine(
                amount=7991.59,
                balance=8009.11,
                cleared_on_date='esse',
                counterparty='totam',
                description='porro',
                id='a1ba928f-c816-4742-8b73-9205929396fe',
                modified_date='fuga',
                reconciled=False,
                reference='in',
                source_modified_date='corporis',
                transaction_type=shared.BankTransactionType.CHECK,
            ),
            shared.BankTransactionLine(
                amount=4370.32,
                balance=9023.49,
                cleared_on_date='quidem',
                counterparty='architecto',
                description='ipsa',
                id='faaa2352-c595-4590-baff-1a3a2fa94677',
                modified_date='velit',
                reconciled=False,
                reference='error',
                source_modified_date='quia',
                transaction_type=shared.BankTransactionType.SER_CHG,
            ),
        ],
    ),
    account_id='vitae',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=674752,
)

res = s.create(req)

if res.create_bank_transactions_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->