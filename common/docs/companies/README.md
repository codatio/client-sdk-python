# companies

## Overview

Create and manage your Codat companies.

### Available Operations

* [create](#create) - Create company
* [delete](#delete) - Delete a company
* [get](#get) - Get company
* [list](#list) - List companies
* [update](#update) - Update company

## create

Create a new company

### Example Usage

```python
import codatcommon
from codatcommon.models import shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = shared.CompanyRequestBody(
    description="corrupti",
    name="Ben Mueller",
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
```

## delete

Delete the given company from Codat.
This operation is not reversible.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteCompanyRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.companies.delete(req)

if res.status_code == 200:
    # handle response
```

## get

Get metadata for a single company

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCompanyRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.companies.get(req)

if res.company is not None:
    # handle response
```

## list

List all companies that you have created in Codat.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListCompaniesRequest(
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="iure",
)

res = s.companies.list(req)

if res.companies is not None:
    # handle response
```

## update

Updates the given company with a new name and description

### Example Usage

```python
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateCompanyRequest(
    company_request_body=shared.CompanyRequestBody(
        description="magnam",
        name="Larry Windler",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.companies.update(req)

if res.company is not None:
    # handle response
```
