from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class GetSyncOptionsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSyncOptionsRequest:
    path_params: GetSyncOptionsPathParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFeesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFeesAccounts:
    account_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationFeesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFeesFeesSupplierSupplierOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFeesFeesSupplier:
    selected_supplier_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedSupplierId'), 'exclude': lambda f: f is None }})
    supplier_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationFeesFeesSupplierSupplierOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supplierOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationFees:
    accounts: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationFeesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    fees_supplier: Optional[GetSyncOptions200ApplicationJSONConfigurationFeesFeesSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feesSupplier'), 'exclude': lambda f: f is None }})
    sync_fees: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncFees'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationNewPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationNewPaymentsAccounts:
    account_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationNewPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationNewPayments:
    accounts: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationNewPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationPaymentsAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationPaymentsAccounts:
    account_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationPaymentsAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationPayments:
    accounts: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationPaymentsAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncPayments'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesAccountsAccountOptions:
    classification: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classification'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    nominal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nominalCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesAccounts:
    account_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesAccountsAccountOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountOptions'), 'exclude': lambda f: f is None }})
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('descriptionText'), 'exclude': lambda f: f is None }})
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('labelText'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions'), 'exclude': lambda f: f is None }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel:
    group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupByOptions'), 'exclude': lambda f: f is None }})
    selected_group_by_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupByOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevels:
    invoice_level: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLevel'), 'exclude': lambda f: f is None }})
    invoice_line_level: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevelsInvoiceLineLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceLineLevel'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingPeriod:
    grouping_period_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriodOptions'), 'exclude': lambda f: f is None }})
    selected_grouping_period: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedGroupingPeriod'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesGrouping:
    grouping_levels: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingLevels] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingLevels'), 'exclude': lambda f: f is None }})
    grouping_period: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGroupingGroupingPeriod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groupingPeriod'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesInvoiceStatus:
    invoice_status_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatusOptions'), 'exclude': lambda f: f is None }})
    selected_invoice_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedInvoiceStatus'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesAccountingTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesCommerceTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesTaxRateMappings:
    selected_accounting_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedAccountingTaxRateId'), 'exclude': lambda f: f is None }})
    selected_commerce_tax_rate_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCommerceTaxRateIds'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRates:
    accounting_tax_rate_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesAccountingTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingTaxRateOptions'), 'exclude': lambda f: f is None }})
    commerce_tax_rate_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesCommerceTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('commerceTaxRateOptions'), 'exclude': lambda f: f is None }})
    default_zero_tax_rate_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesDefaultZeroTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('defaultZeroTaxRateOptions'), 'exclude': lambda f: f is None }})
    selected_default_zero_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedDefaultZeroTaxRateId'), 'exclude': lambda f: f is None }})
    tax_rate_mappings: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRatesTaxRateMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateMappings'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesSalesCustomerCustomerOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesSalesCustomer:
    customer_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesSalesCustomerCustomerOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customerOptions'), 'exclude': lambda f: f is None }})
    selected_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedCustomerId'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesTaxRatesTaxRateOptions:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSalesTaxRates:
    selected_tax_rate_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedTaxRateId'), 'exclude': lambda f: f is None }})
    tax_rate_options: Optional[list[GetSyncOptions200ApplicationJSONConfigurationSalesTaxRatesTaxRateOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRateOptions'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfigurationSales:
    accounts: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationSalesAccounts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accounts'), 'exclude': lambda f: f is None }})
    grouping: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesGrouping] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('grouping'), 'exclude': lambda f: f is None }})
    invoice_status: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesInvoiceStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invoiceStatus'), 'exclude': lambda f: f is None }})
    new_tax_rates: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesNewTaxRates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newTaxRates'), 'exclude': lambda f: f is None }})
    sales_customer: Optional[GetSyncOptions200ApplicationJSONConfigurationSalesSalesCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('salesCustomer'), 'exclude': lambda f: f is None }})
    sync_sales: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncSales'), 'exclude': lambda f: f is None }})
    tax_rates: Optional[dict[str, GetSyncOptions200ApplicationJSONConfigurationSalesTaxRates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('taxRates'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONConfiguration:
    fees: Optional[GetSyncOptions200ApplicationJSONConfigurationFees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fees'), 'exclude': lambda f: f is None }})
    new_payments: Optional[GetSyncOptions200ApplicationJSONConfigurationNewPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newPayments'), 'exclude': lambda f: f is None }})
    payments: Optional[GetSyncOptions200ApplicationJSONConfigurationPayments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('payments'), 'exclude': lambda f: f is None }})
    sales: Optional[GetSyncOptions200ApplicationJSONConfigurationSales] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sales'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSONSchedule:
    frequency_options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequencyOptions'), 'exclude': lambda f: f is None }})
    selected_frequency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('selectedFrequency'), 'exclude': lambda f: f is None }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('startDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    sync_hour_utc: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncHourUtc'), 'exclude': lambda f: f is None }})
    time_zone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('timeZone'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncOptions200ApplicationJSON:
    accounting_software_company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('accountingSoftwareCompanyName'), 'exclude': lambda f: f is None }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId'), 'exclude': lambda f: f is None }})
    configuration: Optional[GetSyncOptions200ApplicationJSONConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration'), 'exclude': lambda f: f is None }})
    configured: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('configured'), 'exclude': lambda f: f is None }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled'), 'exclude': lambda f: f is None }})
    schedule: Optional[GetSyncOptions200ApplicationJSONSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schedule'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetSyncOptionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_sync_options_200_application_json_object: Optional[GetSyncOptions200ApplicationJSON] = dataclasses.field(default=None)
    