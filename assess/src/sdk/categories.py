import requests
from . import utils
from sdk.models import operations
from typing import Optional

class Categories:
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

    
    def get_data_assess_accounts_categories(self) -> operations.GetDataAssessAccountsCategoriesResponse:
        r"""List account categories
        Lists available account categories Codat's categorisation engine can provide. 
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/data/assess/accounts/categories"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataAssessAccountsCategoriesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[operations.GetDataAssessAccountsCategoriesChartOfAccountCategory]])
                res.get_data_assess_accounts_categories_chart_of_account_category_all_ofs = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_accounts_account_id_categories(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesResponse:
        r"""Get suggested and/or confirmed category for a specific account
        Get category for specific nominal account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/accounts/{accountId}/categories", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccount])
                res.categorised_account = out

        return res

    
    def get_data_companies_company_id_connections_connection_id_assess_accounts_categories(self, request: operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequest) -> operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesResponse:
        r"""List suggested and confirmed account categories
        Lists suggested and confirmed chart of account categories for the given company and data connection.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/accounts/categories", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesLinks])
                res.links = out

        return res

    
    def patch_data_companies_company_id_connections_connection_id_assess_accounts_account_id_categories(self, request: operations.PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesRequest) -> operations.PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesResponse:
        r"""Patch account categories
        Update category for a specific nominal account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/accounts/{accountId}/categories", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsAccountIDCategoriesCategorisedAccount])
                res.categorised_account = out

        return res

    
    def patch_data_companies_company_id_connections_connection_id_assess_accounts_categories(self, request: operations.PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesRequest) -> operations.PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesResponse:
        r"""Confirm categories for accounts
        Comfirms the categories for all or a batch of accounts for a specific connection.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/accounts/categories", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[operations.PatchDataCompaniesCompanyIDConnectionsConnectionIDAssessAccountsCategoriesCategorisedAccount]])
                res.categorised_accounts = out

        return res

    