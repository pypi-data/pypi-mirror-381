"""Auto-generated from TypeScript type: PatchScimConnectionCommand"""
from dataclasses import dataclass
from typing import Dict, Any, Optional
from .scim_user_mapping_config import ScimUserMappingConfig


@dataclass
class PatchScimConnectionCommand:
    display_name: Optional[str] = None
    scim_api_key_expiration: Optional[int] = None
    custom_mapping: Optional[ScimUserMappingConfig] = None
    scim_connection_id: Optional[str] = None
    customer_id: Optional[str] = None

    def _to_request(self) -> Dict[str, Any]:
        """Convert dataclass to request format with camelCase field names."""
        data: Dict[str, Any] = {}
        if self.display_name is not None:
            data["displayName"] = self.display_name
        if self.scim_api_key_expiration is not None:
            data["scimApiKeyExpiration"] = self.scim_api_key_expiration
        if self.custom_mapping is not None:
            data["customMapping"] = self.custom_mapping._to_request()
        if self.scim_connection_id is not None:
            data["scimConnectionId"] = self.scim_connection_id
        if self.customer_id is not None:
            data["customerId"] = self.customer_id
        return data