"""Auto-generated from TypeScript type: GetScimUsersCommand"""
from dataclasses import dataclass
from typing import Dict, Any, Optional
from .scim_users_page_equality_filter import ScimUsersPageEqualityFilter


@dataclass
class GetScimUsersCommand:
    filter: Optional[ScimUsersPageEqualityFilter] = None
    page_number: Optional[int] = None
    page_size: Optional[int] = None
    scim_connection_id: Optional[str] = None
    customer_id: Optional[str] = None

    def _to_request(self) -> Dict[str, Any]:
        """Convert dataclass to request format with camelCase field names."""
        data: Dict[str, Any] = {}
        if self.filter is not None:
            data["filter"] = self.filter._to_request()
        if self.page_number is not None:
            data["pageNumber"] = self.page_number
        if self.page_size is not None:
            data["pageSize"] = self.page_size
        if self.scim_connection_id is not None:
            data["scimConnectionId"] = self.scim_connection_id
        if self.customer_id is not None:
            data["customerId"] = self.customer_id
        return data