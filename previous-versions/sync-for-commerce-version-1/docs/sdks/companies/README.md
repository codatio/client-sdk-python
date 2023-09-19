# Companies

## Overview

Create and manage your Codat companies.

### Available Operations

* [delete_company](#delete_company) - Delete a company
* [get_company](#get_company) - Get company
* [update_company](#update_company) - Update company

## delete_company

﻿
Permanently deletes a company, its connections and any cached data. This operation is irreversible. If the company ID does not exist an error is returned.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteCompanyRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.companies.delete_company(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteCompanyRequest](../../models/operations/deletecompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.DeleteCompanyResponse](../../models/operations/deletecompanyresponse.md)**


## get_company

﻿Returns the company for a valid identifier. If the identifier is for a deleted company, a not found response is returned.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCompanyRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.companies.get_company(req)

if res.company is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCompanyRequest](../../models/operations/getcompanyrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.GetCompanyResponse](../../models/operations/getcompanyresponse.md)**


## update_company

﻿Updates both the name and description of the company.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateCompanyRequest(
    create_company=shared.CreateCompany(
        description='Requested early access to the new financing scheme.',
        name='Bank of Dave',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.companies.update_company(req)

if res.company is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCompanyRequest](../../models/operations/updatecompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.UpdateCompanyResponse](../../models/operations/updatecompanyresponse.md)**

