"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .datatypefeature import DataTypeFeature
from .sourcetype import SourceType
from codatcommon import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Integration:
    r"""An integration that Codat supports"""
    enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled') }})
    r"""Whether this integration is enabled for your customers to use."""
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    r"""A unique 4-letter key to represent a platform in each integration. View [accounting](https://docs.codat.io/integrations/accounting/overview#platform-keys), [banking](https://docs.codat.io/integrations/banking/overview#platform-keys), and [commerce](https://docs.codat.io/integrations/commerce/overview#platform-keys) platform keys."""
    logo_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logoUrl') }})
    r"""Static url for integration's logo."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of integration."""
    data_provided_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataProvidedBy'), 'exclude': lambda f: f is None }})
    r"""The name of the data provider."""
    datatype_features: Optional[List[DataTypeFeature]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datatypeFeatures'), 'exclude': lambda f: f is None }})
    integration_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrationId'), 'exclude': lambda f: f is None }})
    r"""A Codat ID representing the integration."""
    is_beta: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBeta'), 'exclude': lambda f: f is None }})
    r"""`True` if the integration is currently in beta release."""
    is_offline_connector: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isOfflineConnector'), 'exclude': lambda f: f is None }})
    r"""`True` if the integration is to an application installed and run locally on an SMBs computer."""
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId'), 'exclude': lambda f: f is None }})
    r"""A source-specific ID used to distinguish between different sources originating from the same data connection. In general, a data connection is a single data source. However, for TrueLayer, `sourceId` is associated with a specific bank and has a many-to-one relationship with the `integrationId`."""
    source_type: Optional[SourceType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    r"""The type of platform of the connection."""
    

