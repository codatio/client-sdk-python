# create_bank_account
Available in: `bank_accounts`

Posts a new bank account to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call []().

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating bank accounts.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBankAccountRequest(
    bank_account=shared.BankAccount(
        account_name="nihil",
        account_number="praesentium",
        account_type="Debit",
        available_balance=557.14,
        balance=6048.46,
        currency="voluptate",
        i_ban="cum",
        id="0074f154-71b5-4e6e-93b9-9d488e1e91e4",
        institution="enim",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        nominal_code="consequatur",
        overdraft_limit=6674.11,
        sort_code="quibusdam",
        source_modified_date="2022-10-23T00:00:00Z",
    ),
    allow_sync_on_push_complete=False,
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=131797,
)

res = s.bank_accounts.create_bank_account(req)

if res.create_bank_account_response is not None:
    # handle response
```