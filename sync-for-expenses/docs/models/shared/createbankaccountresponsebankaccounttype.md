# CreateBankAccountResponseBankAccountType

The type of transactions and balances on the account.  
For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.  
For Debit accounts, positive balances are assets, and positive transactions **increase** assets.

## Example Usage

```python
from codat_sync_for_expenses.models.shared import CreateBankAccountResponseBankAccountType

value = CreateBankAccountResponseBankAccountType.UNKNOWN
```


## Values

| Name      | Value     |
| --------- | --------- |
| `UNKNOWN` | Unknown   |
| `CREDIT`  | Credit    |
| `DEBIT`   | Debit     |