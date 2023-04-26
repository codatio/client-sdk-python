# payment_methods

## Overview

Payment methods

### Available Operations

* [get](#get) - Get payment method
* [list](#list) - List all payment methods

## get

Gets the specified payment method for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPaymentMethodRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    payment_method_id="ea",
)

res = s.payment_methods.get(req)

if res.payment_method is not None:
    # handle response
```

## list

Gets the payment methods for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListPaymentMethodsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="error",
)

res = s.payment_methods.list(req)

if res.payment_methods is not None:
    # handle response
```
