"""codat_sync_for_payables.models.shared — domain-shared models."""

from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .security import Security, SecurityTypedDict
    from codat_sync_for_payables.models.shared.accountmappingoption import AccountMappingOption, AccountMappingOptionTypedDict
    from codat_sync_for_payables.models.shared.accountstatus import AccountStatus
    from codat_sync_for_payables.models.shared.address import Address, AddressTypedDict
    from codat_sync_for_payables.models.shared.addresstype import AddressType
    from codat_sync_for_payables.models.shared.attachment import Attachment, AttachmentTypedDict
    from codat_sync_for_payables.models.shared.bankaccount import BankAccount, BankAccountTypedDict
    from codat_sync_for_payables.models.shared.bankaccountmappingoption import BankAccountMappingOption, BankAccountMappingOptionTypedDict
    from codat_sync_for_payables.models.shared.bankaccountprototype import BankAccountPrototype, BankAccountPrototypeTypedDict
    from codat_sync_for_payables.models.shared.bankaccountstatus import BankAccountStatus
    from codat_sync_for_payables.models.shared.bankaccounttype import BankAccountType
    from codat_sync_for_payables.models.shared.bill import Bill, BillTypedDict
    from codat_sync_for_payables.models.shared.billaccountref import BillAccountRef, BillAccountRefTypedDict
    from codat_sync_for_payables.models.bill_data_type import BillDataType
    from codat_sync_for_payables.models.bill_event_payload import BillEventPayload, BillEventPayloadTypedDict
    from codat_sync_for_payables.models.bill_event_webhook import BillEventWebhook, BillEventWebhookTypedDict
    from codat_sync_for_payables.models.shared.billlineitem import BillLineItem, BillLineItemTypedDict
    from codat_sync_for_payables.models.shared.billmappingoptions import BillMappingOptions, BillMappingOptionsTypedDict
    from codat_sync_for_payables.models.shared.billpayment import BillPayment, BillPaymentTypedDict
    from codat_sync_for_payables.models.shared.billpaymentaccountref import BillPaymentAccountRef, BillPaymentAccountRefTypedDict
    from codat_sync_for_payables.models.shared.billpaymentprototype import BillPaymentPrototype, BillPaymentPrototypeTypedDict
    from codat_sync_for_payables.models.shared.billprototype import BillPrototype, BillPrototypeTypedDict
    from codat_sync_for_payables.models.shared.billstatus import BillStatus
    from codat_sync_for_payables.models.shared.billtaxrateref import BillTaxRateRef, BillTaxRateRefTypedDict
    from codat_sync_for_payables.models.shared.bills import Bills, BillsTypedDict
    from codat_sync_for_payables.models.shared.clientratelimitwebhook import ClientRateLimitWebhook, ClientRateLimitWebhookTypedDict
    from codat_sync_for_payables.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayload, ClientRateLimitWebhookPayloadTypedDict
    from codat_sync_for_payables.models.shared.companies import Companies, CompaniesTypedDict
    from codat_sync_for_payables.models.shared.company import Company, CompanyTypedDict
    from codat_sync_for_payables.models.company_details import CompanyDetails, CompanyDetailsTypedDict
    from codat_sync_for_payables.models.shared.companyinformation import CompanyInformation, CompanyInformationTypedDict
    from codat_sync_for_payables.models.shared.companyreference import CompanyReference, CompanyReferenceTypedDict
    from codat_sync_for_payables.models.company_reference_links import CompanyReferenceLinks, CompanyReferenceLinksTypedDict
    from codat_sync_for_payables.models.shared.companyrequestbody import CompanyRequestBody, CompanyRequestBodyTypedDict
    from codat_sync_for_payables.models.shared.companyupdaterequest import CompanyUpdateRequest, CompanyUpdateRequestTypedDict
    from codat_sync_for_payables.models.shared.connection import Connection, ConnectionTypedDict
    from codat_sync_for_payables.models.shared.connections import Connections, ConnectionsTypedDict
    from codat_sync_for_payables.models.create_connection_request import CreateConnectionRequest, CreateConnectionRequestTypedDict
    from codat_sync_for_payables.models.current_status import CurrentStatus
    from codat_sync_for_payables.models.shared.dataconnectionerror import DataConnectionError, DataConnectionErrorTypedDict
    from codat_sync_for_payables.models.shared.dataconnectionstatus import DataConnectionStatus
    from codat_sync_for_payables.models.data_status import DataStatus, DataStatusTypedDict
    from codat_sync_for_payables.models.data_type import DataType
    from codat_sync_for_payables.models.data_types import DataTypes
    from codat_sync_for_payables.models.dataset_status import DatasetStatus
    from codat_sync_for_payables.models.error_message import ErrorMessage, ErrorMessageTypedDict
    from codat_sync_for_payables.models.error_status import ErrorStatus
    from codat_sync_for_payables.models.shared.errorvalidation import ErrorValidation, ErrorValidationTypedDict
    from codat_sync_for_payables.models.shared.errorvalidationitem import ErrorValidationItem, ErrorValidationItemTypedDict
    from codat_sync_for_payables.models.shared.halref import HalRef, HalRefTypedDict
    from codat_sync_for_payables.models.shared.links import Links, LinksTypedDict
    from codat_sync_for_payables.models.shared.pagination import Pagination, PaginationTypedDict
    from codat_sync_for_payables.models.paging_info import PagingInfo, PagingInfoTypedDict
    from codat_sync_for_payables.models.shared.paymentmappingoptions import PaymentMappingOptions, PaymentMappingOptionsTypedDict
    from codat_sync_for_payables.models.pull_operation import PullOperation, PullOperationTypedDict
    from codat_sync_for_payables.models.pull_operations import PullOperations, PullOperationsTypedDict
    from codat_sync_for_payables.models.push_change_type import PushChangeType
    from codat_sync_for_payables.models.push_operation import PushOperation, PushOperationTypedDict
    from codat_sync_for_payables.models.push_operation_change import PushOperationChange, PushOperationChangeTypedDict
    from codat_sync_for_payables.models.push_operation_ref import PushOperationRef, PushOperationRefTypedDict
    from codat_sync_for_payables.models.push_operation_status import PushOperationStatus
    from codat_sync_for_payables.models.push_operations import PushOperations, PushOperationsTypedDict
    from codat_sync_for_payables.models.source_modified_date import SourceModifiedDate, SourceModifiedDateTypedDict
    from codat_sync_for_payables.models.source_type import SourceType
    from codat_sync_for_payables.models.status import Status
    from codat_sync_for_payables.models.shared.supplier import Supplier, SupplierTypedDict
    from codat_sync_for_payables.models.shared.supplierprototype import SupplierPrototype, SupplierPrototypeTypedDict
    from codat_sync_for_payables.models.shared.supplierref import SupplierRef, SupplierRefTypedDict
    from codat_sync_for_payables.models.shared.supplierstatus import SupplierStatus
    from codat_sync_for_payables.models.shared.suppliers import Suppliers, SuppliersTypedDict
    from codat_sync_for_payables.models.shared.taxratemappingoption import TaxRateMappingOption, TaxRateMappingOptionTypedDict
    from codat_sync_for_payables.models.tax_rate_status import TaxRateStatus
    from codat_sync_for_payables.models.shared.trackingref import TrackingRef, TrackingRefTypedDict
    from codat_sync_for_payables.models.update_connection import UpdateConnection, UpdateConnectionTypedDict
    from codat_sync_for_payables.models.validation import Validation, ValidationTypedDict
    from codat_sync_for_payables.models.validation_item import ValidationItem, ValidationItemTypedDict
    from codat_sync_for_payables.models.shared.accountmappingoption import AccountMappingOptionTypedDict as AccountMappingOptionTypedDict
    from codat_sync_for_payables.models.shared.accountstatus import AccountStatus as AccountStatus
    from codat_sync_for_payables.models.shared.addresstype import AddressType as AddressType
    from codat_sync_for_payables.models.shared.address import AddressTypedDict as AddressTypedDict
    from codat_sync_for_payables.models.shared.attachment import AttachmentTypedDict as AttachmentTypedDict
    from codat_sync_for_payables.models.shared.bankaccountmappingoption import BankAccountMappingOptionTypedDict as BankAccountMappingOptionTypedDict
    from codat_sync_for_payables.models.shared.bankaccountprototype import BankAccountPrototypeTypedDict as BankAccountPrototypeTypedDict
    from codat_sync_for_payables.models.shared.bankaccountstatus import BankAccountStatus as BankAccountStatus
    from codat_sync_for_payables.models.shared.bankaccounttype import BankAccountType as BankAccountType
    from codat_sync_for_payables.models.shared.bankaccount import BankAccountTypedDict as BankAccountTypedDict
    from codat_sync_for_payables.models.shared.billaccountref import BillAccountRefTypedDict as BillAccountRefTypedDict
    from codat_sync_for_payables.models.shared.billlineitem import BillLineItemTypedDict as BillLineItemTypedDict
    from codat_sync_for_payables.models.shared.billmappingoptions import BillMappingOptionsTypedDict as BillMappingOptionsTypedDict
    from codat_sync_for_payables.models.shared.billpaymentaccountref import BillPaymentAccountRefTypedDict as BillPaymentAccountRefTypedDict
    from codat_sync_for_payables.models.shared.billpaymentprototype import BillPaymentPrototypeTypedDict as BillPaymentPrototypeTypedDict
    from codat_sync_for_payables.models.shared.billpayment import BillPaymentTypedDict as BillPaymentTypedDict
    from codat_sync_for_payables.models.shared.billprototype import BillPrototypeTypedDict as BillPrototypeTypedDict
    from codat_sync_for_payables.models.shared.billstatus import BillStatus as BillStatus
    from codat_sync_for_payables.models.shared.billtaxrateref import BillTaxRateRefTypedDict as BillTaxRateRefTypedDict
    from codat_sync_for_payables.models.shared.bill import BillTypedDict as BillTypedDict
    from codat_sync_for_payables.models.shared.bills import BillsTypedDict as BillsTypedDict
    from codat_sync_for_payables.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayloadTypedDict as ClientRateLimitWebhookPayloadTypedDict
    from codat_sync_for_payables.models.shared.clientratelimitwebhook import ClientRateLimitWebhookTypedDict as ClientRateLimitWebhookTypedDict
    from codat_sync_for_payables.models.shared.companies import CompaniesTypedDict as CompaniesTypedDict
    from codat_sync_for_payables.models.shared.companyinformation import CompanyInformationTypedDict as CompanyInformationTypedDict
    from codat_sync_for_payables.models.company_reference_links import CompanyReferenceLinksTypedDict as CompanyReferenceLinksTypedDict
    from codat_sync_for_payables.models.shared.companyreference import CompanyReferenceTypedDict as CompanyReferenceTypedDict
    from codat_sync_for_payables.models.shared.companyrequestbody import CompanyRequestBodyTypedDict as CompanyRequestBodyTypedDict
    from codat_sync_for_payables.models.shared.company import CompanyTypedDict as CompanyTypedDict
    from codat_sync_for_payables.models.shared.companyupdaterequest import CompanyUpdateRequestTypedDict as CompanyUpdateRequestTypedDict
    from codat_sync_for_payables.models.shared.connection import ConnectionTypedDict as ConnectionTypedDict
    from codat_sync_for_payables.models.shared.connections import ConnectionsTypedDict as ConnectionsTypedDict
    from codat_sync_for_payables.models.shared.dataconnectionerror import DataConnectionErrorTypedDict as DataConnectionErrorTypedDict
    from codat_sync_for_payables.models.shared.dataconnectionstatus import DataConnectionStatus as DataConnectionStatus
    from codat_sync_for_payables.models.data_type import DataType as DataType
    from codat_sync_for_payables.models.error_status import ErrorStatus as ErrorStatus
    from codat_sync_for_payables.models.shared.errorvalidationitem import ErrorValidationItemTypedDict as ErrorValidationItemTypedDict
    from codat_sync_for_payables.models.shared.errorvalidation import ErrorValidationTypedDict as ErrorValidationTypedDict
    from codat_sync_for_payables.models.shared.halref import HalRefTypedDict as HalRefTypedDict
    from codat_sync_for_payables.models.shared.links import LinksTypedDict as LinksTypedDict
    from codat_sync_for_payables.models.shared.pagination import PaginationTypedDict as PaginationTypedDict
    from codat_sync_for_payables.models.shared.paymentmappingoptions import PaymentMappingOptionsTypedDict as PaymentMappingOptionsTypedDict
    from codat_sync_for_payables.models.shared.security import Security as Security
    from codat_sync_for_payables.models.shared.security import SecurityTypedDict as SecurityTypedDict
    from codat_sync_for_payables.models.source_type import SourceType as SourceType
    from codat_sync_for_payables.models.shared.supplierprototype import SupplierPrototypeTypedDict as SupplierPrototypeTypedDict
    from codat_sync_for_payables.models.shared.supplierref import SupplierRefTypedDict as SupplierRefTypedDict
    from codat_sync_for_payables.models.shared.supplierstatus import SupplierStatus as SupplierStatus
    from codat_sync_for_payables.models.shared.supplier import SupplierTypedDict as SupplierTypedDict
    from codat_sync_for_payables.models.shared.suppliers import SuppliersTypedDict as SuppliersTypedDict
    from codat_sync_for_payables.models.shared.taxratemappingoption import TaxRateMappingOptionTypedDict as TaxRateMappingOptionTypedDict
    from codat_sync_for_payables.models.tax_rate_status import TaxRateStatus as TaxRateStatus
    from codat_sync_for_payables.models.shared.trackingref import TrackingRefTypedDict as TrackingRefTypedDict
    from codat_sync_for_payables.models.shared.codatfile import CodatFile, CodatFileTypedDict
    from codat_sync_for_payables.models.shared.attachmentupload import AttachmentUpload, AttachmentUploadTypedDict

