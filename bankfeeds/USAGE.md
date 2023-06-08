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
    create_bank_transactions=shared.CreateBankTransactions(
        account_id='corrupti',
        transactions=[
            shared.CreateBankAccountTransaction(
                amount=7151.9,
                date_='2022-10-23T00:00:00.000Z',
                description='unde',
                id='d8d69a67-4e0f-4467-8c87-96ed151a05df',
            ),
            shared.CreateBankAccountTransaction(
                amount=7781.57,
                date_='2022-10-23T00:00:00.000Z',
                description='at',
                id='df7cc78c-a1ba-4928-bc81-6742cb739205',
            ),
            shared.CreateBankAccountTransaction(
                amount=6176.36,
                date_='2022-10-23T00:00:00.000Z',
                description='iste',
                id='396fea75-96eb-410f-aaa2-352c5955907a',
            ),
        ],
    ),
    account_id='EILBDVJVNUAGVKRQ',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=958950,
)

res = s.bank_account_transactions.create(req)

if res.create_bank_transactions_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->