# list_bank_transactions
Available in: `bank_account_transactions`

Gets the latest bank transactions for given account ID and company. Doesn't require connection ID.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBankTransactionsRequest(
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="vero",
)

res = s.bank_account_transactions.list_bank_transactions(req)

if res.bank_account_transactions is not None:
    # handle response
```