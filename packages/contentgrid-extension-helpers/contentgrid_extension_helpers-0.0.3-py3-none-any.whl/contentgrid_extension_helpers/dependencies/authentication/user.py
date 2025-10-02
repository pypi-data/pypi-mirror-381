from typing import Optional, cast, TypeVar, Generic
from fastapi import Depends
from typing_extensions import Annotated
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from contentgrid_extension_helpers.authentication.user import ContentGridUser
from contentgrid_extension_helpers.authentication.oidc import create_current_user_dependency, get_oauth_jwks_client, create_oauth2_scheme

oauth2_scheme = create_oauth2_scheme()

UserModelType = TypeVar('UserModelType', bound=BaseModel)

class ContentGridUserConfig(BaseSettings):
    extension_name : str # Should be the same extension name as defined in tokenmonger and keycloak (without the contentgrid:extension: prefix)
    oauth_issuer: str
    extension_auth_url: str

class ContentGridUserDependency(Generic[UserModelType]):
    def __init__(
        self,         
        extension_name: Optional[str] = None,
        oauth_issuer: Optional[str] = None,
        custom_audience: Optional[str] = None,
        user_model: type[UserModelType] = ContentGridUser,
        algorithms: Optional[list[str]] = None,
        verify_exp: bool = True,
        verify_aud: bool = True,
        verify_iss: bool = True,
        verify_nbf: bool = False,
        verify_iat: bool = False,
    ) -> None:
        
        self.user_model = user_model
        
        # Create config dict with provided parameters
        config_dict = {}
        if extension_name is not None:
            config_dict['extension_name'] = extension_name
        if oauth_issuer is not None:
            config_dict['oauth_issuer'] = oauth_issuer
            
        # Create ExtensionFlowConfig instance which will use env vars for missing values
        self.user_config = ContentGridUserConfig(**config_dict)
        
        if not custom_audience:
            self.audience = f"contentgrid:extension:{self.user_config.extension_name}"
        else:
            self.audience = custom_audience
        
        _ , self.jwks_client = get_oauth_jwks_client(self.user_config.oauth_issuer)
                
        self.user_dependency = create_current_user_dependency(
            jwks_client=self.jwks_client,
            oidc_issuer=self.user_config.oauth_issuer,
            audience=self.audience,
            user_model=user_model,
            algorithms = algorithms,
            verify_exp = verify_exp,
            verify_aud = verify_aud,
            verify_iss = verify_iss,
            verify_nbf = verify_nbf,
            verify_iat = verify_iat,
        )
    
    @property
    def config(self) -> ContentGridUserConfig:
        return self.user_config

    async def __call__(
        self, token: Annotated[str, Depends(oauth2_scheme)]
    ) -> UserModelType:
        user = cast(UserModelType, await self.user_dependency(token))
        return user