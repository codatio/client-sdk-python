# CompanyInfoSDK
(*company_info*)

## Overview

Retrieve standardized data from linked commerce software.

### Available Operations

* [get](#get) - Get company info

## get

Retrieve information about the company, as seen in the commerce software.

This may include information like addresses, tax registration details and social media or website information.

### Example Usage

```python
from codat_commerce import CodatCommerce

s = CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.company_info.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.GetCompanyInfoRequest](../../models/getcompanyinforequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CompanyInfo](../../models/companyinfo.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| models.SDKError                 | 4xx-5xx                         | */*                             |
