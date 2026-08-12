"""codat_platform.models.shared — domain-shared models."""

from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .security import Security, SecurityTypedDict
    from codat_platform.models.access_token import AccessToken, AccessTokenTypedDict
    from codat_platform.models.shared.apikeydetails import APIKeyDetails, APIKeyDetailsTypedDict
    from codat_platform.models.shared.apikeydetails import APIKeyDetailsTypedDict as ApiKeyDetailsTypedDict
    from codat_platform.models.shared.apikeydetails import APIKeyDetails as ApiKeyDetails
    from codat_platform.models.shared.apikeys import APIKeys, APIKeysTypedDict
    from codat_platform.models.shared.apikeys import APIKeysTypedDict as ApiKeysTypedDict
    from codat_platform.models.shared.apikeys import APIKeys as ApiKeys
    from codat_platform.models.shared.branding import Branding, BrandingTypedDict
    from codat_platform.models.shared.brandingbutton import BrandingButton, BrandingButtonTypedDict
    from codat_platform.models.shared.brandingimage import BrandingImage, BrandingImageTypedDict
    from codat_platform.models.shared.brandinglogo import BrandingLogo, BrandingLogoTypedDict
    from codat_platform.models.shared.clientratelimitwebhook import ClientRateLimitWebhook, ClientRateLimitWebhookTypedDict
    from codat_platform.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayload, ClientRateLimitWebhookPayloadTypedDict
    from codat_platform.models.shared.companies import Companies, CompaniesTypedDict
    from codat_platform.models.shared.company import Company, CompanyTypedDict
    from codat_platform.models.shared.companyaccesstoken import CompanyAccessToken, CompanyAccessTokenTypedDict
    from codat_platform.models.shared.companydetails import CompanyDetails, CompanyDetailsTypedDict
    from codat_platform.models.company_product_webhook import CompanyProductWebhook, CompanyProductWebhookTypedDict
    from codat_platform.models.company_product_webhook_payload import CompanyProductWebhookPayload, CompanyProductWebhookPayloadTypedDict
    from codat_platform.models.shared.companyreference import CompanyReference, CompanyReferenceTypedDict
    from codat_platform.models.company_reference_links import CompanyReferenceLinks, CompanyReferenceLinksTypedDict
    from codat_platform.models.shared.companyrequestbody import CompanyRequestBody, CompanyRequestBodyTypedDict
    from codat_platform.models.shared.companysyncsettings import CompanySyncSettings, CompanySyncSettingsTypedDict
    from codat_platform.models.shared.companyupdaterequest import CompanyUpdateRequest, CompanyUpdateRequestTypedDict
    from codat_platform.models.shared.companywebhook import CompanyWebhook, CompanyWebhookTypedDict
    from codat_platform.models.shared.connection import Connection, ConnectionTypedDict
    from codat_platform.models.shared.connectionmanagementaccesstoken import ConnectionManagementAccessToken, ConnectionManagementAccessTokenTypedDict
    from codat_platform.models.shared.connectionmanagementallowedorigins import ConnectionManagementAllowedOrigins, ConnectionManagementAllowedOriginsTypedDict
    from codat_platform.models.shared.connectionwebhook import ConnectionWebhook, ConnectionWebhookTypedDict
    from codat_platform.models.shared.connectionwebhookpayload import ConnectionWebhookPayload, ConnectionWebhookPayloadTypedDict
    from codat_platform.models.shared.connections import Connections, ConnectionsTypedDict
    from codat_platform.models.shared.createapikey import CreateAPIKey, CreateAPIKeyTypedDict
    from codat_platform.models.shared.createapikey import CreateAPIKeyTypedDict as CreateApiKeyTypedDict
    from codat_platform.models.shared.createapikey import CreateAPIKey as CreateApiKey
    from codat_platform.models.create_connection_request import CreateConnectionRequest, CreateConnectionRequestTypedDict
    from codat_platform.models.current_status import CurrentStatus
    from codat_platform.models.shared.customdatatypeconfiguration import CustomDataTypeConfiguration, CustomDataTypeConfigurationTypedDict
    from codat_platform.models.shared.customdatatyperecord import CustomDataTypeRecord, CustomDataTypeRecordTypedDict
    from codat_platform.models.shared.customdatatyperecords import CustomDataTypeRecords, CustomDataTypeRecordsTypedDict
    from codat_platform.models.shared.dataconnectionerror import DataConnectionError, DataConnectionErrorTypedDict
    from codat_platform.models.shared.dataconnectionstatus import DataConnectionStatus
    from codat_platform.models.shared.datastatus import DataStatus, DataStatusTypedDict
    from codat_platform.models.shared.datastatuses import DataStatuses, DataStatusesTypedDict
    from codat_platform.models.shared.datatype import DataType
    from codat_platform.models.shared.datatypefeature import DataTypeFeature, DataTypeFeatureTypedDict
    from codat_platform.models.shared.datatypereadsummary import DataTypeReadSummary, DataTypeReadSummaryTypedDict
    from codat_platform.models.shared.datatypewritewebhook import DataTypeWriteWebhook, DataTypeWriteWebhookTypedDict
    from codat_platform.models.shared.datatypewritewebhookpayload import DataTypeWriteWebhookPayload, DataTypeWriteWebhookPayloadTypedDict
    from codat_platform.models.shared.datatypewritewebhookrecord import DataTypeWriteWebhookRecord, DataTypeWriteWebhookRecordTypedDict
    from codat_platform.models.data_types import DataTypes
    from codat_platform.models.dataset_status import DatasetStatus
    from codat_platform.models.shared.errormessage import ErrorMessage, ErrorMessageTypedDict
    from codat_platform.models.error_status import ErrorStatus
    from codat_platform.models.shared.errorvalidation import ErrorValidation, ErrorValidationTypedDict
    from codat_platform.models.shared.errorvalidationitem import ErrorValidationItem, ErrorValidationItemTypedDict
    from codat_platform.models.shared.featurestate import FeatureState
    from codat_platform.models.shared.featuretype import FeatureType
    from codat_platform.models.shared.halref import HalRef, HalRefTypedDict
    from codat_platform.models.shared.imagereference import ImageReference, ImageReferenceTypedDict
    from codat_platform.models.shared.integration import Integration, IntegrationTypedDict
    from codat_platform.models.shared.integrations import Integrations, IntegrationsTypedDict
    from codat_platform.models.shared.issue import Issue, IssueTypedDict
    from codat_platform.models.issue_links import IssueLinks, IssueLinksTypedDict
    from codat_platform.models.shared.links import Links, LinksTypedDict
    from codat_platform.models.modified_date import ModifiedDate, ModifiedDateTypedDict
    from codat_platform.models.paging_info import PagingInfo, PagingInfoTypedDict
    from codat_platform.models.shared.profile import Profile, ProfileTypedDict
    from codat_platform.models.shared.pulloperation import PullOperation, PullOperationTypedDict
    from codat_platform.models.shared.pulloperations import PullOperations, PullOperationsTypedDict
    from codat_platform.models.shared.pushchangetype import PushChangeType
    from codat_platform.models.shared.pushfieldvalidation import PushFieldValidation, PushFieldValidationTypedDict
    from codat_platform.models.shared.pushoperation import PushOperation, PushOperationTypedDict
    from codat_platform.models.shared.pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
    from codat_platform.models.shared.pushoperationref import PushOperationRef, PushOperationRefTypedDict
    from codat_platform.models.shared.pushoperationstatus import PushOperationStatus
    from codat_platform.models.shared.pushoperations import PushOperations, PushOperationsTypedDict
    from codat_platform.models.shared.pushoption import PushOption, PushOptionTypedDict
    from codat_platform.models.shared.pushoptionchoice import PushOptionChoice, PushOptionChoiceTypedDict
    from codat_platform.models.shared.pushoptionproperty import PushOptionProperty, PushOptionPropertyTypedDict
    from codat_platform.models.shared.pushoptiontype import PushOptionType
    from codat_platform.models.shared.pushvalidationinfo import PushValidationInfo, PushValidationInfoTypedDict
    from codat_platform.models.shared.readcompletedwebhook import ReadCompletedWebhook, ReadCompletedWebhookTypedDict
    from codat_platform.models.shared.readcompletedwebhookpayload import ReadCompletedWebhookPayload, ReadCompletedWebhookPayloadTypedDict
    from codat_platform.models.refresh_product_data_request import RefreshProductDataRequest, RefreshProductDataRequestTypedDict
    from codat_platform.models.set_company_sync_settings_request import SetCompanySyncSettingsRequest, SetCompanySyncSettingsRequestTypedDict
    from codat_platform.models.shared.sourcetype import SourceType
    from codat_platform.models.shared.status import Status
    from codat_platform.models.shared.supplementaldataconfiguration import SupplementalDataConfiguration, SupplementalDataConfigurationTypedDict
    from codat_platform.models.supplemental_data_source_configuration import SupplementalDataSourceConfiguration, SupplementalDataSourceConfigurationTypedDict
    from codat_platform.models.shared.supportedfeature import SupportedFeature, SupportedFeatureTypedDict
    from codat_platform.models.shared.syncsetting import SyncSetting, SyncSettingTypedDict
    from codat_platform.models.shared.syncsettings import SyncSettings, SyncSettingsTypedDict
    from codat_platform.models.shared.updateconnectionstatus import UpdateConnectionStatus, UpdateConnectionStatusTypedDict
    from codat_platform.models.update_profile_sync_settings_request import UpdateProfileSyncSettingsRequest, UpdateProfileSyncSettingsRequestTypedDict
    from codat_platform.models.shared.validation import Validation, ValidationTypedDict
    from codat_platform.models.shared.validationitem import ValidationItem, ValidationItemTypedDict
    from codat_platform.models.validation_item1 import ValidationItem1, ValidationItem1TypedDict
    from codat_platform.models.shared.validationresult import ValidationResult, ValidationResultTypedDict
    from codat_platform.models.shared.webhookconsumer import WebhookConsumer, WebhookConsumerTypedDict
    from codat_platform.models.shared.webhookconsumerprototype import WebhookConsumerPrototype, WebhookConsumerPrototypeTypedDict
    from codat_platform.models.shared.webhookconsumers import WebhookConsumers, WebhookConsumersTypedDict
    from codat_platform.models.webhook_zapier_key import WebhookZapierKey, WebhookZapierKeyTypedDict
    from codat_platform.models.shared.writestatus import WriteStatus
    from codat_platform.models.shared.writetype import WriteType
    from codat_platform.models.shared.schema_datatype import SchemaDataType
    from codat_platform.models.shared.brandingbutton import BrandingButtonTypedDict as BrandingButtonTypedDict
    from codat_platform.models.shared.brandingimage import BrandingImageTypedDict as BrandingImageTypedDict
    from codat_platform.models.shared.brandinglogo import BrandingLogoTypedDict as BrandingLogoTypedDict
    from codat_platform.models.shared.branding import BrandingTypedDict as BrandingTypedDict
    from codat_platform.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayloadTypedDict as ClientRateLimitWebhookPayloadTypedDict
    from codat_platform.models.shared.clientratelimitwebhook import ClientRateLimitWebhookTypedDict as ClientRateLimitWebhookTypedDict
    from codat_platform.models.shared.companies import CompaniesTypedDict as CompaniesTypedDict
    from codat_platform.models.shared.companyaccesstoken import CompanyAccessTokenTypedDict as CompanyAccessTokenTypedDict
    from codat_platform.models.shared.companydetails import CompanyDetailsTypedDict as CompanyDetailsTypedDict
    from codat_platform.models.company_reference_links import CompanyReferenceLinksTypedDict as CompanyReferenceLinksTypedDict
    from codat_platform.models.shared.companyreference import CompanyReferenceTypedDict as CompanyReferenceTypedDict
    from codat_platform.models.shared.companyrequestbody import CompanyRequestBodyTypedDict as CompanyRequestBodyTypedDict
    from codat_platform.models.shared.companysyncsettings import CompanySyncSettingsTypedDict as CompanySyncSettingsTypedDict
    from codat_platform.models.shared.company import CompanyTypedDict as CompanyTypedDict
    from codat_platform.models.shared.companyupdaterequest import CompanyUpdateRequestTypedDict as CompanyUpdateRequestTypedDict
    from codat_platform.models.shared.companywebhook import CompanyWebhookTypedDict as CompanyWebhookTypedDict
    from codat_platform.models.shared.connectionmanagementaccesstoken import ConnectionManagementAccessTokenTypedDict as ConnectionManagementAccessTokenTypedDict
    from codat_platform.models.shared.connectionmanagementallowedorigins import ConnectionManagementAllowedOriginsTypedDict as ConnectionManagementAllowedOriginsTypedDict
    from codat_platform.models.shared.connection import ConnectionTypedDict as ConnectionTypedDict
    from codat_platform.models.shared.connectionwebhookpayload import ConnectionWebhookPayloadTypedDict as ConnectionWebhookPayloadTypedDict
    from codat_platform.models.shared.connectionwebhook import ConnectionWebhookTypedDict as ConnectionWebhookTypedDict
    from codat_platform.models.shared.connections import ConnectionsTypedDict as ConnectionsTypedDict
    from codat_platform.models.shared.customdatatypeconfiguration import CustomDataTypeConfigurationTypedDict as CustomDataTypeConfigurationTypedDict
    from codat_platform.models.shared.customdatatyperecord import CustomDataTypeRecordTypedDict as CustomDataTypeRecordTypedDict
    from codat_platform.models.shared.customdatatyperecords import CustomDataTypeRecordsTypedDict as CustomDataTypeRecordsTypedDict
    from codat_platform.models.shared.dataconnectionerror import DataConnectionErrorTypedDict as DataConnectionErrorTypedDict
    from codat_platform.models.shared.dataconnectionstatus import DataConnectionStatus as DataConnectionStatus
    from codat_platform.models.shared.datastatus import DataStatusTypedDict as DataStatusTypedDict
    from codat_platform.models.shared.datastatuses import DataStatusesTypedDict as DataStatusesTypedDict
    from codat_platform.models.shared.datatypefeature import DataTypeFeatureTypedDict as DataTypeFeatureTypedDict
    from codat_platform.models.shared.datatypereadsummary import DataTypeReadSummaryTypedDict as DataTypeReadSummaryTypedDict
    from codat_platform.models.shared.datatypewritewebhookpayload import DataTypeWriteWebhookPayloadTypedDict as DataTypeWriteWebhookPayloadTypedDict
    from codat_platform.models.shared.datatypewritewebhookrecord import DataTypeWriteWebhookRecordTypedDict as DataTypeWriteWebhookRecordTypedDict
    from codat_platform.models.shared.datatypewritewebhook import DataTypeWriteWebhookTypedDict as DataTypeWriteWebhookTypedDict
    from codat_platform.models.data_types import DataTypes as DataTypes
    from codat_platform.models.dataset_status import DatasetStatus as DatasetStatus
    from codat_platform.models.shared.errormessage import ErrorMessageTypedDict as ErrorMessageTypedDict
    from codat_platform.models.error_status import ErrorStatus as ErrorStatus
    from codat_platform.models.shared.errorvalidationitem import ErrorValidationItemTypedDict as ErrorValidationItemTypedDict
    from codat_platform.models.shared.errorvalidation import ErrorValidationTypedDict as ErrorValidationTypedDict
    from codat_platform.models.shared.featurestate import FeatureState as FeatureState
    from codat_platform.models.shared.featuretype import FeatureType as FeatureType
    from codat_platform.models.shared.halref import HalRefTypedDict as HalRefTypedDict
    from codat_platform.models.shared.imagereference import ImageReferenceTypedDict as ImageReferenceTypedDict
    from codat_platform.models.shared.integration import IntegrationTypedDict as IntegrationTypedDict
    from codat_platform.models.shared.integrations import IntegrationsTypedDict as IntegrationsTypedDict
    from codat_platform.models.issue_links import IssueLinksTypedDict as IssueLinksTypedDict
    from codat_platform.models.shared.issue import IssueTypedDict as IssueTypedDict
    from codat_platform.models.shared.links import LinksTypedDict as LinksTypedDict
    from codat_platform.models.modified_date import ModifiedDateTypedDict as ModifiedDateTypedDict
    from codat_platform.models.shared.profile import ProfileTypedDict as ProfileTypedDict
    from codat_platform.models.shared.pulloperation import PullOperationTypedDict as PullOperationTypedDict
    from codat_platform.models.shared.pulloperations import PullOperationsTypedDict as PullOperationsTypedDict
    from codat_platform.models.shared.pushchangetype import PushChangeType as PushChangeType
    from codat_platform.models.shared.pushfieldvalidation import PushFieldValidationTypedDict as PushFieldValidationTypedDict
    from codat_platform.models.shared.pushoperationchange import PushOperationChangeTypedDict as PushOperationChangeTypedDict
    from codat_platform.models.shared.pushoperationref import PushOperationRefTypedDict as PushOperationRefTypedDict
    from codat_platform.models.shared.pushoperationstatus import PushOperationStatus as PushOperationStatus
    from codat_platform.models.shared.pushoperation import PushOperationTypedDict as PushOperationTypedDict
    from codat_platform.models.shared.pushoperations import PushOperationsTypedDict as PushOperationsTypedDict
    from codat_platform.models.shared.pushoptionchoice import PushOptionChoiceTypedDict as PushOptionChoiceTypedDict
    from codat_platform.models.shared.pushoptionproperty import PushOptionPropertyTypedDict as PushOptionPropertyTypedDict
    from codat_platform.models.shared.pushoptiontype import PushOptionType as PushOptionType
    from codat_platform.models.shared.pushoption import PushOptionTypedDict as PushOptionTypedDict
    from codat_platform.models.shared.pushvalidationinfo import PushValidationInfoTypedDict as PushValidationInfoTypedDict
    from codat_platform.models.shared.readcompletedwebhookpayload import ReadCompletedWebhookPayloadTypedDict as ReadCompletedWebhookPayloadTypedDict
    from codat_platform.models.shared.readcompletedwebhook import ReadCompletedWebhookTypedDict as ReadCompletedWebhookTypedDict
    from codat_platform.models.shared.schema_datatype import SchemaDataType as SchemaDataType
    from codat_platform.models.shared.security import Security as Security
    from codat_platform.models.shared.security import SecurityTypedDict as SecurityTypedDict
    from codat_platform.models.shared.sourcetype import SourceType as SourceType
    from codat_platform.models.shared.status import Status as Status
    from codat_platform.models.shared.supplementaldataconfiguration import SupplementalDataConfigurationTypedDict as SupplementalDataConfigurationTypedDict
    from codat_platform.models.supplemental_data_source_configuration import SupplementalDataSourceConfigurationTypedDict as SupplementalDataSourceConfigurationTypedDict
    from codat_platform.models.shared.supportedfeature import SupportedFeatureTypedDict as SupportedFeatureTypedDict
    from codat_platform.models.shared.syncsetting import SyncSettingTypedDict as SyncSettingTypedDict
    from codat_platform.models.shared.syncsettings import SyncSettingsTypedDict as SyncSettingsTypedDict
    from codat_platform.models.shared.updateconnectionstatus import UpdateConnectionStatusTypedDict as UpdateConnectionStatusTypedDict
    from codat_platform.models.validation_item1 import ValidationItem1TypedDict as ValidationItem1TypedDict
    from codat_platform.models.shared.validationitem import ValidationItemTypedDict as ValidationItemTypedDict
    from codat_platform.models.shared.validationresult import ValidationResultTypedDict as ValidationResultTypedDict
    from codat_platform.models.shared.validation import ValidationTypedDict as ValidationTypedDict
    from codat_platform.models.shared.webhookconsumerprototype import WebhookConsumerPrototypeTypedDict as WebhookConsumerPrototypeTypedDict
    from codat_platform.models.shared.webhookconsumer import WebhookConsumerTypedDict as WebhookConsumerTypedDict
    from codat_platform.models.shared.webhookconsumers import WebhookConsumersTypedDict as WebhookConsumersTypedDict
    from codat_platform.models.shared.writestatus import WriteStatus as WriteStatus
    from codat_platform.models.shared.writetype import WriteType as WriteType
    from codat_platform.models.content import Content, ContentTypedDict
    from codat_platform.models.validationitem1 import ValidationItem1, ValidationItem1TypedDict

