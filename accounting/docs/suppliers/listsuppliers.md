# list_suppliers
Available in: `suppliers`

Gets the latest suppliers for a company, with pagination

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListSuppliersRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="assumenda",
)

res = s.suppliers.list_suppliers(req)

if res.suppliers is not None:
    # handle response
```