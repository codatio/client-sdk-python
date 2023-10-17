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
    request_body=operations.CreateBankAccountMappingBankFeedAccountMapping(
        feed_start_date='2022-10-23T00:00:00.000Z',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.account_mapping.create(req)

if res.bank_feed_account_mapping_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->