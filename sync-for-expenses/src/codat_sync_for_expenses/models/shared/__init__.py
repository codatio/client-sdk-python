"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .accountingaddresstype import AccountingAddressType
from .accountmappinginfo import (
    AccountMappingInfo,
    AccountMappingInfoAccountType,
    AccountMappingInfoTypedDict,
)
from .accountprototype import (
    AccountPrototype,
    AccountPrototypeTypedDict,
    ValidDataTypeLinks,
    ValidDataTypeLinksTypedDict,
)
from .accountstatus import AccountStatus
from .accounttype import AccountType
from .adjustmenttransactionline import (
    AdjustmentTransactionLine,
    AdjustmentTransactionLineTypedDict,
)
from .adjustmenttransactionrequest import (
    AdjustmentTransactionRequest,
    AdjustmentTransactionRequestTypedDict,
)
from .adjustmenttransactionresponse import (
    AdjustmentTransactionResponse,
    AdjustmentTransactionResponseTypedDict,
)
from .apaccountref import ApAccountRef, ApAccountRefTypedDict
from .attachment import Attachment, AttachmentTypedDict
from .attachmentupload import AttachmentUpload, AttachmentUploadTypedDict
from .bankaccount import BankAccount, BankAccountType, BankAccountTypedDict
from .bankaccountdetails import BankAccountDetails, BankAccountDetailsTypedDict
from .bankaccountstatus import BankAccountStatus
from .clientratelimitreachedwebhook import (
    ClientRateLimitReachedWebhook,
    ClientRateLimitReachedWebhookTypedDict,
)
from .clientratelimitreachedwebhookdata import (
    ClientRateLimitReachedWebhookData,
    ClientRateLimitReachedWebhookDataTypedDict,
)
from .clientratelimitresetwebhook import (
    ClientRateLimitResetWebhook,
    ClientRateLimitResetWebhookTypedDict,
)
from .clientratelimitresetwebhookdata import (
    ClientRateLimitResetWebhookData,
    ClientRateLimitResetWebhookDataTypedDict,
)
from .clientratelimitwebhook import (
    ClientRateLimitWebhook,
    ClientRateLimitWebhookTypedDict,
)
from .clientratelimitwebhookpayload import (
    ClientRateLimitWebhookPayload,
    ClientRateLimitWebhookPayloadTypedDict,
)
from .codatfile import CodatFile, CodatFileTypedDict
from .companies import Companies, CompaniesTypedDict
from .company import Company, CompanyTypedDict
from .companyconfiguration import CompanyConfiguration, CompanyConfigurationTypedDict
from .companyinformation import (
    AccountingAddress,
    AccountingAddressTypedDict,
    CompanyInformation,
    CompanyInformationType,
    CompanyInformationTypedDict,
    Phone,
    PhoneTypedDict,
    Weblink,
    WeblinkTypedDict,
)
from .companyreference import (
    CompanyReference,
    CompanyReferenceLinks,
    CompanyReferenceLinksTypedDict,
    CompanyReferenceTypedDict,
)
from .companyrequestbody import CompanyRequestBody, CompanyRequestBodyTypedDict
from .companysyncstatus import CompanySyncStatus, CompanySyncStatusTypedDict
from .connection import Connection, ConnectionTypedDict, SourceType
from .connections import Connections, ConnectionsTypedDict
from .contact import Contact, ContactTypedDict
from .createaccountresponse import (
    AccountingAccount,
    AccountingAccountTypedDict,
    CreateAccountResponse,
    CreateAccountResponseMetadata,
    CreateAccountResponseMetadataTypedDict,
    CreateAccountResponseTypedDict,
    CreateAccountResponseValidDataTypeLinks,
    CreateAccountResponseValidDataTypeLinksTypedDict,
)
from .createbankaccountresponse import (
    AccountingBankAccount,
    AccountingBankAccountTypedDict,
    CreateBankAccountResponse,
    CreateBankAccountResponseBankAccountType,
    CreateBankAccountResponseTypedDict,
)
from .createcustomerresponse import (
    AccountingCustomer,
    AccountingCustomerTypedDict,
    CreateCustomerResponse,
    CreateCustomerResponseTypedDict,
)
from .createexpenseresponse import CreateExpenseResponse, CreateExpenseResponseTypedDict
from .createreimbursableexpenseresponse import (
    CreateReimbursableExpenseResponse,
    CreateReimbursableExpenseResponseTypedDict,
)
from .createsupplierresponse import (
    AccountingSupplier,
    AccountingSupplierTypedDict,
    CreateSupplierResponse,
    CreateSupplierResponseTypedDict,
)
from .customer import Customer, CustomerTypedDict
from .customerdetails import CustomerDetails, CustomerDetailsTypedDict
from .customers import Customers, CustomersTypedDict
from .customerstatus import CustomerStatus
from .dataconnectionerror import (
    DataConnectionError,
    DataConnectionErrorTypedDict,
    ErrorStatus,
)
from .dataconnectionstatus import DataConnectionStatus
from .datastatus import DataStatus, DataStatusTypedDict, DataTypes
from .datatype import DataType
from .errorvalidation import ErrorValidation, ErrorValidationTypedDict
from .errorvalidationitem import ErrorValidationItem, ErrorValidationItemTypedDict
from .expensecontactref import ExpenseContactRef, ExpenseContactRefTypedDict, Type
from .expensessyncwebhook import ExpensesSyncWebhook, ExpensesSyncWebhookTypedDict
from .expensessyncwebhookpayload import (
    ExpensesSyncWebhookPayload,
    ExpensesSyncWebhookPayloadTypedDict,
)
from .expensetransaction import (
    BankAccountReference,
    BankAccountReferenceTypedDict,
    ExpenseTransaction,
    ExpenseTransactionType,
    ExpenseTransactionTypedDict,
)
from .expensetransactionline import (
    ExpenseTransactionLine,
    ExpenseTransactionLineTypedDict,
)
from .halref import HalRef, HalRefTypedDict
from .integrationtype import IntegrationType
from .invoiceto import InvoiceTo, InvoiceToType, InvoiceToTypedDict
from .itemref import ItemRef, ItemRefTypedDict
from .items import Items, ItemsTypedDict
from .links import Links, LinksTypedDict
from .mappingoptions import MappingOptions, MappingOptionsTypedDict
from .metadata import Metadata, MetadataTypedDict
from .phonenumber_items import PhoneNumberItems, PhoneNumberItemsTypedDict
from .phonenumbertype import PhoneNumberType
from .pulloperation import DatasetStatus, PullOperation, PullOperationTypedDict
from .pulloperations import PullOperations, PullOperationsTypedDict
from .pushchangetype import PushChangeType
from .pushfieldvalidation import PushFieldValidation, PushFieldValidationTypedDict
from .pushoperation import PushOperation, PushOperationTypedDict
from .pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
from .pushoperationref import PushOperationRef, PushOperationRefTypedDict
from .pushoperations import PushOperations, PushOperationsTypedDict
from .pushoperationstatus import PushOperationStatus
from .pushoption import PushOption, PushOptionTypedDict
from .pushoptionchoice import PushOptionChoice, PushOptionChoiceTypedDict
from .pushoptionproperty import PushOptionProperty, PushOptionPropertyTypedDict
from .pushoptiontype import PushOptionType
from .pushvalidationinfo import PushValidationInfo, PushValidationInfoTypedDict
from .recordref import RecordRef, RecordRefTypedDict
from .reimbursableexpensetransaction import (
    ReimbursableExpenseTransaction,
    ReimbursableExpenseTransactionTypedDict,
)
from .reimbursableexpensetransactionline import (
    ReimbursableExpenseTransactionLine,
    ReimbursableExpenseTransactionLineTypedDict,
)
from .reimbursementcontactref import (
    ReimbursementContactRef,
    ReimbursementContactRefTypedDict,
)
from .schema_datatype import SchemaDataType
from .schema_transaction import SchemaTransaction, SchemaTransactionTypedDict
from .security import Security, SecurityTypedDict
from .status import Status
from .supplementaldata import SupplementalData, SupplementalDataTypedDict
from .supplier import Supplier, SupplierTypedDict
from .supplierdetails import SupplierDetails, SupplierDetailsTypedDict
from .suppliers import Suppliers, SuppliersTypedDict
from .supplierstatus import SupplierStatus
from .synccompletewebhook import SyncCompleteWebhook, SyncCompleteWebhookTypedDict
from .synccompletewebhookdata import (
    SyncCompleteWebhookData,
    SyncCompleteWebhookDataTypedDict,
)
from .syncfailedwebhook import SyncFailedWebhook, SyncFailedWebhookTypedDict
from .syncfailedwebhookdata import SyncFailedWebhookData, SyncFailedWebhookDataTypedDict
from .taxratemappinginfo import TaxRateMappingInfo, TaxRateMappingInfoTypedDict
from .trackingcategorymappinginfo import (
    TrackingCategoryMappingInfo,
    TrackingCategoryMappingInfoTypedDict,
)
from .trackingref import TrackingRef, TrackingRefDataType, TrackingRefTypedDict
from .trackingrefadjustmenttransaction import (
    TrackingRefAdjustmentTransaction,
    TrackingRefAdjustmentTransactionDataType,
    TrackingRefAdjustmentTransactionTypedDict,
)
from .transaction import Transaction, TransactionDefinitionsStatus, TransactionTypedDict
from .transactions import Transactions, TransactionsTypedDict
from .transactionstatus import TransactionStatus
from .transfertransactionrequest import (
    AccountReference,
    AccountReferenceTypedDict,
    From,
    FromTypedDict,
    To,
    ToTypedDict,
    TransferTransactionRequest,
    TransferTransactionRequestAccountReference,
    TransferTransactionRequestAccountReferenceTypedDict,
    TransferTransactionRequestTypedDict,
)
from .transfertransactionresponse import (
    TransferTransactionResponse,
    TransferTransactionResponseTypedDict,
)
from .updatecustomerresponse import (
    UpdateCustomerResponse,
    UpdateCustomerResponseAccountingCustomer,
    UpdateCustomerResponseAccountingCustomerTypedDict,
    UpdateCustomerResponseTypedDict,
)
from .updateexpenserequest import (
    UpdateExpenseRequest,
    UpdateExpenseRequestBankAccountReference,
    UpdateExpenseRequestBankAccountReferenceTypedDict,
    UpdateExpenseRequestType,
    UpdateExpenseRequestTypedDict,
)
from .updateexpenseresponse import UpdateExpenseResponse, UpdateExpenseResponseTypedDict
from .updatereimbursableexpensetransactionrequest import (
    UpdateReimbursableExpenseTransactionRequest,
    UpdateReimbursableExpenseTransactionRequestTypedDict,
)
from .updatesupplierresponse import (
    UpdateSupplierResponse,
    UpdateSupplierResponseAccountingSupplier,
    UpdateSupplierResponseAccountingSupplierTypedDict,
    UpdateSupplierResponseTypedDict,
)
from .validation import Validation, ValidationTypedDict
from .validationitem import ValidationItem, ValidationItemTypedDict
from .validfor import ValidFor
from .validtransactiontypes import ValidTransactionTypes

