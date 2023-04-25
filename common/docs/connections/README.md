# connections

## Overview

Manage your companies' data connections.

### Available Operations

* [create_data_connection](#create_data_connection) - Create connection
* [delete_company_connection](#delete_company_connection) - Delete connection
* [get_company_connection](#get_company_connection) - Get connection
* [list_company_connections](#list_company_connections) - List connections
* [unlink_company_connection](#unlink_company_connection) - Unlink connection
* [update_connection_authorization](#update_connection_authorization) - Update authorization

## create_data_connection

Create a data connection for a company

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateDataConnectionRequest(
    request_body=operations.CreateDataConnectionRequestBody(
        platform_key="molestiae",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.connections.create_data_connection(req)

if res.connection is not None:
    # handle response
```

## delete_company_connection

Revoke and remove a connection from a company.
This operation is not reversible - the end user would need to reauthorize a new data connection if you wish to view new data for this company.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteCompanyConnectionRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.connections.delete_company_connection(req)

if res.status_code == 200:
    # handle response
```

## get_company_connection

Get a single connection for a company

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCompanyConnectionRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.connections.get_company_connection(req)

if res.connection is not None:
    # handle response
```

## list_company_connections

List the connections for a company

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListCompanyConnectionsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="minus",
)

res = s.connections.list_company_connections(req)

if res.connections is not None:
    # handle response
```

## unlink_company_connection

This allows you to deauthorize a connection, without deleting it from Codat. This means you can still view any data that has previously been pulled into Codat, and also lets you re-authorize in future if your customer wishes to resume sharing their data.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UnlinkCompanyConnectionRequest(
    request_body=operations.UnlinkCompanyConnectionRequestBody(
        status="placeat",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.connections.unlink_company_connection(req)

if res.connection is not None:
    # handle response
```

## update_connection_authorization

Update data connection's authorization.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateConnectionAuthorizationRequest(
    request_body={
        "iusto": "excepturi",
        "nisi": "recusandae",
        "temporibus": "ab",
    },
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.connections.update_connection_authorization(req)

if res.connection is not None:
    # handle response
```
