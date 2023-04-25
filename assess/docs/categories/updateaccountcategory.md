# update_account_category
Available in: `categories`

Update category for a specific nominal account

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateAccountCategoryRequest(
    confirm_category=shared.ConfirmCategory(
        confirmed=shared.AccountCategory(
            detail_type="quibusdam",
            subtype="unde",
            type="nulla",
        ),
    ),
    account_id="corrupti",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.categories.update_account_category(req)

if res.categorised_account is not None:
    # handle response
```