# BillStatus

Current state of the bill. If creating a bill the status must be `Open`.

## Example Usage

```python
from codat_sync_for_payables.models.shared import BillStatus

value = BillStatus.UNKNOWN
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `UNKNOWN`        | Unknown          |
| `OPEN`           | Open             |
| `PARTIALLY_PAID` | PartiallyPaid    |
| `PAID`           | Paid             |
| `VOID`           | Void             |
| `DRAFT`          | Draft            |