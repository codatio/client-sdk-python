# create_bank_feed
Available in: `codat_bank_feeds`

Put BankFeed BankAccounts for a single data source connected to a single company.

## Example Usage
```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBankFeedRequest(
    request_body=[
        shared.BankFeedAccount(
            account_name="quam",
            account_number="molestiae",
            account_type="velit",
            balance=6235.1,
            currency="quia",
            feed_start_date="2022-10-23T00:00:00Z",
            id="51aa52c3-f5ad-4019-9a1f-fe78f097b007",
            modified_date="2022-10-23T00:00:00Z",
            sort_code="ut",
            status="maiores",
        ),
        shared.BankFeedAccount(
            account_name="dicta",
            account_number="corporis",
            account_type="dolore",
            balance=4808.94,
            currency="dicta",
            feed_start_date="2022-10-23T00:00:00Z",
            id="b5e6e13b-99d4-488e-9e91-e450ad2abd44",
            modified_date="2022-10-23T00:00:00Z",
            sort_code="qui",
            status="aliquid",
        ),
    ],
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.codat_bank_feeds.create_bank_feed(req)

if res.bank_feed_accounts is not None:
    # handle response
```