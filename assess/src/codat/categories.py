import requests
from . import utils
from codat.models import operations
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

    
    def get_account_category(self, request: operations.GetAccountCategoryRequest) -> operations.GetAccountCategoryResponse:
        r"""Get suggested and/or confirmed category for a specific account
        Get category for specific nominal account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/accounts/{accountId}/categories", request.path_params)
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAccountCategoryResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAccountCategoryCategorisedAccount])
                res.categorised_account = out

        return res

    
    def list_accounts_categories(self, request: operations.ListAccountsCategoriesRequest) -> operations.ListAccountsCategoriesResponse:
        r"""List suggested and confirmed account categories
        Lists suggested and confirmed chart of account categories for the given company and data connection.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/accounts/categories", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListAccountsCategoriesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListAccountsCategoriesLinks])
                res.links = out

        return res

    
    def list_available_account_categories(self) -> operations.ListAvailableAccountCategoriesResponse:
        r"""List account categories
        Lists available account categories Codat's categorisation engine can provide. 
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/data/assess/accounts/categories"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListAvailableAccountCategoriesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[operations.ListAvailableAccountCategoriesChartOfAccountCategory]])
                res.list_available_account_categories_chart_of_account_category_all_ofs = out

        return res

    
    def update_account_category(self, request: operations.UpdateAccountCategoryRequest) -> operations.UpdateAccountCategoryResponse:
        r"""Patch account categories
        Update category for a specific nominal account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/accounts/{accountId}/categories", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateAccountCategoryResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.UpdateAccountCategoryCategorisedAccount])
                res.categorised_account = out

        return res

    
    def update_accounts_categories(self, request: operations.UpdateAccountsCategoriesRequest) -> operations.UpdateAccountsCategoriesResponse:
        r"""Confirm categories for accounts
        Comfirms the categories for all or a batch of accounts for a specific connection.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/data/companies/{companyId}/connections/{connectionId}/assess/accounts/categories", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateAccountsCategoriesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[list[operations.UpdateAccountsCategoriesCategorisedAccount]])
                res.categorised_accounts = out

        return res

    