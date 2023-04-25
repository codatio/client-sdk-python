# create_bank_transactions
Available in: `bank_account_transactions`

Posts bank transactions to the accounting package for a given company.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support POST methods.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBankTransactionsRequest(
    bank_transactions=shared.BankTransactions(
        account_id="cum",
        transactions=[
            shared.BankTransactionLine(
                amount=2165.5,
                balance=5684.34,
                cleared_on_date="2022-10-23T00:00:00Z",
                counterparty="aspernatur",
                description="perferendis",
                id="5929396f-ea75-496e-b10f-aaa2352c5955",
                modified_date="2022-10-23T00:00:00Z",
                reconciled=False,
                reference="excepturi",
                source_modified_date="2022-10-23T00:00:00Z",
                transaction_type="Unknown",
            ),
            shared.BankTransactionLine(
                amount=4386.01,
                balance=6342.74,
                cleared_on_date="2022-10-23T00:00:00Z",
                counterparty="doloribus",
                description="sapiente",
                id="1a3a2fa9-4677-4392-91aa-52c3f5ad019d",
                modified_date="2022-10-23T00:00:00Z",
                reconciled=False,
                reference="laborum",
                source_modified_date="2022-10-23T00:00:00Z",
                transaction_type="Credit",
            ),
        ],
    ),
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    allow_sync_on_push_complete=False,
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=971945,
)

res = s.bank_account_transactions.create_bank_transactions(req)

if res.create_bank_transactions_response is not None:
    # handle response
```