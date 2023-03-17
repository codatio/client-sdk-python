<!-- Start SDK Example Usage -->
```python
import bankfeeds
from bankfeeds.models import operations, shared

s = bankfeeds.BankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBankFeedRequest(
    request_body=[
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="deserunt",
            account_number="porro",
            account_type="Debit",
            balance=6027.63,
            currency="vero",
            feed_start_date="2022-08-30T03:07:32.663Z",
            id="nulla",
            modified_date="2022-10-13T09:05:10.752Z",
            sort_code="fuga",
            status="facilis",
        ),
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="eum",
            account_number="iusto",
            account_type="Unknown",
            balance=8917.73,
            currency="inventore",
            feed_start_date="2022-03-30T06:37:00.036Z",
            id="enim",
            modified_date="2022-10-28T01:21:16.568Z",
            sort_code="voluptatum",
            status="autem",
        ),
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="vel",
            account_number="non",
            account_type="Credit",
            balance=5680.45,
            currency="reprehenderit",
            feed_start_date="2022-04-13T04:04:33.501Z",
            id="quo",
            modified_date="2023-02-19T02:01:34.925Z",
            sort_code="laboriosam",
            status="dicta",
        ),
    ],
    company_id="est",
    connection_id="voluptatem",
)
    
res = s.create_bank_feed(req)

if res.bank_feed_bank_accounts is not None:
    # handle response
```
<!-- End SDK Example Usage -->