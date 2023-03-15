import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Webhooks:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def create_rule(self, request: operations.CreateRuleWebhook) -> operations.CreateRuleResponse:
        r"""Create webhook
        Create a new webhook configuration
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/rules'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateRuleResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateRuleWebhook])
                res.webhook = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateRule401ApplicationJSON])
                res.create_rule_401_application_json_object = out

        return res

    def get_webhook(self, request: operations.GetWebhookRequest) -> operations.GetWebhookResponse:
        r"""Get webhook
        Get a single webhook
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetWebhookRequest, base_url, '/rules/{ruleId}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetWebhookResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetWebhookWebhook])
                res.webhook = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetWebhook401ApplicationJSON])
                res.get_webhook_401_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetWebhook404ApplicationJSON])
                res.get_webhook_404_application_json_object = out

        return res

    def list_rules(self, request: operations.ListRulesRequest) -> operations.ListRulesResponse:
        r"""List webhooks
        List webhooks that you are subscribed to.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/rules'
        
        query_params = utils.get_query_params(operations.ListRulesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListRulesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListRulesLinks])
                res.links = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListRules400ApplicationJSON])
                res.list_rules_400_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListRules401ApplicationJSON])
                res.list_rules_401_application_json_object = out

        return res

    