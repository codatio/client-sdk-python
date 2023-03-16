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
            feed_start_date="2022-08-29T22:22:37.640Z",
            id="nulla",
            modified_date="2022-10-13T04:20:15.729Z",
            sort_code="fuga",
            status="facilis",
        ),
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="eum",
            account_number="iusto",
            account_type="Unknown",
            balance=8917.73,
            currency="inventore",
            feed_start_date="2022-03-30T01:52:05.014Z",
            id="enim",
            modified_date="2022-10-27T20:36:21.545Z",
            sort_code="voluptatum",
            status="autem",
        ),
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="vel",
            account_number="non",
            account_type="Credit",
            balance=5680.45,
            currency="reprehenderit",
            feed_start_date="2022-04-12T23:19:38.479Z",
            id="quo",
            modified_date="2023-02-18T21:16:39.903Z",
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