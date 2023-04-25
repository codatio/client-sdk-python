# payments

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [list_payment_methods](#list_payment_methods) - List payment methods
* [list_payments](#list_payments) - List payments

## list_payment_methods

Retrieve a list of payment methods, such as card, cash or other online payment methods, as held in the linked commerce platform.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListPaymentMethodsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="quibusdam",
)

res = s.payments.list_payment_methods(req)

if res.payment_methods is not None:
    # handle response
```

## list_payments

List commerce payments for the given company & data connection.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListPaymentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="unde",
)

res = s.payments.list_payments(req)

if res.payments is not None:
    # handle response
```
