"""codat_sync_for_expenses.models.shared — domain-shared models."""

from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .security import Security, SecurityTypedDict
    from codat_sync_for_expenses.models.account import Account, AccountTypedDict
    from codat_sync_for_expenses.models.shared.accountmappinginfo import AccountMappingInfo, AccountMappingInfoTypedDict
    from codat_sync_for_expenses.models.account_mapping_info_account_type import AccountMappingInfoAccountType
    from codat_sync_for_expenses.models.shared.accountprototype import AccountPrototype, AccountPrototypeTypedDict
    from codat_sync_for_expenses.models.account_reference import AccountReference, AccountReferenceTypedDict
    from codat_sync_for_expenses.models.account_reference1 import AccountReference1, AccountReference1TypedDict
    from codat_sync_for_expenses.models.shared.accountstatus import AccountStatus
    from codat_sync_for_expenses.models.shared.accounttype import AccountType
    from codat_sync_for_expenses.models.accounting_address import AccountingAddress, AccountingAddressTypedDict
    from codat_sync_for_expenses.models.shared.accountingaddresstype import AccountingAddressType
    from codat_sync_for_expenses.models.shared.adjustmenttransactionline import AdjustmentTransactionLine, AdjustmentTransactionLineTypedDict
    from codat_sync_for_expenses.models.shared.adjustmenttransactionrequest import AdjustmentTransactionRequest, AdjustmentTransactionRequestTypedDict
    from codat_sync_for_expenses.models.shared.adjustmenttransactionresponse import AdjustmentTransactionResponse, AdjustmentTransactionResponseTypedDict
    from codat_sync_for_expenses.models.shared.apaccountref import ApAccountRef, ApAccountRefTypedDict
    from codat_sync_for_expenses.models.shared.attachment import Attachment, AttachmentTypedDict
    from codat_sync_for_expenses.models.shared.bankaccount import BankAccount, BankAccountTypedDict
    from codat_sync_for_expenses.models.shared.bankaccountdetails import BankAccountDetails, BankAccountDetailsTypedDict
    from codat_sync_for_expenses.models.bank_account_prototype import BankAccountPrototype, BankAccountPrototypeTypedDict
    from codat_sync_for_expenses.models.bank_account_reference import BankAccountReference, BankAccountReferenceTypedDict
    from codat_sync_for_expenses.models.shared.bankaccountstatus import BankAccountStatus
    from codat_sync_for_expenses.models.bank_account_type import BankAccountType
    from codat_sync_for_expenses.models.shared.clientratelimitwebhook import ClientRateLimitWebhook, ClientRateLimitWebhookTypedDict
    from codat_sync_for_expenses.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayload, ClientRateLimitWebhookPayloadTypedDict
    from codat_sync_for_expenses.models.shared.companies import Companies, CompaniesTypedDict
    from codat_sync_for_expenses.models.shared.company import Company, CompanyTypedDict
    from codat_sync_for_expenses.models.shared.companyconfiguration import CompanyConfiguration, CompanyConfigurationTypedDict
    from codat_sync_for_expenses.models.company_details import CompanyDetails, CompanyDetailsTypedDict
    from codat_sync_for_expenses.models.company_information import CompanyInformation, CompanyInformationTypedDict
    from codat_sync_for_expenses.models.company_information_type import CompanyInformationType
    from codat_sync_for_expenses.models.shared.companyreference import CompanyReference, CompanyReferenceTypedDict
    from codat_sync_for_expenses.models.company_reference_links import CompanyReferenceLinks, CompanyReferenceLinksTypedDict
    from codat_sync_for_expenses.models.shared.companyrequestbody import CompanyRequestBody, CompanyRequestBodyTypedDict
    from codat_sync_for_expenses.models.shared.companysyncstatus import CompanySyncStatus, CompanySyncStatusTypedDict
    from codat_sync_for_expenses.models.shared.companyupdaterequest import CompanyUpdateRequest, CompanyUpdateRequestTypedDict
    from codat_sync_for_expenses.models.shared.connection import Connection, ConnectionTypedDict
    from codat_sync_for_expenses.models.shared.connections import Connections, ConnectionsTypedDict
    from codat_sync_for_expenses.models.shared.contact import Contact, ContactTypedDict
    from codat_sync_for_expenses.models.shared.createaccountresponse import CreateAccountResponse, CreateAccountResponseTypedDict
    from codat_sync_for_expenses.models.create_account_response_all_of_data import CreateAccountResponseAllOfData, CreateAccountResponseAllOfDataTypedDict
    from codat_sync_for_expenses.models.create_bank_account_response import CreateBankAccountResponse, CreateBankAccountResponseTypedDict
    from codat_sync_for_expenses.models.create_bank_account_response_all_of_data import CreateBankAccountResponseAllOfData, CreateBankAccountResponseAllOfDataTypedDict
    from codat_sync_for_expenses.models.create_connection_request import CreateConnectionRequest, CreateConnectionRequestTypedDict
    from codat_sync_for_expenses.models.shared.createcustomerresponse import CreateCustomerResponse, CreateCustomerResponseTypedDict
    from codat_sync_for_expenses.models.create_customer_response_all_of_data import CreateCustomerResponseAllOfData, CreateCustomerResponseAllOfDataTypedDict
    from codat_sync_for_expenses.models.shared.createexpenseresponse import CreateExpenseResponse, CreateExpenseResponseTypedDict
    from codat_sync_for_expenses.models.shared.createreimbursableexpenseresponse import CreateReimbursableExpenseResponse, CreateReimbursableExpenseResponseTypedDict
    from codat_sync_for_expenses.models.shared.createsupplierresponse import CreateSupplierResponse, CreateSupplierResponseTypedDict
    from codat_sync_for_expenses.models.create_supplier_response_all_of_data import CreateSupplierResponseAllOfData, CreateSupplierResponseAllOfDataTypedDict
    from codat_sync_for_expenses.models.current_status import CurrentStatus
    from codat_sync_for_expenses.models.shared.customer import Customer, CustomerTypedDict
    from codat_sync_for_expenses.models.shared.customerdetails import CustomerDetails, CustomerDetailsTypedDict
    from codat_sync_for_expenses.models.shared.customerstatus import CustomerStatus
    from codat_sync_for_expenses.models.shared.customers import Customers, CustomersTypedDict
    from codat_sync_for_expenses.models.shared.dataconnectionerror import DataConnectionError, DataConnectionErrorTypedDict
    from codat_sync_for_expenses.models.shared.dataconnectionstatus import DataConnectionStatus
    from codat_sync_for_expenses.models.shared.datastatus import DataStatus, DataStatusTypedDict
    from codat_sync_for_expenses.models.data_statuses import DataStatuses, DataStatusesTypedDict
    from codat_sync_for_expenses.models.shared.datatype import DataType
    from codat_sync_for_expenses.models.data_types import DataTypes
    from codat_sync_for_expenses.models.dataset_status import DatasetStatus
    from codat_sync_for_expenses.models.error_message import ErrorMessage, ErrorMessageTypedDict
    from codat_sync_for_expenses.models.error_status import ErrorStatus
    from codat_sync_for_expenses.models.shared.errorvalidation import ErrorValidation, ErrorValidationTypedDict
    from codat_sync_for_expenses.models.shared.errorvalidationitem import ErrorValidationItem, ErrorValidationItemTypedDict
    from codat_sync_for_expenses.models.expense_contact_ref import ExpenseContactRef, ExpenseContactRefTypedDict
    from codat_sync_for_expenses.models.shared.expensetransaction import ExpenseTransaction, ExpenseTransactionTypedDict
    from codat_sync_for_expenses.models.shared.expensetransactionline import ExpenseTransactionLine, ExpenseTransactionLineTypedDict
    from codat_sync_for_expenses.models.expense_transaction_type import ExpenseTransactionType
    from codat_sync_for_expenses.models.shared.expensessyncwebhook import ExpensesSyncWebhook, ExpensesSyncWebhookTypedDict
    from codat_sync_for_expenses.models.shared.expensessyncwebhookpayload import ExpensesSyncWebhookPayload, ExpensesSyncWebhookPayloadTypedDict
    from codat_sync_for_expenses.models.expenses_sync_webhook_status import ExpensesSyncWebhookStatus
    from codat_sync_for_expenses.models.shared.halref import HalRef, HalRefTypedDict
    from codat_sync_for_expenses.models.shared.integrationtype import IntegrationType
    from codat_sync_for_expenses.models.shared.invoiceto import InvoiceTo, InvoiceToTypedDict
    from codat_sync_for_expenses.models.invoice_to_type import InvoiceToType
    from codat_sync_for_expenses.models.shared.itemref import ItemRef, ItemRefTypedDict
    from codat_sync_for_expenses.models.shared.items import Items, ItemsTypedDict
    from codat_sync_for_expenses.models.shared.links import Links, LinksTypedDict
    from codat_sync_for_expenses.models.shared.mappingoptions import MappingOptions, MappingOptionsTypedDict
    from codat_sync_for_expenses.models.shared.metadata import Metadata, MetadataTypedDict
    from codat_sync_for_expenses.models.model3 import Model3, Model3TypedDict
    from codat_sync_for_expenses.models.paging_info import PagingInfo, PagingInfoTypedDict
    from codat_sync_for_expenses.models.shared.phonenumber_items import PhoneNumberItems, PhoneNumberItemsTypedDict
    from codat_sync_for_expenses.models.phone_number_items_type import PhoneNumberItemsType
    from codat_sync_for_expenses.models.shared.pulloperation import PullOperation, PullOperationTypedDict
    from codat_sync_for_expenses.models.shared.pulloperations import PullOperations, PullOperationsTypedDict
    from codat_sync_for_expenses.models.shared.pushchangetype import PushChangeType
    from codat_sync_for_expenses.models.shared.pushfieldvalidation import PushFieldValidation, PushFieldValidationTypedDict
    from codat_sync_for_expenses.models.shared.pushoperation import PushOperation, PushOperationTypedDict
    from codat_sync_for_expenses.models.shared.pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
    from codat_sync_for_expenses.models.shared.pushoperationref import PushOperationRef, PushOperationRefTypedDict
    from codat_sync_for_expenses.models.shared.pushoperationstatus import PushOperationStatus
    from codat_sync_for_expenses.models.shared.pushoperations import PushOperations, PushOperationsTypedDict
    from codat_sync_for_expenses.models.shared.pushoption import PushOption, PushOptionTypedDict
    from codat_sync_for_expenses.models.shared.pushoptionchoice import PushOptionChoice, PushOptionChoiceTypedDict
    from codat_sync_for_expenses.models.shared.pushoptionproperty import PushOptionProperty, PushOptionPropertyTypedDict
    from codat_sync_for_expenses.models.shared.pushoptiontype import PushOptionType
    from codat_sync_for_expenses.models.shared.pushvalidationinfo import PushValidationInfo, PushValidationInfoTypedDict
    from codat_sync_for_expenses.models.shared.recordref import RecordRef, RecordRefTypedDict
    from codat_sync_for_expenses.models.shared.reimbursableexpensetransaction import ReimbursableExpenseTransaction, ReimbursableExpenseTransactionTypedDict
    from codat_sync_for_expenses.models.shared.reimbursableexpensetransactionline import ReimbursableExpenseTransactionLine, ReimbursableExpenseTransactionLineTypedDict
    from codat_sync_for_expenses.models.shared.reimbursementcontactref import ReimbursementContactRef, ReimbursementContactRefTypedDict
    from codat_sync_for_expenses.models.shared.schema_transaction import SchemaTransaction, SchemaTransactionTypedDict
    from codat_sync_for_expenses.models.source_type import SourceType
    from codat_sync_for_expenses.models.shared.status import Status
    from codat_sync_for_expenses.models.shared.supplementaldata import SupplementalData, SupplementalDataTypedDict
    from codat_sync_for_expenses.models.shared.supplier import Supplier, SupplierTypedDict
    from codat_sync_for_expenses.models.shared.supplierdetails import SupplierDetails, SupplierDetailsTypedDict
    from codat_sync_for_expenses.models.shared.supplierstatus import SupplierStatus
    from codat_sync_for_expenses.models.shared.suppliers import Suppliers, SuppliersTypedDict
    from codat_sync_for_expenses.models.sync_complete_webhook import SyncCompleteWebhook, SyncCompleteWebhookTypedDict
    from codat_sync_for_expenses.models.sync_complete_webhook_data import SyncCompleteWebhookData, SyncCompleteWebhookDataTypedDict
    from codat_sync_for_expenses.models.sync_failed_webhook import SyncFailedWebhook, SyncFailedWebhookTypedDict
    from codat_sync_for_expenses.models.sync_failed_webhook_data import SyncFailedWebhookData, SyncFailedWebhookDataTypedDict
    from codat_sync_for_expenses.models.sync_initiated import SyncInitiated, SyncInitiatedTypedDict
    from codat_sync_for_expenses.models.shared.taxratemappinginfo import TaxRateMappingInfo, TaxRateMappingInfoTypedDict
    from codat_sync_for_expenses.models.shared.trackingcategorymappinginfo import TrackingCategoryMappingInfo, TrackingCategoryMappingInfoTypedDict
    from codat_sync_for_expenses.models.shared.trackingref import TrackingRef, TrackingRefTypedDict
    from codat_sync_for_expenses.models.shared.trackingrefadjustmenttransaction import TrackingRefAdjustmentTransaction, TrackingRefAdjustmentTransactionTypedDict
    from codat_sync_for_expenses.models.tracking_ref_adjustment_transaction_data_type import TrackingRefAdjustmentTransactionDataType
    from codat_sync_for_expenses.models.tracking_ref_data_type import TrackingRefDataType
    from codat_sync_for_expenses.models.transaction import Transaction, TransactionTypedDict
    from codat_sync_for_expenses.models.shared.transactionstatus import TransactionStatus
    from codat_sync_for_expenses.models.shared.transactions import Transactions, TransactionsTypedDict
    from codat_sync_for_expenses.models.shared.transfertransactionrequest import TransferTransactionRequest, TransferTransactionRequestTypedDict
    from codat_sync_for_expenses.models.transfer_transaction_request_from import TransferTransactionRequestFrom, TransferTransactionRequestFromTypedDict
    from codat_sync_for_expenses.models.transfer_transaction_request_to import TransferTransactionRequestTo, TransferTransactionRequestToTypedDict
    from codat_sync_for_expenses.models.shared.transfertransactionresponse import TransferTransactionResponse, TransferTransactionResponseTypedDict
    from codat_sync_for_expenses.models.type import Type
    from codat_sync_for_expenses.models.update_connection import UpdateConnection, UpdateConnectionTypedDict
    from codat_sync_for_expenses.models.shared.updatecustomerresponse import UpdateCustomerResponse, UpdateCustomerResponseTypedDict
    from codat_sync_for_expenses.models.update_customer_response_all_of_data import UpdateCustomerResponseAllOfData, UpdateCustomerResponseAllOfDataTypedDict
    from codat_sync_for_expenses.models.shared.updateexpenserequest import UpdateExpenseRequest, UpdateExpenseRequestTypedDict
    from codat_sync_for_expenses.models.update_expense_request_type import UpdateExpenseRequestType
    from codat_sync_for_expenses.models.shared.updateexpenseresponse import UpdateExpenseResponse, UpdateExpenseResponseTypedDict
    from codat_sync_for_expenses.models.shared.updatereimbursableexpensetransactionrequest import UpdateReimbursableExpenseTransactionRequest, UpdateReimbursableExpenseTransactionRequestTypedDict
    from codat_sync_for_expenses.models.shared.updatesupplierresponse import UpdateSupplierResponse, UpdateSupplierResponseTypedDict
    from codat_sync_for_expenses.models.update_supplier_response_all_of_data import UpdateSupplierResponseAllOfData, UpdateSupplierResponseAllOfDataTypedDict
    from codat_sync_for_expenses.models.valid_data_type_links import ValidDataTypeLinks, ValidDataTypeLinksTypedDict
    from codat_sync_for_expenses.models.shared.validfor import ValidFor
    from codat_sync_for_expenses.models.shared.validtransactiontypes import ValidTransactionTypes
    from codat_sync_for_expenses.models.shared.validation import Validation, ValidationTypedDict
    from codat_sync_for_expenses.models.shared.validationitem import ValidationItem, ValidationItemTypedDict
    from codat_sync_for_expenses.models.weblink import Weblink, WeblinkTypedDict
    from codat_sync_for_expenses.models.shared.companyinformation import CompanyInformationSchemasType
    from codat_sync_for_expenses.models.shared.createbankaccountresponse import CreateBankAccountResponseBankAccountType
    from codat_sync_for_expenses.models.shared.schema_datatype import SchemaDataType
    from codat_sync_for_expenses.models.shared.transaction import TransactionDefinitionsStatus
    from codat_sync_for_expenses.models.account_mapping_info_account_type import AccountMappingInfoAccountType as AccountMappingInfoAccountType
    from codat_sync_for_expenses.models.shared.accountmappinginfo import AccountMappingInfoTypedDict as AccountMappingInfoTypedDict
    from codat_sync_for_expenses.models.shared.accountprototype import AccountPrototypeTypedDict as AccountPrototypeTypedDict
    from codat_sync_for_expenses.models.account_reference import AccountReferenceTypedDict as AccountReferenceTypedDict
    from codat_sync_for_expenses.models.shared.accountstatus import AccountStatus as AccountStatus
    from codat_sync_for_expenses.models.shared.accounttype import AccountType as AccountType
    from codat_sync_for_expenses.models.create_account_response_all_of_data import CreateAccountResponseAllOfData as AccountingAccount
    from codat_sync_for_expenses.models.create_account_response_all_of_data import CreateAccountResponseAllOfData as AccountingAccountTypedDict
    from codat_sync_for_expenses.models.shared.accountingaddresstype import AccountingAddressType as AccountingAddressType
    from codat_sync_for_expenses.models.accounting_address import AccountingAddressTypedDict as AccountingAddressTypedDict
    from codat_sync_for_expenses.models.create_bank_account_response_all_of_data import CreateBankAccountResponseAllOfData as AccountingBankAccount
    from codat_sync_for_expenses.models.create_bank_account_response_all_of_data import CreateBankAccountResponseAllOfData as AccountingBankAccountTypedDict
    from codat_sync_for_expenses.models.create_customer_response_all_of_data import CreateCustomerResponseAllOfData as AccountingCustomer
    from codat_sync_for_expenses.models.create_customer_response_all_of_data import CreateCustomerResponseAllOfData as AccountingCustomerTypedDict
    from codat_sync_for_expenses.models.create_supplier_response_all_of_data import CreateSupplierResponseAllOfData as AccountingSupplier
    from codat_sync_for_expenses.models.create_supplier_response_all_of_data import CreateSupplierResponseAllOfData as AccountingSupplierTypedDict
    from codat_sync_for_expenses.models.shared.adjustmenttransactionline import AdjustmentTransactionLineTypedDict as AdjustmentTransactionLineTypedDict
    from codat_sync_for_expenses.models.shared.adjustmenttransactionrequest import AdjustmentTransactionRequestTypedDict as AdjustmentTransactionRequestTypedDict
    from codat_sync_for_expenses.models.shared.adjustmenttransactionresponse import AdjustmentTransactionResponseTypedDict as AdjustmentTransactionResponseTypedDict
    from codat_sync_for_expenses.models.shared.apaccountref import ApAccountRefTypedDict as ApAccountRefTypedDict
    from codat_sync_for_expenses.models.shared.attachment import AttachmentTypedDict as AttachmentTypedDict
    from codat_sync_for_expenses.models.shared.bankaccountdetails import BankAccountDetailsTypedDict as BankAccountDetailsTypedDict
    from codat_sync_for_expenses.models.bank_account_reference import BankAccountReferenceTypedDict as BankAccountReferenceTypedDict
    from codat_sync_for_expenses.models.shared.bankaccountstatus import BankAccountStatus as BankAccountStatus
    from codat_sync_for_expenses.models.bank_account_type import BankAccountType as BankAccountType
    from codat_sync_for_expenses.models.shared.bankaccount import BankAccountTypedDict as BankAccountTypedDict
    from codat_sync_for_expenses.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayloadTypedDict as ClientRateLimitWebhookPayloadTypedDict
    from codat_sync_for_expenses.models.shared.clientratelimitwebhook import ClientRateLimitWebhookTypedDict as ClientRateLimitWebhookTypedDict
    from codat_sync_for_expenses.models.shared.companies import CompaniesTypedDict as CompaniesTypedDict
    from codat_sync_for_expenses.models.shared.companyconfiguration import CompanyConfigurationTypedDict as CompanyConfigurationTypedDict
    from codat_sync_for_expenses.models.shared.companyinformation import CompanyInformationSchemasType as CompanyInformationSchemasType
    from codat_sync_for_expenses.models.company_information_type import CompanyInformationType as CompanyInformationType
    from codat_sync_for_expenses.models.company_information import CompanyInformationTypedDict as CompanyInformationTypedDict
    from codat_sync_for_expenses.models.company_reference_links import CompanyReferenceLinksTypedDict as CompanyReferenceLinksTypedDict
    from codat_sync_for_expenses.models.shared.companyreference import CompanyReferenceTypedDict as CompanyReferenceTypedDict
    from codat_sync_for_expenses.models.shared.companyrequestbody import CompanyRequestBodyTypedDict as CompanyRequestBodyTypedDict
    from codat_sync_for_expenses.models.shared.companysyncstatus import CompanySyncStatusTypedDict as CompanySyncStatusTypedDict
    from codat_sync_for_expenses.models.shared.company import CompanyTypedDict as CompanyTypedDict
    from codat_sync_for_expenses.models.shared.companyupdaterequest import CompanyUpdateRequestTypedDict as CompanyUpdateRequestTypedDict
    from codat_sync_for_expenses.models.shared.connection import ConnectionTypedDict as ConnectionTypedDict
    from codat_sync_for_expenses.models.shared.connections import ConnectionsTypedDict as ConnectionsTypedDict
    from codat_sync_for_expenses.models.shared.contact import ContactTypedDict as ContactTypedDict
    from codat_sync_for_expenses.models.shared.metadata import Metadata as CreateAccountResponseMetadata
    from codat_sync_for_expenses.models.shared.metadata import MetadataTypedDict as CreateAccountResponseMetadataTypedDict
    from codat_sync_for_expenses.models.shared.createaccountresponse import CreateAccountResponseTypedDict as CreateAccountResponseTypedDict
    from codat_sync_for_expenses.models.valid_data_type_links import ValidDataTypeLinks as CreateAccountResponseValidDataTypeLinks
    from codat_sync_for_expenses.models.valid_data_type_links import ValidDataTypeLinksTypedDict as CreateAccountResponseValidDataTypeLinksTypedDict
    from codat_sync_for_expenses.models.shared.createbankaccountresponse import CreateBankAccountResponseBankAccountType as CreateBankAccountResponseBankAccountType
    from codat_sync_for_expenses.models.create_bank_account_response import CreateBankAccountResponseTypedDict as CreateBankAccountResponseTypedDict
    from codat_sync_for_expenses.models.shared.createcustomerresponse import CreateCustomerResponseTypedDict as CreateCustomerResponseTypedDict
    from codat_sync_for_expenses.models.shared.createexpenseresponse import CreateExpenseResponseTypedDict as CreateExpenseResponseTypedDict
    from codat_sync_for_expenses.models.shared.createreimbursableexpenseresponse import CreateReimbursableExpenseResponseTypedDict as CreateReimbursableExpenseResponseTypedDict
    from codat_sync_for_expenses.models.shared.createsupplierresponse import CreateSupplierResponseTypedDict as CreateSupplierResponseTypedDict
    from codat_sync_for_expenses.models.shared.customerdetails import CustomerDetailsTypedDict as CustomerDetailsTypedDict
    from codat_sync_for_expenses.models.shared.customerstatus import CustomerStatus as CustomerStatus
    from codat_sync_for_expenses.models.shared.customer import CustomerTypedDict as CustomerTypedDict
    from codat_sync_for_expenses.models.shared.customers import CustomersTypedDict as CustomersTypedDict
    from codat_sync_for_expenses.models.shared.dataconnectionerror import DataConnectionErrorTypedDict as DataConnectionErrorTypedDict
    from codat_sync_for_expenses.models.shared.dataconnectionstatus import DataConnectionStatus as DataConnectionStatus
    from codat_sync_for_expenses.models.shared.datastatus import DataStatusTypedDict as DataStatusTypedDict
    from codat_sync_for_expenses.models.shared.datatype import DataType as DataType
    from codat_sync_for_expenses.models.data_types import DataTypes as DataTypes
    from codat_sync_for_expenses.models.dataset_status import DatasetStatus as DatasetStatus
    from codat_sync_for_expenses.models.error_status import ErrorStatus as ErrorStatus
    from codat_sync_for_expenses.models.shared.errorvalidationitem import ErrorValidationItemTypedDict as ErrorValidationItemTypedDict
    from codat_sync_for_expenses.models.shared.errorvalidation import ErrorValidationTypedDict as ErrorValidationTypedDict
    from codat_sync_for_expenses.models.shared.expensecontactref import ExpenseContactRefType as ExpenseContactRefType
    from codat_sync_for_expenses.models.expense_contact_ref import ExpenseContactRefTypedDict as ExpenseContactRefTypedDict
    from codat_sync_for_expenses.models.shared.expensetransactionline import ExpenseTransactionLineTypedDict as ExpenseTransactionLineTypedDict
    from codat_sync_for_expenses.models.expense_transaction_type import ExpenseTransactionType as ExpenseTransactionType
    from codat_sync_for_expenses.models.shared.expensetransaction import ExpenseTransactionTypedDict as ExpenseTransactionTypedDict
    from codat_sync_for_expenses.models.shared.expensessyncwebhookpayload import ExpensesSyncWebhookPayloadTypedDict as ExpensesSyncWebhookPayloadTypedDict
    from codat_sync_for_expenses.models.shared.expensessyncwebhook import ExpensesSyncWebhookTypedDict as ExpensesSyncWebhookTypedDict
    from codat_sync_for_expenses.models.transfer_transaction_request_from import TransferTransactionRequestFrom as From
    from codat_sync_for_expenses.models.transfer_transaction_request_from import TransferTransactionRequestFromTypedDict as FromTypedDict
    from codat_sync_for_expenses.models.shared.halref import HalRefTypedDict as HalRefTypedDict
    from codat_sync_for_expenses.models.shared.integrationtype import IntegrationType as IntegrationType
    from codat_sync_for_expenses.models.invoice_to_type import InvoiceToType as InvoiceToType
    from codat_sync_for_expenses.models.shared.invoiceto import InvoiceToTypedDict as InvoiceToTypedDict
    from codat_sync_for_expenses.models.shared.itemref import ItemRefTypedDict as ItemRefTypedDict
    from codat_sync_for_expenses.models.shared.items import ItemsTypedDict as ItemsTypedDict
    from codat_sync_for_expenses.models.shared.links import LinksTypedDict as LinksTypedDict
    from codat_sync_for_expenses.models.shared.mappingoptions import MappingOptionsTypedDict as MappingOptionsTypedDict
    from codat_sync_for_expenses.models.shared.metadata import MetadataTypedDict as MetadataTypedDict
    from codat_sync_for_expenses.models.shared.phonenumber_items import PhoneNumberItems as Phone
    from codat_sync_for_expenses.models.shared.phonenumber_items import PhoneNumberItemsTypedDict as PhoneNumberItemsTypedDict
    from codat_sync_for_expenses.models.shared.phonenumber_items import PhoneNumberItemsTypedDict as PhoneTypedDict
    from codat_sync_for_expenses.models.shared.pulloperation import PullOperationTypedDict as PullOperationTypedDict
    from codat_sync_for_expenses.models.shared.pulloperations import PullOperationsTypedDict as PullOperationsTypedDict
    from codat_sync_for_expenses.models.shared.pushchangetype import PushChangeType as PushChangeType
    from codat_sync_for_expenses.models.shared.pushfieldvalidation import PushFieldValidationTypedDict as PushFieldValidationTypedDict
    from codat_sync_for_expenses.models.shared.pushoperationchange import PushOperationChangeTypedDict as PushOperationChangeTypedDict
    from codat_sync_for_expenses.models.shared.pushoperationref import PushOperationRefTypedDict as PushOperationRefTypedDict
    from codat_sync_for_expenses.models.shared.pushoperationstatus import PushOperationStatus as PushOperationStatus
    from codat_sync_for_expenses.models.shared.pushoperation import PushOperationTypedDict as PushOperationTypedDict
    from codat_sync_for_expenses.models.shared.pushoperations import PushOperationsTypedDict as PushOperationsTypedDict
    from codat_sync_for_expenses.models.shared.pushoptionchoice import PushOptionChoiceTypedDict as PushOptionChoiceTypedDict
    from codat_sync_for_expenses.models.shared.pushoptionproperty import PushOptionPropertyTypedDict as PushOptionPropertyTypedDict
    from codat_sync_for_expenses.models.shared.pushoptiontype import PushOptionType as PushOptionType
    from codat_sync_for_expenses.models.shared.pushoption import PushOptionTypedDict as PushOptionTypedDict
    from codat_sync_for_expenses.models.shared.pushvalidationinfo import PushValidationInfoTypedDict as PushValidationInfoTypedDict
    from codat_sync_for_expenses.models.shared.recordref import RecordRefTypedDict as RecordRefTypedDict
    from codat_sync_for_expenses.models.shared.reimbursableexpensetransactionline import ReimbursableExpenseTransactionLineTypedDict as ReimbursableExpenseTransactionLineTypedDict
    from codat_sync_for_expenses.models.shared.reimbursableexpensetransaction import ReimbursableExpenseTransactionTypedDict as ReimbursableExpenseTransactionTypedDict
    from codat_sync_for_expenses.models.shared.reimbursementcontactref import ReimbursementContactRefTypedDict as ReimbursementContactRefTypedDict
    from codat_sync_for_expenses.models.shared.schema_datatype import SchemaDataType as SchemaDataType
    from codat_sync_for_expenses.models.shared.schema_transaction import SchemaTransactionTypedDict as SchemaTransactionTypedDict
    from codat_sync_for_expenses.models.shared.security import Security as Security
    from codat_sync_for_expenses.models.shared.security import SecurityTypedDict as SecurityTypedDict
    from codat_sync_for_expenses.models.source_type import SourceType as SourceType
    from codat_sync_for_expenses.models.shared.status import Status as Status
    from codat_sync_for_expenses.models.shared.supplementaldata import SupplementalDataTypedDict as SupplementalDataTypedDict
    from codat_sync_for_expenses.models.shared.supplierdetails import SupplierDetailsTypedDict as SupplierDetailsTypedDict
    from codat_sync_for_expenses.models.shared.supplierstatus import SupplierStatus as SupplierStatus
    from codat_sync_for_expenses.models.shared.supplier import SupplierTypedDict as SupplierTypedDict
    from codat_sync_for_expenses.models.shared.suppliers import SuppliersTypedDict as SuppliersTypedDict
    from codat_sync_for_expenses.models.shared.taxratemappinginfo import TaxRateMappingInfoTypedDict as TaxRateMappingInfoTypedDict
    from codat_sync_for_expenses.models.transfer_transaction_request_to import TransferTransactionRequestTo as To
    from codat_sync_for_expenses.models.transfer_transaction_request_to import TransferTransactionRequestToTypedDict as ToTypedDict
    from codat_sync_for_expenses.models.shared.trackingcategorymappinginfo import TrackingCategoryMappingInfoTypedDict as TrackingCategoryMappingInfoTypedDict
    from codat_sync_for_expenses.models.tracking_ref_adjustment_transaction_data_type import TrackingRefAdjustmentTransactionDataType as TrackingRefAdjustmentTransactionDataType
    from codat_sync_for_expenses.models.shared.trackingrefadjustmenttransaction import TrackingRefAdjustmentTransactionTypedDict as TrackingRefAdjustmentTransactionTypedDict
    from codat_sync_for_expenses.models.tracking_ref_data_type import TrackingRefDataType as TrackingRefDataType
    from codat_sync_for_expenses.models.shared.trackingref import TrackingRefTypedDict as TrackingRefTypedDict
    from codat_sync_for_expenses.models.shared.transaction import TransactionDefinitionsStatus as TransactionDefinitionsStatus
    from codat_sync_for_expenses.models.shared.transactionstatus import TransactionStatus as TransactionStatus
    from codat_sync_for_expenses.models.transaction import TransactionTypedDict as TransactionTypedDict
    from codat_sync_for_expenses.models.shared.transactions import TransactionsTypedDict as TransactionsTypedDict
    from codat_sync_for_expenses.models.account_reference import AccountReference as TransferTransactionRequestAccountReference
    from codat_sync_for_expenses.models.account_reference import AccountReferenceTypedDict as TransferTransactionRequestAccountReferenceTypedDict
    from codat_sync_for_expenses.models.shared.transfertransactionrequest import TransferTransactionRequestTypedDict as TransferTransactionRequestTypedDict
    from codat_sync_for_expenses.models.shared.transfertransactionresponse import TransferTransactionResponseTypedDict as TransferTransactionResponseTypedDict
    from codat_sync_for_expenses.models.type import Type as Type
    from codat_sync_for_expenses.models.update_customer_response_all_of_data import UpdateCustomerResponseAllOfData as UpdateCustomerResponseAccountingCustomer
    from codat_sync_for_expenses.models.update_customer_response_all_of_data import UpdateCustomerResponseAllOfData as UpdateCustomerResponseAccountingCustomerTypedDict
    from codat_sync_for_expenses.models.shared.updatecustomerresponse import UpdateCustomerResponseTypedDict as UpdateCustomerResponseTypedDict
    from codat_sync_for_expenses.models.bank_account_reference import BankAccountReference as UpdateExpenseRequestBankAccountReference
    from codat_sync_for_expenses.models.bank_account_reference import BankAccountReferenceTypedDict as UpdateExpenseRequestBankAccountReferenceTypedDict
    from codat_sync_for_expenses.models.update_expense_request_type import UpdateExpenseRequestType as UpdateExpenseRequestType
    from codat_sync_for_expenses.models.shared.updateexpenserequest import UpdateExpenseRequestTypedDict as UpdateExpenseRequestTypedDict
    from codat_sync_for_expenses.models.shared.updateexpenseresponse import UpdateExpenseResponseTypedDict as UpdateExpenseResponseTypedDict
    from codat_sync_for_expenses.models.shared.updatereimbursableexpensetransactionrequest import UpdateReimbursableExpenseTransactionRequestTypedDict as UpdateReimbursableExpenseTransactionRequestTypedDict
    from codat_sync_for_expenses.models.update_supplier_response_all_of_data import UpdateSupplierResponseAllOfData as UpdateSupplierResponseAccountingSupplier
    from codat_sync_for_expenses.models.update_supplier_response_all_of_data import UpdateSupplierResponseAllOfData as UpdateSupplierResponseAccountingSupplierTypedDict
    from codat_sync_for_expenses.models.shared.updatesupplierresponse import UpdateSupplierResponseTypedDict as UpdateSupplierResponseTypedDict
    from codat_sync_for_expenses.models.valid_data_type_links import ValidDataTypeLinksTypedDict as ValidDataTypeLinksTypedDict
    from codat_sync_for_expenses.models.shared.validfor import ValidFor as ValidFor
    from codat_sync_for_expenses.models.shared.validtransactiontypes import ValidTransactionTypes as ValidTransactionTypes
    from codat_sync_for_expenses.models.shared.validationitem import ValidationItemTypedDict as ValidationItemTypedDict
    from codat_sync_for_expenses.models.shared.validation import ValidationTypedDict as ValidationTypedDict
    from codat_sync_for_expenses.models.weblink import WeblinkTypedDict as WeblinkTypedDict
    from codat_sync_for_expenses.models.shared.codatfile import CodatFile, CodatFileTypedDict
    from codat_sync_for_expenses.models.shared.attachmentupload import AttachmentUpload, AttachmentUploadTypedDict

