"""codat_bankfeeds.models.shared — domain-shared models."""

from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .security import Security, SecurityTypedDict
    from codat_bankfeeds.models.access_token import AccessToken, AccessTokenTypedDict
    from codat_bankfeeds.models.shared.accountinfo import AccountInfo, AccountInfoTypedDict
    from codat_bankfeeds.models.shared.accounttype import AccountType
    from codat_bankfeeds.models.accounting_bank_account import AccountingBankAccount, AccountingBankAccountTypedDict
    from codat_bankfeeds.models.shared.bankaccountcreateresponse import BankAccountCreateResponse, BankAccountCreateResponseTypedDict
    from codat_bankfeeds.models.bank_account_create_response_all_of_data import BankAccountCreateResponseAllOfData, BankAccountCreateResponseAllOfDataTypedDict
    from codat_bankfeeds.models.bank_account_create_response_bank_account_type import BankAccountCreateResponseBankAccountType
    from codat_bankfeeds.models.shared.bankaccountcredentials import BankAccountCredentials, BankAccountCredentialsTypedDict
    from codat_bankfeeds.models.shared.bankaccountprototype import BankAccountPrototype, BankAccountPrototypeTypedDict
    from codat_bankfeeds.models.shared.bankaccountstatus import BankAccountStatus
    from codat_bankfeeds.models.bank_account_type import BankAccountType
    from codat_bankfeeds.models.shared.bankaccounts import BankAccounts, BankAccountsTypedDict
    from codat_bankfeeds.models.bank_accounts_bank_account_type import BankAccountsBankAccountType
    from codat_bankfeeds.models.shared.bankfeedaccountmapping import BankFeedAccountMapping, BankFeedAccountMappingTypedDict
    from codat_bankfeeds.models.shared.bankfeedaccountmappingresponse import BankFeedAccountMappingResponse, BankFeedAccountMappingResponseTypedDict
    from codat_bankfeeds.models.shared.bankfeedmapping import BankFeedMapping, BankFeedMappingTypedDict
    from codat_bankfeeds.models.bank_transaction import BankTransaction, BankTransactionTypedDict
    from codat_bankfeeds.models.bank_transaction_type import BankTransactionType
    from codat_bankfeeds.models.shared.clientratelimitwebhook import ClientRateLimitWebhook, ClientRateLimitWebhookTypedDict
    from codat_bankfeeds.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayload, ClientRateLimitWebhookPayloadTypedDict
    from codat_bankfeeds.models.shared.companies import Companies, CompaniesTypedDict
    from codat_bankfeeds.models.shared.company import Company, CompanyTypedDict
    from codat_bankfeeds.models.shared.companyaccesstoken import CompanyAccessToken, CompanyAccessTokenTypedDict
    from codat_bankfeeds.models.company_details import CompanyDetails, CompanyDetailsTypedDict
    from codat_bankfeeds.models.shared.companyinformation import CompanyInformation, CompanyInformationTypedDict
    from codat_bankfeeds.models.shared.companyreference import CompanyReference, CompanyReferenceTypedDict
    from codat_bankfeeds.models.company_reference_links import CompanyReferenceLinks, CompanyReferenceLinksTypedDict
    from codat_bankfeeds.models.shared.companyrequestbody import CompanyRequestBody, CompanyRequestBodyTypedDict
    from codat_bankfeeds.models.shared.companyupdaterequest import CompanyUpdateRequest, CompanyUpdateRequestTypedDict
    from codat_bankfeeds.models.shared.connection import Connection, ConnectionTypedDict
    from codat_bankfeeds.models.shared.connections import Connections, ConnectionsTypedDict
    from codat_bankfeeds.models.shared.createbanktransactions import CreateBankTransactions, CreateBankTransactionsTypedDict
    from codat_bankfeeds.models.shared.createbanktransactionsresponse import CreateBankTransactionsResponse, CreateBankTransactionsResponseTypedDict
    from codat_bankfeeds.models.create_batch_source_account201_response_inner import CreateBatchSourceAccount201ResponseInner, CreateBatchSourceAccount201ResponseInnerTypedDict
    from codat_bankfeeds.models.create_batch_source_account207_response_inner import CreateBatchSourceAccount207ResponseInner, CreateBatchSourceAccount207ResponseInnerTypedDict
    from codat_bankfeeds.models.create_batch_source_account_request_body import CreateBatchSourceAccountRequestBody, CreateBatchSourceAccountRequestBodyTypedDict
    from codat_bankfeeds.models.create_connection_request import CreateConnectionRequest, CreateConnectionRequestTypedDict
    from codat_bankfeeds.models.create_source_account200_response import CreateSourceAccount200Response, CreateSourceAccount200ResponseTypedDict
    from codat_bankfeeds.models.create_source_account_request import CreateSourceAccountRequest, CreateSourceAccountRequestTypedDict
    from codat_bankfeeds.models.shared.dataconnectionerror import DataConnectionError, DataConnectionErrorTypedDict
    from codat_bankfeeds.models.shared.dataconnectionstatus import DataConnectionStatus
    from codat_bankfeeds.models.shared.datatype import DataType
    from codat_bankfeeds.models.dataset_status import DatasetStatus
    from codat_bankfeeds.models.error_message import ErrorMessage, ErrorMessageTypedDict
    from codat_bankfeeds.models.error_status import ErrorStatus
    from codat_bankfeeds.models.shared.errorvalidation import ErrorValidation, ErrorValidationTypedDict
    from codat_bankfeeds.models.shared.errorvalidationitem import ErrorValidationItem, ErrorValidationItemTypedDict
    from codat_bankfeeds.models.shared.generateotpresponse import GenerateOtpResponse, GenerateOtpResponseTypedDict
    from codat_bankfeeds.models.shared.halref import HalRef, HalRefTypedDict
    from codat_bankfeeds.models.items import Items, ItemsTypedDict
    from codat_bankfeeds.models.items_bank_account_type import ItemsBankAccountType
    from codat_bankfeeds.models.shared.links import Links, LinksTypedDict
    from codat_bankfeeds.models.list_source_accounts200_response import ListSourceAccounts200Response, ListSourceAccounts200ResponseTypedDict
    from codat_bankfeeds.models.metadata import Metadata, MetadataTypedDict
    from codat_bankfeeds.models.model1 import Model1, Model1TypedDict
    from codat_bankfeeds.models.pull_operation import PullOperation, PullOperationTypedDict
    from codat_bankfeeds.models.pull_operations import PullOperations, PullOperationsTypedDict
    from codat_bankfeeds.models.shared.pushchangetype import PushChangeType
    from codat_bankfeeds.models.shared.pushfieldvalidation import PushFieldValidation, PushFieldValidationTypedDict
    from codat_bankfeeds.models.shared.pushoperation import PushOperation, PushOperationTypedDict
    from codat_bankfeeds.models.shared.pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
    from codat_bankfeeds.models.shared.pushoperationref import PushOperationRef, PushOperationRefTypedDict
    from codat_bankfeeds.models.shared.pushoperationstatus import PushOperationStatus
    from codat_bankfeeds.models.shared.pushoperations import PushOperations, PushOperationsTypedDict
    from codat_bankfeeds.models.shared.pushoption import PushOption, PushOptionTypedDict
    from codat_bankfeeds.models.shared.pushoptionchoice import PushOptionChoice, PushOptionChoiceTypedDict
    from codat_bankfeeds.models.shared.pushoptionproperty import PushOptionProperty, PushOptionPropertyTypedDict
    from codat_bankfeeds.models.shared.pushoptiontype import PushOptionType
    from codat_bankfeeds.models.shared.pushvalidationinfo import PushValidationInfo, PushValidationInfoTypedDict
    from codat_bankfeeds.models.shared.routinginfo import RoutingInfo, RoutingInfoTypedDict
    from codat_bankfeeds.models.shared.sourceaccount import SourceAccount, SourceAccountTypedDict
    from codat_bankfeeds.models.shared.sourceaccountbatchcreateresponse import SourceAccountBatchCreateResponse, SourceAccountBatchCreateResponseTypedDict
    from codat_bankfeeds.models.shared.sourceaccountbatchcreateresult import SourceAccountBatchCreateResult, SourceAccountBatchCreateResultTypedDict
    from codat_bankfeeds.models.shared.sourceaccountbatcherrorresponse import SourceAccountBatchErrorResponse, SourceAccountBatchErrorResponseTypedDict
    from codat_bankfeeds.models.source_account_batch_error_response_result import SourceAccountBatchErrorResponseResult, SourceAccountBatchErrorResponseResultTypedDict
    from codat_bankfeeds.models.shared.sourceaccountprototype import SourceAccountPrototype, SourceAccountPrototypeTypedDict
    from codat_bankfeeds.models.source_account_v2 import SourceAccountV2, SourceAccountV2TypedDict
    from codat_bankfeeds.models.shared.sourceaccountv2batchcreateresponse import SourceAccountV2BatchCreateResponse, SourceAccountV2BatchCreateResponseTypedDict
    from codat_bankfeeds.models.shared.sourceaccountv2batchcreateresult import SourceAccountV2BatchCreateResult, SourceAccountV2BatchCreateResultTypedDict
    from codat_bankfeeds.models.shared.sourceaccountv2prototype import SourceAccountV2Prototype, SourceAccountV2PrototypeTypedDict
    from codat_bankfeeds.models.source_account_v2_status import SourceAccountV2Status
    from codat_bankfeeds.models.shared.sourceaccountwebhook import SourceAccountWebhook, SourceAccountWebhookTypedDict
    from codat_bankfeeds.models.shared.sourceaccountwebhookpayload import SourceAccountWebhookPayload, SourceAccountWebhookPayloadTypedDict
    from codat_bankfeeds.models.source_type import SourceType
    from codat_bankfeeds.models.shared.startscheduledsyncresult import StartScheduledSyncResult, StartScheduledSyncResultTypedDict
    from codat_bankfeeds.models.status import Status
    from codat_bankfeeds.models.supplemental_data import SupplementalData, SupplementalDataTypedDict
    from codat_bankfeeds.models.shared.syncstatusresult import SyncStatusResult, SyncStatusResultTypedDict
    from codat_bankfeeds.models.shared.targetaccountoption import TargetAccountOption, TargetAccountOptionTypedDict
    from codat_bankfeeds.models.type import Type
    from codat_bankfeeds.models.update_connection import UpdateConnection, UpdateConnectionTypedDict
    from codat_bankfeeds.models.shared.validation import Validation, ValidationTypedDict
    from codat_bankfeeds.models.shared.validationitem import ValidationItem, ValidationItemTypedDict
    from codat_bankfeeds.models.shared.sourceaccountv2 import SourceAccountV2AccountType
    from codat_bankfeeds.models.shared.accountinfo import AccountInfoTypedDict as AccountInfoTypedDict
    from codat_bankfeeds.models.shared.accounttype import AccountType as AccountType
    from codat_bankfeeds.models.accounting_bank_account import AccountingBankAccountTypedDict as AccountingBankAccountTypedDict
    from codat_bankfeeds.models.bank_account_create_response_bank_account_type import BankAccountCreateResponseBankAccountType as BankAccountCreateResponseBankAccountType
    from codat_bankfeeds.models.shared.bankaccountcreateresponse import BankAccountCreateResponseTypedDict as BankAccountCreateResponseTypedDict
    from codat_bankfeeds.models.shared.bankaccountcredentials import BankAccountCredentialsTypedDict as BankAccountCredentialsTypedDict
    from codat_bankfeeds.models.shared.bankaccountprototype import BankAccountPrototypeTypedDict as BankAccountPrototypeTypedDict
    from codat_bankfeeds.models.shared.bankaccountstatus import BankAccountStatus as BankAccountStatus
    from codat_bankfeeds.models.bank_account_type import BankAccountType as BankAccountType
    from codat_bankfeeds.models.accounting_bank_account import AccountingBankAccount as BankAccountsAccountingBankAccount
    from codat_bankfeeds.models.accounting_bank_account import AccountingBankAccountTypedDict as BankAccountsAccountingBankAccountTypedDict
    from codat_bankfeeds.models.bank_accounts_bank_account_type import BankAccountsBankAccountType as BankAccountsBankAccountType
    from codat_bankfeeds.models.metadata import Metadata as BankAccountsMetadata
    from codat_bankfeeds.models.metadata import MetadataTypedDict as BankAccountsMetadataTypedDict
    from codat_bankfeeds.models.supplemental_data import SupplementalData as BankAccountsSupplementalData
    from codat_bankfeeds.models.supplemental_data import SupplementalDataTypedDict as BankAccountsSupplementalDataTypedDict
    from codat_bankfeeds.models.shared.bankaccounts import BankAccountsTypedDict as BankAccountsTypedDict
    from codat_bankfeeds.models.shared.bankfeedaccountmappingresponse import BankFeedAccountMappingResponseTypedDict as BankFeedAccountMappingResponseTypedDict
    from codat_bankfeeds.models.shared.bankfeedaccountmapping import BankFeedAccountMappingTypedDict as BankFeedAccountMappingTypedDict
    from codat_bankfeeds.models.shared.bankfeedmapping import BankFeedMappingTypedDict as BankFeedMappingTypedDict
    from codat_bankfeeds.models.bank_transaction_type import BankTransactionType as BankTransactionType
    from codat_bankfeeds.models.bank_transaction import BankTransaction as BankTransactions
    from codat_bankfeeds.models.bank_transaction import BankTransactionTypedDict as BankTransactionsTypedDict
    from codat_bankfeeds.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayloadTypedDict as ClientRateLimitWebhookPayloadTypedDict
    from codat_bankfeeds.models.shared.clientratelimitwebhook import ClientRateLimitWebhookTypedDict as ClientRateLimitWebhookTypedDict
    from codat_bankfeeds.models.shared.companies import CompaniesTypedDict as CompaniesTypedDict
    from codat_bankfeeds.models.shared.companyaccesstoken import CompanyAccessTokenTypedDict as CompanyAccessTokenTypedDict
    from codat_bankfeeds.models.shared.companyinformation import CompanyInformationTypedDict as CompanyInformationTypedDict
    from codat_bankfeeds.models.company_reference_links import CompanyReferenceLinksTypedDict as CompanyReferenceLinksTypedDict
    from codat_bankfeeds.models.shared.companyreference import CompanyReferenceTypedDict as CompanyReferenceTypedDict
    from codat_bankfeeds.models.shared.companyrequestbody import CompanyRequestBodyTypedDict as CompanyRequestBodyTypedDict
    from codat_bankfeeds.models.shared.company import CompanyTypedDict as CompanyTypedDict
    from codat_bankfeeds.models.shared.companyupdaterequest import CompanyUpdateRequestTypedDict as CompanyUpdateRequestTypedDict
    from codat_bankfeeds.models.shared.connection import ConnectionTypedDict as ConnectionTypedDict
    from codat_bankfeeds.models.shared.connections import ConnectionsTypedDict as ConnectionsTypedDict
    from codat_bankfeeds.models.shared.createbanktransactionsresponse import CreateBankTransactionsResponseTypedDict as CreateBankTransactionsResponseTypedDict
    from codat_bankfeeds.models.shared.createbanktransactions import CreateBankTransactionsTypedDict as CreateBankTransactionsTypedDict
    from codat_bankfeeds.models.shared.dataconnectionerror import DataConnectionErrorTypedDict as DataConnectionErrorTypedDict
    from codat_bankfeeds.models.shared.dataconnectionstatus import DataConnectionStatus as DataConnectionStatus
    from codat_bankfeeds.models.shared.datatype import DataType as DataType
    from codat_bankfeeds.models.error_status import ErrorStatus as ErrorStatus
    from codat_bankfeeds.models.shared.errorvalidationitem import ErrorValidationItemTypedDict as ErrorValidationItemTypedDict
    from codat_bankfeeds.models.shared.errorvalidation import ErrorValidationTypedDict as ErrorValidationTypedDict
    from codat_bankfeeds.models.shared.generateotpresponse import GenerateOtpResponseTypedDict as GenerateOtpResponseTypedDict
    from codat_bankfeeds.models.shared.halref import HalRefTypedDict as HalRefTypedDict
    from codat_bankfeeds.models.shared.links import LinksTypedDict as LinksTypedDict
    from codat_bankfeeds.models.metadata import MetadataTypedDict as MetadataTypedDict
    from codat_bankfeeds.models.shared.pushchangetype import PushChangeType as PushChangeType
    from codat_bankfeeds.models.shared.pushfieldvalidation import PushFieldValidationTypedDict as PushFieldValidationTypedDict
    from codat_bankfeeds.models.shared.pushoperationchange import PushOperationChangeTypedDict as PushOperationChangeTypedDict
    from codat_bankfeeds.models.shared.pushoperationref import PushOperationRefTypedDict as PushOperationRefTypedDict
    from codat_bankfeeds.models.shared.pushoperationstatus import PushOperationStatus as PushOperationStatus
    from codat_bankfeeds.models.shared.pushoperation import PushOperationTypedDict as PushOperationTypedDict
    from codat_bankfeeds.models.shared.pushoperations import PushOperationsTypedDict as PushOperationsTypedDict
    from codat_bankfeeds.models.shared.pushoptionchoice import PushOptionChoiceTypedDict as PushOptionChoiceTypedDict
    from codat_bankfeeds.models.shared.pushoptionproperty import PushOptionPropertyTypedDict as PushOptionPropertyTypedDict
    from codat_bankfeeds.models.shared.pushoptiontype import PushOptionType as PushOptionType
    from codat_bankfeeds.models.shared.pushoption import PushOptionTypedDict as PushOptionTypedDict
    from codat_bankfeeds.models.shared.pushvalidationinfo import PushValidationInfoTypedDict as PushValidationInfoTypedDict
    from codat_bankfeeds.models.source_account_batch_error_response_result import SourceAccountBatchErrorResponseResult as Result
    from codat_bankfeeds.models.source_account_batch_error_response_result import SourceAccountBatchErrorResponseResultTypedDict as ResultTypedDict
    from codat_bankfeeds.models.shared.routinginfo import RoutingInfoTypedDict as RoutingInfoTypedDict
    from codat_bankfeeds.models.shared.security import Security as Security
    from codat_bankfeeds.models.shared.security import SecurityTypedDict as SecurityTypedDict
    from codat_bankfeeds.models.shared.sourceaccountbatchcreateresponse import SourceAccountBatchCreateResponseTypedDict as SourceAccountBatchCreateResponseTypedDict
    from codat_bankfeeds.models.shared.sourceaccountbatchcreateresult import SourceAccountBatchCreateResultTypedDict as SourceAccountBatchCreateResultTypedDict
    from codat_bankfeeds.models.shared.sourceaccountbatcherrorresponse import SourceAccountBatchErrorResponseTypedDict as SourceAccountBatchErrorResponseTypedDict
    from codat_bankfeeds.models.shared.sourceaccountprototype import SourceAccountPrototypeTypedDict as SourceAccountPrototypeTypedDict
    from codat_bankfeeds.models.shared.sourceaccount import SourceAccountTypedDict as SourceAccountTypedDict
    from codat_bankfeeds.models.shared.sourceaccountv2 import SourceAccountV2AccountType as SourceAccountV2AccountType
    from codat_bankfeeds.models.shared.sourceaccountv2batchcreateresponse import SourceAccountV2BatchCreateResponseTypedDict as SourceAccountV2BatchCreateResponseTypedDict
    from codat_bankfeeds.models.shared.sourceaccountv2batchcreateresult import SourceAccountV2BatchCreateResultTypedDict as SourceAccountV2BatchCreateResultTypedDict
    from codat_bankfeeds.models.shared.sourceaccountv2prototype import SourceAccountV2PrototypeTypedDict as SourceAccountV2PrototypeTypedDict
    from codat_bankfeeds.models.source_account_v2_status import SourceAccountV2Status as SourceAccountV2Status
    from codat_bankfeeds.models.source_account_v2 import SourceAccountV2TypedDict as SourceAccountV2TypedDict
    from codat_bankfeeds.models.shared.sourceaccountwebhookpayload import SourceAccountWebhookPayloadTypedDict as SourceAccountWebhookPayloadTypedDict
    from codat_bankfeeds.models.shared.sourceaccountwebhook import SourceAccountWebhookTypedDict as SourceAccountWebhookTypedDict
    from codat_bankfeeds.models.source_type import SourceType as SourceType
    from codat_bankfeeds.models.shared.startscheduledsyncresult import StartScheduledSyncResultTypedDict as StartScheduledSyncResultTypedDict
    from codat_bankfeeds.models.status import Status as Status
    from codat_bankfeeds.models.supplemental_data import SupplementalDataTypedDict as SupplementalDataTypedDict
    from codat_bankfeeds.models.shared.syncstatusresult import SyncStatusResultTypedDict as SyncStatusResultTypedDict
    from codat_bankfeeds.models.shared.targetaccountoption import TargetAccountOptionTypedDict as TargetAccountOptionTypedDict
    from codat_bankfeeds.models.type import Type as Type
    from codat_bankfeeds.models.shared.validationitem import ValidationItemTypedDict as ValidationItemTypedDict
    from codat_bankfeeds.models.shared.validation import ValidationTypedDict as ValidationTypedDict
    from codat_bankfeeds.models.shared.source_account_webhook_payload_source_account import SourceAccountWebhookPayloadSourceAccount
    from codat_bankfeeds.models.shared.source_account_webhook_payload_source_account_typed_dict import SourceAccountWebhookPayloadSourceAccountTypedDict

