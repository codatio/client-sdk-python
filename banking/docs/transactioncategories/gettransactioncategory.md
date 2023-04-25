# get_transaction_category
Available in: `transaction_categories`

Gets a specified bank transaction category for a given company

## Example Usage
```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetTransactionCategoryRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    transaction_category_id="quibusdam",
)

res = s.transaction_categories.get_transaction_category(req)

if res.transaction_category is not None:
    # handle response
```