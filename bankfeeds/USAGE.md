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
            feed_start_date="2022-09-03T03:06:20.417Z",
            id="nulla",
            modified_date="2022-10-17T09:03:58.506Z",
            sort_code="fuga",
            status="facilis",
        ),
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="eum",
            account_number="iusto",
            account_type="Unknown",
            balance=8917.73,
            currency="inventore",
            feed_start_date="2022-04-03T06:35:47.790Z",
            id="enim",
            modified_date="2022-11-01T01:20:04.322Z",
            sort_code="voluptatum",
            status="autem",
        ),
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="vel",
            account_number="non",
            account_type="Credit",
            balance=5680.45,
            currency="reprehenderit",
            feed_start_date="2022-04-17T04:03:21.255Z",
            id="quo",
            modified_date="2023-02-23T02:00:22.679Z",
            sort_code="laboriosam",
            status="dicta",
        ),
    ],
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)
    
res = s.create_bank_feed(req)

if res.bank_feed_bank_accounts is not None:
    # handle response
```
<!-- End SDK Example Usage -->