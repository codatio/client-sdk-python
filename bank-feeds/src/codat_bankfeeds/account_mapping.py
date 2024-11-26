"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from codat_bankfeeds import utils
from codat_bankfeeds._hooks import HookContext
from codat_bankfeeds.models import errors, operations, shared
from codat_bankfeeds.types import BaseModel, OptionalNullable, UNSET
from typing import Any, List, Optional, Union, cast


class AccountMapping(BaseSDK):
    r"""Extra functionality for building an account management UI."""

    def create(
        self,
        *,
        request: Union[
            operations.CreateBankAccountMappingRequest,
            operations.CreateBankAccountMappingRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.BankFeedAccountMappingResponse]:
        r"""Create bank feed account mapping

        The *Create bank account mapping* endpoint creates a new mapping between a source bank account and a potential account in the accounting software (target account).

        A bank feed account mapping is a specified link between the source account (provided by the Codat user) and the target account (the end user's account in the underlying software).

        To find valid target account options, first call the [List bank feed account mappings](https://docs.codat.io//bank-feeds-api#/operations/get-bank-account-mapping) endpoint.

        > **For custom builds only**
        >
        > Only use this endpoint if you are building your own account management UI.

        #### Account mapping variability

        The method of mapping the source account to the target account varies depending on the accounting software your company uses.

        #### Mapping options:

        1. **API Mapping**: Integrate the mapping journey directly into your application for a seamless user experience.
        2. **Codat UI Mapping**: If you prefer a quicker setup, you can utilize Codat's provided user interface for mapping.
        3. **Accounting Platform Mapping**: For some accounting software, the mapping process must be conducted within the software itself.

        ### Integration-specific behaviour

        | Bank Feed Integration | API Mapping | Codat UI Mapping | Accounting Platform Mapping |
        | --------------------- | ----------- | ---------------- | --------------------------- |
        | Xero                  | ✅          | ✅               |                             |
        | FreeAgent             | ✅          | ✅               |                             |
        | Oracle NetSuite       | ✅          | ✅               |                             |
        | Exact Online (NL)     | ✅          | ✅               |                             |
        | QuickBooks Online     |             |                  | ✅                          |
        | Sage                  |             |                  | ✅                          |

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, operations.CreateBankAccountMappingRequest
            )
        request = cast(operations.CreateBankAccountMappingRequest, request)

        req = self.build_request(
            method="POST",
            path="/companies/{companyId}/connections/{connectionId}/bankFeedAccounts/mapping",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.bank_feed_account_mapping,
                False,
                True,
                "json",
                Optional[shared.BankFeedAccountMapping],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="create-bank-account-mapping",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[shared.BankFeedAccountMappingResponse]
            )
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_async(
        self,
        *,
        request: Union[
            operations.CreateBankAccountMappingRequest,
            operations.CreateBankAccountMappingRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.BankFeedAccountMappingResponse]:
        r"""Create bank feed account mapping

        The *Create bank account mapping* endpoint creates a new mapping between a source bank account and a potential account in the accounting software (target account).

        A bank feed account mapping is a specified link between the source account (provided by the Codat user) and the target account (the end user's account in the underlying software).

        To find valid target account options, first call the [List bank feed account mappings](https://docs.codat.io//bank-feeds-api#/operations/get-bank-account-mapping) endpoint.

        > **For custom builds only**
        >
        > Only use this endpoint if you are building your own account management UI.

        #### Account mapping variability

        The method of mapping the source account to the target account varies depending on the accounting software your company uses.

        #### Mapping options:

        1. **API Mapping**: Integrate the mapping journey directly into your application for a seamless user experience.
        2. **Codat UI Mapping**: If you prefer a quicker setup, you can utilize Codat's provided user interface for mapping.
        3. **Accounting Platform Mapping**: For some accounting software, the mapping process must be conducted within the software itself.

        ### Integration-specific behaviour

        | Bank Feed Integration | API Mapping | Codat UI Mapping | Accounting Platform Mapping |
        | --------------------- | ----------- | ---------------- | --------------------------- |
        | Xero                  | ✅          | ✅               |                             |
        | FreeAgent             | ✅          | ✅               |                             |
        | Oracle NetSuite       | ✅          | ✅               |                             |
        | Exact Online (NL)     | ✅          | ✅               |                             |
        | QuickBooks Online     |             |                  | ✅                          |
        | Sage                  |             |                  | ✅                          |

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, operations.CreateBankAccountMappingRequest
            )
        request = cast(operations.CreateBankAccountMappingRequest, request)

        req = self.build_request_async(
            method="POST",
            path="/companies/{companyId}/connections/{connectionId}/bankFeedAccounts/mapping",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.bank_feed_account_mapping,
                False,
                True,
                "json",
                Optional[shared.BankFeedAccountMapping],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="create-bank-account-mapping",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[shared.BankFeedAccountMappingResponse]
            )
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get(
        self,
        *,
        request: Union[
            operations.GetBankAccountMappingRequest,
            operations.GetBankAccountMappingRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[List[shared.BankFeedMapping]]:
        r"""List bank feed accounts

        The *List bank accounts* endpoint returns information about a source bank account and any current or potential target mapping accounts.

        A bank feed account mapping is a specified link between the source account (provided by the Codat user) and the target account (the end user's account in the underlying software).

        > **For custom builds only**
        >
        > Only use this endpoint if you are building your own account management UI.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetBankAccountMappingRequest)
        request = cast(operations.GetBankAccountMappingRequest, request)

        req = self.build_request(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/bankFeedAccounts/mapping",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="get-bank-account-mapping",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[List[shared.BankFeedMapping]]
            )
        if utils.match_response(
            http_res,
            ["401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_async(
        self,
        *,
        request: Union[
            operations.GetBankAccountMappingRequest,
            operations.GetBankAccountMappingRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[List[shared.BankFeedMapping]]:
        r"""List bank feed accounts

        The *List bank accounts* endpoint returns information about a source bank account and any current or potential target mapping accounts.

        A bank feed account mapping is a specified link between the source account (provided by the Codat user) and the target account (the end user's account in the underlying software).

        > **For custom builds only**
        >
        > Only use this endpoint if you are building your own account management UI.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetBankAccountMappingRequest)
        request = cast(operations.GetBankAccountMappingRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/bankFeedAccounts/mapping",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="get-bank-account-mapping",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[List[shared.BankFeedMapping]]
            )
        if utils.match_response(
            http_res,
            ["401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
