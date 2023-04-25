# create_data_connection
Available in: `connections`

Create a data connection for a company

## Example Usage
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