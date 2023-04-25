# get_supplier
Available in: `suppliers`

Gets a single supplier corresponding to the given ID.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSupplierRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.get_supplier(req)

if res.supplier is not None:
    # handle response
```