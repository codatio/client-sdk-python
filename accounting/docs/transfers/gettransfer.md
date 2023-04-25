# get_transfer
Available in: `transfers`

Gets the specified transfer for a given company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetTransferRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    transfer_id="autem",
)

res = s.transfers.get_transfer(req)

if res.transfer is not None:
    # handle response
```