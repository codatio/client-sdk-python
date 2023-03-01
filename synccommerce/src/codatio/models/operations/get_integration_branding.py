from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class GetIntegrationBrandingPathParams:
    platform_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'platformKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetIntegrationBrandingRequest:
    path_params: GetIntegrationBrandingPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetIntegrationBrandingResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    