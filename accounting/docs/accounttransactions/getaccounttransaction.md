# get_account_transaction
Available in: `account_transactions`

Gets the account transactions for a given company.Gets the specified account transaction for a given company and connection.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountTransactionRequest(
    account_transaction_id="provident",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.account_transactions.get_account_transaction(req)

if res.account_transaction is not None:
    # handle response
```