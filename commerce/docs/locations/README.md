# locations

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [list](#list) - List locations

## list

Retrieve a list of locations as seen in the commerce platform.

A `location` is a geographic place at which stocks of products may be held, or from where orders were placed.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListLocationsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.locations.list(req)

if res.locations_response is not None:
    # handle response
```
