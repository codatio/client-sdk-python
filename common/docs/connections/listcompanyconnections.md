# list_company_connections
Available in: `connections`

List the connections for a company

## Example Usage
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