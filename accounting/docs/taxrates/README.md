# tax_rates

## Overview

Tax rates

### Available Operations

* [get](#get) - Get tax rate
* [list](#list) - List all tax rates

## get

Gets the specified tax rate for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetTaxRateRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    tax_rate_id='iusto',
)

res = s.tax_rates.get(req)

if res.tax_rate is not None:
    # handle response
```

## list

Gets the latest tax rates for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListTaxRatesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='vel',
)

res = s.tax_rates.list(req)

if res.tax_rates is not None:
    # handle response
```
