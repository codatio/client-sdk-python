# DatasetStatusChangedErrorWebhookData


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `data_type`                                                  | [Optional[shared.DataType]](../../models/shared/datatype.md) | :heavy_minus_sign:                                           | Available Data types                                         | invoices                                                     |
| `dataset_id`                                                 | *Optional[str]*                                              | :heavy_minus_sign:                                           | Unique identifier for the dataset that completed its sync.   |                                                              |
| `dataset_status`                                             | *Optional[str]*                                              | :heavy_minus_sign:                                           | The current status of the dataset's sync.                    |                                                              |