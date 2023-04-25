# list_available_account_categories
Available in: `categories`

Lists available account categories Codat's categorisation engine can provide. 

## Example Usage
```python
import codatassess


s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


res = s.categories.list_available_account_categories()

if res.categories is not None:
    # handle response
```