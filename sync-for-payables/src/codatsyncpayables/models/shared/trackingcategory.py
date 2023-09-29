"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import status as shared_status
from codatsyncpayables import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TrackingCategory:
    r"""Details of a category used for tracking transactions.

    > Language tip
    >
    > Parameters used to track types of spend in various parts of an organization can be called  **dimensions**, **projects**, **classes**, or **locations** in different accounting platforms. In Codat, we refer to these as tracking categories.

    View the coverage for tracking categories in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=trackingCategories\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    Tracking categories are used to monitor cost centres and control budgets that sit outside the standard chart of accounts. Customers may use tracking categories to group together and track the income and costs of specific departments, projects, locations or customers.

    From their accounting system, customers can: 

    - Create and maintain tracking categories and tracking category types.
    - View all tracking categories that are available for use.
    - View the relationships between the categories.
    - Assign invoices, bills, credit notes, or bill credit notes to one or more categories.
    - View the categories that a transaction belongs to.
    - View all transactions in a tracking category.

    ### Tracking categories per platform

    Review the platform-specific tracking categories that Codat supports, and the level they are assigned to in the source platform. 

    <table>
    <thead>
      <tr>
        <th>Platform</th>
        <th>Tracking category</th>
        <th>Tracking level</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Dynamics 365</b></td>
        <td>Dimensions</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td><b>Freshbooks</b></td>
        <td>Expense&nbsp;categories</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td><b>MYOB</b></td>
        <td>Categories</td>
        <td>Transaction</td>
      </tr>
      <tr>
        <td rowspan=4><b>Netsuite</b></td>
        <td>Classes</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td>Locations</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td>Departments</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td>Custom&nbsp;segments</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td rowspan=2><b>QuickBooks Desktop</b></td>
        <td>Classes</td>
        <td>Line item or transaction level</td>
      </tr>
      <tr>
        <td>Locations</td>
        <td>Transaction</td>
      </tr>
      <tr>
        <td rowspan=2><b>QuickBooks Online</b></td>
        <td>Classes</td>
        <td>Line item or transaction level</td>
      </tr>
      <tr>
        <td>Locations</td>
        <td>Transaction</td>
      </tr>
      <tr>
        <td rowspan=3><b>Sage 200</b></td>
        <td>Cost&nbsp;centers</td>
        <td>Line item</td>
      </tr>
      <tr>
          <td>Departments</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td>Analysis&nbsp;codes</td>
        <td>Transaction</td>
      </tr>
      <tr>
        <td rowspan=3><b>Sage 50</b></td>
        <td>Departments</td>
        <td>Line item</td>
      </tr>
      <tr>
         <td>Costcodes</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td>Projects</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td><b>Sage Intacct</b></td>
        <td>Dimensions</td>
        <td>Line item</td>
      </tr>
      <tr>
        <td><b>Xero</b></td>
        <td>Tracking&nbsp;categories</td>
        <td>Line item</td>
      </tr>
    </tbody>
    </table>

    > **Example use case**
    >
    > Monitor the budget for your annual conference using a tracking category called 'AnnualConference2020' with the **type** set to **Costing**.

    If a tracking category has a parent category, the ID of that parent category is displayed. There is also a `hasChildren` field that shows whether there are child subcategories nested beneath.
    """
    has_children: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasChildren'), 'exclude': lambda f: f is None }})
    r"""Boolean value indicating whether this category has SubCategories."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The identifier for the item, unique per tracking category."""
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the tracking category."""
    parent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentId') }})
    r"""The identifier for this item's immediate parent."""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    status: Optional[shared_status.Status] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Current state of the tracking category."""
    

