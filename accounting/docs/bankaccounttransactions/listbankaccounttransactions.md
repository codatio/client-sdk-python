# list_bank_account_transactions
Available in: `bank_account_transactions`

Gets bank transactions for a given bank account ID

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBankAccountTransactionsRequest(
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="voluptatibus",
)

res = s.bank_account_transactions.list_bank_account_transactions(req)

if res.bank_transactions_response is not None:
    # handle response
```