_dynamic_imports: dict[str, tuple[str, str]] = {
    'AccountMappingOption': ('codat_sync_for_payables.models.shared.accountmappingoption', 'AccountMappingOption'),
    'AccountMappingOptionTypedDict': ('codat_sync_for_payables.models.shared.accountmappingoption', 'AccountMappingOptionTypedDict'),
    'AccountStatus': ('codat_sync_for_payables.models.shared.accountstatus', 'AccountStatus'),
    'Address': ('codat_sync_for_payables.models.shared.address', 'Address'),
    'AddressType': ('codat_sync_for_payables.models.shared.addresstype', 'AddressType'),
    'AddressTypedDict': ('codat_sync_for_payables.models.shared.address', 'AddressTypedDict'),
    'Attachment': ('codat_sync_for_payables.models.shared.attachment', 'Attachment'),
    'AttachmentTypedDict': ('codat_sync_for_payables.models.shared.attachment', 'AttachmentTypedDict'),
    'AttachmentUpload': ('codat_sync_for_payables.models.shared.attachmentupload', 'AttachmentUpload'),
    'AttachmentUploadTypedDict': ('codat_sync_for_payables.models.shared.attachmentupload', 'AttachmentUploadTypedDict'),
    'BankAccount': ('codat_sync_for_payables.models.shared.bankaccount', 'BankAccount'),
    'BankAccountMappingOption': ('codat_sync_for_payables.models.shared.bankaccountmappingoption', 'BankAccountMappingOption'),
    'BankAccountMappingOptionTypedDict': ('codat_sync_for_payables.models.shared.bankaccountmappingoption', 'BankAccountMappingOptionTypedDict'),
    'BankAccountPrototype': ('codat_sync_for_payables.models.shared.bankaccountprototype', 'BankAccountPrototype'),
    'BankAccountPrototypeTypedDict': ('codat_sync_for_payables.models.shared.bankaccountprototype', 'BankAccountPrototypeTypedDict'),
    'BankAccountStatus': ('codat_sync_for_payables.models.shared.bankaccountstatus', 'BankAccountStatus'),
    'BankAccountType': ('codat_sync_for_payables.models.shared.bankaccounttype', 'BankAccountType'),
    'BankAccountTypedDict': ('codat_sync_for_payables.models.shared.bankaccount', 'BankAccountTypedDict'),
    'Bill': ('codat_sync_for_payables.models.shared.bill', 'Bill'),
    'BillAccountRef': ('codat_sync_for_payables.models.shared.billaccountref', 'BillAccountRef'),
    'BillAccountRefTypedDict': ('codat_sync_for_payables.models.shared.billaccountref', 'BillAccountRefTypedDict'),
    'BillDataType': ('codat_sync_for_payables.models.bill_data_type', 'BillDataType'),
    'BillEventPayload': ('codat_sync_for_payables.models.bill_event_payload', 'BillEventPayload'),
    'BillEventPayloadTypedDict': ('codat_sync_for_payables.models.bill_event_payload', 'BillEventPayloadTypedDict'),
    'BillEventWebhook': ('codat_sync_for_payables.models.bill_event_webhook', 'BillEventWebhook'),
    'BillEventWebhookTypedDict': ('codat_sync_for_payables.models.bill_event_webhook', 'BillEventWebhookTypedDict'),
    'BillLineItem': ('codat_sync_for_payables.models.shared.billlineitem', 'BillLineItem'),
    'BillLineItemTypedDict': ('codat_sync_for_payables.models.shared.billlineitem', 'BillLineItemTypedDict'),
    'BillMappingOptions': ('codat_sync_for_payables.models.shared.billmappingoptions', 'BillMappingOptions'),
    'BillMappingOptionsTypedDict': ('codat_sync_for_payables.models.shared.billmappingoptions', 'BillMappingOptionsTypedDict'),
    'BillPayment': ('codat_sync_for_payables.models.shared.billpayment', 'BillPayment'),
    'BillPaymentAccountRef': ('codat_sync_for_payables.models.shared.billpaymentaccountref', 'BillPaymentAccountRef'),
    'BillPaymentAccountRefTypedDict': ('codat_sync_for_payables.models.shared.billpaymentaccountref', 'BillPaymentAccountRefTypedDict'),
    'BillPaymentPrototype': ('codat_sync_for_payables.models.shared.billpaymentprototype', 'BillPaymentPrototype'),
    'BillPaymentPrototypeTypedDict': ('codat_sync_for_payables.models.shared.billpaymentprototype', 'BillPaymentPrototypeTypedDict'),
    'BillPaymentTypedDict': ('codat_sync_for_payables.models.shared.billpayment', 'BillPaymentTypedDict'),
    'BillPrototype': ('codat_sync_for_payables.models.shared.billprototype', 'BillPrototype'),
    'BillPrototypeTypedDict': ('codat_sync_for_payables.models.shared.billprototype', 'BillPrototypeTypedDict'),
    'BillStatus': ('codat_sync_for_payables.models.shared.billstatus', 'BillStatus'),
    'BillTaxRateRef': ('codat_sync_for_payables.models.shared.billtaxrateref', 'BillTaxRateRef'),
    'BillTaxRateRefTypedDict': ('codat_sync_for_payables.models.shared.billtaxrateref', 'BillTaxRateRefTypedDict'),
    'BillTypedDict': ('codat_sync_for_payables.models.shared.bill', 'BillTypedDict'),
    'Bills': ('codat_sync_for_payables.models.shared.bills', 'Bills'),
    'BillsTypedDict': ('codat_sync_for_payables.models.shared.bills', 'BillsTypedDict'),
    'ClientRateLimitWebhook': ('codat_sync_for_payables.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhook'),
    'ClientRateLimitWebhookPayload': ('codat_sync_for_payables.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayload'),
    'ClientRateLimitWebhookPayloadTypedDict': ('codat_sync_for_payables.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayloadTypedDict'),
    'ClientRateLimitWebhookTypedDict': ('codat_sync_for_payables.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhookTypedDict'),
    'CodatFile': ('codat_sync_for_payables.models.shared.codatfile', 'CodatFile'),
    'CodatFileTypedDict': ('codat_sync_for_payables.models.shared.codatfile', 'CodatFileTypedDict'),
    'Companies': ('codat_sync_for_payables.models.shared.companies', 'Companies'),
    'CompaniesTypedDict': ('codat_sync_for_payables.models.shared.companies', 'CompaniesTypedDict'),
    'Company': ('codat_sync_for_payables.models.shared.company', 'Company'),
    'CompanyDetails': ('codat_sync_for_payables.models.company_details', 'CompanyDetails'),
    'CompanyDetailsTypedDict': ('codat_sync_for_payables.models.company_details', 'CompanyDetailsTypedDict'),
    'CompanyInformation': ('codat_sync_for_payables.models.shared.companyinformation', 'CompanyInformation'),
    'CompanyInformationTypedDict': ('codat_sync_for_payables.models.shared.companyinformation', 'CompanyInformationTypedDict'),
    'CompanyReference': ('codat_sync_for_payables.models.shared.companyreference', 'CompanyReference'),
    'CompanyReferenceLinks': ('codat_sync_for_payables.models.company_reference_links', 'CompanyReferenceLinks'),
    'CompanyReferenceLinksTypedDict': ('codat_sync_for_payables.models.company_reference_links', 'CompanyReferenceLinksTypedDict'),
    'CompanyReferenceTypedDict': ('codat_sync_for_payables.models.shared.companyreference', 'CompanyReferenceTypedDict'),
    'CompanyRequestBody': ('codat_sync_for_payables.models.shared.companyrequestbody', 'CompanyRequestBody'),
    'CompanyRequestBodyTypedDict': ('codat_sync_for_payables.models.shared.companyrequestbody', 'CompanyRequestBodyTypedDict'),
    'CompanyTypedDict': ('codat_sync_for_payables.models.shared.company', 'CompanyTypedDict'),
    'CompanyUpdateRequest': ('codat_sync_for_payables.models.shared.companyupdaterequest', 'CompanyUpdateRequest'),
    'CompanyUpdateRequestTypedDict': ('codat_sync_for_payables.models.shared.companyupdaterequest', 'CompanyUpdateRequestTypedDict'),
    'Connection': ('codat_sync_for_payables.models.shared.connection', 'Connection'),
    'ConnectionTypedDict': ('codat_sync_for_payables.models.shared.connection', 'ConnectionTypedDict'),
    'Connections': ('codat_sync_for_payables.models.shared.connections', 'Connections'),
    'ConnectionsTypedDict': ('codat_sync_for_payables.models.shared.connections', 'ConnectionsTypedDict'),
    'CreateConnectionRequest': ('codat_sync_for_payables.models.create_connection_request', 'CreateConnectionRequest'),
    'CreateConnectionRequestTypedDict': ('codat_sync_for_payables.models.create_connection_request', 'CreateConnectionRequestTypedDict'),
    'CurrentStatus': ('codat_sync_for_payables.models.current_status', 'CurrentStatus'),
    'DataConnectionError': ('codat_sync_for_payables.models.shared.dataconnectionerror', 'DataConnectionError'),
    'DataConnectionErrorTypedDict': ('codat_sync_for_payables.models.shared.dataconnectionerror', 'DataConnectionErrorTypedDict'),
    'DataConnectionStatus': ('codat_sync_for_payables.models.shared.dataconnectionstatus', 'DataConnectionStatus'),
    'DataStatus': ('codat_sync_for_payables.models.data_status', 'DataStatus'),
    'DataStatusTypedDict': ('codat_sync_for_payables.models.data_status', 'DataStatusTypedDict'),
    'DataType': ('codat_sync_for_payables.models.data_type', 'DataType'),
    'DataTypes': ('codat_sync_for_payables.models.data_types', 'DataTypes'),
    'DatasetStatus': ('codat_sync_for_payables.models.dataset_status', 'DatasetStatus'),
    'ErrorMessage': ('codat_sync_for_payables.models.error_message', 'ErrorMessage'),
    'ErrorMessageTypedDict': ('codat_sync_for_payables.models.error_message', 'ErrorMessageTypedDict'),
    'ErrorStatus': ('codat_sync_for_payables.models.error_status', 'ErrorStatus'),
    'ErrorValidation': ('codat_sync_for_payables.models.shared.errorvalidation', 'ErrorValidation'),
    'ErrorValidationItem': ('codat_sync_for_payables.models.shared.errorvalidationitem', 'ErrorValidationItem'),
    'ErrorValidationItemTypedDict': ('codat_sync_for_payables.models.shared.errorvalidationitem', 'ErrorValidationItemTypedDict'),
    'ErrorValidationTypedDict': ('codat_sync_for_payables.models.shared.errorvalidation', 'ErrorValidationTypedDict'),
    'HalRef': ('codat_sync_for_payables.models.shared.halref', 'HalRef'),
    'HalRefTypedDict': ('codat_sync_for_payables.models.shared.halref', 'HalRefTypedDict'),
    'Links': ('codat_sync_for_payables.models.shared.links', 'Links'),
    'LinksTypedDict': ('codat_sync_for_payables.models.shared.links', 'LinksTypedDict'),
    'Pagination': ('codat_sync_for_payables.models.shared.pagination', 'Pagination'),
    'PaginationTypedDict': ('codat_sync_for_payables.models.shared.pagination', 'PaginationTypedDict'),
    'PagingInfo': ('codat_sync_for_payables.models.paging_info', 'PagingInfo'),
    'PagingInfoTypedDict': ('codat_sync_for_payables.models.paging_info', 'PagingInfoTypedDict'),
    'PaymentMappingOptions': ('codat_sync_for_payables.models.shared.paymentmappingoptions', 'PaymentMappingOptions'),
    'PaymentMappingOptionsTypedDict': ('codat_sync_for_payables.models.shared.paymentmappingoptions', 'PaymentMappingOptionsTypedDict'),
    'PullOperation': ('codat_sync_for_payables.models.pull_operation', 'PullOperation'),
    'PullOperationTypedDict': ('codat_sync_for_payables.models.pull_operation', 'PullOperationTypedDict'),
    'PullOperations': ('codat_sync_for_payables.models.pull_operations', 'PullOperations'),
    'PullOperationsTypedDict': ('codat_sync_for_payables.models.pull_operations', 'PullOperationsTypedDict'),
    'PushChangeType': ('codat_sync_for_payables.models.push_change_type', 'PushChangeType'),
    'PushOperation': ('codat_sync_for_payables.models.push_operation', 'PushOperation'),
    'PushOperationChange': ('codat_sync_for_payables.models.push_operation_change', 'PushOperationChange'),
    'PushOperationChangeTypedDict': ('codat_sync_for_payables.models.push_operation_change', 'PushOperationChangeTypedDict'),
    'PushOperationRef': ('codat_sync_for_payables.models.push_operation_ref', 'PushOperationRef'),
    'PushOperationRefTypedDict': ('codat_sync_for_payables.models.push_operation_ref', 'PushOperationRefTypedDict'),
    'PushOperationStatus': ('codat_sync_for_payables.models.push_operation_status', 'PushOperationStatus'),
    'PushOperationTypedDict': ('codat_sync_for_payables.models.push_operation', 'PushOperationTypedDict'),
    'PushOperations': ('codat_sync_for_payables.models.push_operations', 'PushOperations'),
    'PushOperationsTypedDict': ('codat_sync_for_payables.models.push_operations', 'PushOperationsTypedDict'),
    'Security': ('codat_sync_for_payables.models.shared.security', 'Security'),
    'SecurityTypedDict': ('codat_sync_for_payables.models.shared.security', 'SecurityTypedDict'),
    'SourceModifiedDate': ('codat_sync_for_payables.models.source_modified_date', 'SourceModifiedDate'),
    'SourceModifiedDateTypedDict': ('codat_sync_for_payables.models.source_modified_date', 'SourceModifiedDateTypedDict'),
    'SourceType': ('codat_sync_for_payables.models.source_type', 'SourceType'),
    'Status': ('codat_sync_for_payables.models.status', 'Status'),
    'Supplier': ('codat_sync_for_payables.models.shared.supplier', 'Supplier'),
    'SupplierPrototype': ('codat_sync_for_payables.models.shared.supplierprototype', 'SupplierPrototype'),
    'SupplierPrototypeTypedDict': ('codat_sync_for_payables.models.shared.supplierprototype', 'SupplierPrototypeTypedDict'),
    'SupplierRef': ('codat_sync_for_payables.models.shared.supplierref', 'SupplierRef'),
    'SupplierRefTypedDict': ('codat_sync_for_payables.models.shared.supplierref', 'SupplierRefTypedDict'),
    'SupplierStatus': ('codat_sync_for_payables.models.shared.supplierstatus', 'SupplierStatus'),
    'SupplierTypedDict': ('codat_sync_for_payables.models.shared.supplier', 'SupplierTypedDict'),
    'Suppliers': ('codat_sync_for_payables.models.shared.suppliers', 'Suppliers'),
    'SuppliersTypedDict': ('codat_sync_for_payables.models.shared.suppliers', 'SuppliersTypedDict'),
    'TaxRateMappingOption': ('codat_sync_for_payables.models.shared.taxratemappingoption', 'TaxRateMappingOption'),
    'TaxRateMappingOptionTypedDict': ('codat_sync_for_payables.models.shared.taxratemappingoption', 'TaxRateMappingOptionTypedDict'),
    'TaxRateStatus': ('codat_sync_for_payables.models.tax_rate_status', 'TaxRateStatus'),
    'TrackingRef': ('codat_sync_for_payables.models.shared.trackingref', 'TrackingRef'),
    'TrackingRefTypedDict': ('codat_sync_for_payables.models.shared.trackingref', 'TrackingRefTypedDict'),
    'UpdateConnection': ('codat_sync_for_payables.models.update_connection', 'UpdateConnection'),
    'UpdateConnectionTypedDict': ('codat_sync_for_payables.models.update_connection', 'UpdateConnectionTypedDict'),
    'Validation': ('codat_sync_for_payables.models.validation', 'Validation'),
    'ValidationItem': ('codat_sync_for_payables.models.validation_item', 'ValidationItem'),
    'ValidationItemTypedDict': ('codat_sync_for_payables.models.validation_item', 'ValidationItemTypedDict'),
    'ValidationTypedDict': ('codat_sync_for_payables.models.validation', 'ValidationTypedDict'),
}


def __getattr__(attr_name):
    try:
        module_path, source_name = _dynamic_imports[attr_name]
    except KeyError:
        raise AttributeError(
            f"module {__name__!r} has no attribute {attr_name!r}"
        ) from None
    module = import_module(module_path, __package__)
    return getattr(module, source_name)


def __dir__():
    return sorted(set(globals()) | set(_dynamic_imports))
