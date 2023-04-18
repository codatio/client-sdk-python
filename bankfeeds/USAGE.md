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
            id="8d69a674-e0f4-467c-8879-6ed151a05dfc",
            modified_date="2022-10-23T00:00:00Z",
            sort_code="odit",
            status="at",
        ),
        shared.BankFeedAccount(
            account_name="at",
            account_number="maiores",
            account_type="molestiae",
            balance=7991.59,
            currency="quod",
            feed_start_date="2022-10-23T00:00:00Z",
            id="78ca1ba9-28fc-4816-b42c-b73920592939",
            modified_date="2022-10-23T00:00:00Z",
            sort_code="laboriosam",
            status="hic",
        ),
        shared.BankFeedAccount(
            account_name="saepe",
            account_number="fuga",
            account_type="in",
            balance=3595.08,
            currency="iste",
            feed_start_date="2022-10-23T00:00:00Z",
            id="6eb10faa-a235-42c5-9559-07aff1a3a2fa",
            modified_date="2022-10-23T00:00:00Z",
            sort_code="occaecati",
            status="numquam",
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