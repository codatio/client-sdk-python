# get_tax_rate
Available in: `tax_rates`

Gets the specified tax rate for a given company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetTaxRateRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    tax_rate_id="est",
)

res = s.tax_rates.get_tax_rate(req)

if res.tax_rate is not None:
    # handle response
```