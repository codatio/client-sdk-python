<!-- Start SDK Example Usage -->
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
            account_name="provident",
            account_number="distinctio",
            account_type="quibusdam",
            balance=6027.63,
            currency="nulla",
            feed_start_date="2022-10-23T00:00:00Z",
            id="corrupti",
            modified_date="2022-10-23T00:00:00Z",
            sort_code="illum",
            status="vel",
        ),
        shared.BankFeedAccount(
            account_name="error",
            account_number="deserunt",
            account_type="suscipit",
            balance=4375.87,
            currency="magnam",
            feed_start_date="2022-10-23T00:00:00Z",
            id="debitis",
            modified_date="2022-10-23T00:00:00Z",
            sort_code="ipsa",
            status="delectus",
        ),
        shared.BankFeedAccount(
            account_name="tempora",
            account_number="suscipit",
            account_type="molestiae",
            balance=7917.25,
            currency="placeat",
            feed_start_date="2022-10-23T00:00:00Z",
            id="voluptatum",
            modified_date="2022-10-23T00:00:00Z",
            sort_code="iusto",
            status="excepturi",
        ),
    ],
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)
    
res = s.create_bank_feed(req)

if res.bank_feed_accounts is not None:
    # handle response
```
<!-- End SDK Example Usage -->