import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class ConfigureSyncPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFeesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFeesAccounts:
    account_options: Optional[list[ConfigureSyncRequestBodyConfigurationFeesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFeesFeesSupplierSupplierOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFeesFeesSupplier:
    selected_supplier_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedSupplierId') }})
    supplier_options: Optional[list[ConfigureSyncRequestBodyConfigurationFeesFeesSupplierSupplierOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFees:
    accounts: Optional[dict[str, ConfigureSyncRequestBodyConfigurationFeesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    fees_supplier: Optional[ConfigureSyncRequestBodyConfigurationFeesFeesSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feesSupplier') }})
    sync_fees: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncFees') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationNewPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationNewPaymentsAccounts:
    account_options: Optional[list[ConfigureSyncRequestBodyConfigurationNewPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationNewPayments:
    accounts: Optional[dict[str, ConfigureSyncRequestBodyConfigurationNewPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationPaymentsAccounts:
    account_options: Optional[list[ConfigureSyncRequestBodyConfigurationPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationPayments:
    accounts: Optional[dict[str, ConfigureSyncRequestBodyConfigurationPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesAccounts:
    account_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevelsInvoiceLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions') }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions') }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevels:
    invoice_level: Optional[ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevelsInvoiceLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLevel') }})
    invoice_line_level: Optional[ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLineLevel') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingPeriod:
    grouping_period_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriodOptions') }})
    selected_grouping_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupingPeriod') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGrouping:
    grouping_levels: Optional[ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevels] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingLevels') }})
    grouping_period: Optional[ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingPeriod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriod') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesInvoiceStatus:
    invoice_status_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatusOptions') }})
    selected_invoice_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedInvoiceStatus') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesAccountingTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesCommerceTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesTaxRateMappings:
    selected_accounting_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountingTaxRateId') }})
    selected_commerce_tax_rate_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCommerceTaxRateIds') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRates:
    accounting_tax_rate_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesAccountingTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingTaxRateOptions') }})
    commerce_tax_rate_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesCommerceTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('commerceTaxRateOptions') }})
    default_zero_tax_rate_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('defaultZeroTaxRateOptions') }})
    selected_default_zero_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedDefaultZeroTaxRateId') }})
    tax_rate_mappings: Optional[list[ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesTaxRateMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateMappings') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesSalesCustomerCustomerOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesSalesCustomer:
    customer_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesSalesCustomerCustomerOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerOptions') }})
    selected_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCustomerId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesTaxRatesTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesTaxRates:
    selected_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedTaxRateId') }})
    tax_rate_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesTaxRatesTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSales:
    accounts: Optional[dict[str, ConfigureSyncRequestBodyConfigurationSalesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    grouping: Optional[ConfigureSyncRequestBodyConfigurationSalesGrouping] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('grouping') }})
    invoice_status: Optional[ConfigureSyncRequestBodyConfigurationSalesInvoiceStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatus') }})
    new_tax_rates: Optional[ConfigureSyncRequestBodyConfigurationSalesNewTaxRates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newTaxRates') }})
    sales_customer: Optional[ConfigureSyncRequestBodyConfigurationSalesSalesCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('salesCustomer') }})
    sync_sales: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncSales') }})
    tax_rates: Optional[dict[str, ConfigureSyncRequestBodyConfigurationSalesTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRates') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfiguration:
    fees: Optional[ConfigureSyncRequestBodyConfigurationFees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fees') }})
    new_payments: Optional[ConfigureSyncRequestBodyConfigurationNewPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newPayments') }})
    payments: Optional[ConfigureSyncRequestBodyConfigurationPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('payments') }})
    sales: Optional[ConfigureSyncRequestBodyConfigurationSales] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sales') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBodySchedule:
    frequency_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequencyOptions') }})
    selected_frequency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedFrequency') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('startDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    sync_hour_utc: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncHourUtc') }})
    time_zone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeZone') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSyncRequestBody:
    accounting_software_company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingSoftwareCompanyName') }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    configuration: Optional[ConfigureSyncRequestBodyConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    configured: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configured') }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }})
    schedule: Optional[ConfigureSyncRequestBodySchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schedule') }})
    

@dataclasses.dataclass
class ConfigureSyncRequest:
    path_params: ConfigureSyncPathParams = dataclasses.field()
    request: Optional[ConfigureSyncRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFeesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFeesAccounts:
    account_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationFeesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFeesFeesSupplierSupplierOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFeesFeesSupplier:
    selected_supplier_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedSupplierId') }})
    supplier_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationFeesFeesSupplierSupplierOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFees:
    accounts: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationFeesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    fees_supplier: Optional[ConfigureSync200ApplicationJSONConfigurationFeesFeesSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feesSupplier') }})
    sync_fees: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncFees') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationNewPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationNewPaymentsAccounts:
    account_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationNewPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationNewPayments:
    accounts: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationNewPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationPaymentsAccounts:
    account_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationPayments:
    accounts: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesAccounts:
    account_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions') }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions') }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevels:
    invoice_level: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLevel') }})
    invoice_line_level: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLineLevel') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingPeriod:
    grouping_period_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriodOptions') }})
    selected_grouping_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupingPeriod') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGrouping:
    grouping_levels: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevels] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingLevels') }})
    grouping_period: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingPeriod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriod') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesInvoiceStatus:
    invoice_status_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatusOptions') }})
    selected_invoice_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedInvoiceStatus') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesAccountingTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesCommerceTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesTaxRateMappings:
    selected_accounting_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountingTaxRateId') }})
    selected_commerce_tax_rate_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCommerceTaxRateIds') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRates:
    accounting_tax_rate_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesAccountingTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingTaxRateOptions') }})
    commerce_tax_rate_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesCommerceTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('commerceTaxRateOptions') }})
    default_zero_tax_rate_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('defaultZeroTaxRateOptions') }})
    selected_default_zero_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedDefaultZeroTaxRateId') }})
    tax_rate_mappings: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesTaxRateMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateMappings') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesSalesCustomerCustomerOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesSalesCustomer:
    customer_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesSalesCustomerCustomerOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerOptions') }})
    selected_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCustomerId') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesTaxRatesTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesTaxRates:
    selected_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedTaxRateId') }})
    tax_rate_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesTaxRatesTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSales:
    accounts: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationSalesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    grouping: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGrouping] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('grouping') }})
    invoice_status: Optional[ConfigureSync200ApplicationJSONConfigurationSalesInvoiceStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatus') }})
    new_tax_rates: Optional[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newTaxRates') }})
    sales_customer: Optional[ConfigureSync200ApplicationJSONConfigurationSalesSalesCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('salesCustomer') }})
    sync_sales: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncSales') }})
    tax_rates: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationSalesTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRates') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfiguration:
    fees: Optional[ConfigureSync200ApplicationJSONConfigurationFees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fees') }})
    new_payments: Optional[ConfigureSync200ApplicationJSONConfigurationNewPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newPayments') }})
    payments: Optional[ConfigureSync200ApplicationJSONConfigurationPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('payments') }})
    sales: Optional[ConfigureSync200ApplicationJSONConfigurationSales] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sales') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONSchedule:
    frequency_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequencyOptions') }})
    selected_frequency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedFrequency') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('startDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    sync_hour_utc: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncHourUtc') }})
    time_zone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeZone') }})
    

@dataclass_json
@dataclasses.dataclass
class ConfigureSync200ApplicationJSON:
    accounting_software_company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingSoftwareCompanyName') }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    configuration: Optional[ConfigureSync200ApplicationJSONConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    configured: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configured') }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }})
    schedule: Optional[ConfigureSync200ApplicationJSONSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schedule') }})
    

@dataclasses.dataclass
class ConfigureSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    configure_sync_200_application_json_object: Optional[ConfigureSync200ApplicationJSON] = dataclasses.field(default=None)
    