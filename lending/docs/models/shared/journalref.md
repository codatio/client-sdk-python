# JournalRef

Links journal entries to the relevant journal in accounting integrations that use multi-book accounting (multiple journals).


## Fields

| Field                           | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `additional_properties`         | Dict[str, *Any*]                | :heavy_check_mark:              | N/A                             |
| `id`                            | *str*                           | :heavy_check_mark:              | GUID of the underlying journal. |
| `name`                          | *OptionalNullable[str]*         | :heavy_minus_sign:              | Name of journal                 |