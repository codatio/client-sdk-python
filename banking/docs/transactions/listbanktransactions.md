# list_bank_transactions
Available in: `transactions`

Gets a list of transactions incurred by a company across all bank accounts.

## Example Usage
```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBankTransactionsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="corrupti",
)

res = s.transactions.list_bank_transactions(req)

if res.transactions is not None:
    # handle response
```