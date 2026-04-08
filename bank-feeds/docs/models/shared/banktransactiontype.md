# BankTransactionType

Type of transaction for the bank statement line.

## Example Usage

```python
from codat_bankfeeds.models.shared import BankTransactionType

value = BankTransactionType.UNKNOWN
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `UNKNOWN`      | Unknown        |
| `CREDIT`       | Credit         |
| `DEBIT`        | Debit          |
| `INT`          | Int            |
| `DIV`          | Div            |
| `FEE`          | Fee            |
| `SER_CHG`      | SerChg         |
| `DEP`          | Dep            |
| `ATM`          | Atm            |
| `POS`          | Pos            |
| `XFER`         | Xfer           |
| `CHECK`        | Check          |
| `PAYMENT`      | Payment        |
| `CASH`         | Cash           |
| `DIRECT_DEP`   | DirectDep      |
| `DIRECT_DEBIT` | DirectDebit    |
| `REPEAT_PMT`   | RepeatPmt      |
| `OTHER`        | Other          |