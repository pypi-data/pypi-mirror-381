"""
Data models for authentication (User and Service)
"""

from typing import List, Optional, Union

from pydantic import BaseModel, Field


class BaseAuthContext(BaseModel):
    """
    Base authentication context with common fields and methods.
    Both UserContext and ServiceContext inherit from this.
    """

    auth_source: str = Field(
        "unknown", description="Authentication source (user/service/kong/keycloak/bypass)"
    )
    roles: List[str] = Field(default_factory=list, description="Assigned roles")
    session_id: Optional[str] = Field(None, description="Session identifier")
    client_id: Optional[str] = Field(None, description="OAuth client ID")

    @property
    def is_service(self) -> bool:
        """Check if this is a service context (overridden in subclasses)"""
        return False

    @property
    def is_admin(self) -> bool:
        """Check if has admin role"""
        return "admin" in self.roles

    def has_role(self, role: str) -> bool:
        """Check if has specific role"""
        return role in self.roles or self.is_admin

    def has_any_role(self, roles: List[str]) -> bool:
        """Check if has any of the specified roles"""
        return bool(set(roles) & set(self.roles)) or self.is_admin

    def has_all_roles(self, roles: List[str]) -> bool:
        """Check if has all of the specified roles"""
        return all(self.has_role(role) for role in roles)

    class Config:
        frozen = False  # Allow mutation for middleware enrichment


class UserContext(BaseAuthContext):
    """
    Authenticated user context containing all user claims and metadata.
    This is the primary model passed through the application after user authentication.
    """

    user_id: str = Field(..., description="Unique user identifier")
    username: Optional[str] = Field(None, description="Username")
    email: Optional[str] = Field(None, description="User email address")
    scopes: List[str] = Field(default_factory=list, description="OAuth scopes")

    @property
    def is_service(self) -> bool:
        """Check if this is a service context"""
        return False

    @property
    def is_supplier(self) -> bool:
        """Check if user has supplier role"""
        return "supplier" in self.roles or self.is_admin

    @property
    def is_customer(self) -> bool:
        """Check if user has customer role"""
        return "customer" in self.roles

    @property
    def is_moderator(self) -> bool:
        """Check if user has moderator role"""
        return "moderator" in self.roles or self.is_admin

    def has_scope(self, scope: str) -> bool:
        """Check if user has specific scope"""
        return scope in self.scopes

    def has_any_scope(self, scopes: List[str]) -> bool:
        """Check if user has any of the specified scopes"""
        return bool(set(scopes) & set(self.scopes))


class ServiceContext(BaseAuthContext):
    """
    Authenticated service context for service-to-service communication.
    This model is passed through the application after service authentication.
    """

    service_name: str = Field(..., description="Service identifier (client_id)")
    service_id: Optional[str] = Field(default=None, description="Service user ID (sub claim)")

    @property
    def is_service(self) -> bool:
        """Check if this is a service context"""
        return True

    @property
    def is_supplier(self) -> bool:
        """Services don't have supplier role by default"""
        return False

    @property
    def is_customer(self) -> bool:
        """Services don't have customer role by default"""
        return False

    @property
    def is_moderator(self) -> bool:
        """Check if service has moderator role"""
        return "moderator" in self.roles or self.is_admin

    def has_scope(self, scope: str) -> bool:
        """Services don't have OAuth scopes"""
        return False

    def has_any_scope(self, scopes: List[str]) -> bool:
        """Services don't have OAuth scopes"""
        return False


# Union type for either user or service authentication
AuthContext = Union[UserContext, ServiceContext]
