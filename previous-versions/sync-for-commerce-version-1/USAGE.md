<!-- Start SDK Example Usage -->


```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingAccountRequest(
    accounting_account=shared.AccountingAccount(
        currency='USD',
        current_balance=0,
        description='Invoices the business has issued but has not yet collected payment on.',
        fully_qualified_category='Asset.Current',
        fully_qualified_name='Fixed Asset',
        id='1b6266d1-1e44-46c5-8eb5-a8f98e03124e',
        is_bank_account=False,
        metadata=shared.AccountingAccountMetadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        name='Accounts Receivable',
        nominal_code='610',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.AccountStatus.ACTIVE,
        type=shared.AccountType.ASSET,
        valid_datatype_links=[
            shared.AccountingAccountValidDataTypeLinks(
                links=[
                    'unde',
                ],
                property='nulla',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=544883,
)

res = s.accounting_accounts.create_accounting_account(req)

if res.accounting_create_account_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->