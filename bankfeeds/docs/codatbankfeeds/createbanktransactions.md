# create_bank_transactions
Available in: `codat_bank_feeds`

Posts bank transactions to the accounting package for a given company.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support POST methods.

## Example Usage
```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBankTransactionsRequest(
    bank_transactions=shared.BankTransactions(
        account_id="cupiditate",
        transactions=[
            shared.BankTransactionLine(
                amount=201.07,
                balance=1649.4,
                cleared_on_date="2022-10-23T00:00:00Z",
                counterparty="assumenda",
                description="ipsam",
                id="02a94bb4-f63c-4969-a9a3-efa77dfb14cd",
                modified_date="2022-10-23T00:00:00Z",
                reconciled=False,
                reference="ea",
                source_modified_date="2022-10-23T00:00:00Z",
                transaction_type="Dep",
            ),
            shared.BankTransactionLine(
                amount=6754.39,
                balance=8811.04,
                cleared_on_date="2022-10-23T00:00:00Z",
                counterparty="non",
                description="occaecati",
                id="5efb9ba8-8f3a-4669-9707-4ba4469b6e21",
                modified_date="2022-10-23T00:00:00Z",
                reconciled=False,
                reference="magnam",
                source_modified_date="2022-10-23T00:00:00Z",
                transaction_type="Credit",
            ),
            shared.BankTransactionLine(
                amount=5699.65,
                balance=3540.47,
                cleared_on_date="2022-10-23T00:00:00Z",
                counterparty="provident",
                description="quos",
                id="90afa563-e251-46fe-8c8b-711e5b7fd2ed",
                modified_date="2022-10-23T00:00:00Z",
                reconciled=False,
                reference="accusantium",
                source_modified_date="2022-10-23T00:00:00Z",
                transaction_type="Debit",
            ),
        ],
    ),
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    allow_sync_on_push_complete=False,
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=508315,
)

res = s.codat_bank_feeds.create_bank_transactions(req)

if res.create_bank_transactions_response is not None:
    # handle response
```