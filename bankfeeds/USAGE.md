<!-- Start SDK Example Usage -->


```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBankAccountMappingRequest(
    bank_feed_account_mapping=shared.BankFeedAccountMapping(
        feed_start_date='2022-10-23T00:00:00.000Z',
        source_account_id='provident',
        target_account_id='distinctio',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.account_mapping.create(req)

if res.account_mapping_result is not None:
    # handle response
```
<!-- End SDK Example Usage -->