# GroupsSDK
(*groups*)

## Overview

Define and manage sets of companies based on a chosen characteristic.

### Available Operations

* [add_company](#add_company) - Add company
* [create](#create) - Create group
* [list](#list) - List groups
* [remove_company](#remove_company) - Remove company

## add_company

﻿Use the *Add company* endpoint to assign a company to a group. A company can belong to multiple groups, but can only be added to one group at a time.

[Groups](https://docs.codat.io/platform-api#/schemas/Group) define a set of companies that are organized based on a chosen characteristic and can be managed in the same way.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.groups.add_company(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "company_group_assignment": {
        "group_id": "d7a6c4b4-dc87-45f6-b803-62f466398680",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.AddCompanyToGroupRequest](../../models/addcompanytogrouprequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.Company](../../models/company.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| models.SDKError             | 4xx-5xx                     | */*                         |


## create

﻿Use the *Create group* endpoint to generate a new group that you can assign your companies to.

[Groups](https://docs.codat.io/platform-api#/schemas/Group) define a set of companies that are organized based on a chosen characteristic and can be managed in the same way.

### Tips and traps

* The maximum length for the group name is 50 characters.
* It's possible to create up to 20 groups per client.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.groups.create(request={
    "name": "Corporate cards department",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GroupPrototype](../../models/groupprototype.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Group](../../models/group.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ErrorMessage         | 401,402,403,409,429,500,503 | application/json            |
| models.SDKError             | 4xx-5xx                     | */*                         |


## list

Use the *List group* endpoint to return a list of all groups that currently exist for your client.

[Groups](https://docs.codat.io/platform-api#/schemas/Group) define a set of companies that are organized based on a chosen characteristic and can be managed in the same way.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.groups.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Groups](../../models/groups.md)**

### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ErrorMessage     | 401,402,403,429,500,503 | application/json        |
| models.SDKError         | 4xx-5xx                 | */*                     |


## remove_company

﻿Use the *Remove company* endpoint to remove a company from a group.

[Groups](https://docs.codat.io/platform-api#/schemas/Group) define a set of companies that are organized based on a chosen characteristic and can be managed in the same way.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.groups.remove_company(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "group_id": "60d2fa12-8a04-11ee-b9d1-0242ac120002",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.RemoveCompanyFromGroupRequest](../../models/removecompanyfromgrouprequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| models.SDKError             | 4xx-5xx                     | */*                         |
