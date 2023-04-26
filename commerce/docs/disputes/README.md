# disputes

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [list](#list) - List disputes

## list

List commerce disputes

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListDisputesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="provident",
)

res = s.disputes.list(req)

if res.disputes is not None:
    # handle response
```
