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
            account_name='provident',
            account_number='distinctio',
            account_type='quibusdam',
            balance=6027.63,
            currency='nulla',
            feed_start_date='corrupti',
            id='d69a674e-0f46-47cc-8796-ed151a05dfc2',
            modified_date='at',
            sort_code='at',
            status='maiores',
        ),
        shared.BankFeedAccount(
            account_name='molestiae',
            account_number='quod',
            account_type='quod',
            balance=4614.79,
            currency='totam',
            feed_start_date='porro',
            id='a1ba928f-c816-4742-8b73-9205929396fe',
            modified_date='fuga',
            sort_code='in',
            status='corporis',
        ),
        shared.BankFeedAccount(
            account_name='iste',
            account_number='iure',
            account_type='saepe',
            balance=6976.31,
            currency='architecto',
            feed_start_date='ipsa',
            id='faaa2352-c595-4590-baff-1a3a2fa94677',
            modified_date='velit',
            sort_code='error',
            status='quia',
        ),
    ],
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.create_bank_feed(req)

if res.bank_feed_accounts is not None:
    # handle response
```
<!-- End SDK Example Usage -->