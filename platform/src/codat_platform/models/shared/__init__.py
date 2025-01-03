"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .apikeydetails import APIKeyDetails, APIKeyDetailsTypedDict
from .apikeys import APIKeys, APIKeysTypedDict
from .branding import Branding, BrandingTypedDict
from .brandingbutton import BrandingButton, BrandingButtonTypedDict
from .brandingimage import BrandingImage, BrandingImageTypedDict
from .brandinglogo import BrandingLogo, BrandingLogoTypedDict
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
from .companies import Companies, CompaniesTypedDict
from .company import Company, CompanyTypedDict
from .companyaccesstoken import CompanyAccessToken, CompanyAccessTokenTypedDict
from .companydetails import CompanyDetails, CompanyDetailsTypedDict
from .companyreference import (
    CompanyReference,
    CompanyReferenceLinks,
    CompanyReferenceLinksTypedDict,
    CompanyReferenceTypedDict,
)
from .companyrequestbody import CompanyRequestBody, CompanyRequestBodyTypedDict
from .companywebhook import CompanyWebhook, CompanyWebhookTypedDict
from .connection import Connection, ConnectionTypedDict
from .connectionmanagementaccesstoken import (
    ConnectionManagementAccessToken,
    ConnectionManagementAccessTokenTypedDict,
)
from .connectionmanagementallowedorigins import (
    ConnectionManagementAllowedOrigins,
    ConnectionManagementAllowedOriginsTypedDict,
)
from .connections import Connections, ConnectionsTypedDict
from .connectionstatuschangedwebhook import (
    ConnectionStatusChangedWebhook,
    ConnectionStatusChangedWebhookTypedDict,
)
from .connectionstatuschangedwebhookdata import (
    ConnectionStatusChangedWebhookData,
    ConnectionStatusChangedWebhookDataTypedDict,
)
from .connectionwebhook import ConnectionWebhook, ConnectionWebhookTypedDict
from .connectionwebhookpayload import (
    ConnectionWebhookPayload,
    ConnectionWebhookPayloadTypedDict,
)
from .createapikey import CreateAPIKey, CreateAPIKeyTypedDict
from .createrule import CreateRule, CreateRuleTypedDict
from .customdatatypeconfiguration import (
    CustomDataTypeConfiguration,
    CustomDataTypeConfigurationTypedDict,
)
from .customdatatyperecord import (
    Content,
    ContentTypedDict,
    CustomDataTypeRecord,
    CustomDataTypeRecordTypedDict,
    ModifiedDate,
    ModifiedDateTypedDict,
)
from .customdatatyperecords import CustomDataTypeRecords, CustomDataTypeRecordsTypedDict
from .dataconnectionerror import (
    DataConnectionError,
    DataConnectionErrorTypedDict,
    ErrorStatus,
)
from .dataconnectionstatus import DataConnectionStatus
from .datasetdatachangedwebhook import (
    DatasetDataChangedWebhook,
    DatasetDataChangedWebhookData,
    DatasetDataChangedWebhookDataTypedDict,
    DatasetDataChangedWebhookTypedDict,
)
from .datasetstatuschangederrorwebhook import (
    DatasetStatusChangedErrorWebhook,
    DatasetStatusChangedErrorWebhookTypedDict,
)
from .datasetstatuschangederrorwebhookdata import (
    DatasetStatusChangedErrorWebhookData,
    DatasetStatusChangedErrorWebhookDataTypedDict,
)
from .datastatus import DataStatus, DataStatusDataTypes, DataStatusTypedDict
from .datastatuses import DataStatuses, DataStatusesTypedDict
from .datasynccompletedwebhook import (
    DataSyncCompletedWebhook,
    DataSyncCompletedWebhookTypedDict,
)
from .datasynccompletedwebhookdata import (
    DataSyncCompletedWebhookData,
    DataSyncCompletedWebhookDataTypedDict,
)
from .datatype import DataType
from .datatypefeature import DataTypeFeature, DataTypeFeatureTypedDict
from .datatypewritewebhook import DataTypeWriteWebhook, DataTypeWriteWebhookTypedDict
from .datatypewritewebhookpayload import (
    DataTypeWriteWebhookPayload,
    DataTypeWriteWebhookPayloadTypedDict,
)
from .datatypewritewebhookrecord import (
    DataTypeWriteWebhookRecord,
    DataTypeWriteWebhookRecordTypedDict,
)
from .errormessage import ErrorMessage, ErrorMessageTypedDict
from .errorvalidation import ErrorValidation, ErrorValidationTypedDict
from .errorvalidationitem import ErrorValidationItem, ErrorValidationItemTypedDict
from .featurestate import FeatureState
from .featuretype import FeatureType
from .halref import HalRef, HalRefTypedDict
from .imagereference import ImageReference, ImageReferenceTypedDict
from .integration import Integration, IntegrationTypedDict
from .integrations import Integrations, IntegrationsTypedDict
from .links import Links, LinksTypedDict
from .newcompanysynchronizedwebhook import (
    NewCompanySynchronizedWebhook,
    NewCompanySynchronizedWebhookTypedDict,
)
from .profile import Profile, ProfileTypedDict
from .pulloperation import DatasetStatus, PullOperation, PullOperationTypedDict
from .pulloperations import PullOperations, PullOperationsTypedDict
from .pushchangetype import PushChangeType
from .pushfieldvalidation import PushFieldValidation, PushFieldValidationTypedDict
from .pushoperation import PushOperation, PushOperationTypedDict
from .pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
from .pushoperationref import PushOperationRef, PushOperationRefTypedDict
from .pushoperations import PushOperations, PushOperationsTypedDict
from .pushoperationstatus import PushOperationStatus
from .pushoperationstatuschangedwebhook import (
    PushOperationStatusChangedWebhook,
    PushOperationStatusChangedWebhookTypedDict,
)
from .pushoperationstatuschangedwebhookdata import (
    PushOperationStatusChangedWebhookData,
    PushOperationStatusChangedWebhookDataTypedDict,
)
from .pushoperationtimedoutwebhook import (
    PushOperationTimedOutWebhook,
    PushOperationTimedOutWebhookTypedDict,
)
from .pushoperationtimedoutwebhookdata import (
    PushOperationTimedOutWebhookData,
    PushOperationTimedOutWebhookDataTypedDict,
)
from .pushoption import PushOption, PushOptionTypedDict
from .pushoptionchoice import PushOptionChoice, PushOptionChoiceTypedDict
from .pushoptionproperty import PushOptionProperty, PushOptionPropertyTypedDict
from .pushoptiontype import PushOptionType
from .pushvalidationinfo import PushValidationInfo, PushValidationInfoTypedDict
from .readcompletedwebhook import ReadCompletedWebhook, ReadCompletedWebhookTypedDict
from .readcompletedwebhookpayload import (
    DataTypes,
    DataTypesTypedDict,
    ReadCompletedWebhookPayload,
    ReadCompletedWebhookPayloadTypedDict,
)
from .schema_datatype import SchemaDataType
from .security import Security, SecurityTypedDict
from .sourcetype import SourceType
from .status import Status
from .supplementaldataconfiguration import (
    SupplementalDataConfiguration,
    SupplementalDataConfigurationTypedDict,
    SupplementalDataSourceConfiguration,
    SupplementalDataSourceConfigurationTypedDict,
)
from .supportedfeature import SupportedFeature, SupportedFeatureTypedDict
from .syncsetting import SyncSetting, SyncSettingTypedDict
from .syncsettings import SyncSettings, SyncSettingsTypedDict
from .updateconnectionstatus import (
    UpdateConnectionStatus,
    UpdateConnectionStatusTypedDict,
)
from .validation import Validation, ValidationTypedDict
from .validationitem import ValidationItem, ValidationItemTypedDict
from .webhook import Webhook, WebhookTypedDict
from .webhookconsumer import WebhookConsumer, WebhookConsumerTypedDict
from .webhookconsumerprototype import (
    WebhookConsumerPrototype,
    WebhookConsumerPrototypeTypedDict,
)
from .webhookconsumers import WebhookConsumers, WebhookConsumersTypedDict
from .webhooknotifier import WebhookNotifier, WebhookNotifierTypedDict
from .webhooks import Webhooks, WebhooksTypedDict
from .writestatus import WriteStatus
from .writetype import WriteType