_dynamic_imports: dict[str, tuple[str, str]] = {
    'AccessToken': ('codat_bankfeeds.models.access_token', 'AccessToken'),
    'AccessTokenTypedDict': ('codat_bankfeeds.models.access_token', 'AccessTokenTypedDict'),
    'AccountInfo': ('codat_bankfeeds.models.shared.accountinfo', 'AccountInfo'),
    'AccountInfoTypedDict': ('codat_bankfeeds.models.shared.accountinfo', 'AccountInfoTypedDict'),
    'AccountType': ('codat_bankfeeds.models.shared.accounttype', 'AccountType'),
    'AccountingBankAccount': ('codat_bankfeeds.models.accounting_bank_account', 'AccountingBankAccount'),
    'AccountingBankAccountTypedDict': ('codat_bankfeeds.models.accounting_bank_account', 'AccountingBankAccountTypedDict'),
    'BankAccountCreateResponse': ('codat_bankfeeds.models.shared.bankaccountcreateresponse', 'BankAccountCreateResponse'),
    'BankAccountCreateResponseAllOfData': ('codat_bankfeeds.models.bank_account_create_response_all_of_data', 'BankAccountCreateResponseAllOfData'),
    'BankAccountCreateResponseAllOfDataTypedDict': ('codat_bankfeeds.models.bank_account_create_response_all_of_data', 'BankAccountCreateResponseAllOfDataTypedDict'),
    'BankAccountCreateResponseBankAccountType': ('codat_bankfeeds.models.bank_account_create_response_bank_account_type', 'BankAccountCreateResponseBankAccountType'),
    'BankAccountCreateResponseTypedDict': ('codat_bankfeeds.models.shared.bankaccountcreateresponse', 'BankAccountCreateResponseTypedDict'),
    'BankAccountCredentials': ('codat_bankfeeds.models.shared.bankaccountcredentials', 'BankAccountCredentials'),
    'BankAccountCredentialsTypedDict': ('codat_bankfeeds.models.shared.bankaccountcredentials', 'BankAccountCredentialsTypedDict'),
    'BankAccountPrototype': ('codat_bankfeeds.models.shared.bankaccountprototype', 'BankAccountPrototype'),
    'BankAccountPrototypeTypedDict': ('codat_bankfeeds.models.shared.bankaccountprototype', 'BankAccountPrototypeTypedDict'),
    'BankAccountStatus': ('codat_bankfeeds.models.shared.bankaccountstatus', 'BankAccountStatus'),
    'BankAccountType': ('codat_bankfeeds.models.bank_account_type', 'BankAccountType'),
    'BankAccounts': ('codat_bankfeeds.models.shared.bankaccounts', 'BankAccounts'),
    'BankAccountsAccountingBankAccount': ('codat_bankfeeds.models.accounting_bank_account', 'AccountingBankAccount'),
    'BankAccountsAccountingBankAccountTypedDict': ('codat_bankfeeds.models.accounting_bank_account', 'AccountingBankAccountTypedDict'),
    'BankAccountsBankAccountType': ('codat_bankfeeds.models.bank_accounts_bank_account_type', 'BankAccountsBankAccountType'),
    'BankAccountsMetadata': ('codat_bankfeeds.models.metadata', 'Metadata'),
    'BankAccountsMetadataTypedDict': ('codat_bankfeeds.models.metadata', 'MetadataTypedDict'),
    'BankAccountsSupplementalData': ('codat_bankfeeds.models.supplemental_data', 'SupplementalData'),
    'BankAccountsSupplementalDataTypedDict': ('codat_bankfeeds.models.supplemental_data', 'SupplementalDataTypedDict'),
    'BankAccountsTypedDict': ('codat_bankfeeds.models.shared.bankaccounts', 'BankAccountsTypedDict'),
    'BankFeedAccountMapping': ('codat_bankfeeds.models.shared.bankfeedaccountmapping', 'BankFeedAccountMapping'),
    'BankFeedAccountMappingResponse': ('codat_bankfeeds.models.shared.bankfeedaccountmappingresponse', 'BankFeedAccountMappingResponse'),
    'BankFeedAccountMappingResponseTypedDict': ('codat_bankfeeds.models.shared.bankfeedaccountmappingresponse', 'BankFeedAccountMappingResponseTypedDict'),
    'BankFeedAccountMappingTypedDict': ('codat_bankfeeds.models.shared.bankfeedaccountmapping', 'BankFeedAccountMappingTypedDict'),
    'BankFeedMapping': ('codat_bankfeeds.models.shared.bankfeedmapping', 'BankFeedMapping'),
    'BankFeedMappingTypedDict': ('codat_bankfeeds.models.shared.bankfeedmapping', 'BankFeedMappingTypedDict'),
    'BankTransaction': ('codat_bankfeeds.models.bank_transaction', 'BankTransaction'),
    'BankTransactionType': ('codat_bankfeeds.models.bank_transaction_type', 'BankTransactionType'),
    'BankTransactionTypedDict': ('codat_bankfeeds.models.bank_transaction', 'BankTransactionTypedDict'),
    'BankTransactions': ('codat_bankfeeds.models.bank_transaction', 'BankTransaction'),
    'BankTransactionsTypedDict': ('codat_bankfeeds.models.bank_transaction', 'BankTransactionTypedDict'),
    'ClientRateLimitWebhook': ('codat_bankfeeds.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhook'),
    'ClientRateLimitWebhookPayload': ('codat_bankfeeds.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayload'),
    'ClientRateLimitWebhookPayloadTypedDict': ('codat_bankfeeds.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayloadTypedDict'),
    'ClientRateLimitWebhookTypedDict': ('codat_bankfeeds.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhookTypedDict'),
    'Companies': ('codat_bankfeeds.models.shared.companies', 'Companies'),
    'CompaniesTypedDict': ('codat_bankfeeds.models.shared.companies', 'CompaniesTypedDict'),
    'Company': ('codat_bankfeeds.models.shared.company', 'Company'),
    'CompanyAccessToken': ('codat_bankfeeds.models.shared.companyaccesstoken', 'CompanyAccessToken'),
    'CompanyAccessTokenTypedDict': ('codat_bankfeeds.models.shared.companyaccesstoken', 'CompanyAccessTokenTypedDict'),
    'CompanyDetails': ('codat_bankfeeds.models.company_details', 'CompanyDetails'),
    'CompanyDetailsTypedDict': ('codat_bankfeeds.models.company_details', 'CompanyDetailsTypedDict'),
    'CompanyInformation': ('codat_bankfeeds.models.shared.companyinformation', 'CompanyInformation'),
    'CompanyInformationTypedDict': ('codat_bankfeeds.models.shared.companyinformation', 'CompanyInformationTypedDict'),
    'CompanyReference': ('codat_bankfeeds.models.shared.companyreference', 'CompanyReference'),
    'CompanyReferenceLinks': ('codat_bankfeeds.models.company_reference_links', 'CompanyReferenceLinks'),
    'CompanyReferenceLinksTypedDict': ('codat_bankfeeds.models.company_reference_links', 'CompanyReferenceLinksTypedDict'),
    'CompanyReferenceTypedDict': ('codat_bankfeeds.models.shared.companyreference', 'CompanyReferenceTypedDict'),
    'CompanyRequestBody': ('codat_bankfeeds.models.shared.companyrequestbody', 'CompanyRequestBody'),
    'CompanyRequestBodyTypedDict': ('codat_bankfeeds.models.shared.companyrequestbody', 'CompanyRequestBodyTypedDict'),
    'CompanyTypedDict': ('codat_bankfeeds.models.shared.company', 'CompanyTypedDict'),
    'CompanyUpdateRequest': ('codat_bankfeeds.models.shared.companyupdaterequest', 'CompanyUpdateRequest'),
    'CompanyUpdateRequestTypedDict': ('codat_bankfeeds.models.shared.companyupdaterequest', 'CompanyUpdateRequestTypedDict'),
    'Connection': ('codat_bankfeeds.models.shared.connection', 'Connection'),
    'ConnectionTypedDict': ('codat_bankfeeds.models.shared.connection', 'ConnectionTypedDict'),
    'Connections': ('codat_bankfeeds.models.shared.connections', 'Connections'),
    'ConnectionsTypedDict': ('codat_bankfeeds.models.shared.connections', 'ConnectionsTypedDict'),
    'CreateBankTransactions': ('codat_bankfeeds.models.shared.createbanktransactions', 'CreateBankTransactions'),
    'CreateBankTransactionsResponse': ('codat_bankfeeds.models.shared.createbanktransactionsresponse', 'CreateBankTransactionsResponse'),
    'CreateBankTransactionsResponseTypedDict': ('codat_bankfeeds.models.shared.createbanktransactionsresponse', 'CreateBankTransactionsResponseTypedDict'),
    'CreateBankTransactionsTypedDict': ('codat_bankfeeds.models.shared.createbanktransactions', 'CreateBankTransactionsTypedDict'),
    'CreateBatchSourceAccount201ResponseInner': ('codat_bankfeeds.models.create_batch_source_account201_response_inner', 'CreateBatchSourceAccount201ResponseInner'),
    'CreateBatchSourceAccount201ResponseInnerTypedDict': ('codat_bankfeeds.models.create_batch_source_account201_response_inner', 'CreateBatchSourceAccount201ResponseInnerTypedDict'),
    'CreateBatchSourceAccount207ResponseInner': ('codat_bankfeeds.models.create_batch_source_account207_response_inner', 'CreateBatchSourceAccount207ResponseInner'),
    'CreateBatchSourceAccount207ResponseInnerTypedDict': ('codat_bankfeeds.models.create_batch_source_account207_response_inner', 'CreateBatchSourceAccount207ResponseInnerTypedDict'),
    'CreateBatchSourceAccountRequestBody': ('codat_bankfeeds.models.create_batch_source_account_request_body', 'CreateBatchSourceAccountRequestBody'),
    'CreateBatchSourceAccountRequestBodyTypedDict': ('codat_bankfeeds.models.create_batch_source_account_request_body', 'CreateBatchSourceAccountRequestBodyTypedDict'),
    'CreateConnectionRequest': ('codat_bankfeeds.models.create_connection_request', 'CreateConnectionRequest'),
    'CreateConnectionRequestTypedDict': ('codat_bankfeeds.models.create_connection_request', 'CreateConnectionRequestTypedDict'),
    'CreateSourceAccount200Response': ('codat_bankfeeds.models.create_source_account200_response', 'CreateSourceAccount200Response'),
    'CreateSourceAccount200ResponseTypedDict': ('codat_bankfeeds.models.create_source_account200_response', 'CreateSourceAccount200ResponseTypedDict'),
    'CreateSourceAccountRequest': ('codat_bankfeeds.models.create_source_account_request', 'CreateSourceAccountRequest'),
    'CreateSourceAccountRequestTypedDict': ('codat_bankfeeds.models.create_source_account_request', 'CreateSourceAccountRequestTypedDict'),
    'DataConnectionError': ('codat_bankfeeds.models.shared.dataconnectionerror', 'DataConnectionError'),
    'DataConnectionErrorTypedDict': ('codat_bankfeeds.models.shared.dataconnectionerror', 'DataConnectionErrorTypedDict'),
    'DataConnectionStatus': ('codat_bankfeeds.models.shared.dataconnectionstatus', 'DataConnectionStatus'),
    'DataType': ('codat_bankfeeds.models.shared.datatype', 'DataType'),
    'DatasetStatus': ('codat_bankfeeds.models.dataset_status', 'DatasetStatus'),
    'ErrorMessage': ('codat_bankfeeds.models.error_message', 'ErrorMessage'),
    'ErrorMessageTypedDict': ('codat_bankfeeds.models.error_message', 'ErrorMessageTypedDict'),
    'ErrorStatus': ('codat_bankfeeds.models.error_status', 'ErrorStatus'),
    'ErrorValidation': ('codat_bankfeeds.models.shared.errorvalidation', 'ErrorValidation'),
    'ErrorValidationItem': ('codat_bankfeeds.models.shared.errorvalidationitem', 'ErrorValidationItem'),
    'ErrorValidationItemTypedDict': ('codat_bankfeeds.models.shared.errorvalidationitem', 'ErrorValidationItemTypedDict'),
    'ErrorValidationTypedDict': ('codat_bankfeeds.models.shared.errorvalidation', 'ErrorValidationTypedDict'),
    'GenerateOtpResponse': ('codat_bankfeeds.models.shared.generateotpresponse', 'GenerateOtpResponse'),
    'GenerateOtpResponseTypedDict': ('codat_bankfeeds.models.shared.generateotpresponse', 'GenerateOtpResponseTypedDict'),
    'HalRef': ('codat_bankfeeds.models.shared.halref', 'HalRef'),
    'HalRefTypedDict': ('codat_bankfeeds.models.shared.halref', 'HalRefTypedDict'),
    'Items': ('codat_bankfeeds.models.items', 'Items'),
    'ItemsBankAccountType': ('codat_bankfeeds.models.items_bank_account_type', 'ItemsBankAccountType'),
    'ItemsTypedDict': ('codat_bankfeeds.models.items', 'ItemsTypedDict'),
    'Links': ('codat_bankfeeds.models.shared.links', 'Links'),
    'LinksTypedDict': ('codat_bankfeeds.models.shared.links', 'LinksTypedDict'),
    'ListSourceAccounts200Response': ('codat_bankfeeds.models.list_source_accounts200_response', 'ListSourceAccounts200Response'),
    'ListSourceAccounts200ResponseTypedDict': ('codat_bankfeeds.models.list_source_accounts200_response', 'ListSourceAccounts200ResponseTypedDict'),
    'Metadata': ('codat_bankfeeds.models.metadata', 'Metadata'),
    'MetadataTypedDict': ('codat_bankfeeds.models.metadata', 'MetadataTypedDict'),
    'Model1': ('codat_bankfeeds.models.model1', 'Model1'),
    'Model1TypedDict': ('codat_bankfeeds.models.model1', 'Model1TypedDict'),
    'PullOperation': ('codat_bankfeeds.models.pull_operation', 'PullOperation'),
    'PullOperationTypedDict': ('codat_bankfeeds.models.pull_operation', 'PullOperationTypedDict'),
    'PullOperations': ('codat_bankfeeds.models.pull_operations', 'PullOperations'),
    'PullOperationsTypedDict': ('codat_bankfeeds.models.pull_operations', 'PullOperationsTypedDict'),
    'PushChangeType': ('codat_bankfeeds.models.shared.pushchangetype', 'PushChangeType'),
    'PushFieldValidation': ('codat_bankfeeds.models.shared.pushfieldvalidation', 'PushFieldValidation'),
    'PushFieldValidationTypedDict': ('codat_bankfeeds.models.shared.pushfieldvalidation', 'PushFieldValidationTypedDict'),
    'PushOperation': ('codat_bankfeeds.models.shared.pushoperation', 'PushOperation'),
    'PushOperationChange': ('codat_bankfeeds.models.shared.pushoperationchange', 'PushOperationChange'),
    'PushOperationChangeTypedDict': ('codat_bankfeeds.models.shared.pushoperationchange', 'PushOperationChangeTypedDict'),
    'PushOperationRef': ('codat_bankfeeds.models.shared.pushoperationref', 'PushOperationRef'),
    'PushOperationRefTypedDict': ('codat_bankfeeds.models.shared.pushoperationref', 'PushOperationRefTypedDict'),
    'PushOperationStatus': ('codat_bankfeeds.models.shared.pushoperationstatus', 'PushOperationStatus'),
    'PushOperationTypedDict': ('codat_bankfeeds.models.shared.pushoperation', 'PushOperationTypedDict'),
    'PushOperations': ('codat_bankfeeds.models.shared.pushoperations', 'PushOperations'),
    'PushOperationsTypedDict': ('codat_bankfeeds.models.shared.pushoperations', 'PushOperationsTypedDict'),
    'PushOption': ('codat_bankfeeds.models.shared.pushoption', 'PushOption'),
    'PushOptionChoice': ('codat_bankfeeds.models.shared.pushoptionchoice', 'PushOptionChoice'),
    'PushOptionChoiceTypedDict': ('codat_bankfeeds.models.shared.pushoptionchoice', 'PushOptionChoiceTypedDict'),
    'PushOptionProperty': ('codat_bankfeeds.models.shared.pushoptionproperty', 'PushOptionProperty'),
    'PushOptionPropertyTypedDict': ('codat_bankfeeds.models.shared.pushoptionproperty', 'PushOptionPropertyTypedDict'),
    'PushOptionType': ('codat_bankfeeds.models.shared.pushoptiontype', 'PushOptionType'),
    'PushOptionTypedDict': ('codat_bankfeeds.models.shared.pushoption', 'PushOptionTypedDict'),
    'PushValidationInfo': ('codat_bankfeeds.models.shared.pushvalidationinfo', 'PushValidationInfo'),
    'PushValidationInfoTypedDict': ('codat_bankfeeds.models.shared.pushvalidationinfo', 'PushValidationInfoTypedDict'),
    'Result': ('codat_bankfeeds.models.source_account_batch_error_response_result', 'SourceAccountBatchErrorResponseResult'),
    'ResultTypedDict': ('codat_bankfeeds.models.source_account_batch_error_response_result', 'SourceAccountBatchErrorResponseResultTypedDict'),
    'RoutingInfo': ('codat_bankfeeds.models.shared.routinginfo', 'RoutingInfo'),
    'RoutingInfoTypedDict': ('codat_bankfeeds.models.shared.routinginfo', 'RoutingInfoTypedDict'),
    'Security': ('codat_bankfeeds.models.shared.security', 'Security'),
    'SecurityTypedDict': ('codat_bankfeeds.models.shared.security', 'SecurityTypedDict'),
    'SourceAccount': ('codat_bankfeeds.models.shared.sourceaccount', 'SourceAccount'),
    'SourceAccountBatchCreateResponse': ('codat_bankfeeds.models.shared.sourceaccountbatchcreateresponse', 'SourceAccountBatchCreateResponse'),
    'SourceAccountBatchCreateResponseTypedDict': ('codat_bankfeeds.models.shared.sourceaccountbatchcreateresponse', 'SourceAccountBatchCreateResponseTypedDict'),
    'SourceAccountBatchCreateResult': ('codat_bankfeeds.models.shared.sourceaccountbatchcreateresult', 'SourceAccountBatchCreateResult'),
    'SourceAccountBatchCreateResultTypedDict': ('codat_bankfeeds.models.shared.sourceaccountbatchcreateresult', 'SourceAccountBatchCreateResultTypedDict'),
    'SourceAccountBatchErrorResponse': ('codat_bankfeeds.models.shared.sourceaccountbatcherrorresponse', 'SourceAccountBatchErrorResponse'),
    'SourceAccountBatchErrorResponseResult': ('codat_bankfeeds.models.source_account_batch_error_response_result', 'SourceAccountBatchErrorResponseResult'),
    'SourceAccountBatchErrorResponseResultTypedDict': ('codat_bankfeeds.models.source_account_batch_error_response_result', 'SourceAccountBatchErrorResponseResultTypedDict'),
    'SourceAccountBatchErrorResponseTypedDict': ('codat_bankfeeds.models.shared.sourceaccountbatcherrorresponse', 'SourceAccountBatchErrorResponseTypedDict'),
    'SourceAccountPrototype': ('codat_bankfeeds.models.shared.sourceaccountprototype', 'SourceAccountPrototype'),
    'SourceAccountPrototypeTypedDict': ('codat_bankfeeds.models.shared.sourceaccountprototype', 'SourceAccountPrototypeTypedDict'),
    'SourceAccountTypedDict': ('codat_bankfeeds.models.shared.sourceaccount', 'SourceAccountTypedDict'),
    'SourceAccountV2': ('codat_bankfeeds.models.source_account_v2', 'SourceAccountV2'),
    'SourceAccountV2AccountType': ('codat_bankfeeds.models.shared.sourceaccountv2', 'SourceAccountV2AccountType'),
    'SourceAccountV2BatchCreateResponse': ('codat_bankfeeds.models.shared.sourceaccountv2batchcreateresponse', 'SourceAccountV2BatchCreateResponse'),
    'SourceAccountV2BatchCreateResponseTypedDict': ('codat_bankfeeds.models.shared.sourceaccountv2batchcreateresponse', 'SourceAccountV2BatchCreateResponseTypedDict'),
    'SourceAccountV2BatchCreateResult': ('codat_bankfeeds.models.shared.sourceaccountv2batchcreateresult', 'SourceAccountV2BatchCreateResult'),
    'SourceAccountV2BatchCreateResultTypedDict': ('codat_bankfeeds.models.shared.sourceaccountv2batchcreateresult', 'SourceAccountV2BatchCreateResultTypedDict'),
    'SourceAccountV2Prototype': ('codat_bankfeeds.models.shared.sourceaccountv2prototype', 'SourceAccountV2Prototype'),
    'SourceAccountV2PrototypeTypedDict': ('codat_bankfeeds.models.shared.sourceaccountv2prototype', 'SourceAccountV2PrototypeTypedDict'),
    'SourceAccountV2Status': ('codat_bankfeeds.models.source_account_v2_status', 'SourceAccountV2Status'),
    'SourceAccountV2TypedDict': ('codat_bankfeeds.models.source_account_v2', 'SourceAccountV2TypedDict'),
    'SourceAccountWebhook': ('codat_bankfeeds.models.shared.sourceaccountwebhook', 'SourceAccountWebhook'),
    'SourceAccountWebhookPayload': ('codat_bankfeeds.models.shared.sourceaccountwebhookpayload', 'SourceAccountWebhookPayload'),
    'SourceAccountWebhookPayloadSourceAccount': ('codat_bankfeeds.models.shared.source_account_webhook_payload_source_account', 'SourceAccountWebhookPayloadSourceAccount'),
    'SourceAccountWebhookPayloadSourceAccountTypedDict': ('codat_bankfeeds.models.shared.source_account_webhook_payload_source_account_typed_dict', 'SourceAccountWebhookPayloadSourceAccountTypedDict'),
    'SourceAccountWebhookPayloadTypedDict': ('codat_bankfeeds.models.shared.sourceaccountwebhookpayload', 'SourceAccountWebhookPayloadTypedDict'),
    'SourceAccountWebhookTypedDict': ('codat_bankfeeds.models.shared.sourceaccountwebhook', 'SourceAccountWebhookTypedDict'),
    'SourceType': ('codat_bankfeeds.models.source_type', 'SourceType'),
    'StartScheduledSyncResult': ('codat_bankfeeds.models.shared.startscheduledsyncresult', 'StartScheduledSyncResult'),
    'StartScheduledSyncResultTypedDict': ('codat_bankfeeds.models.shared.startscheduledsyncresult', 'StartScheduledSyncResultTypedDict'),
    'Status': ('codat_bankfeeds.models.status', 'Status'),
    'SupplementalData': ('codat_bankfeeds.models.supplemental_data', 'SupplementalData'),
    'SupplementalDataTypedDict': ('codat_bankfeeds.models.supplemental_data', 'SupplementalDataTypedDict'),
    'SyncStatusResult': ('codat_bankfeeds.models.shared.syncstatusresult', 'SyncStatusResult'),
    'SyncStatusResultTypedDict': ('codat_bankfeeds.models.shared.syncstatusresult', 'SyncStatusResultTypedDict'),
    'TargetAccountOption': ('codat_bankfeeds.models.shared.targetaccountoption', 'TargetAccountOption'),
    'TargetAccountOptionTypedDict': ('codat_bankfeeds.models.shared.targetaccountoption', 'TargetAccountOptionTypedDict'),
    'Type': ('codat_bankfeeds.models.type', 'Type'),
    'UpdateConnection': ('codat_bankfeeds.models.update_connection', 'UpdateConnection'),
    'UpdateConnectionTypedDict': ('codat_bankfeeds.models.update_connection', 'UpdateConnectionTypedDict'),
    'Validation': ('codat_bankfeeds.models.shared.validation', 'Validation'),
    'ValidationItem': ('codat_bankfeeds.models.shared.validationitem', 'ValidationItem'),
    'ValidationItemTypedDict': ('codat_bankfeeds.models.shared.validationitem', 'ValidationItemTypedDict'),
    'ValidationTypedDict': ('codat_bankfeeds.models.shared.validation', 'ValidationTypedDict'),
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
