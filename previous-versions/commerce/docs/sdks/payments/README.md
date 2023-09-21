# Payments

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [get](#get) - Get payment
* [get_method](#get_method) - Get payment method
* [list](#list) - List payments
* [list_methods](#list_methods) - List payment methods

## get

The *Get payment* endpoint returns a single payment for a given paymentId.

[Payments](https://docs.codat.io/commerce-api#/schemas/Payment) contain details of all payments made by customers to the company.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-payments) for integrations that support getting a specific payment.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations, shared

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

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetPaymentRequest](../../models/operations/getpaymentrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.GetPaymentResponse](../../models/operations/getpaymentresponse.md)**


## get_method

The *Get payment method* endpoint returns a single payment method for a given paymentMethodId.

[Payment methods](https://docs.codat.io/commerce-api#/schemas/PaymentMethod) represent the payment method(s) used to make payments.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-paymentMethods) for integrations that support getting a specific payment method.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations, shared

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

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPaymentMethodRequest](../../models/operations/getpaymentmethodrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.GetPaymentMethodResponse](../../models/operations/getpaymentmethodresponse.md)**


## list

The *List payments* endpoint returns a list of [payments](https://docs.codat.io/commerce-api#/schemas/Payment) for a given company's connection.

[Payments](https://docs.codat.io/commerce-api#/schemas/Payment) contain details of all payments made by customers to the company.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations, shared

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

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListPaymentsRequest](../../models/operations/listpaymentsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |


### Response

**[operations.ListPaymentsResponse](../../models/operations/listpaymentsresponse.md)**


## list_methods

The *List payment methods* endpoint returns a list of [payment methods](https://docs.codat.io/commerce-api#/schemas/PaymentMethod) for a given company's connection.

[Payment methods](https://docs.codat.io/commerce-api#/schemas/PaymentMethod) represent the payment method(s) used to make payments.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations, shared

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

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPaymentMethodsRequest](../../models/operations/listpaymentmethodsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.ListPaymentMethodsResponse](../../models/operations/listpaymentmethodsresponse.md)**

