# list_accounts_categories
Available in: `categories`

Lists suggested and confirmed chart of account categories for the given company and data connection.

## Example Usage
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListAccountsCategoriesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="distinctio",
)

res = s.categories.list_accounts_categories(req)

if res.categorised_accounts is not None:
    # handle response
```