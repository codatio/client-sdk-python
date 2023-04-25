# update_bank_feed
Available in: `codat_bank_feeds`

Update a single BankFeed BankAccount for a single data source connected to a single company.

## Example Usage
```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateBankFeedRequest(
    bank_feed_account=shared.BankFeedAccount(
        account_name="magni",
        account_number="sunt",
        account_type="quo",
        balance=8480.09,
        currency="pariatur",
        feed_start_date="2022-10-23T00:00:00Z",
        id="c692601f-b576-4b0d-9f0d-30c5fbb25870",
        modified_date="2022-10-23T00:00:00Z",
        sort_code="quis",
        status="nesciunt",
    ),
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.codat_bank_feeds.update_bank_feed(req)

if res.bank_feed_account is not None:
    # handle response
```