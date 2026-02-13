## Python SDK Changes:
* `codat_platform.companies.update()`:  `response.data_connections[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.connections.create()`:  `response.connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.connections.update_authorization()`:  `response.connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.connections.unlink()`:  `response.connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.companies.create()`:  `response.data_connections[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.companies.get()`:  `response.data_connections[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.companies.list()`:  `response.results[].data_connections[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.companies.replace()`:  `response.data_connections[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.connections.list()`:  `response.results[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.connections.get()`:  `response.connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_platform.companies.get_company_sync_settings()`: **Added**
* `codat_platform.companies.refresh_product_data()`: **Added**
* `codat_platform.read_data.get_validation_results()`: **Added**
* `codat_platform.companies.set_company_sync_settings()`: **Added**
* `codat_platform.refresh_data.all()`:  `error.status[400]` **Added**
* `codat_platform.refresh_data.by_data_type()`:  `error.status[400]` **Added**
* `codat_platform.refresh_data.get()`:  `response.account_transactions.last_successful_sync` **Changed**
* `codat_lending.banking.categorized_statement.get()`:  `response.report_items[].transactions[].is_recurring` **Added**
