"""Auto-generated from TypeScript type: GetScimUserCommand"""
from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class GetScimUserCommand:
    user_id: str
    scim_connection_id: Optional[str] = None
    customer_id: Optional[str] = None

    def _to_request(self) -> Dict[str, Any]:
        """Convert dataclass to request format with camelCase field names."""
        data: Dict[str, Any] = {}
        data["userId"] = self.user_id
        if self.scim_connection_id is not None:
            data["scimConnectionId"] = self.scim_connection_id
        if self.customer_id is not None:
            data["customerId"] = self.customer_id
        return data