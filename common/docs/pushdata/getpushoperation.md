# get_push_operation
Available in: `push_data`

Retrieve push operation.

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPushOperationRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    push_operation_key="05dfc2dd-f7cc-478c-a1ba-928fc816742c",
)

res = s.push_data.get_push_operation(req)

if res.push_operation is not None:
    # handle response
```