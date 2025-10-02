"""Auto-generated from TypeScript type: ResetScimApiKeyCommand"""
from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class ResetScimApiKeyCommand:
    scim_api_key_expiration: Optional[int] = None
    scim_connection_id: Optional[str] = None
    customer_id: Optional[str] = None

    def _to_request(self) -> Dict[str, Any]:
        """Convert dataclass to request format with camelCase field names."""
        data: Dict[str, Any] = {}
        if self.scim_api_key_expiration is not None:
            data["scimApiKeyExpiration"] = self.scim_api_key_expiration
        if self.scim_connection_id is not None:
            data["scimConnectionId"] = self.scim_connection_id
        if self.customer_id is not None:
            data["customerId"] = self.customer_id
        return data