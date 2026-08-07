# ValidFor

## Example Usage

```python
from codat_sync_for_expenses.models.shared import ValidFor

value = ValidFor.EXPENSE_TRANSACTIONS_PAYMENT
```


## Values

| Name                                | Value                               |
| ----------------------------------- | ----------------------------------- |
| `EXPENSE_TRANSACTIONS_PAYMENT`      | expense-transactions.Payment        |
| `EXPENSE_TRANSACTIONS_REFUND`       | expense-transactions.Refund         |
| `EXPENSE_TRANSACTIONS_REWARD`       | expense-transactions.Reward         |
| `EXPENSE_TRANSACTIONS_CHARGEBACK`   | expense-transactions.Chargeback     |
| `REIMBURSABLE_EXPENSE_TRANSACTIONS` | reimbursable-expense-transactions   |
| `TRANSFER_TRANSACTIONS`             | transfer-transactions               |
| `ADJUSTMENT_TRANSACTIONS`           | adjustment-transactions             |