import requests
from . import utils
from codat.models import operations
from typing import Optional

class PushData:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def get_companies_company_id_connections_connection_id_push(self, request: operations.GetCompaniesCompanyIDConnectionsConnectionIDPushRequest) -> operations.GetCompaniesCompanyIDConnectionsConnectionIDPushResponse:
        r"""List push options
        Before pushing data into accounting software, it is often necessary to collect some details from the user as to how they would like the data to be inserted. This includes names and amounts on transactional entities, but also factors such as categorisation of entities, which is often handled differently between different accounting packages. A good example of this is specifying where on the balance sheet/profit and loss reports the user would like a newly-created nominal account to appear.
        
        Codat does not wish to limit users to pushing to a very limited number of standard categories, so we have implemented an \"options\" endpoint, which allows us to expose to our clients the fields which are required to be pushed for a specific linked company, and the options which may be selected for each field.
        
        
        > **Supported Integrations**
        > 
        > Check out our [Knowledge UI](https://knowledge.codat.io/) for integrations that support push (POST/PUT methods).
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/options/{dataType}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompaniesCompanyIDConnectionsConnectionIDPushResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDConnectionsConnectionIDPushPushOption])
                res.push_option = out

        return res

    
    def get_companies_company_id_push(self, request: operations.GetCompaniesCompanyIDPushRequest) -> operations.GetCompaniesCompanyIDPushResponse:
        r"""List push operations
        List push operation records.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/push", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompaniesCompanyIDPushResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDPushLinks])
                res.links = out

        return res

    
    def get_companies_company_id_push_push_operation_key(self, request: operations.GetCompaniesCompanyIDPushPushOperationKeyRequest) -> operations.GetCompaniesCompanyIDPushPushOperationKeyResponse:
        r"""Get push operation
        Retrieve push operation.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/push/{pushOperationKey}", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCompaniesCompanyIDPushPushOperationKeyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetCompaniesCompanyIDPushPushOperationKey200ApplicationJSON])
                res.get_companies_company_id_push_push_operation_key_200_application_json_object = out

        return res

    