__all__ = [
    "AccountMappingInfo",
    "AccountMappingInfoAccountType",
    "AccountMappingInfoTypedDict",
    "AccountPrototype",
    "AccountPrototypeTypedDict",
    "AccountReference",
    "AccountReferenceTypedDict",
    "AccountStatus",
    "AccountType",
    "AccountingAccount",
    "AccountingAccountTypedDict",
    "AccountingAddress",
    "AccountingAddressType",
    "AccountingAddressTypedDict",
    "AccountingBankAccount",
    "AccountingBankAccountTypedDict",
    "AccountingCustomer",
    "AccountingCustomerTypedDict",
    "AccountingSupplier",
    "AccountingSupplierTypedDict",
    "AdjustmentTransactionLine",
    "AdjustmentTransactionLineTypedDict",
    "AdjustmentTransactionRequest",
    "AdjustmentTransactionRequestTypedDict",
    "AdjustmentTransactionResponse",
    "AdjustmentTransactionResponseTypedDict",
    "ApAccountRef",
    "ApAccountRefTypedDict",
    "Attachment",
    "AttachmentTypedDict",
    "AttachmentUpload",
    "AttachmentUploadTypedDict",
    "BankAccount",
    "BankAccountDetails",
    "BankAccountDetailsTypedDict",
    "BankAccountReference",
    "BankAccountReferenceTypedDict",
    "BankAccountStatus",
    "BankAccountType",
    "BankAccountTypedDict",
    "ClientRateLimitReachedWebhook",
    "ClientRateLimitReachedWebhookData",
    "ClientRateLimitReachedWebhookDataTypedDict",
    "ClientRateLimitReachedWebhookTypedDict",
    "ClientRateLimitResetWebhook",
    "ClientRateLimitResetWebhookData",
    "ClientRateLimitResetWebhookDataTypedDict",
    "ClientRateLimitResetWebhookTypedDict",
    "ClientRateLimitWebhook",
    "ClientRateLimitWebhookPayload",
    "ClientRateLimitWebhookPayloadTypedDict",
    "ClientRateLimitWebhookTypedDict",
    "CodatFile",
    "CodatFileTypedDict",
    "Companies",
    "CompaniesTypedDict",
    "Company",
    "CompanyConfiguration",
    "CompanyConfigurationTypedDict",
    "CompanyInformation",
    "CompanyInformationType",
    "CompanyInformationTypedDict",
    "CompanyReference",
    "CompanyReferenceLinks",
    "CompanyReferenceLinksTypedDict",
    "CompanyReferenceTypedDict",
    "CompanyRequestBody",
    "CompanyRequestBodyTypedDict",
    "CompanySyncStatus",
    "CompanySyncStatusTypedDict",
    "CompanyTypedDict",
    "Connection",
    "ConnectionTypedDict",
    "Connections",
    "ConnectionsTypedDict",
    "Contact",
    "ContactTypedDict",
    "CreateAccountResponse",
    "CreateAccountResponseMetadata",
    "CreateAccountResponseMetadataTypedDict",
    "CreateAccountResponseTypedDict",
    "CreateAccountResponseValidDataTypeLinks",
    "CreateAccountResponseValidDataTypeLinksTypedDict",
    "CreateBankAccountResponse",
    "CreateBankAccountResponseBankAccountType",
    "CreateBankAccountResponseTypedDict",
    "CreateCustomerResponse",
    "CreateCustomerResponseTypedDict",
    "CreateExpenseResponse",
    "CreateExpenseResponseTypedDict",
    "CreateReimbursableExpenseResponse",
    "CreateReimbursableExpenseResponseTypedDict",
    "CreateSupplierResponse",
    "CreateSupplierResponseTypedDict",
    "Customer",
    "CustomerDetails",
    "CustomerDetailsTypedDict",
    "CustomerStatus",
    "CustomerTypedDict",
    "Customers",
    "CustomersTypedDict",
    "DataConnectionError",
    "DataConnectionErrorTypedDict",
    "DataConnectionStatus",
    "DataStatus",
    "DataStatusTypedDict",
    "DataType",
    "DataTypes",
    "DatasetStatus",
    "ErrorStatus",
    "ErrorValidation",
    "ErrorValidationItem",
    "ErrorValidationItemTypedDict",
    "ErrorValidationTypedDict",
    "ExpenseContactRef",
    "ExpenseContactRefTypedDict",
    "ExpenseTransaction",
    "ExpenseTransactionLine",
    "ExpenseTransactionLineTypedDict",
    "ExpenseTransactionType",
    "ExpenseTransactionTypedDict",
    "ExpensesSyncWebhook",
    "ExpensesSyncWebhookPayload",
    "ExpensesSyncWebhookPayloadTypedDict",
    "ExpensesSyncWebhookTypedDict",
    "From",
    "FromTypedDict",
    "HalRef",
    "HalRefTypedDict",
    "IntegrationType",
    "InvoiceTo",
    "InvoiceToType",
    "InvoiceToTypedDict",
    "ItemRef",
    "ItemRefTypedDict",
    "Items",
    "ItemsTypedDict",
    "Links",
    "LinksTypedDict",
    "MappingOptions",
    "MappingOptionsTypedDict",
    "Metadata",
    "MetadataTypedDict",
    "Phone",
    "PhoneNumberItems",
    "PhoneNumberItemsTypedDict",
    "PhoneNumberType",
    "PhoneTypedDict",
    "PullOperation",
    "PullOperationTypedDict",
    "PullOperations",
    "PullOperationsTypedDict",
    "PushChangeType",
    "PushFieldValidation",
    "PushFieldValidationTypedDict",
    "PushOperation",
    "PushOperationChange",
    "PushOperationChangeTypedDict",
    "PushOperationRef",
    "PushOperationRefTypedDict",
    "PushOperationStatus",
    "PushOperationTypedDict",
    "PushOperations",
    "PushOperationsTypedDict",
    "PushOption",
    "PushOptionChoice",
    "PushOptionChoiceTypedDict",
    "PushOptionProperty",
    "PushOptionPropertyTypedDict",
    "PushOptionType",
    "PushOptionTypedDict",
    "PushValidationInfo",
    "PushValidationInfoTypedDict",
    "RecordRef",
    "RecordRefTypedDict",
    "ReimbursableExpenseTransaction",
    "ReimbursableExpenseTransactionLine",
    "ReimbursableExpenseTransactionLineTypedDict",
    "ReimbursableExpenseTransactionTypedDict",
    "ReimbursementContactRef",
    "ReimbursementContactRefTypedDict",
    "SchemaDataType",
    "SchemaTransaction",
    "SchemaTransactionTypedDict",
    "Security",
    "SecurityTypedDict",
    "SourceType",
    "Status",
    "SupplementalData",
    "SupplementalDataTypedDict",
    "Supplier",
    "SupplierDetails",
    "SupplierDetailsTypedDict",
    "SupplierStatus",
    "SupplierTypedDict",
    "Suppliers",
    "SuppliersTypedDict",
    "SyncCompleteWebhook",
    "SyncCompleteWebhookData",
    "SyncCompleteWebhookDataTypedDict",
    "SyncCompleteWebhookTypedDict",
    "SyncFailedWebhook",
    "SyncFailedWebhookData",
    "SyncFailedWebhookDataTypedDict",
    "SyncFailedWebhookTypedDict",
    "TaxRateMappingInfo",
    "TaxRateMappingInfoTypedDict",
    "To",
    "ToTypedDict",
    "TrackingCategoryMappingInfo",
    "TrackingCategoryMappingInfoTypedDict",
    "TrackingRef",
    "TrackingRefAdjustmentTransaction",
    "TrackingRefAdjustmentTransactionDataType",
    "TrackingRefAdjustmentTransactionTypedDict",
    "TrackingRefDataType",
    "TrackingRefTypedDict",
    "Transaction",
    "TransactionDefinitionsStatus",
    "TransactionStatus",
    "TransactionTypedDict",
    "Transactions",
    "TransactionsTypedDict",
    "TransferTransactionRequest",
    "TransferTransactionRequestAccountReference",
    "TransferTransactionRequestAccountReferenceTypedDict",
    "TransferTransactionRequestTypedDict",
    "TransferTransactionResponse",
    "TransferTransactionResponseTypedDict",
    "Type",
    "UpdateCustomerResponse",
    "UpdateCustomerResponseAccountingCustomer",
    "UpdateCustomerResponseAccountingCustomerTypedDict",
    "UpdateCustomerResponseTypedDict",
    "UpdateExpenseRequest",
    "UpdateExpenseRequestBankAccountReference",
    "UpdateExpenseRequestBankAccountReferenceTypedDict",
    "UpdateExpenseRequestType",
    "UpdateExpenseRequestTypedDict",
    "UpdateExpenseResponse",
    "UpdateExpenseResponseTypedDict",
    "UpdateReimbursableExpenseTransactionRequest",
    "UpdateReimbursableExpenseTransactionRequestTypedDict",
    "UpdateSupplierResponse",
    "UpdateSupplierResponseAccountingSupplier",
    "UpdateSupplierResponseAccountingSupplierTypedDict",
    "UpdateSupplierResponseTypedDict",
    "ValidDataTypeLinks",
    "ValidDataTypeLinksTypedDict",
    "ValidFor",
    "ValidTransactionTypes",
    "Validation",
    "ValidationItem",
    "ValidationItemTypedDict",
    "ValidationTypedDict",
    "Weblink",
    "WeblinkTypedDict",
]
