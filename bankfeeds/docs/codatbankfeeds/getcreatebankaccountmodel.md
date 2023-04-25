# get_create_bank_account_model
Available in: `codat_bank_feeds`

Gets the options of pushing bank account transactions.

## Example Usage
```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateBankAccountModelRequest(
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.codat_bank_feeds.get_create_bank_account_model(req)

if res.push_option is not None:
    # handle response
```