# tax_rates

## Overview

Tax rates

### Available Operations

* [get_tax_rate](#get_tax_rate) - Get tax rate
* [list_tax_rates](#list_tax_rates) - List all tax rates

## get_tax_rate

Gets the specified tax rate for a given company.

### Example Usage

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
    tax_rate_id="at",
)

res = s.tax_rates.get_tax_rate(req)

if res.tax_rate is not None:
    # handle response
```

## list_tax_rates

Gets the latest tax rates for a given company.

### Example Usage

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
    query="excepturi",
)

res = s.tax_rates.list_tax_rates(req)

if res.tax_rates is not None:
    # handle response
```
