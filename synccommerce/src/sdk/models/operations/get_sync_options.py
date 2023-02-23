import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetSyncOptionsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSyncOptionsRequest:
    path_params: GetSyncOptionsPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFeesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFeesAccounts:
    account_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationFeesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFeesFeesSupplierSupplierOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFeesFeesSupplier:
    selected_supplier_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedSupplierId') }})
    supplier_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationFeesFeesSupplierSupplierOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFees:
    accounts: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationFeesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    fees_supplier: Optional[GetSyncOptions200ApplicationJSONConfigurationFeesFeesSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feesSupplier') }})
    sync_fees: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncFees') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationNewPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationNewPaymentsAccounts:
    account_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationNewPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationNewPayments:
    accounts: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationNewPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationPaymentsAccounts:
    account_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationPayments:
    accounts: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesAccounts:
    account_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions') }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText') }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions') }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions') }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevels:
    invoice_level: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLevel') }})
    invoice_line_level: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLineLevel') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingPeriod:
    grouping_period_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriodOptions') }})
    selected_grouping_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupingPeriod') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGrouping:
    grouping_levels: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevels] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingLevels') }})
    grouping_period: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingPeriod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriod') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesInvoiceStatus:
    invoice_status_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatusOptions') }})
    selected_invoice_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedInvoiceStatus') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesAccountingTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesCommerceTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesTaxRateMappings:
    selected_accounting_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountingTaxRateId') }})
    selected_commerce_tax_rate_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCommerceTaxRateIds') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRates:
    accounting_tax_rate_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesAccountingTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingTaxRateOptions') }})
    commerce_tax_rate_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesCommerceTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('commerceTaxRateOptions') }})
    default_zero_tax_rate_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('defaultZeroTaxRateOptions') }})
    selected_default_zero_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedDefaultZeroTaxRateId') }})
    tax_rate_mappings: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesTaxRateMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateMappings') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesSalesCustomerCustomerOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesSalesCustomer:
    customer_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesSalesCustomerCustomerOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerOptions') }})
    selected_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCustomerId') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesTaxRatesTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesTaxRates:
    selected_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedTaxRateId') }})
    tax_rate_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesTaxRatesTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateOptions') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSales:
    accounts: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationSalesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts') }})
    grouping: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGrouping] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('grouping') }})
    invoice_status: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesInvoiceStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatus') }})
    new_tax_rates: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newTaxRates') }})
    sales_customer: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesSalesCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('salesCustomer') }})
    sync_sales: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncSales') }})
    tax_rates: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationSalesTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRates') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfiguration:
    fees: Optional[GetSyncOptions200ApplicationJSONConfigurationFees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fees') }})
    new_payments: Optional[GetSyncOptions200ApplicationJSONConfigurationNewPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newPayments') }})
    payments: Optional[GetSyncOptions200ApplicationJSONConfigurationPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('payments') }})
    sales: Optional[GetSyncOptions200ApplicationJSONConfigurationSales] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sales') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONSchedule:
    frequency_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequencyOptions') }})
    selected_frequency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedFrequency') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('startDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    sync_hour_utc: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncHourUtc') }})
    time_zone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeZone') }})
    

@dataclass_json
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSON:
    accounting_software_company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingSoftwareCompanyName') }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    configuration: Optional[GetSyncOptions200ApplicationJSONConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    configured: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configured') }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }})
    schedule: Optional[GetSyncOptions200ApplicationJSONSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schedule') }})
    

@dataclasses.dataclass
class GetSyncOptionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_sync_options_200_application_json_object: Optional[GetSyncOptions200ApplicationJSON] = dataclasses.field(default=None)
    