# update_connection_authorization
Available in: `connections`

Update data connection's authorization.

## Example Usage
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