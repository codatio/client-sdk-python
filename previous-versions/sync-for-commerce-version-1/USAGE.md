<!-- Start SDK Example Usage -->


```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared
from decimal import Decimal

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingAccountRequest(
    accounting_account=shared.AccountingAccount(
        currency='GBP',
        current_balance=Decimal('0'),
        description='Invoices the business has issued but has not yet collected payment on.',
        fully_qualified_category='Asset.Current',
        fully_qualified_name='Cash On Hand',
        id='1b6266d1-1e44-46c5-8eb5-a8f98e03124e',
        metadata=shared.AccountingAccountMetadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        name='Accounts Receivable',
        nominal_code='610',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.AccountStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "key": {
                    "key": 'string',
                },
            },
        ),
        type=shared.AccountType.ASSET,
        valid_datatype_links=[
            shared.AccountingAccountValidDataTypeLinks(
                links=[
                    'string',
                ],
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounting_accounts.create_accounting_account(req)

if res.accounting_create_account_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->