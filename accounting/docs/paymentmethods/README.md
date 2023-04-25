# payment_methods

## Overview

Payment methods

### Available Operations

* [get_payment_method](#get_payment_method) - Get payment method
* [list_payment_methods](#list_payment_methods) - List all payment methods

## get_payment_method

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
    payment_method_id="harum",
)

res = s.payment_methods.get_payment_method(req)

if res.payment_method is not None:
    # handle response
```

## list_payment_methods

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

res = s.payment_methods.list_payment_methods(req)

if res.payment_methods is not None:
    # handle response
```
