"""Auto-generated from TypeScript type: PatchOidcClientCommand"""
from dataclasses import dataclass
from typing import Dict, Any, Optional, List
from .optional_idp_info_from_customer import OptionalIdpInfoFromCustomer
from .scim_matching_definition import ScimMatchingDefinition


@dataclass
class PatchOidcClientCommand:
    idp_info_from_customer: Optional[OptionalIdpInfoFromCustomer] = None
    display_name: Optional[str] = None
    email_domain_allowlist: Optional[List[str]] = None
    redirect_url: Optional[str] = None
    additional_scopes: Optional[List[str]] = None
    scim_matching_definition: Optional[ScimMatchingDefinition] = None
    oidc_client_id: Optional[str] = None
    customer_id: Optional[str] = None

    def _to_request(self) -> Dict[str, Any]:
        """Convert dataclass to request format with camelCase field names."""
        data: Dict[str, Any] = {}
        if self.idp_info_from_customer is not None:
            data["idpInfoFromCustomer"] = self.idp_info_from_customer._to_request()
        if self.display_name is not None:
            data["displayName"] = self.display_name
        if self.email_domain_allowlist is not None:
            data["emailDomainAllowlist"] = self.email_domain_allowlist
        if self.redirect_url is not None:
            data["redirectUrl"] = self.redirect_url
        if self.additional_scopes is not None:
            data["additionalScopes"] = self.additional_scopes
        if self.scim_matching_definition is not None:
            data["scimMatchingDefinition"] = self.scim_matching_definition._to_request()
        if self.oidc_client_id is not None:
            data["oidcClientId"] = self.oidc_client_id
        if self.customer_id is not None:
            data["customerId"] = self.customer_id
        return data