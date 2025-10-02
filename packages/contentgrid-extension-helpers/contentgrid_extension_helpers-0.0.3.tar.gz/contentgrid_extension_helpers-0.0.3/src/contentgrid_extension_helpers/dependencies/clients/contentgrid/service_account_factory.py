from typing import Annotated, Optional, Type, TypeVar, List
from fastapi import Query
from contentgrid_application_client.application import ContentGridApplicationClient
from contentgrid_hal_client.hal import HALFormsClient
from contentgrid_hal_client.security import ClientCredentialsApplicationAuthenticationManager
from pydantic import Field, HttpUrl
from pydantic_settings import SettingsConfigDict
from .client_factory import ContentGridBaseClientFactory, ContentGridClientFactorySettings

T = TypeVar('T', ContentGridApplicationClient, HALFormsClient)

class ContentGridServiceAccountFactorySettings(ContentGridClientFactorySettings):
    model_config = SettingsConfigDict(env_prefix='CG_')

    auth_url: str
    client_name: str
    client_secret: str
    # Default endpoint for service account, can be overridden
    default_endpoint: Optional[str] = Field(default=None, alias='CG_APP_URL')
    # Allowed domains for service account access
    allowed_domains: Optional[List[str]] = None

class ContentGridServiceAccountFactory(ContentGridBaseClientFactory):
    def __init__(
        self,
        auth_url: Optional[str] = None,
        client_name: Optional[str] = None,
        client_secret: Optional[str] = None,
        default_endpoint: Optional[str] = None,
        allowed_domains: Optional[List[str]] = None,
    ) -> None:
        # Create config dict with provided parameters
        config_dict = {}
        if auth_url is not None:
            config_dict['auth_url'] = auth_url
        if client_name is not None:
            config_dict['client_name'] = client_name
        if client_secret is not None:
            config_dict['client_secret'] = client_secret
        if default_endpoint is not None:
            config_dict['default_endpoint'] = default_endpoint
        if allowed_domains is not None:
            config_dict['allowed_domains'] = allowed_domains
            
        # Create ServiceAccountFactorySettings instance which will use env vars for missing values
        self.service_account_config = ContentGridServiceAccountFactorySettings(**config_dict)

        self.authentication_manager = ClientCredentialsApplicationAuthenticationManager(
            auth_uri=self.service_account_config.auth_url,
            client_id=self.service_account_config.client_name,
            client_secret=self.service_account_config.client_secret,
        )
        super().__init__()
        
    @property
    def config(self) -> ContentGridServiceAccountFactorySettings:
        return self.service_account_config
        
    def get_client(self, origin: Optional[HttpUrl] = None, client_type: Type[T] = ContentGridApplicationClient) -> T:
        """Get a client of the specified type using service account authentication."""
        client_endpoint = self._get_client_endpoint(
            origin=origin,
            allowed_domains=self.service_account_config.allowed_domains,
            default_endpoint=self.service_account_config.default_endpoint
        )
        
        # Create a new authentication manager instance for this specific endpoint
        auth_manager = ClientCredentialsApplicationAuthenticationManager(
            auth_uri=self.service_account_config.auth_url,
            client_id=self.service_account_config.client_name,
            client_secret=self.service_account_config.client_secret,
            resources=[client_endpoint]
        )
        
        return client_type(
            client_endpoint=client_endpoint,
            auth_manager=auth_manager,
        )
        
    def create_client_dependency(self, client_type: Type[T] = ContentGridApplicationClient):
        """Create a dependency function for the specified client type (no user required)."""
        def client_dependency(
            origin: Annotated[Optional[HttpUrl], Query()] = None
        ) -> T:
            return self.get_client(origin, client_type)

        return client_dependency