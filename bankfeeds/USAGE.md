<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBankFeedRequest(
    request_body=[
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="deserunt",
            account_number="porro",
            account_type="debit",
            balance=6027.63,
            currency="vero",
            feed_start_date="perspiciatis",
            id="nulla",
            modified_date="nihil",
            sort_code="fuga",
            status="facilis",
        ),
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="eum",
            account_number="iusto",
            account_type="unknown",
            balance=8917.73,
            currency="inventore",
            feed_start_date="sapiente",
            id="enim",
            modified_date="eum",
            sort_code="voluptatum",
            status="autem",
        ),
        operations.CreateBankFeedBankFeedBankAccount(
            account_name="vel",
            account_number="non",
            account_type="credit",
            balance=5680.45,
            currency="reprehenderit",
            feed_start_date="molestiae",
            id="quo",
            modified_date="quasi",
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