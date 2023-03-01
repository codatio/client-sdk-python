import requests
from . import utils
from codat.models import operations
from typing import Optional

class Products:
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

    
    def list_commerce_product_categories(self, request: operations.ListCommerceProductCategoriesRequest) -> operations.ListCommerceProductCategoriesResponse:
        r"""List product categories
        Product categories are used to classify a group of products together, either by type (eg \"Furniture\"), or sometimes by tax profile.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/commerce-productCategories", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListCommerceProductCategoriesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListCommerceProductCategoriesLinks])
                res.links = out

        return res

    
    def list_commerce_products(self, request: operations.ListCommerceProductsRequest) -> operations.ListCommerceProductsResponse:
        r"""List products
        The Products data type provides the company's product inventory, and includes the price and quantity of all products, and product variants, available for sale.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/companies/{companyId}/connections/{connectionId}/data/commerce-products", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListCommerceProductsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListCommerceProductsLinks])
                res.links = out

        return res

    