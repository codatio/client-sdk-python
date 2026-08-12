# DataTypeReadSummary


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `connection_id`                                                           | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Unique identifier for a company's data connection.                        |
| `data_type`                                                               | [Optional[shared.DataType]](../../models/shared/datatype.md)              | :heavy_minus_sign:                                                        | Available data types                                                      |
| `issues`                                                                  | List[[shared.Issue](../../models/shared/issue.md)]                        | :heavy_minus_sign:                                                        | A array of issues encountered during a data read.                         |
| `records_modified`                                                        | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | `True` if records have been created, updated or deleted in Codat's cache. |
| `status`                                                                  | [Optional[shared.Status]](../../models/shared/status.md)                  | :heavy_minus_sign:                                                        | The current status of the dataset.                                        |