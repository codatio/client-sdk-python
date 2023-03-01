from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class ConfigureSyncPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFeesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFeesAccounts:
    account_options: Optional[list[ConfigureSyncRequestBodyConfigurationFeesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFeesFeesSupplierSupplierOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFeesFeesSupplier:
    selected_supplier_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedSupplierId'), 'exclude': lambda f: f is None }})
    supplier_options: Optional[list[ConfigureSyncRequestBodyConfigurationFeesFeesSupplierSupplierOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationFees:
    accounts: Optional[dict[str, ConfigureSyncRequestBodyConfigurationFeesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    fees_supplier: Optional[ConfigureSyncRequestBodyConfigurationFeesFeesSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feesSupplier'), 'exclude': lambda f: f is None }})
    sync_fees: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncFees'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationNewPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationNewPaymentsAccounts:
    account_options: Optional[list[ConfigureSyncRequestBodyConfigurationNewPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationNewPayments:
    accounts: Optional[dict[str, ConfigureSyncRequestBodyConfigurationNewPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationPaymentsAccounts:
    account_options: Optional[list[ConfigureSyncRequestBodyConfigurationPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationPayments:
    accounts: Optional[dict[str, ConfigureSyncRequestBodyConfigurationPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesAccounts:
    account_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevelsInvoiceLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions'), 'exclude': lambda f: f is None }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions'), 'exclude': lambda f: f is None }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevels:
    invoice_level: Optional[ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevelsInvoiceLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLevel'), 'exclude': lambda f: f is None }})
    invoice_line_level: Optional[ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLineLevel'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingPeriod:
    grouping_period_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriodOptions'), 'exclude': lambda f: f is None }})
    selected_grouping_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupingPeriod'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesGrouping:
    grouping_levels: Optional[ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingLevels] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingLevels'), 'exclude': lambda f: f is None }})
    grouping_period: Optional[ConfigureSyncRequestBodyConfigurationSalesGroupingGroupingPeriod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriod'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesInvoiceStatus:
    invoice_status_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatusOptions'), 'exclude': lambda f: f is None }})
    selected_invoice_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedInvoiceStatus'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesAccountingTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesCommerceTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesTaxRateMappings:
    selected_accounting_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountingTaxRateId'), 'exclude': lambda f: f is None }})
    selected_commerce_tax_rate_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCommerceTaxRateIds'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesNewTaxRates:
    accounting_tax_rate_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesAccountingTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingTaxRateOptions'), 'exclude': lambda f: f is None }})
    commerce_tax_rate_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesCommerceTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('commerceTaxRateOptions'), 'exclude': lambda f: f is None }})
    default_zero_tax_rate_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('defaultZeroTaxRateOptions'), 'exclude': lambda f: f is None }})
    selected_default_zero_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedDefaultZeroTaxRateId'), 'exclude': lambda f: f is None }})
    tax_rate_mappings: Optional[list[ConfigureSyncRequestBodyConfigurationSalesNewTaxRatesTaxRateMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateMappings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesSalesCustomerCustomerOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesSalesCustomer:
    customer_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesSalesCustomerCustomerOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerOptions'), 'exclude': lambda f: f is None }})
    selected_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCustomerId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesTaxRatesTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSalesTaxRates:
    selected_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedTaxRateId'), 'exclude': lambda f: f is None }})
    tax_rate_options: Optional[list[ConfigureSyncRequestBodyConfigurationSalesTaxRatesTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfigurationSales:
    accounts: Optional[dict[str, ConfigureSyncRequestBodyConfigurationSalesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    grouping: Optional[ConfigureSyncRequestBodyConfigurationSalesGrouping] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('grouping'), 'exclude': lambda f: f is None }})
    invoice_status: Optional[ConfigureSyncRequestBodyConfigurationSalesInvoiceStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatus'), 'exclude': lambda f: f is None }})
    new_tax_rates: Optional[ConfigureSyncRequestBodyConfigurationSalesNewTaxRates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newTaxRates'), 'exclude': lambda f: f is None }})
    sales_customer: Optional[ConfigureSyncRequestBodyConfigurationSalesSalesCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('salesCustomer'), 'exclude': lambda f: f is None }})
    sync_sales: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncSales'), 'exclude': lambda f: f is None }})
    tax_rates: Optional[dict[str, ConfigureSyncRequestBodyConfigurationSalesTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRates'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodyConfiguration:
    fees: Optional[ConfigureSyncRequestBodyConfigurationFees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fees'), 'exclude': lambda f: f is None }})
    new_payments: Optional[ConfigureSyncRequestBodyConfigurationNewPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newPayments'), 'exclude': lambda f: f is None }})
    payments: Optional[ConfigureSyncRequestBodyConfigurationPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('payments'), 'exclude': lambda f: f is None }})
    sales: Optional[ConfigureSyncRequestBodyConfigurationSales] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sales'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBodySchedule:
    frequency_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequencyOptions'), 'exclude': lambda f: f is None }})
    selected_frequency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedFrequency'), 'exclude': lambda f: f is None }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('startDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    sync_hour_utc: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncHourUtc'), 'exclude': lambda f: f is None }})
    time_zone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeZone'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSyncRequestBody:
    accounting_software_company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingSoftwareCompanyName'), 'exclude': lambda f: f is None }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId'), 'exclude': lambda f: f is None }})
    configuration: Optional[ConfigureSyncRequestBodyConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration'), 'exclude': lambda f: f is None }})
    configured: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configured'), 'exclude': lambda f: f is None }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled'), 'exclude': lambda f: f is None }})
    schedule: Optional[ConfigureSyncRequestBodySchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schedule'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ConfigureSyncRequest:
    path_params: ConfigureSyncPathParams = dataclasses.field()
    request: Optional[ConfigureSyncRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFeesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFeesAccounts:
    account_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationFeesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFeesFeesSupplierSupplierOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFeesFeesSupplier:
    selected_supplier_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedSupplierId'), 'exclude': lambda f: f is None }})
    supplier_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationFeesFeesSupplierSupplierOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationFees:
    accounts: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationFeesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    fees_supplier: Optional[ConfigureSync200ApplicationJSONConfigurationFeesFeesSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feesSupplier'), 'exclude': lambda f: f is None }})
    sync_fees: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncFees'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationNewPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationNewPaymentsAccounts:
    account_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationNewPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationNewPayments:
    accounts: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationNewPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationPaymentsAccounts:
    account_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationPayments:
    accounts: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesAccounts:
    account_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions'), 'exclude': lambda f: f is None }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions'), 'exclude': lambda f: f is None }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevels:
    invoice_level: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLevel'), 'exclude': lambda f: f is None }})
    invoice_line_level: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLineLevel'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingPeriod:
    grouping_period_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriodOptions'), 'exclude': lambda f: f is None }})
    selected_grouping_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupingPeriod'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesGrouping:
    grouping_levels: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingLevels] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingLevels'), 'exclude': lambda f: f is None }})
    grouping_period: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGroupingGroupingPeriod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriod'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesInvoiceStatus:
    invoice_status_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatusOptions'), 'exclude': lambda f: f is None }})
    selected_invoice_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedInvoiceStatus'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesAccountingTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesCommerceTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesTaxRateMappings:
    selected_accounting_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountingTaxRateId'), 'exclude': lambda f: f is None }})
    selected_commerce_tax_rate_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCommerceTaxRateIds'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRates:
    accounting_tax_rate_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesAccountingTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingTaxRateOptions'), 'exclude': lambda f: f is None }})
    commerce_tax_rate_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesCommerceTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('commerceTaxRateOptions'), 'exclude': lambda f: f is None }})
    default_zero_tax_rate_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('defaultZeroTaxRateOptions'), 'exclude': lambda f: f is None }})
    selected_default_zero_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedDefaultZeroTaxRateId'), 'exclude': lambda f: f is None }})
    tax_rate_mappings: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRatesTaxRateMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateMappings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesSalesCustomerCustomerOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesSalesCustomer:
    customer_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesSalesCustomerCustomerOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerOptions'), 'exclude': lambda f: f is None }})
    selected_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCustomerId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesTaxRatesTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSalesTaxRates:
    selected_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedTaxRateId'), 'exclude': lambda f: f is None }})
    tax_rate_options: Optional[list[ConfigureSync200ApplicationJSONConfigurationSalesTaxRatesTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfigurationSales:
    accounts: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationSalesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    grouping: Optional[ConfigureSync200ApplicationJSONConfigurationSalesGrouping] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('grouping'), 'exclude': lambda f: f is None }})
    invoice_status: Optional[ConfigureSync200ApplicationJSONConfigurationSalesInvoiceStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatus'), 'exclude': lambda f: f is None }})
    new_tax_rates: Optional[ConfigureSync200ApplicationJSONConfigurationSalesNewTaxRates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newTaxRates'), 'exclude': lambda f: f is None }})
    sales_customer: Optional[ConfigureSync200ApplicationJSONConfigurationSalesSalesCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('salesCustomer'), 'exclude': lambda f: f is None }})
    sync_sales: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncSales'), 'exclude': lambda f: f is None }})
    tax_rates: Optional[dict[str, ConfigureSync200ApplicationJSONConfigurationSalesTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRates'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONConfiguration:
    fees: Optional[ConfigureSync200ApplicationJSONConfigurationFees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fees'), 'exclude': lambda f: f is None }})
    new_payments: Optional[ConfigureSync200ApplicationJSONConfigurationNewPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newPayments'), 'exclude': lambda f: f is None }})
    payments: Optional[ConfigureSync200ApplicationJSONConfigurationPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('payments'), 'exclude': lambda f: f is None }})
    sales: Optional[ConfigureSync200ApplicationJSONConfigurationSales] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sales'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSONSchedule:
    frequency_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequencyOptions'), 'exclude': lambda f: f is None }})
    selected_frequency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedFrequency'), 'exclude': lambda f: f is None }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('startDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    sync_hour_utc: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncHourUtc'), 'exclude': lambda f: f is None }})
    time_zone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeZone'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfigureSync200ApplicationJSON:
    accounting_software_company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingSoftwareCompanyName'), 'exclude': lambda f: f is None }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId'), 'exclude': lambda f: f is None }})
    configuration: Optional[ConfigureSync200ApplicationJSONConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration'), 'exclude': lambda f: f is None }})
    configured: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configured'), 'exclude': lambda f: f is None }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled'), 'exclude': lambda f: f is None }})
    schedule: Optional[ConfigureSync200ApplicationJSONSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schedule'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ConfigureSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    configure_sync_200_application_json_object: Optional[ConfigureSync200ApplicationJSON] = dataclasses.field(default=None)
    