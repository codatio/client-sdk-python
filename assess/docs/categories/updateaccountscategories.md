# update_accounts_categories
Available in: `categories`

Comfirms the categories for all or a batch of accounts for a specific connection.

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateAccountsCategoriesRequest(
    confirm_categories=shared.ConfirmCategories(
        categories=[
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id="69a674e0-f467-4cc8-b96e-d151a05dfc2d",
                ),
                confirmed=shared.AccountCategory(
                    detail_type="at",
                    subtype="maiores",
                    type="molestiae",
                ),
            ),
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id="cc78ca1b-a928-4fc8-9674-2cb739205929",
                ),
                confirmed=shared.AccountCategory(
                    detail_type="dolor",
                    subtype="natus",
                    type="laboriosam",
                ),
            ),
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id="fea7596e-b10f-4aaa-a352-c5955907aff1",
                ),
                confirmed=shared.AccountCategory(
                    detail_type="mollitia",
                    subtype="dolorem",
                    type="culpa",
                ),
            ),
            shared.ConfirmCategoriesCategories(
                account_ref=shared.ConfirmCategoriesCategoriesAccountRef(
                    id="2fa94677-3925-41aa-92c3-f5ad019da1ff",
                ),
                confirmed=shared.AccountCategory(
                    detail_type="vero",
                    subtype="nihil",
                    type="praesentium",
                ),
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.categories.update_accounts_categories(req)

if res.categorised_accounts is not None:
    # handle response
```