from typing import Annotated, Optional, Type, TypeVar

from contentgrid_extension_helpers.authentication.user import ContentGridUser
from fastapi import Depends, Query
from contentgrid_extension_helpers.authentication.oidc import (
    create_oauth2_scheme,
)
from contentgrid_application_client.application import ContentGridApplicationClient
from contentgrid_hal_client.hal import HALFormsClient
from contentgrid_hal_client.security import IdentityAuthenticationManager
from pydantic import HttpUrl
from contentgrid_extension_helpers.dependencies.authentication.user import ContentGridUserDependency
from .client_factory import ContentGridBaseClientFactory, ContentGridClientFactorySettings

T = TypeVar('T', ContentGridApplicationClient, HALFormsClient)

oauth2_scheme = create_oauth2_scheme()

class ExtensionFlowConfig(ContentGridClientFactorySettings):
    extension_client_name: str 
    extension_client_secret: str
    system_exchange_uri: str = "https://extensions.sandbox.contentgrid.cloud/authentication/system/token"
    extension_auth_url: str = "https://auth.sandbox.contentgrid.cloud/realms/extensions/protocol/openid-connect/token"
    delegated_exchange_uri: str = "https://extensions.sandbox.contentgrid.cloud/authentication/delegated/token"

class ContentGridExtensionFlowClientFactory(ContentGridBaseClientFactory):
    def __init__(
        self,
        extension_auth_url: Optional[str] = None,
        extension_client_name: Optional[str] = None,
        extension_client_secret: Optional[str] = None,
        system_exchange_uri: Optional[str] = None,
        delegated_exchange_uri: Optional[str] = None,
    ) -> None:
        # Create config dict with provided parameters
        config_dict = {}
        if extension_auth_url is not None:
            config_dict['extension_auth_url'] = extension_auth_url
        if extension_client_name is not None:
            config_dict['extension_client_name'] = extension_client_name
        if extension_client_secret is not None:
            config_dict['extension_client_secret'] = extension_client_secret
        if system_exchange_uri is not None:
            config_dict['system_exchange_uri'] = system_exchange_uri
        if delegated_exchange_uri is not None:
            config_dict['delegated_exchange_uri'] = delegated_exchange_uri
            
        # Create ExtensionFlowConfig instance which will use env vars for missing values
        self.extension_config = ExtensionFlowConfig(**config_dict)

        self.identity_auth_manager = IdentityAuthenticationManager(
            auth_uri=self.extension_config.extension_auth_url,
            client_id=self.extension_config.extension_client_name,
            client_secret=self.extension_config.extension_client_secret,
            system_exchange_uri=self.extension_config.system_exchange_uri,
            delegated_exchange_uri=self.extension_config.delegated_exchange_uri,
        )
        super().__init__()
        
    @property
    def config(self) -> ExtensionFlowConfig:
        return self.extension_config
        
    def get_client(self, user: ContentGridUser, origin: Optional[HttpUrl], client_type: Type[T] = ContentGridApplicationClient) -> T:
        """Get a client of the specified type."""
        client_endpoint = self._get_client_endpoint(
            origin=origin,
            allowed_domains=user.domains
        )
        auth_manager = self.identity_auth_manager.for_user(user.access_token, urls={client_endpoint})
        
        return client_type(
            client_endpoint=client_endpoint,
            auth_manager=auth_manager,
        )
        
    def create_client_dependency(self, user_dependency: ContentGridUserDependency, client_type: Type[T] = ContentGridApplicationClient):
        """Create a dependency function for the specified client type."""
        def client_dependency(
            user: Annotated[ContentGridUser, Depends(user_dependency)], 
            origin: Annotated[Optional[HttpUrl], Query()] = None
        ) -> T:
            return self.get_client(user, origin, client_type)

        return client_dependency