_dynamic_imports: dict[str, tuple[str, str]] = {
    'APIKeyDetails': ('codat_platform.models.shared.apikeydetails', 'APIKeyDetails'),
    'ApiKeyDetails': ('codat_platform.models.shared.apikeydetails', 'APIKeyDetails'),
    'APIKeyDetailsTypedDict': ('codat_platform.models.shared.apikeydetails', 'APIKeyDetailsTypedDict'),
    'ApiKeyDetailsTypedDict': ('codat_platform.models.shared.apikeydetails', 'APIKeyDetailsTypedDict'),
    'APIKeys': ('codat_platform.models.shared.apikeys', 'APIKeys'),
    'ApiKeys': ('codat_platform.models.shared.apikeys', 'APIKeys'),
    'APIKeysTypedDict': ('codat_platform.models.shared.apikeys', 'APIKeysTypedDict'),
    'ApiKeysTypedDict': ('codat_platform.models.shared.apikeys', 'APIKeysTypedDict'),
    'AccessToken': ('codat_platform.models.access_token', 'AccessToken'),
    'AccessTokenTypedDict': ('codat_platform.models.access_token', 'AccessTokenTypedDict'),
    'Branding': ('codat_platform.models.shared.branding', 'Branding'),
    'BrandingButton': ('codat_platform.models.shared.brandingbutton', 'BrandingButton'),
    'BrandingButtonTypedDict': ('codat_platform.models.shared.brandingbutton', 'BrandingButtonTypedDict'),
    'BrandingImage': ('codat_platform.models.shared.brandingimage', 'BrandingImage'),
    'BrandingImageTypedDict': ('codat_platform.models.shared.brandingimage', 'BrandingImageTypedDict'),
    'BrandingLogo': ('codat_platform.models.shared.brandinglogo', 'BrandingLogo'),
    'BrandingLogoTypedDict': ('codat_platform.models.shared.brandinglogo', 'BrandingLogoTypedDict'),
    'BrandingTypedDict': ('codat_platform.models.shared.branding', 'BrandingTypedDict'),
    'ClientRateLimitWebhook': ('codat_platform.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhook'),
    'ClientRateLimitWebhookPayload': ('codat_platform.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayload'),
    'ClientRateLimitWebhookPayloadTypedDict': ('codat_platform.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayloadTypedDict'),
    'ClientRateLimitWebhookTypedDict': ('codat_platform.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhookTypedDict'),
    'Companies': ('codat_platform.models.shared.companies', 'Companies'),
    'CompaniesTypedDict': ('codat_platform.models.shared.companies', 'CompaniesTypedDict'),
    'Company': ('codat_platform.models.shared.company', 'Company'),
    'CompanyAccessToken': ('codat_platform.models.shared.companyaccesstoken', 'CompanyAccessToken'),
    'CompanyAccessTokenTypedDict': ('codat_platform.models.shared.companyaccesstoken', 'CompanyAccessTokenTypedDict'),
    'CompanyDetails': ('codat_platform.models.shared.companydetails', 'CompanyDetails'),
    'CompanyDetailsTypedDict': ('codat_platform.models.shared.companydetails', 'CompanyDetailsTypedDict'),
    'CompanyProductWebhook': ('codat_platform.models.company_product_webhook', 'CompanyProductWebhook'),
    'CompanyProductWebhookPayload': ('codat_platform.models.company_product_webhook_payload', 'CompanyProductWebhookPayload'),
    'CompanyProductWebhookPayloadTypedDict': ('codat_platform.models.company_product_webhook_payload', 'CompanyProductWebhookPayloadTypedDict'),
    'CompanyProductWebhookTypedDict': ('codat_platform.models.company_product_webhook', 'CompanyProductWebhookTypedDict'),
    'CompanyReference': ('codat_platform.models.shared.companyreference', 'CompanyReference'),
    'CompanyReferenceLinks': ('codat_platform.models.company_reference_links', 'CompanyReferenceLinks'),
    'CompanyReferenceLinksTypedDict': ('codat_platform.models.company_reference_links', 'CompanyReferenceLinksTypedDict'),
    'CompanyReferenceTypedDict': ('codat_platform.models.shared.companyreference', 'CompanyReferenceTypedDict'),
    'CompanyRequestBody': ('codat_platform.models.shared.companyrequestbody', 'CompanyRequestBody'),
    'CompanyRequestBodyTypedDict': ('codat_platform.models.shared.companyrequestbody', 'CompanyRequestBodyTypedDict'),
    'CompanySyncSettings': ('codat_platform.models.shared.companysyncsettings', 'CompanySyncSettings'),
    'CompanySyncSettingsTypedDict': ('codat_platform.models.shared.companysyncsettings', 'CompanySyncSettingsTypedDict'),
    'CompanyTypedDict': ('codat_platform.models.shared.company', 'CompanyTypedDict'),
    'CompanyUpdateRequest': ('codat_platform.models.shared.companyupdaterequest', 'CompanyUpdateRequest'),
    'CompanyUpdateRequestTypedDict': ('codat_platform.models.shared.companyupdaterequest', 'CompanyUpdateRequestTypedDict'),
    'CompanyWebhook': ('codat_platform.models.shared.companywebhook', 'CompanyWebhook'),
    'CompanyWebhookTypedDict': ('codat_platform.models.shared.companywebhook', 'CompanyWebhookTypedDict'),
    'Connection': ('codat_platform.models.shared.connection', 'Connection'),
    'ConnectionManagementAccessToken': ('codat_platform.models.shared.connectionmanagementaccesstoken', 'ConnectionManagementAccessToken'),
    'ConnectionManagementAccessTokenTypedDict': ('codat_platform.models.shared.connectionmanagementaccesstoken', 'ConnectionManagementAccessTokenTypedDict'),
    'ConnectionManagementAllowedOrigins': ('codat_platform.models.shared.connectionmanagementallowedorigins', 'ConnectionManagementAllowedOrigins'),
    'ConnectionManagementAllowedOriginsTypedDict': ('codat_platform.models.shared.connectionmanagementallowedorigins', 'ConnectionManagementAllowedOriginsTypedDict'),
    'ConnectionTypedDict': ('codat_platform.models.shared.connection', 'ConnectionTypedDict'),
    'ConnectionWebhook': ('codat_platform.models.shared.connectionwebhook', 'ConnectionWebhook'),
    'ConnectionWebhookPayload': ('codat_platform.models.shared.connectionwebhookpayload', 'ConnectionWebhookPayload'),
    'ConnectionWebhookPayloadTypedDict': ('codat_platform.models.shared.connectionwebhookpayload', 'ConnectionWebhookPayloadTypedDict'),
    'ConnectionWebhookTypedDict': ('codat_platform.models.shared.connectionwebhook', 'ConnectionWebhookTypedDict'),
    'Connections': ('codat_platform.models.shared.connections', 'Connections'),
    'ConnectionsTypedDict': ('codat_platform.models.shared.connections', 'ConnectionsTypedDict'),
    'Content': ('codat_platform.models.content', 'Content'),
    'ContentTypedDict': ('codat_platform.models.content', 'ContentTypedDict'),
    'CreateAPIKey': ('codat_platform.models.shared.createapikey', 'CreateAPIKey'),
    'CreateApiKey': ('codat_platform.models.shared.createapikey', 'CreateAPIKey'),
    'CreateAPIKeyTypedDict': ('codat_platform.models.shared.createapikey', 'CreateAPIKeyTypedDict'),
    'CreateApiKeyTypedDict': ('codat_platform.models.shared.createapikey', 'CreateAPIKeyTypedDict'),
    'CreateConnectionRequest': ('codat_platform.models.create_connection_request', 'CreateConnectionRequest'),
    'CreateConnectionRequestTypedDict': ('codat_platform.models.create_connection_request', 'CreateConnectionRequestTypedDict'),
    'CurrentStatus': ('codat_platform.models.current_status', 'CurrentStatus'),
    'CustomDataTypeConfiguration': ('codat_platform.models.shared.customdatatypeconfiguration', 'CustomDataTypeConfiguration'),
    'CustomDataTypeConfigurationTypedDict': ('codat_platform.models.shared.customdatatypeconfiguration', 'CustomDataTypeConfigurationTypedDict'),
    'CustomDataTypeRecord': ('codat_platform.models.shared.customdatatyperecord', 'CustomDataTypeRecord'),
    'CustomDataTypeRecordTypedDict': ('codat_platform.models.shared.customdatatyperecord', 'CustomDataTypeRecordTypedDict'),
    'CustomDataTypeRecords': ('codat_platform.models.shared.customdatatyperecords', 'CustomDataTypeRecords'),
    'CustomDataTypeRecordsTypedDict': ('codat_platform.models.shared.customdatatyperecords', 'CustomDataTypeRecordsTypedDict'),
    'DataConnectionError': ('codat_platform.models.shared.dataconnectionerror', 'DataConnectionError'),
    'DataConnectionErrorTypedDict': ('codat_platform.models.shared.dataconnectionerror', 'DataConnectionErrorTypedDict'),
    'DataConnectionStatus': ('codat_platform.models.shared.dataconnectionstatus', 'DataConnectionStatus'),
    'DataStatus': ('codat_platform.models.shared.datastatus', 'DataStatus'),
    'DataStatusTypedDict': ('codat_platform.models.shared.datastatus', 'DataStatusTypedDict'),
    'DataStatuses': ('codat_platform.models.shared.datastatuses', 'DataStatuses'),
    'DataStatusesTypedDict': ('codat_platform.models.shared.datastatuses', 'DataStatusesTypedDict'),
    'DataType': ('codat_platform.models.shared.datatype', 'DataType'),
    'DataTypeFeature': ('codat_platform.models.shared.datatypefeature', 'DataTypeFeature'),
    'DataTypeFeatureTypedDict': ('codat_platform.models.shared.datatypefeature', 'DataTypeFeatureTypedDict'),
    'DataTypeReadSummary': ('codat_platform.models.shared.datatypereadsummary', 'DataTypeReadSummary'),
    'DataTypeReadSummaryTypedDict': ('codat_platform.models.shared.datatypereadsummary', 'DataTypeReadSummaryTypedDict'),
    'DataTypeWriteWebhook': ('codat_platform.models.shared.datatypewritewebhook', 'DataTypeWriteWebhook'),
    'DataTypeWriteWebhookPayload': ('codat_platform.models.shared.datatypewritewebhookpayload', 'DataTypeWriteWebhookPayload'),
    'DataTypeWriteWebhookPayloadTypedDict': ('codat_platform.models.shared.datatypewritewebhookpayload', 'DataTypeWriteWebhookPayloadTypedDict'),
    'DataTypeWriteWebhookRecord': ('codat_platform.models.shared.datatypewritewebhookrecord', 'DataTypeWriteWebhookRecord'),
    'DataTypeWriteWebhookRecordTypedDict': ('codat_platform.models.shared.datatypewritewebhookrecord', 'DataTypeWriteWebhookRecordTypedDict'),
    'DataTypeWriteWebhookTypedDict': ('codat_platform.models.shared.datatypewritewebhook', 'DataTypeWriteWebhookTypedDict'),
    'DataTypes': ('codat_platform.models.data_types', 'DataTypes'),
    'DatasetStatus': ('codat_platform.models.dataset_status', 'DatasetStatus'),
    'ErrorMessage': ('codat_platform.models.shared.errormessage', 'ErrorMessage'),
    'ErrorMessageTypedDict': ('codat_platform.models.shared.errormessage', 'ErrorMessageTypedDict'),
    'ErrorStatus': ('codat_platform.models.error_status', 'ErrorStatus'),
    'ErrorValidation': ('codat_platform.models.shared.errorvalidation', 'ErrorValidation'),
    'ErrorValidationItem': ('codat_platform.models.shared.errorvalidationitem', 'ErrorValidationItem'),
    'ErrorValidationItemTypedDict': ('codat_platform.models.shared.errorvalidationitem', 'ErrorValidationItemTypedDict'),
    'ErrorValidationTypedDict': ('codat_platform.models.shared.errorvalidation', 'ErrorValidationTypedDict'),
    'FeatureState': ('codat_platform.models.shared.featurestate', 'FeatureState'),
    'FeatureType': ('codat_platform.models.shared.featuretype', 'FeatureType'),
    'HalRef': ('codat_platform.models.shared.halref', 'HalRef'),
    'HalRefTypedDict': ('codat_platform.models.shared.halref', 'HalRefTypedDict'),
    'ImageReference': ('codat_platform.models.shared.imagereference', 'ImageReference'),
    'ImageReferenceTypedDict': ('codat_platform.models.shared.imagereference', 'ImageReferenceTypedDict'),
    'Integration': ('codat_platform.models.shared.integration', 'Integration'),
    'IntegrationTypedDict': ('codat_platform.models.shared.integration', 'IntegrationTypedDict'),
    'Integrations': ('codat_platform.models.shared.integrations', 'Integrations'),
    'IntegrationsTypedDict': ('codat_platform.models.shared.integrations', 'IntegrationsTypedDict'),
    'Issue': ('codat_platform.models.shared.issue', 'Issue'),
    'IssueLinks': ('codat_platform.models.issue_links', 'IssueLinks'),
    'IssueLinksTypedDict': ('codat_platform.models.issue_links', 'IssueLinksTypedDict'),
    'IssueTypedDict': ('codat_platform.models.shared.issue', 'IssueTypedDict'),
    'Links': ('codat_platform.models.shared.links', 'Links'),
    'LinksTypedDict': ('codat_platform.models.shared.links', 'LinksTypedDict'),
    'ModifiedDate': ('codat_platform.models.modified_date', 'ModifiedDate'),
    'ModifiedDateTypedDict': ('codat_platform.models.modified_date', 'ModifiedDateTypedDict'),
    'PagingInfo': ('codat_platform.models.paging_info', 'PagingInfo'),
    'PagingInfoTypedDict': ('codat_platform.models.paging_info', 'PagingInfoTypedDict'),
    'Profile': ('codat_platform.models.shared.profile', 'Profile'),
    'ProfileTypedDict': ('codat_platform.models.shared.profile', 'ProfileTypedDict'),
    'PullOperation': ('codat_platform.models.shared.pulloperation', 'PullOperation'),
    'PullOperationTypedDict': ('codat_platform.models.shared.pulloperation', 'PullOperationTypedDict'),
    'PullOperations': ('codat_platform.models.shared.pulloperations', 'PullOperations'),
    'PullOperationsTypedDict': ('codat_platform.models.shared.pulloperations', 'PullOperationsTypedDict'),
    'PushChangeType': ('codat_platform.models.shared.pushchangetype', 'PushChangeType'),
    'PushFieldValidation': ('codat_platform.models.shared.pushfieldvalidation', 'PushFieldValidation'),
    'PushFieldValidationTypedDict': ('codat_platform.models.shared.pushfieldvalidation', 'PushFieldValidationTypedDict'),
    'PushOperation': ('codat_platform.models.shared.pushoperation', 'PushOperation'),
    'PushOperationChange': ('codat_platform.models.shared.pushoperationchange', 'PushOperationChange'),
    'PushOperationChangeTypedDict': ('codat_platform.models.shared.pushoperationchange', 'PushOperationChangeTypedDict'),
    'PushOperationRef': ('codat_platform.models.shared.pushoperationref', 'PushOperationRef'),
    'PushOperationRefTypedDict': ('codat_platform.models.shared.pushoperationref', 'PushOperationRefTypedDict'),
    'PushOperationStatus': ('codat_platform.models.shared.pushoperationstatus', 'PushOperationStatus'),
    'PushOperationTypedDict': ('codat_platform.models.shared.pushoperation', 'PushOperationTypedDict'),
    'PushOperations': ('codat_platform.models.shared.pushoperations', 'PushOperations'),
    'PushOperationsTypedDict': ('codat_platform.models.shared.pushoperations', 'PushOperationsTypedDict'),
    'PushOption': ('codat_platform.models.shared.pushoption', 'PushOption'),
    'PushOptionChoice': ('codat_platform.models.shared.pushoptionchoice', 'PushOptionChoice'),
    'PushOptionChoiceTypedDict': ('codat_platform.models.shared.pushoptionchoice', 'PushOptionChoiceTypedDict'),
    'PushOptionProperty': ('codat_platform.models.shared.pushoptionproperty', 'PushOptionProperty'),
    'PushOptionPropertyTypedDict': ('codat_platform.models.shared.pushoptionproperty', 'PushOptionPropertyTypedDict'),
    'PushOptionType': ('codat_platform.models.shared.pushoptiontype', 'PushOptionType'),
    'PushOptionTypedDict': ('codat_platform.models.shared.pushoption', 'PushOptionTypedDict'),
    'PushValidationInfo': ('codat_platform.models.shared.pushvalidationinfo', 'PushValidationInfo'),
    'PushValidationInfoTypedDict': ('codat_platform.models.shared.pushvalidationinfo', 'PushValidationInfoTypedDict'),
    'ReadCompletedWebhook': ('codat_platform.models.shared.readcompletedwebhook', 'ReadCompletedWebhook'),
    'ReadCompletedWebhookPayload': ('codat_platform.models.shared.readcompletedwebhookpayload', 'ReadCompletedWebhookPayload'),
    'ReadCompletedWebhookPayloadTypedDict': ('codat_platform.models.shared.readcompletedwebhookpayload', 'ReadCompletedWebhookPayloadTypedDict'),
    'ReadCompletedWebhookTypedDict': ('codat_platform.models.shared.readcompletedwebhook', 'ReadCompletedWebhookTypedDict'),
    'RefreshProductDataRequest': ('codat_platform.models.refresh_product_data_request', 'RefreshProductDataRequest'),
    'RefreshProductDataRequestTypedDict': ('codat_platform.models.refresh_product_data_request', 'RefreshProductDataRequestTypedDict'),
    'SchemaDataType': ('codat_platform.models.shared.schema_datatype', 'SchemaDataType'),
    'Security': ('codat_platform.models.shared.security', 'Security'),
    'SecurityTypedDict': ('codat_platform.models.shared.security', 'SecurityTypedDict'),
    'SetCompanySyncSettingsRequest': ('codat_platform.models.set_company_sync_settings_request', 'SetCompanySyncSettingsRequest'),
    'SetCompanySyncSettingsRequestTypedDict': ('codat_platform.models.set_company_sync_settings_request', 'SetCompanySyncSettingsRequestTypedDict'),
    'SourceType': ('codat_platform.models.shared.sourcetype', 'SourceType'),
    'Status': ('codat_platform.models.shared.status', 'Status'),
    'SupplementalDataConfiguration': ('codat_platform.models.shared.supplementaldataconfiguration', 'SupplementalDataConfiguration'),
    'SupplementalDataConfigurationTypedDict': ('codat_platform.models.shared.supplementaldataconfiguration', 'SupplementalDataConfigurationTypedDict'),
    'SupplementalDataSourceConfiguration': ('codat_platform.models.supplemental_data_source_configuration', 'SupplementalDataSourceConfiguration'),
    'SupplementalDataSourceConfigurationTypedDict': ('codat_platform.models.supplemental_data_source_configuration', 'SupplementalDataSourceConfigurationTypedDict'),
    'SupportedFeature': ('codat_platform.models.shared.supportedfeature', 'SupportedFeature'),
    'SupportedFeatureTypedDict': ('codat_platform.models.shared.supportedfeature', 'SupportedFeatureTypedDict'),
    'SyncSetting': ('codat_platform.models.shared.syncsetting', 'SyncSetting'),
    'SyncSettingTypedDict': ('codat_platform.models.shared.syncsetting', 'SyncSettingTypedDict'),
    'SyncSettings': ('codat_platform.models.shared.syncsettings', 'SyncSettings'),
    'SyncSettingsTypedDict': ('codat_platform.models.shared.syncsettings', 'SyncSettingsTypedDict'),
    'UpdateConnectionStatus': ('codat_platform.models.shared.updateconnectionstatus', 'UpdateConnectionStatus'),
    'UpdateConnectionStatusTypedDict': ('codat_platform.models.shared.updateconnectionstatus', 'UpdateConnectionStatusTypedDict'),
    'UpdateProfileSyncSettingsRequest': ('codat_platform.models.update_profile_sync_settings_request', 'UpdateProfileSyncSettingsRequest'),
    'UpdateProfileSyncSettingsRequestTypedDict': ('codat_platform.models.update_profile_sync_settings_request', 'UpdateProfileSyncSettingsRequestTypedDict'),
    'Validation': ('codat_platform.models.shared.validation', 'Validation'),
    'ValidationItem': ('codat_platform.models.shared.validationitem', 'ValidationItem'),
    'ValidationItem1': ('codat_platform.models.validationitem1', 'ValidationItem1'),
    'ValidationItem1TypedDict': ('codat_platform.models.validationitem1', 'ValidationItem1TypedDict'),
    'ValidationItemTypedDict': ('codat_platform.models.shared.validationitem', 'ValidationItemTypedDict'),
    'ValidationResult': ('codat_platform.models.shared.validationresult', 'ValidationResult'),
    'ValidationResultTypedDict': ('codat_platform.models.shared.validationresult', 'ValidationResultTypedDict'),
    'ValidationTypedDict': ('codat_platform.models.shared.validation', 'ValidationTypedDict'),
    'WebhookConsumer': ('codat_platform.models.shared.webhookconsumer', 'WebhookConsumer'),
    'WebhookConsumerPrototype': ('codat_platform.models.shared.webhookconsumerprototype', 'WebhookConsumerPrototype'),
    'WebhookConsumerPrototypeTypedDict': ('codat_platform.models.shared.webhookconsumerprototype', 'WebhookConsumerPrototypeTypedDict'),
    'WebhookConsumerTypedDict': ('codat_platform.models.shared.webhookconsumer', 'WebhookConsumerTypedDict'),
    'WebhookConsumers': ('codat_platform.models.shared.webhookconsumers', 'WebhookConsumers'),
    'WebhookConsumersTypedDict': ('codat_platform.models.shared.webhookconsumers', 'WebhookConsumersTypedDict'),
    'WebhookZapierKey': ('codat_platform.models.webhook_zapier_key', 'WebhookZapierKey'),
    'WebhookZapierKeyTypedDict': ('codat_platform.models.webhook_zapier_key', 'WebhookZapierKeyTypedDict'),
    'WriteStatus': ('codat_platform.models.shared.writestatus', 'WriteStatus'),
    'WriteType': ('codat_platform.models.shared.writetype', 'WriteType'),
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
