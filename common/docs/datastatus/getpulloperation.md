# get_pull_operation
Available in: `data_status`

Retrieve information about a single dataset or pull operation.

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPullOperationRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    dataset_id="eaed9f0f-e77b-4bc9-a58f-ab8b4b99ab18",
)

res = s.data_status.get_pull_operation(req)

if res.pull_operation is not None:
    # handle response
```