__all__ = [
    "APIKeyDetails",
    "APIKeyDetailsTypedDict",
    "APIKeys",
    "APIKeysTypedDict",
    "Branding",
    "BrandingButton",
    "BrandingButtonTypedDict",
    "BrandingImage",
    "BrandingImageTypedDict",
    "BrandingLogo",
    "BrandingLogoTypedDict",
    "BrandingTypedDict",
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
    "Companies",
    "CompaniesTypedDict",
    "Company",
    "CompanyAccessToken",
    "CompanyAccessTokenTypedDict",
    "CompanyDetails",
    "CompanyDetailsTypedDict",
    "CompanyReference",
    "CompanyReferenceLinks",
    "CompanyReferenceLinksTypedDict",
    "CompanyReferenceTypedDict",
    "CompanyRequestBody",
    "CompanyRequestBodyTypedDict",
    "CompanyTypedDict",
    "CompanyWebhook",
    "CompanyWebhookTypedDict",
    "Connection",
    "ConnectionManagementAccessToken",
    "ConnectionManagementAccessTokenTypedDict",
    "ConnectionManagementAllowedOrigins",
    "ConnectionManagementAllowedOriginsTypedDict",
    "ConnectionStatusChangedWebhook",
    "ConnectionStatusChangedWebhookData",
    "ConnectionStatusChangedWebhookDataTypedDict",
    "ConnectionStatusChangedWebhookTypedDict",
    "ConnectionTypedDict",
    "ConnectionWebhook",
    "ConnectionWebhookPayload",
    "ConnectionWebhookPayloadTypedDict",
    "ConnectionWebhookTypedDict",
    "Connections",
    "ConnectionsTypedDict",
    "Content",
    "ContentTypedDict",
    "CreateAPIKey",
    "CreateAPIKeyTypedDict",
    "CreateRule",
    "CreateRuleTypedDict",
    "CustomDataTypeConfiguration",
    "CustomDataTypeConfigurationTypedDict",
    "CustomDataTypeRecord",
    "CustomDataTypeRecordTypedDict",
    "CustomDataTypeRecords",
    "CustomDataTypeRecordsTypedDict",
    "DataConnectionError",
    "DataConnectionErrorTypedDict",
    "DataConnectionStatus",
    "DataStatus",
    "DataStatusDataTypes",
    "DataStatusTypedDict",
    "DataStatuses",
    "DataStatusesTypedDict",
    "DataSyncCompletedWebhook",
    "DataSyncCompletedWebhookData",
    "DataSyncCompletedWebhookDataTypedDict",
    "DataSyncCompletedWebhookTypedDict",
    "DataType",
    "DataTypeFeature",
    "DataTypeFeatureTypedDict",
    "DataTypeWriteWebhook",
    "DataTypeWriteWebhookPayload",
    "DataTypeWriteWebhookPayloadTypedDict",
    "DataTypeWriteWebhookRecord",
    "DataTypeWriteWebhookRecordTypedDict",
    "DataTypeWriteWebhookTypedDict",
    "DataTypes",
    "DataTypesTypedDict",
    "DatasetDataChangedWebhook",
    "DatasetDataChangedWebhookData",
    "DatasetDataChangedWebhookDataTypedDict",
    "DatasetDataChangedWebhookTypedDict",
    "DatasetStatus",
    "DatasetStatusChangedErrorWebhook",
    "DatasetStatusChangedErrorWebhookData",
    "DatasetStatusChangedErrorWebhookDataTypedDict",
    "DatasetStatusChangedErrorWebhookTypedDict",
    "ErrorMessage",
    "ErrorMessageTypedDict",
    "ErrorStatus",
    "ErrorValidation",
    "ErrorValidationItem",
    "ErrorValidationItemTypedDict",
    "ErrorValidationTypedDict",
    "FeatureState",
    "FeatureType",
    "HalRef",
    "HalRefTypedDict",
    "ImageReference",
    "ImageReferenceTypedDict",
    "Integration",
    "IntegrationTypedDict",
    "Integrations",
    "IntegrationsTypedDict",
    "Links",
    "LinksTypedDict",
    "ModifiedDate",
    "ModifiedDateTypedDict",
    "NewCompanySynchronizedWebhook",
    "NewCompanySynchronizedWebhookTypedDict",
    "Profile",
    "ProfileTypedDict",
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
    "PushOperationStatusChangedWebhook",
    "PushOperationStatusChangedWebhookData",
    "PushOperationStatusChangedWebhookDataTypedDict",
    "PushOperationStatusChangedWebhookTypedDict",
    "PushOperationTimedOutWebhook",
    "PushOperationTimedOutWebhookData",
    "PushOperationTimedOutWebhookDataTypedDict",
    "PushOperationTimedOutWebhookTypedDict",
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
    "ReadCompletedWebhook",
    "ReadCompletedWebhookPayload",
    "ReadCompletedWebhookPayloadTypedDict",
    "ReadCompletedWebhookTypedDict",
    "SchemaDataType",
    "Security",
    "SecurityTypedDict",
    "SourceType",
    "Status",
    "SupplementalDataConfiguration",
    "SupplementalDataConfigurationTypedDict",
    "SupplementalDataSourceConfiguration",
    "SupplementalDataSourceConfigurationTypedDict",
    "SupportedFeature",
    "SupportedFeatureTypedDict",
    "SyncSetting",
    "SyncSettingTypedDict",
    "SyncSettings",
    "SyncSettingsTypedDict",
    "UpdateConnectionStatus",
    "UpdateConnectionStatusTypedDict",
    "Validation",
    "ValidationItem",
    "ValidationItemTypedDict",
    "ValidationTypedDict",
    "Webhook",
    "WebhookConsumer",
    "WebhookConsumerPrototype",
    "WebhookConsumerPrototypeTypedDict",
    "WebhookConsumerTypedDict",
    "WebhookConsumers",
    "WebhookConsumersTypedDict",
    "WebhookNotifier",
    "WebhookNotifierTypedDict",
    "WebhookTypedDict",
    "Webhooks",
    "WebhooksTypedDict",
    "WriteStatus",
    "WriteType",
]
