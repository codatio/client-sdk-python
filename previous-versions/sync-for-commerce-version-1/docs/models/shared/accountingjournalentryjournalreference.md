# AccountingJournalEntryJournalReference

Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals).


## Fields

| Field                           | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `id`                            | *str*                           | :heavy_check_mark:              | GUID of the underlying journal. |
| `name`                          | *Optional[str]*                 | :heavy_minus_sign:              | Name of journal                 |