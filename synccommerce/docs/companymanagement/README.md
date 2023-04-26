# company_management

## Overview

Create new and manage existing Sync for Commerce companies.

### Available Operations

* [create_company](#create_company) - Create Sync for Commerce company
* [create_connection](#create_connection) - Create connection
* [list_companies](#list_companies) - List companies
* [list_connections](#list_connections) - List data connections
* [update_connection](#update_connection) - Update data connection

## create_company

Creates a Codat company with a commerce partner data connection.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = shared.CreateCompany(
    name="Bob's Burgers",
)

res = s.company_management.create_company(req)

if res.company is not None:
    # handle response
```

## create_connection

Create a data connection for company.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateConnectionRequest(
    request_body="corrupti",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.company_management.create_connection(req)

if res.connection is not None:
    # handle response
```

## list_companies

Retrieve a list of all companies the client has created.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListCompaniesRequest(
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="provident",
)

res = s.company_management.list_companies(req)

if res.companies is not None:
    # handle response
```

## list_connections

Retrieve previously created data connections.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListConnectionsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="distinctio",
)

res = s.company_management.list_connections(req)

if res.connections is not None:
    # handle response
```

## update_connection

Update a data connection

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateConnectionRequest(
    update_connection=shared.UpdateConnection(
        status="Linked",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.company_management.update_connection(req)

if res.connection is not None:
    # handle response
```
