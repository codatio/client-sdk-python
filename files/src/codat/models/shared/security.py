from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class Security:
    auth_header: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    