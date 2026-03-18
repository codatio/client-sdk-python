## Python SDK Changes:
* `codat_sync_expenses.connections.create_partner_expense_connection()`:  `response.connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_sync_expenses.companies.create()`:  `response.data_connections[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_sync_expenses.companies.get()`:  `response.data_connections[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_sync_expenses.companies.list()`: 
  *  `request.tags` **Added**
  *  `response.results[].data_connections[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_sync_expenses.companies.update()`: 
  * `request` **Changed** (Breaking ⚠️)
    - `company_request_body` **Removed** (Breaking ⚠️)
    - `company_update_request` **Added**
  *  `response.data_connections[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_sync_expenses.connections.create()`:  `response.connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_sync_expenses.connections.get()`:  `response.connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_sync_expenses.connections.list()`:  `response.results[].connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_sync_expenses.connections.unlink()`:  `response.connection_info.Map<any>` **Changed** (Breaking ⚠️)
* `codat_sync_expenses.companies.replace()`: **Added**
* `codat_sync_expenses.manage_data.get()`:  `response.account_transactions.last_successful_sync` **Changed**
* `codat_sync_expenses.manage_data.refresh_all_data_types()`:  `error.status[400]` **Added**
* `codat_sync_expenses.manage_data.refresh_data_type()`:  `error.status[400]` **Added**
