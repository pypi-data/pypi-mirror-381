"""Auto-generated from TypeScript type: InitiateOidcLoginCommand"""
from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class InitiateOidcLoginCommand:
    post_login_redirect_url: Optional[str] = None
    oidc_client_id: Optional[str] = None
    customer_id: Optional[str] = None

    def _to_request(self) -> Dict[str, Any]:
        """Convert dataclass to request format with camelCase field names."""
        data: Dict[str, Any] = {}
        if self.post_login_redirect_url is not None:
            data["postLoginRedirectUrl"] = self.post_login_redirect_url
        if self.oidc_client_id is not None:
            data["oidcClientId"] = self.oidc_client_id
        if self.customer_id is not None:
            data["customerId"] = self.customer_id
        return data