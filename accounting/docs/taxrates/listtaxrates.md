# list_tax_rates
Available in: `tax_rates`

Gets the latest tax rates for a given company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListTaxRatesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="est",
)

res = s.tax_rates.list_tax_rates(req)

if res.tax_rates is not None:
    # handle response
```