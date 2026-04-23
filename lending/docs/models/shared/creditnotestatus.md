# CreditNoteStatus

Current state of the credit note.

## Example Usage

```python
from codat_lending.models.shared import CreditNoteStatus

value = CreditNoteStatus.UNKNOWN
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `UNKNOWN`        | Unknown          |
| `DRAFT`          | Draft            |
| `SUBMITTED`      | Submitted        |
| `PAID`           | Paid             |
| `VOID`           | Void             |
| `PARTIALLY_PAID` | PartiallyPaid    |