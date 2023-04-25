# get_bank_feeds
Available in: `codat_bank_feeds`

Get BankFeed BankAccounts for a single data source connected to a single company.

## Example Usage
```python
import codatbankfeeds
from codatbankfeeds.models import operations

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBankFeedsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.codat_bank_feeds.get_bank_feeds(req)

if res.bank_feed_accounts is not None:
    # handle response
```