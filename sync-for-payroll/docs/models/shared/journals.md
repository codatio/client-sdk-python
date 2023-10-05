# Journals


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `links`                                                    | [Optional[shared.Links]](undefined/models/shared/links.md) | :heavy_check_mark:                                         | N/A                                                        |
| `page_number`                                              | *Optional[int]*                                            | :heavy_check_mark:                                         | Current page number.                                       |
| `page_size`                                                | *Optional[int]*                                            | :heavy_check_mark:                                         | Number of items to return in results array.                |
| `results`                                                  | list[[shared.Journal](undefined/models/shared/journal.md)] | :heavy_minus_sign:                                         | N/A                                                        |
| `total_results`                                            | *Optional[int]*                                            | :heavy_check_mark:                                         | Total number of items.                                     |