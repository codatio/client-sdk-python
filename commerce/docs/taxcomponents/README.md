# tax_components

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [get](#get) - Get tax component
* [list](#list) - List tax components

## get

This endpoint returns a specific tax rate from the commerce platform, including tax rate names and values. This supports the mapping of tax rates from the commerce platform to the accounting platform.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetTaxComponentRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    tax_id='ipsa',
)

res = s.tax_components.get(req)

if res.tax_component is not None:
    # handle response
```

## list

This endpoint returns a lists of tax rates from the commerce platform, including tax rate names and values. This supports the mapping of tax rates from the commerce platform to the accounting platform.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListTaxComponentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='delectus',
)

res = s.tax_components.list(req)

if res.tax_components is not None:
    # handle response
```
