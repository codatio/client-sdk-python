"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .add_company_to_groupop import (
    AddCompanyToGroupRequest,
    AddCompanyToGroupRequestTypedDict,
)
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
from .company import Company, CompanyTags, CompanyTagsTypedDict, CompanyTypedDict
from .companydetails import CompanyDetails, CompanyDetailsTypedDict, Tags, TagsTypedDict
from .companygroupassignment import (
    CompanyGroupAssignment,
    CompanyGroupAssignmentTypedDict,
)
from .companyreference import CompanyReference, CompanyReferenceTypedDict
from .companyrequestbody import CompanyRequestBody, CompanyRequestBodyTypedDict
from .companywebhook import CompanyWebhook, CompanyWebhookTypedDict
from .configure_custom_data_typeop import (
    ConfigureCustomDataTypeRequest,
    ConfigureCustomDataTypeRequestTypedDict,
)
from .configure_supplemental_dataop import (
    ConfigureSupplementalDataPathParamDataType,
    ConfigureSupplementalDataRequest,
    ConfigureSupplementalDataRequestTypedDict,
)
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
from .create_connectionop import (
    CreateConnectionRequest,
    CreateConnectionRequestBody,
    CreateConnectionRequestBodyTypedDict,
    CreateConnectionRequestTypedDict,
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
from .datastatus import DataStatus, DataStatusTypedDict, DataTypes
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
from .delete_api_keyop import DeleteAPIKeyRequest, DeleteAPIKeyRequestTypedDict
from .delete_companyop import DeleteCompanyRequest, DeleteCompanyRequestTypedDict
from .delete_connectionop import (
    DeleteConnectionRequest,
    DeleteConnectionRequestTypedDict,
)
from .delete_webhook_consumerop import (
    DeleteWebhookConsumerRequest,
    DeleteWebhookConsumerRequestTypedDict,
)
from .errormessage import ErrorMessage, ErrorMessageData
from .errorvalidation import ErrorValidation, ErrorValidationTypedDict
from .errorvalidationitem import ErrorValidationItem, ErrorValidationItemTypedDict
from .featurestate import FeatureState
from .featuretype import FeatureType
from .get_company_data_statusop import (
    GetCompanyDataStatusRequest,
    GetCompanyDataStatusRequestTypedDict,
)
from .get_company_push_historyop import (
    GetCompanyPushHistoryRequest,
    GetCompanyPushHistoryRequestTypedDict,
)
from .get_companyop import GetCompanyRequest, GetCompanyRequestTypedDict
from .get_connection_management_access_tokenop import (
    GetConnectionManagementAccessTokenRequest,
    GetConnectionManagementAccessTokenRequestTypedDict,
)
from .get_connectionop import GetConnectionRequest, GetConnectionRequestTypedDict
from .get_create_update_model_options_by_data_typeop import (
    GetCreateUpdateModelOptionsByDataTypeRequest,
    GetCreateUpdateModelOptionsByDataTypeRequestTypedDict,
)
from .get_custom_data_type_configurationop import (
    GetCustomDataTypeConfigurationRequest,
    GetCustomDataTypeConfigurationRequestTypedDict,
)
from .get_integrationop import GetIntegrationRequest, GetIntegrationRequestTypedDict
from .get_integrations_brandingop import (
    GetIntegrationsBrandingRequest,
    GetIntegrationsBrandingRequestTypedDict,
)
from .get_pull_operationop import (
    GetPullOperationRequest,
    GetPullOperationRequestTypedDict,
)
from .get_push_operationop import (
    GetPushOperationRequest,
    GetPushOperationRequestTypedDict,
)
from .get_supplemental_data_configurationop import (
    GetSupplementalDataConfigurationRequest,
    GetSupplementalDataConfigurationRequestTypedDict,
    PathParamDataType,
)
from .get_webhookop import GetWebhookRequest, GetWebhookRequestTypedDict
from .group import Group, GroupTypedDict
from .groupprototype import GroupPrototype, GroupPrototypeTypedDict
from .groupref import GroupRef, GroupRefTypedDict
from .groups import Groups, GroupsTypedDict
from .halref import HalRef, HalRefTypedDict
from .imagereference import ImageReference, ImageReferenceTypedDict
from .integration import Integration, IntegrationTypedDict
from .integrations import Integrations, IntegrationsTypedDict
from .links import Links, LinksTypedDict
from .list_companiesop import ListCompaniesRequest, ListCompaniesRequestTypedDict
from .list_connectionsop import ListConnectionsRequest, ListConnectionsRequestTypedDict
from .list_custom_data_type_recordsop import (
    ListCustomDataTypeRecordsRequest,
    ListCustomDataTypeRecordsRequestTypedDict,
)
from .list_integrationsop import (
    ListIntegrationsRequest,
    ListIntegrationsRequestTypedDict,
)
from .list_pull_operationsop import (
    ListPullOperationsRequest,
    ListPullOperationsRequestTypedDict,
)
from .list_rulesop import ListRulesRequest, ListRulesRequestTypedDict
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
from .refresh_company_dataop import (
    RefreshCompanyDataRequest,
    RefreshCompanyDataRequestTypedDict,
)
from .refresh_custom_data_typeop import (
    RefreshCustomDataTypeRequest,
    RefreshCustomDataTypeRequestTypedDict,
)
from .refresh_data_typeop import RefreshDataTypeRequest, RefreshDataTypeRequestTypedDict
from .remove_company_from_groupop import (
    RemoveCompanyFromGroupRequest,
    RemoveCompanyFromGroupRequestTypedDict,
)
from .schema_datatype import SchemaDataType
from .sdkerror import SDKError
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
from .unlink_connectionop import (
    UnlinkConnectionRequest,
    UnlinkConnectionRequestTypedDict,
)
from .update_companyop import UpdateCompanyRequest, UpdateCompanyRequestTypedDict
from .update_connection_authorizationop import (
    UpdateConnectionAuthorizationRequest,
    UpdateConnectionAuthorizationRequestTypedDict,
)
from .update_profile_syncsettingsop import (
    UpdateProfileSyncSettingsRequestBody,
    UpdateProfileSyncSettingsRequestBodyTypedDict,
)
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
    "AddCompanyToGroupRequest",
    "AddCompanyToGroupRequestTypedDict",
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
    "CompanyDetails",
    "CompanyDetailsTypedDict",
    "CompanyGroupAssignment",
    "CompanyGroupAssignmentTypedDict",
    "CompanyReference",
    "CompanyReferenceTypedDict",
    "CompanyRequestBody",
    "CompanyRequestBodyTypedDict",
    "CompanyTags",
    "CompanyTagsTypedDict",
    "CompanyTypedDict",
    "CompanyWebhook",
    "CompanyWebhookTypedDict",
    "ConfigureCustomDataTypeRequest",
    "ConfigureCustomDataTypeRequestTypedDict",
    "ConfigureSupplementalDataPathParamDataType",
    "ConfigureSupplementalDataRequest",
    "ConfigureSupplementalDataRequestTypedDict",
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
    "Connections",
    "ConnectionsTypedDict",
    "Content",
    "ContentTypedDict",
    "CreateAPIKey",
    "CreateAPIKeyTypedDict",
    "CreateConnectionRequest",
    "CreateConnectionRequestBody",
    "CreateConnectionRequestBodyTypedDict",
    "CreateConnectionRequestTypedDict",
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
    "DatasetDataChangedWebhook",
    "DatasetDataChangedWebhookData",
    "DatasetDataChangedWebhookDataTypedDict",
    "DatasetDataChangedWebhookTypedDict",
    "DatasetStatus",
    "DatasetStatusChangedErrorWebhook",
    "DatasetStatusChangedErrorWebhookData",
    "DatasetStatusChangedErrorWebhookDataTypedDict",
    "DatasetStatusChangedErrorWebhookTypedDict",
    "DeleteAPIKeyRequest",
    "DeleteAPIKeyRequestTypedDict",
    "DeleteCompanyRequest",
    "DeleteCompanyRequestTypedDict",
    "DeleteConnectionRequest",
    "DeleteConnectionRequestTypedDict",
    "DeleteWebhookConsumerRequest",
    "DeleteWebhookConsumerRequestTypedDict",
    "ErrorMessage",
    "ErrorMessageData",
    "ErrorStatus",
    "ErrorValidation",
    "ErrorValidationItem",
    "ErrorValidationItemTypedDict",
    "ErrorValidationTypedDict",
    "FeatureState",
    "FeatureType",
    "GetCompanyDataStatusRequest",
    "GetCompanyDataStatusRequestTypedDict",
    "GetCompanyPushHistoryRequest",
    "GetCompanyPushHistoryRequestTypedDict",
    "GetCompanyRequest",
    "GetCompanyRequestTypedDict",
    "GetConnectionManagementAccessTokenRequest",
    "GetConnectionManagementAccessTokenRequestTypedDict",
    "GetConnectionRequest",
    "GetConnectionRequestTypedDict",
    "GetCreateUpdateModelOptionsByDataTypeRequest",
    "GetCreateUpdateModelOptionsByDataTypeRequestTypedDict",
    "GetCustomDataTypeConfigurationRequest",
    "GetCustomDataTypeConfigurationRequestTypedDict",
    "GetIntegrationRequest",
    "GetIntegrationRequestTypedDict",
    "GetIntegrationsBrandingRequest",
    "GetIntegrationsBrandingRequestTypedDict",
    "GetPullOperationRequest",
    "GetPullOperationRequestTypedDict",
    "GetPushOperationRequest",
    "GetPushOperationRequestTypedDict",
    "GetSupplementalDataConfigurationRequest",
    "GetSupplementalDataConfigurationRequestTypedDict",
    "GetWebhookRequest",
    "GetWebhookRequestTypedDict",
    "Group",
    "GroupPrototype",
    "GroupPrototypeTypedDict",
    "GroupRef",
    "GroupRefTypedDict",
    "GroupTypedDict",
    "Groups",
    "GroupsTypedDict",
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
    "ListCompaniesRequest",
    "ListCompaniesRequestTypedDict",
    "ListConnectionsRequest",
    "ListConnectionsRequestTypedDict",
    "ListCustomDataTypeRecordsRequest",
    "ListCustomDataTypeRecordsRequestTypedDict",
    "ListIntegrationsRequest",
    "ListIntegrationsRequestTypedDict",
    "ListPullOperationsRequest",
    "ListPullOperationsRequestTypedDict",
    "ListRulesRequest",
    "ListRulesRequestTypedDict",
    "ModifiedDate",
    "ModifiedDateTypedDict",
    "NewCompanySynchronizedWebhook",
    "NewCompanySynchronizedWebhookTypedDict",
    "PathParamDataType",
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
    "RefreshCompanyDataRequest",
    "RefreshCompanyDataRequestTypedDict",
    "RefreshCustomDataTypeRequest",
    "RefreshCustomDataTypeRequestTypedDict",
    "RefreshDataTypeRequest",
    "RefreshDataTypeRequestTypedDict",
    "RemoveCompanyFromGroupRequest",
    "RemoveCompanyFromGroupRequestTypedDict",
    "SDKError",
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
    "Tags",
    "TagsTypedDict",
    "UnlinkConnectionRequest",
    "UnlinkConnectionRequestTypedDict",
    "UpdateCompanyRequest",
    "UpdateCompanyRequestTypedDict",
    "UpdateConnectionAuthorizationRequest",
    "UpdateConnectionAuthorizationRequestTypedDict",
    "UpdateConnectionStatus",
    "UpdateConnectionStatusTypedDict",
    "UpdateProfileSyncSettingsRequestBody",
    "UpdateProfileSyncSettingsRequestBodyTypedDict",
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
