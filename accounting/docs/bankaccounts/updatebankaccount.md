# update_bank_account
Available in: `bank_accounts`

Posts an updated bank account to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call []().

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support updating bank accounts.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateBankAccountRequest(
    bank_account=shared.BankAccount(
        account_name="quibusdam",
        account_number="labore",
        account_type="Unknown",
        available_balance=1831.91,
        balance=3978.21,
        currency="cupiditate",
        i_ban="quos",
        id="02d502a9-4bb4-4f63-8969-e9a3efa77dfb",
        institution="dicta",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        nominal_code="magnam",
        overdraft_limit=7670.24,
        sort_code="facere",
        source_modified_date="2022-10-23T00:00:00Z",
    ),
    bank_account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    timeout_in_minutes=411820,
)

res = s.bank_accounts.update_bank_account(req)

if res.update_bank_account_response is not None:
    # handle response
```