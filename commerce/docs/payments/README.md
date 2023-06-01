# payments

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [get](#get) - Get payment
* [get_method](#get_method) - Get payment method
* [list](#list) - List payments
* [list_methods](#list_methods) - List payment methods

## get

Get a specific commerce payment for the given company & data connection.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetPaymentRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    payment_id='illum',
)

res = s.payments.get(req)

if res.payment is not None:
    # handle response
```

## get_method

Retrieve a specific payment method, such as card, cash or other online payment methods, as held in the linked commerce platform.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetPaymentMethodRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    payment_method_id='vel',
)

res = s.payments.get_method(req)

if res.payment_method is not None:
    # handle response
```

## list

List commerce payments for the given company & data connection.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListPaymentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='error',
)

res = s.payments.list(req)

if res.payments is not None:
    # handle response
```

## list_methods

Retrieve a list of payment methods, such as card, cash or other online payment methods, as held in the linked commerce platform.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListPaymentMethodsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='deserunt',
)

res = s.payments.list_methods(req)

if res.payment_methods is not None:
    # handle response
```