_dynamic_imports: dict[str, tuple[str, str]] = {
    'Account': ('codat_sync_for_expenses.models.account', 'Account'),
    'AccountMappingInfo': ('codat_sync_for_expenses.models.shared.accountmappinginfo', 'AccountMappingInfo'),
    'AccountMappingInfoAccountType': ('codat_sync_for_expenses.models.account_mapping_info_account_type', 'AccountMappingInfoAccountType'),
    'AccountMappingInfoTypedDict': ('codat_sync_for_expenses.models.shared.accountmappinginfo', 'AccountMappingInfoTypedDict'),
    'AccountPrototype': ('codat_sync_for_expenses.models.shared.accountprototype', 'AccountPrototype'),
    'AccountPrototypeTypedDict': ('codat_sync_for_expenses.models.shared.accountprototype', 'AccountPrototypeTypedDict'),
    'AccountReference': ('codat_sync_for_expenses.models.account_reference', 'AccountReference'),
    'AccountReference1': ('codat_sync_for_expenses.models.account_reference1', 'AccountReference1'),
    'AccountReference1TypedDict': ('codat_sync_for_expenses.models.account_reference1', 'AccountReference1TypedDict'),
    'AccountReferenceTypedDict': ('codat_sync_for_expenses.models.account_reference', 'AccountReferenceTypedDict'),
    'AccountStatus': ('codat_sync_for_expenses.models.shared.accountstatus', 'AccountStatus'),
    'AccountType': ('codat_sync_for_expenses.models.shared.accounttype', 'AccountType'),
    'AccountTypedDict': ('codat_sync_for_expenses.models.account', 'AccountTypedDict'),
    'AccountingAccount': ('codat_sync_for_expenses.models.create_account_response_all_of_data', 'CreateAccountResponseAllOfData'),
    'AccountingAccountTypedDict': ('codat_sync_for_expenses.models.create_account_response_all_of_data', 'CreateAccountResponseAllOfData'),
    'AccountingAddress': ('codat_sync_for_expenses.models.accounting_address', 'AccountingAddress'),
    'AccountingAddressType': ('codat_sync_for_expenses.models.shared.accountingaddresstype', 'AccountingAddressType'),
    'AccountingAddressTypedDict': ('codat_sync_for_expenses.models.accounting_address', 'AccountingAddressTypedDict'),
    'AccountingBankAccount': ('codat_sync_for_expenses.models.create_bank_account_response_all_of_data', 'CreateBankAccountResponseAllOfData'),
    'AccountingBankAccountTypedDict': ('codat_sync_for_expenses.models.create_bank_account_response_all_of_data', 'CreateBankAccountResponseAllOfData'),
    'AccountingCustomer': ('codat_sync_for_expenses.models.create_customer_response_all_of_data', 'CreateCustomerResponseAllOfData'),
    'AccountingCustomerTypedDict': ('codat_sync_for_expenses.models.create_customer_response_all_of_data', 'CreateCustomerResponseAllOfData'),
    'AccountingSupplier': ('codat_sync_for_expenses.models.create_supplier_response_all_of_data', 'CreateSupplierResponseAllOfData'),
    'AccountingSupplierTypedDict': ('codat_sync_for_expenses.models.create_supplier_response_all_of_data', 'CreateSupplierResponseAllOfData'),
    'AdjustmentTransactionLine': ('codat_sync_for_expenses.models.shared.adjustmenttransactionline', 'AdjustmentTransactionLine'),
    'AdjustmentTransactionLineTypedDict': ('codat_sync_for_expenses.models.shared.adjustmenttransactionline', 'AdjustmentTransactionLineTypedDict'),
    'AdjustmentTransactionRequest': ('codat_sync_for_expenses.models.shared.adjustmenttransactionrequest', 'AdjustmentTransactionRequest'),
    'AdjustmentTransactionRequestTypedDict': ('codat_sync_for_expenses.models.shared.adjustmenttransactionrequest', 'AdjustmentTransactionRequestTypedDict'),
    'AdjustmentTransactionResponse': ('codat_sync_for_expenses.models.shared.adjustmenttransactionresponse', 'AdjustmentTransactionResponse'),
    'AdjustmentTransactionResponseTypedDict': ('codat_sync_for_expenses.models.shared.adjustmenttransactionresponse', 'AdjustmentTransactionResponseTypedDict'),
    'ApAccountRef': ('codat_sync_for_expenses.models.shared.apaccountref', 'ApAccountRef'),
    'ApAccountRefTypedDict': ('codat_sync_for_expenses.models.shared.apaccountref', 'ApAccountRefTypedDict'),
    'Attachment': ('codat_sync_for_expenses.models.shared.attachment', 'Attachment'),
    'AttachmentTypedDict': ('codat_sync_for_expenses.models.shared.attachment', 'AttachmentTypedDict'),
    'AttachmentUpload': ('codat_sync_for_expenses.models.shared.attachmentupload', 'AttachmentUpload'),
    'AttachmentUploadTypedDict': ('codat_sync_for_expenses.models.shared.attachmentupload', 'AttachmentUploadTypedDict'),
    'BankAccount': ('codat_sync_for_expenses.models.shared.bankaccount', 'BankAccount'),
    'BankAccountDetails': ('codat_sync_for_expenses.models.shared.bankaccountdetails', 'BankAccountDetails'),
    'BankAccountDetailsTypedDict': ('codat_sync_for_expenses.models.shared.bankaccountdetails', 'BankAccountDetailsTypedDict'),
    'BankAccountPrototype': ('codat_sync_for_expenses.models.bank_account_prototype', 'BankAccountPrototype'),
    'BankAccountPrototypeTypedDict': ('codat_sync_for_expenses.models.bank_account_prototype', 'BankAccountPrototypeTypedDict'),
    'BankAccountReference': ('codat_sync_for_expenses.models.bank_account_reference', 'BankAccountReference'),
    'BankAccountReferenceTypedDict': ('codat_sync_for_expenses.models.bank_account_reference', 'BankAccountReferenceTypedDict'),
    'BankAccountStatus': ('codat_sync_for_expenses.models.shared.bankaccountstatus', 'BankAccountStatus'),
    'BankAccountType': ('codat_sync_for_expenses.models.bank_account_type', 'BankAccountType'),
    'BankAccountTypedDict': ('codat_sync_for_expenses.models.shared.bankaccount', 'BankAccountTypedDict'),
    'ClientRateLimitWebhook': ('codat_sync_for_expenses.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhook'),
    'ClientRateLimitWebhookPayload': ('codat_sync_for_expenses.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayload'),
    'ClientRateLimitWebhookPayloadTypedDict': ('codat_sync_for_expenses.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayloadTypedDict'),
    'ClientRateLimitWebhookTypedDict': ('codat_sync_for_expenses.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhookTypedDict'),
    'CodatFile': ('codat_sync_for_expenses.models.shared.codatfile', 'CodatFile'),
    'CodatFileTypedDict': ('codat_sync_for_expenses.models.shared.codatfile', 'CodatFileTypedDict'),
    'Companies': ('codat_sync_for_expenses.models.shared.companies', 'Companies'),
    'CompaniesTypedDict': ('codat_sync_for_expenses.models.shared.companies', 'CompaniesTypedDict'),
    'Company': ('codat_sync_for_expenses.models.shared.company', 'Company'),
    'CompanyConfiguration': ('codat_sync_for_expenses.models.shared.companyconfiguration', 'CompanyConfiguration'),
    'CompanyConfigurationTypedDict': ('codat_sync_for_expenses.models.shared.companyconfiguration', 'CompanyConfigurationTypedDict'),
    'CompanyDetails': ('codat_sync_for_expenses.models.company_details', 'CompanyDetails'),
    'CompanyDetailsTypedDict': ('codat_sync_for_expenses.models.company_details', 'CompanyDetailsTypedDict'),
    'CompanyInformation': ('codat_sync_for_expenses.models.company_information', 'CompanyInformation'),
    'CompanyInformationSchemasType': ('codat_sync_for_expenses.models.shared.companyinformation', 'CompanyInformationSchemasType'),
    'CompanyInformationType': ('codat_sync_for_expenses.models.company_information_type', 'CompanyInformationType'),
    'CompanyInformationTypedDict': ('codat_sync_for_expenses.models.company_information', 'CompanyInformationTypedDict'),
    'CompanyReference': ('codat_sync_for_expenses.models.shared.companyreference', 'CompanyReference'),
    'CompanyReferenceLinks': ('codat_sync_for_expenses.models.company_reference_links', 'CompanyReferenceLinks'),
    'CompanyReferenceLinksTypedDict': ('codat_sync_for_expenses.models.company_reference_links', 'CompanyReferenceLinksTypedDict'),
    'CompanyReferenceTypedDict': ('codat_sync_for_expenses.models.shared.companyreference', 'CompanyReferenceTypedDict'),
    'CompanyRequestBody': ('codat_sync_for_expenses.models.shared.companyrequestbody', 'CompanyRequestBody'),
    'CompanyRequestBodyTypedDict': ('codat_sync_for_expenses.models.shared.companyrequestbody', 'CompanyRequestBodyTypedDict'),
    'CompanySyncStatus': ('codat_sync_for_expenses.models.shared.companysyncstatus', 'CompanySyncStatus'),
    'CompanySyncStatusTypedDict': ('codat_sync_for_expenses.models.shared.companysyncstatus', 'CompanySyncStatusTypedDict'),
    'CompanyTypedDict': ('codat_sync_for_expenses.models.shared.company', 'CompanyTypedDict'),
    'CompanyUpdateRequest': ('codat_sync_for_expenses.models.shared.companyupdaterequest', 'CompanyUpdateRequest'),
    'CompanyUpdateRequestTypedDict': ('codat_sync_for_expenses.models.shared.companyupdaterequest', 'CompanyUpdateRequestTypedDict'),
    'Connection': ('codat_sync_for_expenses.models.shared.connection', 'Connection'),
    'ConnectionTypedDict': ('codat_sync_for_expenses.models.shared.connection', 'ConnectionTypedDict'),
    'Connections': ('codat_sync_for_expenses.models.shared.connections', 'Connections'),
    'ConnectionsTypedDict': ('codat_sync_for_expenses.models.shared.connections', 'ConnectionsTypedDict'),
    'Contact': ('codat_sync_for_expenses.models.shared.contact', 'Contact'),
    'ContactTypedDict': ('codat_sync_for_expenses.models.shared.contact', 'ContactTypedDict'),
    'CreateAccountResponse': ('codat_sync_for_expenses.models.shared.createaccountresponse', 'CreateAccountResponse'),
    'CreateAccountResponseAllOfData': ('codat_sync_for_expenses.models.create_account_response_all_of_data', 'CreateAccountResponseAllOfData'),
    'CreateAccountResponseAllOfDataTypedDict': ('codat_sync_for_expenses.models.create_account_response_all_of_data', 'CreateAccountResponseAllOfDataTypedDict'),
    'CreateAccountResponseMetadata': ('codat_sync_for_expenses.models.shared.metadata', 'Metadata'),
    'CreateAccountResponseMetadataTypedDict': ('codat_sync_for_expenses.models.shared.metadata', 'MetadataTypedDict'),
    'CreateAccountResponseTypedDict': ('codat_sync_for_expenses.models.shared.createaccountresponse', 'CreateAccountResponseTypedDict'),
    'CreateAccountResponseValidDataTypeLinks': ('codat_sync_for_expenses.models.valid_data_type_links', 'ValidDataTypeLinks'),
    'CreateAccountResponseValidDataTypeLinksTypedDict': ('codat_sync_for_expenses.models.valid_data_type_links', 'ValidDataTypeLinksTypedDict'),
    'CreateBankAccountResponse': ('codat_sync_for_expenses.models.create_bank_account_response', 'CreateBankAccountResponse'),
    'CreateBankAccountResponseAllOfData': ('codat_sync_for_expenses.models.create_bank_account_response_all_of_data', 'CreateBankAccountResponseAllOfData'),
    'CreateBankAccountResponseAllOfDataTypedDict': ('codat_sync_for_expenses.models.create_bank_account_response_all_of_data', 'CreateBankAccountResponseAllOfDataTypedDict'),
    'CreateBankAccountResponseBankAccountType': ('codat_sync_for_expenses.models.shared.createbankaccountresponse', 'CreateBankAccountResponseBankAccountType'),
    'CreateBankAccountResponseTypedDict': ('codat_sync_for_expenses.models.create_bank_account_response', 'CreateBankAccountResponseTypedDict'),
    'CreateConnectionRequest': ('codat_sync_for_expenses.models.create_connection_request', 'CreateConnectionRequest'),
    'CreateConnectionRequestTypedDict': ('codat_sync_for_expenses.models.create_connection_request', 'CreateConnectionRequestTypedDict'),
    'CreateCustomerResponse': ('codat_sync_for_expenses.models.shared.createcustomerresponse', 'CreateCustomerResponse'),
    'CreateCustomerResponseAllOfData': ('codat_sync_for_expenses.models.create_customer_response_all_of_data', 'CreateCustomerResponseAllOfData'),
    'CreateCustomerResponseAllOfDataTypedDict': ('codat_sync_for_expenses.models.create_customer_response_all_of_data', 'CreateCustomerResponseAllOfDataTypedDict'),
    'CreateCustomerResponseTypedDict': ('codat_sync_for_expenses.models.shared.createcustomerresponse', 'CreateCustomerResponseTypedDict'),
    'CreateExpenseResponse': ('codat_sync_for_expenses.models.shared.createexpenseresponse', 'CreateExpenseResponse'),
    'CreateExpenseResponseTypedDict': ('codat_sync_for_expenses.models.shared.createexpenseresponse', 'CreateExpenseResponseTypedDict'),
    'CreateReimbursableExpenseResponse': ('codat_sync_for_expenses.models.shared.createreimbursableexpenseresponse', 'CreateReimbursableExpenseResponse'),
    'CreateReimbursableExpenseResponseTypedDict': ('codat_sync_for_expenses.models.shared.createreimbursableexpenseresponse', 'CreateReimbursableExpenseResponseTypedDict'),
    'CreateSupplierResponse': ('codat_sync_for_expenses.models.shared.createsupplierresponse', 'CreateSupplierResponse'),
    'CreateSupplierResponseAllOfData': ('codat_sync_for_expenses.models.create_supplier_response_all_of_data', 'CreateSupplierResponseAllOfData'),
    'CreateSupplierResponseAllOfDataTypedDict': ('codat_sync_for_expenses.models.create_supplier_response_all_of_data', 'CreateSupplierResponseAllOfDataTypedDict'),
    'CreateSupplierResponseTypedDict': ('codat_sync_for_expenses.models.shared.createsupplierresponse', 'CreateSupplierResponseTypedDict'),
    'CurrentStatus': ('codat_sync_for_expenses.models.current_status', 'CurrentStatus'),
    'Customer': ('codat_sync_for_expenses.models.shared.customer', 'Customer'),
    'CustomerDetails': ('codat_sync_for_expenses.models.shared.customerdetails', 'CustomerDetails'),
    'CustomerDetailsTypedDict': ('codat_sync_for_expenses.models.shared.customerdetails', 'CustomerDetailsTypedDict'),
    'CustomerStatus': ('codat_sync_for_expenses.models.shared.customerstatus', 'CustomerStatus'),
    'CustomerTypedDict': ('codat_sync_for_expenses.models.shared.customer', 'CustomerTypedDict'),
    'Customers': ('codat_sync_for_expenses.models.shared.customers', 'Customers'),
    'CustomersTypedDict': ('codat_sync_for_expenses.models.shared.customers', 'CustomersTypedDict'),
    'DataConnectionError': ('codat_sync_for_expenses.models.shared.dataconnectionerror', 'DataConnectionError'),
    'DataConnectionErrorTypedDict': ('codat_sync_for_expenses.models.shared.dataconnectionerror', 'DataConnectionErrorTypedDict'),
    'DataConnectionStatus': ('codat_sync_for_expenses.models.shared.dataconnectionstatus', 'DataConnectionStatus'),
    'DataStatus': ('codat_sync_for_expenses.models.shared.datastatus', 'DataStatus'),
    'DataStatusTypedDict': ('codat_sync_for_expenses.models.shared.datastatus', 'DataStatusTypedDict'),
    'DataStatuses': ('codat_sync_for_expenses.models.data_statuses', 'DataStatuses'),
    'DataStatusesTypedDict': ('codat_sync_for_expenses.models.data_statuses', 'DataStatusesTypedDict'),
    'DataType': ('codat_sync_for_expenses.models.shared.datatype', 'DataType'),
    'DataTypes': ('codat_sync_for_expenses.models.data_types', 'DataTypes'),
    'DatasetStatus': ('codat_sync_for_expenses.models.dataset_status', 'DatasetStatus'),
    'ErrorMessage': ('codat_sync_for_expenses.models.error_message', 'ErrorMessage'),
    'ErrorMessageTypedDict': ('codat_sync_for_expenses.models.error_message', 'ErrorMessageTypedDict'),
    'ErrorStatus': ('codat_sync_for_expenses.models.error_status', 'ErrorStatus'),
    'ErrorValidation': ('codat_sync_for_expenses.models.shared.errorvalidation', 'ErrorValidation'),
    'ErrorValidationItem': ('codat_sync_for_expenses.models.shared.errorvalidationitem', 'ErrorValidationItem'),
    'ErrorValidationItemTypedDict': ('codat_sync_for_expenses.models.shared.errorvalidationitem', 'ErrorValidationItemTypedDict'),
    'ErrorValidationTypedDict': ('codat_sync_for_expenses.models.shared.errorvalidation', 'ErrorValidationTypedDict'),
    'ExpenseContactRef': ('codat_sync_for_expenses.models.expense_contact_ref', 'ExpenseContactRef'),
    'ExpenseContactRefType': ('codat_sync_for_expenses.models.shared.expensecontactref', 'ExpenseContactRefType'),
    'ExpenseContactRefTypedDict': ('codat_sync_for_expenses.models.expense_contact_ref', 'ExpenseContactRefTypedDict'),
    'ExpenseTransaction': ('codat_sync_for_expenses.models.shared.expensetransaction', 'ExpenseTransaction'),
    'ExpenseTransactionLine': ('codat_sync_for_expenses.models.shared.expensetransactionline', 'ExpenseTransactionLine'),
    'ExpenseTransactionLineTypedDict': ('codat_sync_for_expenses.models.shared.expensetransactionline', 'ExpenseTransactionLineTypedDict'),
    'ExpenseTransactionType': ('codat_sync_for_expenses.models.expense_transaction_type', 'ExpenseTransactionType'),
    'ExpenseTransactionTypedDict': ('codat_sync_for_expenses.models.shared.expensetransaction', 'ExpenseTransactionTypedDict'),
    'ExpensesSyncWebhook': ('codat_sync_for_expenses.models.shared.expensessyncwebhook', 'ExpensesSyncWebhook'),
    'ExpensesSyncWebhookPayload': ('codat_sync_for_expenses.models.shared.expensessyncwebhookpayload', 'ExpensesSyncWebhookPayload'),
    'ExpensesSyncWebhookPayloadTypedDict': ('codat_sync_for_expenses.models.shared.expensessyncwebhookpayload', 'ExpensesSyncWebhookPayloadTypedDict'),
    'ExpensesSyncWebhookStatus': ('codat_sync_for_expenses.models.expenses_sync_webhook_status', 'ExpensesSyncWebhookStatus'),
    'ExpensesSyncWebhookTypedDict': ('codat_sync_for_expenses.models.shared.expensessyncwebhook', 'ExpensesSyncWebhookTypedDict'),
    'From': ('codat_sync_for_expenses.models.transfer_transaction_request_from', 'TransferTransactionRequestFrom'),
    'FromTypedDict': ('codat_sync_for_expenses.models.transfer_transaction_request_from', 'TransferTransactionRequestFromTypedDict'),
    'HalRef': ('codat_sync_for_expenses.models.shared.halref', 'HalRef'),
    'HalRefTypedDict': ('codat_sync_for_expenses.models.shared.halref', 'HalRefTypedDict'),
    'IntegrationType': ('codat_sync_for_expenses.models.shared.integrationtype', 'IntegrationType'),
    'InvoiceTo': ('codat_sync_for_expenses.models.shared.invoiceto', 'InvoiceTo'),
    'InvoiceToType': ('codat_sync_for_expenses.models.invoice_to_type', 'InvoiceToType'),
    'InvoiceToTypedDict': ('codat_sync_for_expenses.models.shared.invoiceto', 'InvoiceToTypedDict'),
    'ItemRef': ('codat_sync_for_expenses.models.shared.itemref', 'ItemRef'),
    'ItemRefTypedDict': ('codat_sync_for_expenses.models.shared.itemref', 'ItemRefTypedDict'),
    'Items': ('codat_sync_for_expenses.models.shared.items', 'Items'),
    'ItemsTypedDict': ('codat_sync_for_expenses.models.shared.items', 'ItemsTypedDict'),
    'Links': ('codat_sync_for_expenses.models.shared.links', 'Links'),
    'LinksTypedDict': ('codat_sync_for_expenses.models.shared.links', 'LinksTypedDict'),
    'MappingOptions': ('codat_sync_for_expenses.models.shared.mappingoptions', 'MappingOptions'),
    'MappingOptionsTypedDict': ('codat_sync_for_expenses.models.shared.mappingoptions', 'MappingOptionsTypedDict'),
    'Metadata': ('codat_sync_for_expenses.models.shared.metadata', 'Metadata'),
    'MetadataTypedDict': ('codat_sync_for_expenses.models.shared.metadata', 'MetadataTypedDict'),
    'Model3': ('codat_sync_for_expenses.models.model3', 'Model3'),
    'Model3TypedDict': ('codat_sync_for_expenses.models.model3', 'Model3TypedDict'),
    'PagingInfo': ('codat_sync_for_expenses.models.paging_info', 'PagingInfo'),
    'PagingInfoTypedDict': ('codat_sync_for_expenses.models.paging_info', 'PagingInfoTypedDict'),
    'Phone': ('codat_sync_for_expenses.models.shared.phonenumber_items', 'PhoneNumberItems'),
    'PhoneNumberItems': ('codat_sync_for_expenses.models.shared.phonenumber_items', 'PhoneNumberItems'),
    'PhoneNumberItemsType': ('codat_sync_for_expenses.models.phone_number_items_type', 'PhoneNumberItemsType'),
    'PhoneNumberItemsTypedDict': ('codat_sync_for_expenses.models.shared.phonenumber_items', 'PhoneNumberItemsTypedDict'),
    'PhoneTypedDict': ('codat_sync_for_expenses.models.shared.phonenumber_items', 'PhoneNumberItemsTypedDict'),
    'PullOperation': ('codat_sync_for_expenses.models.shared.pulloperation', 'PullOperation'),
    'PullOperationTypedDict': ('codat_sync_for_expenses.models.shared.pulloperation', 'PullOperationTypedDict'),
    'PullOperations': ('codat_sync_for_expenses.models.shared.pulloperations', 'PullOperations'),
    'PullOperationsTypedDict': ('codat_sync_for_expenses.models.shared.pulloperations', 'PullOperationsTypedDict'),
    'PushChangeType': ('codat_sync_for_expenses.models.shared.pushchangetype', 'PushChangeType'),
    'PushFieldValidation': ('codat_sync_for_expenses.models.shared.pushfieldvalidation', 'PushFieldValidation'),
    'PushFieldValidationTypedDict': ('codat_sync_for_expenses.models.shared.pushfieldvalidation', 'PushFieldValidationTypedDict'),
    'PushOperation': ('codat_sync_for_expenses.models.shared.pushoperation', 'PushOperation'),
    'PushOperationChange': ('codat_sync_for_expenses.models.shared.pushoperationchange', 'PushOperationChange'),
    'PushOperationChangeTypedDict': ('codat_sync_for_expenses.models.shared.pushoperationchange', 'PushOperationChangeTypedDict'),
    'PushOperationRef': ('codat_sync_for_expenses.models.shared.pushoperationref', 'PushOperationRef'),
    'PushOperationRefTypedDict': ('codat_sync_for_expenses.models.shared.pushoperationref', 'PushOperationRefTypedDict'),
    'PushOperationStatus': ('codat_sync_for_expenses.models.shared.pushoperationstatus', 'PushOperationStatus'),
    'PushOperationTypedDict': ('codat_sync_for_expenses.models.shared.pushoperation', 'PushOperationTypedDict'),
    'PushOperations': ('codat_sync_for_expenses.models.shared.pushoperations', 'PushOperations'),
    'PushOperationsTypedDict': ('codat_sync_for_expenses.models.shared.pushoperations', 'PushOperationsTypedDict'),
    'PushOption': ('codat_sync_for_expenses.models.shared.pushoption', 'PushOption'),
    'PushOptionChoice': ('codat_sync_for_expenses.models.shared.pushoptionchoice', 'PushOptionChoice'),
    'PushOptionChoiceTypedDict': ('codat_sync_for_expenses.models.shared.pushoptionchoice', 'PushOptionChoiceTypedDict'),
    'PushOptionProperty': ('codat_sync_for_expenses.models.shared.pushoptionproperty', 'PushOptionProperty'),
    'PushOptionPropertyTypedDict': ('codat_sync_for_expenses.models.shared.pushoptionproperty', 'PushOptionPropertyTypedDict'),
    'PushOptionType': ('codat_sync_for_expenses.models.shared.pushoptiontype', 'PushOptionType'),
    'PushOptionTypedDict': ('codat_sync_for_expenses.models.shared.pushoption', 'PushOptionTypedDict'),
    'PushValidationInfo': ('codat_sync_for_expenses.models.shared.pushvalidationinfo', 'PushValidationInfo'),
    'PushValidationInfoTypedDict': ('codat_sync_for_expenses.models.shared.pushvalidationinfo', 'PushValidationInfoTypedDict'),
    'RecordRef': ('codat_sync_for_expenses.models.shared.recordref', 'RecordRef'),
    'RecordRefTypedDict': ('codat_sync_for_expenses.models.shared.recordref', 'RecordRefTypedDict'),
    'ReimbursableExpenseTransaction': ('codat_sync_for_expenses.models.shared.reimbursableexpensetransaction', 'ReimbursableExpenseTransaction'),
    'ReimbursableExpenseTransactionLine': ('codat_sync_for_expenses.models.shared.reimbursableexpensetransactionline', 'ReimbursableExpenseTransactionLine'),
    'ReimbursableExpenseTransactionLineTypedDict': ('codat_sync_for_expenses.models.shared.reimbursableexpensetransactionline', 'ReimbursableExpenseTransactionLineTypedDict'),
    'ReimbursableExpenseTransactionTypedDict': ('codat_sync_for_expenses.models.shared.reimbursableexpensetransaction', 'ReimbursableExpenseTransactionTypedDict'),
    'ReimbursementContactRef': ('codat_sync_for_expenses.models.shared.reimbursementcontactref', 'ReimbursementContactRef'),
    'ReimbursementContactRefTypedDict': ('codat_sync_for_expenses.models.shared.reimbursementcontactref', 'ReimbursementContactRefTypedDict'),
    'SchemaDataType': ('codat_sync_for_expenses.models.shared.schema_datatype', 'SchemaDataType'),
    'SchemaTransaction': ('codat_sync_for_expenses.models.shared.schema_transaction', 'SchemaTransaction'),
    'SchemaTransactionTypedDict': ('codat_sync_for_expenses.models.shared.schema_transaction', 'SchemaTransactionTypedDict'),
    'Security': ('codat_sync_for_expenses.models.shared.security', 'Security'),
    'SecurityTypedDict': ('codat_sync_for_expenses.models.shared.security', 'SecurityTypedDict'),
    'SourceType': ('codat_sync_for_expenses.models.source_type', 'SourceType'),
    'Status': ('codat_sync_for_expenses.models.shared.status', 'Status'),
    'SupplementalData': ('codat_sync_for_expenses.models.shared.supplementaldata', 'SupplementalData'),
    'SupplementalDataTypedDict': ('codat_sync_for_expenses.models.shared.supplementaldata', 'SupplementalDataTypedDict'),
    'Supplier': ('codat_sync_for_expenses.models.shared.supplier', 'Supplier'),
    'SupplierDetails': ('codat_sync_for_expenses.models.shared.supplierdetails', 'SupplierDetails'),
    'SupplierDetailsTypedDict': ('codat_sync_for_expenses.models.shared.supplierdetails', 'SupplierDetailsTypedDict'),
    'SupplierStatus': ('codat_sync_for_expenses.models.shared.supplierstatus', 'SupplierStatus'),
    'SupplierTypedDict': ('codat_sync_for_expenses.models.shared.supplier', 'SupplierTypedDict'),
    'Suppliers': ('codat_sync_for_expenses.models.shared.suppliers', 'Suppliers'),
    'SuppliersTypedDict': ('codat_sync_for_expenses.models.shared.suppliers', 'SuppliersTypedDict'),
    'SyncCompleteWebhook': ('codat_sync_for_expenses.models.sync_complete_webhook', 'SyncCompleteWebhook'),
    'SyncCompleteWebhookData': ('codat_sync_for_expenses.models.sync_complete_webhook_data', 'SyncCompleteWebhookData'),
    'SyncCompleteWebhookDataTypedDict': ('codat_sync_for_expenses.models.sync_complete_webhook_data', 'SyncCompleteWebhookDataTypedDict'),
    'SyncCompleteWebhookTypedDict': ('codat_sync_for_expenses.models.sync_complete_webhook', 'SyncCompleteWebhookTypedDict'),
    'SyncFailedWebhook': ('codat_sync_for_expenses.models.sync_failed_webhook', 'SyncFailedWebhook'),
    'SyncFailedWebhookData': ('codat_sync_for_expenses.models.sync_failed_webhook_data', 'SyncFailedWebhookData'),
    'SyncFailedWebhookDataTypedDict': ('codat_sync_for_expenses.models.sync_failed_webhook_data', 'SyncFailedWebhookDataTypedDict'),
    'SyncFailedWebhookTypedDict': ('codat_sync_for_expenses.models.sync_failed_webhook', 'SyncFailedWebhookTypedDict'),
    'SyncInitiated': ('codat_sync_for_expenses.models.sync_initiated', 'SyncInitiated'),
    'SyncInitiatedTypedDict': ('codat_sync_for_expenses.models.sync_initiated', 'SyncInitiatedTypedDict'),
    'TaxRateMappingInfo': ('codat_sync_for_expenses.models.shared.taxratemappinginfo', 'TaxRateMappingInfo'),
    'TaxRateMappingInfoTypedDict': ('codat_sync_for_expenses.models.shared.taxratemappinginfo', 'TaxRateMappingInfoTypedDict'),
    'To': ('codat_sync_for_expenses.models.transfer_transaction_request_to', 'TransferTransactionRequestTo'),
    'ToTypedDict': ('codat_sync_for_expenses.models.transfer_transaction_request_to', 'TransferTransactionRequestToTypedDict'),
    'TrackingCategoryMappingInfo': ('codat_sync_for_expenses.models.shared.trackingcategorymappinginfo', 'TrackingCategoryMappingInfo'),
    'TrackingCategoryMappingInfoTypedDict': ('codat_sync_for_expenses.models.shared.trackingcategorymappinginfo', 'TrackingCategoryMappingInfoTypedDict'),
    'TrackingRef': ('codat_sync_for_expenses.models.shared.trackingref', 'TrackingRef'),
    'TrackingRefAdjustmentTransaction': ('codat_sync_for_expenses.models.shared.trackingrefadjustmenttransaction', 'TrackingRefAdjustmentTransaction'),
    'TrackingRefAdjustmentTransactionDataType': ('codat_sync_for_expenses.models.tracking_ref_adjustment_transaction_data_type', 'TrackingRefAdjustmentTransactionDataType'),
    'TrackingRefAdjustmentTransactionTypedDict': ('codat_sync_for_expenses.models.shared.trackingrefadjustmenttransaction', 'TrackingRefAdjustmentTransactionTypedDict'),
    'TrackingRefDataType': ('codat_sync_for_expenses.models.tracking_ref_data_type', 'TrackingRefDataType'),
    'TrackingRefTypedDict': ('codat_sync_for_expenses.models.shared.trackingref', 'TrackingRefTypedDict'),
    'Transaction': ('codat_sync_for_expenses.models.transaction', 'Transaction'),
    'TransactionDefinitionsStatus': ('codat_sync_for_expenses.models.shared.transaction', 'TransactionDefinitionsStatus'),
    'TransactionStatus': ('codat_sync_for_expenses.models.shared.transactionstatus', 'TransactionStatus'),
    'TransactionTypedDict': ('codat_sync_for_expenses.models.transaction', 'TransactionTypedDict'),
    'Transactions': ('codat_sync_for_expenses.models.shared.transactions', 'Transactions'),
    'TransactionsTypedDict': ('codat_sync_for_expenses.models.shared.transactions', 'TransactionsTypedDict'),
    'TransferTransactionRequest': ('codat_sync_for_expenses.models.shared.transfertransactionrequest', 'TransferTransactionRequest'),
    'TransferTransactionRequestAccountReference': ('codat_sync_for_expenses.models.account_reference', 'AccountReference'),
    'TransferTransactionRequestAccountReferenceTypedDict': ('codat_sync_for_expenses.models.account_reference', 'AccountReferenceTypedDict'),
    'TransferTransactionRequestFrom': ('codat_sync_for_expenses.models.transfer_transaction_request_from', 'TransferTransactionRequestFrom'),
    'TransferTransactionRequestFromTypedDict': ('codat_sync_for_expenses.models.transfer_transaction_request_from', 'TransferTransactionRequestFromTypedDict'),
    'TransferTransactionRequestTo': ('codat_sync_for_expenses.models.transfer_transaction_request_to', 'TransferTransactionRequestTo'),
    'TransferTransactionRequestToTypedDict': ('codat_sync_for_expenses.models.transfer_transaction_request_to', 'TransferTransactionRequestToTypedDict'),
    'TransferTransactionRequestTypedDict': ('codat_sync_for_expenses.models.shared.transfertransactionrequest', 'TransferTransactionRequestTypedDict'),
    'TransferTransactionResponse': ('codat_sync_for_expenses.models.shared.transfertransactionresponse', 'TransferTransactionResponse'),
    'TransferTransactionResponseTypedDict': ('codat_sync_for_expenses.models.shared.transfertransactionresponse', 'TransferTransactionResponseTypedDict'),
    'Type': ('codat_sync_for_expenses.models.type', 'Type'),
    'UpdateConnection': ('codat_sync_for_expenses.models.update_connection', 'UpdateConnection'),
    'UpdateConnectionTypedDict': ('codat_sync_for_expenses.models.update_connection', 'UpdateConnectionTypedDict'),
    'UpdateCustomerResponse': ('codat_sync_for_expenses.models.shared.updatecustomerresponse', 'UpdateCustomerResponse'),
    'UpdateCustomerResponseAccountingCustomer': ('codat_sync_for_expenses.models.update_customer_response_all_of_data', 'UpdateCustomerResponseAllOfData'),
    'UpdateCustomerResponseAccountingCustomerTypedDict': ('codat_sync_for_expenses.models.update_customer_response_all_of_data', 'UpdateCustomerResponseAllOfData'),
    'UpdateCustomerResponseAllOfData': ('codat_sync_for_expenses.models.update_customer_response_all_of_data', 'UpdateCustomerResponseAllOfData'),
    'UpdateCustomerResponseAllOfDataTypedDict': ('codat_sync_for_expenses.models.update_customer_response_all_of_data', 'UpdateCustomerResponseAllOfDataTypedDict'),
    'UpdateCustomerResponseTypedDict': ('codat_sync_for_expenses.models.shared.updatecustomerresponse', 'UpdateCustomerResponseTypedDict'),
    'UpdateExpenseRequest': ('codat_sync_for_expenses.models.shared.updateexpenserequest', 'UpdateExpenseRequest'),
    'UpdateExpenseRequestBankAccountReference': ('codat_sync_for_expenses.models.bank_account_reference', 'BankAccountReference'),
    'UpdateExpenseRequestBankAccountReferenceTypedDict': ('codat_sync_for_expenses.models.bank_account_reference', 'BankAccountReferenceTypedDict'),
    'UpdateExpenseRequestType': ('codat_sync_for_expenses.models.update_expense_request_type', 'UpdateExpenseRequestType'),
    'UpdateExpenseRequestTypedDict': ('codat_sync_for_expenses.models.shared.updateexpenserequest', 'UpdateExpenseRequestTypedDict'),
    'UpdateExpenseResponse': ('codat_sync_for_expenses.models.shared.updateexpenseresponse', 'UpdateExpenseResponse'),
    'UpdateExpenseResponseTypedDict': ('codat_sync_for_expenses.models.shared.updateexpenseresponse', 'UpdateExpenseResponseTypedDict'),
    'UpdateReimbursableExpenseTransactionRequest': ('codat_sync_for_expenses.models.shared.updatereimbursableexpensetransactionrequest', 'UpdateReimbursableExpenseTransactionRequest'),
    'UpdateReimbursableExpenseTransactionRequestTypedDict': ('codat_sync_for_expenses.models.shared.updatereimbursableexpensetransactionrequest', 'UpdateReimbursableExpenseTransactionRequestTypedDict'),
    'UpdateSupplierResponse': ('codat_sync_for_expenses.models.shared.updatesupplierresponse', 'UpdateSupplierResponse'),
    'UpdateSupplierResponseAccountingSupplier': ('codat_sync_for_expenses.models.update_supplier_response_all_of_data', 'UpdateSupplierResponseAllOfData'),
    'UpdateSupplierResponseAccountingSupplierTypedDict': ('codat_sync_for_expenses.models.update_supplier_response_all_of_data', 'UpdateSupplierResponseAllOfData'),
    'UpdateSupplierResponseAllOfData': ('codat_sync_for_expenses.models.update_supplier_response_all_of_data', 'UpdateSupplierResponseAllOfData'),
    'UpdateSupplierResponseAllOfDataTypedDict': ('codat_sync_for_expenses.models.update_supplier_response_all_of_data', 'UpdateSupplierResponseAllOfDataTypedDict'),
    'UpdateSupplierResponseTypedDict': ('codat_sync_for_expenses.models.shared.updatesupplierresponse', 'UpdateSupplierResponseTypedDict'),
    'ValidDataTypeLinks': ('codat_sync_for_expenses.models.valid_data_type_links', 'ValidDataTypeLinks'),
    'ValidDataTypeLinksTypedDict': ('codat_sync_for_expenses.models.valid_data_type_links', 'ValidDataTypeLinksTypedDict'),
    'ValidFor': ('codat_sync_for_expenses.models.shared.validfor', 'ValidFor'),
    'ValidTransactionTypes': ('codat_sync_for_expenses.models.shared.validtransactiontypes', 'ValidTransactionTypes'),
    'Validation': ('codat_sync_for_expenses.models.shared.validation', 'Validation'),
    'ValidationItem': ('codat_sync_for_expenses.models.shared.validationitem', 'ValidationItem'),
    'ValidationItemTypedDict': ('codat_sync_for_expenses.models.shared.validationitem', 'ValidationItemTypedDict'),
    'ValidationTypedDict': ('codat_sync_for_expenses.models.shared.validation', 'ValidationTypedDict'),
    'Weblink': ('codat_sync_for_expenses.models.weblink', 'Weblink'),
    'WeblinkTypedDict': ('codat_sync_for_expenses.models.weblink', 'WeblinkTypedDict'),
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
