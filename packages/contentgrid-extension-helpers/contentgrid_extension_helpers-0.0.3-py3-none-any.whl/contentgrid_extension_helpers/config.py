
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional
    
# Pydantic settings is used throughout this file.
# The library allows for easy configuration management, including environment variable loading and validation.
# Each field can be configured to load from environment variables, and validation can be applied to ensure correct types and formats.
# Example:
# class MyConfig(BaseSettings):
#     my_field: str = "default_value"
#     my_required_bool: bool  # This field must be provided
#     my_optional_field: Optional[int] = None
# 
# ENVIRONMENT VARIABLES:
# MY_FIELD=my_value
# MY_REQUIRED_BOOL=t
# MY_OPTIONAL_FIELD=42
# See https://docs.pydantic.dev/latest/api/pydantic_settings/ for more details.

class ExtensionConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=['.env', '.env.secret'],
        env_file_encoding='utf-8',
        extra='ignore',
    )
    
    cors_origins : List[str] = [] # is taken into account if production is True

    # Server Configuration
    server_url: Optional[str] = None  # Base URL for the server, can be set to None for local development
    server_host: Optional[str] = ""
    server_port: Optional[int] = None
    web_concurrency: Optional[int] = None
    
    # Environment Configuration
    ci: bool = False
    production: bool = False


extension_config = ExtensionConfig()