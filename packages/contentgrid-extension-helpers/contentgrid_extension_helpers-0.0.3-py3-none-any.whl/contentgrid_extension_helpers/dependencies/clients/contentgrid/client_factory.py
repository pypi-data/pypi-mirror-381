from abc import ABC
from typing import Optional, TypeVar, List
from contentgrid_hal_client.hal import HALFormsClient
from fastapi import HTTPException, status
from pydantic import HttpUrl
from pydantic_settings import BaseSettings
import logging


T = TypeVar('T', bound=HALFormsClient)

logger = logging.getLogger(__name__)

class ContentGridClientFactorySettings(BaseSettings):
    pass

class ContentGridBaseClientFactory(ABC):
    def __init__(self) -> None:
        self.env_config = ContentGridClientFactorySettings()
        
    def _get_client_endpoint(
        self,
        origin: Optional[HttpUrl] = None,
        allowed_domains: Optional[List[str]] = None,
        default_endpoint: Optional[str] = None
    ) -> str:
        """
        Get client endpoint with domain validation.
        
        Args:
            origin: Origin URL to validate and use
            allowed_domains: List of allowed domain strings for validation
            default_endpoint: Default endpoint to use if no origin provided
            user: ContentGrid user (optional, used for domain extraction if no allowed_domains)
            
        Returns:
            Validated client endpoint URL
            
        Raises:
            ValueError: If domain validation fails in production mode
        """
        if allowed_domains is None:
            # No domains available, will rely on default_endpoint or production check
            allowed_domains = []
            
        if origin:
            origin_host = origin.host
            origin_scheme = origin.scheme
            endpoint = f"{origin_scheme}://{origin_host}"
            
            # Validate domain if we have allowed domains defined (even if empty)
            if origin_host not in allowed_domains:
                error_msg = f"Origin domain '{origin_host}' not in allowed domains: {allowed_domains}"
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=error_msg, 
                )
            
            return endpoint
        
        elif default_endpoint:
            # Use default endpoint
            return default_endpoint
            
        elif allowed_domains:
            # Fallback to the first allowed domain
            return "https://" + allowed_domains[0]
            
        else:
            error_msg = "No endpoint available: provide either 'origin', 'default_endpoint', or ensure 'allowed_domains'/'user.domains' are available"
            raise ValueError(error_msg)