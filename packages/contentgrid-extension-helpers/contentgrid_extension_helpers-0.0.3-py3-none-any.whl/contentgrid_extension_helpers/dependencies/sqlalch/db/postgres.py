
from typing import Optional, Dict, Any
from .base_factory import DatabaseConfig, DatabaseSessionFactory

class PostgresConfig(DatabaseConfig):
    pg_host: Optional[str] = None
    pg_port: Optional[int] = None
    pg_user: Optional[str] = None
    pg_passwd: Optional[str] = None
    pg_dbname: Optional[str] = None
    
    # Database Connection Pool Configuration
    db_pool_size: int = 10
    db_max_overflow: int = 20
    db_pool_recycle: int = 3600
    db_pool_pre_ping: bool = True

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

class PostgresSessionFactory(DatabaseSessionFactory):
    """Factory class to create PostgreSQL database connections."""
    def __init__(self, pg_host: Optional[str] = None, pg_port: Optional[int] = None,
                 pg_user: Optional[str] = None, pg_passwd: Optional[str] = None,
                 pg_dbname: Optional[str] = None, debug: Optional[bool] = None,
                 db_pool_size: Optional[int] = None, db_max_overflow: Optional[int] = None,
                 db_pool_recycle: Optional[int] = None, db_pool_pre_ping: Optional[bool] = None):
        """Initialize with PostgreSQL configuration."""
        # Create config dict with provided parameters
        config_dict = {}
        if debug is not None:
            config_dict['debug'] = debug
        if db_pool_size is not None:
            config_dict['db_pool_size'] = db_pool_size
        if db_max_overflow is not None:
            config_dict['db_max_overflow'] = db_max_overflow
        if db_pool_recycle is not None:
            config_dict['db_pool_recycle'] = db_pool_recycle
        if db_pool_pre_ping is not None:
            config_dict['db_pool_pre_ping'] = db_pool_pre_ping
            
        # Override with explicit parameters if provided
        if pg_host is not None:
            config_dict['pg_host'] = pg_host
        if pg_port is not None:
            config_dict['pg_port'] = pg_port
        if pg_user is not None:
            config_dict['pg_user'] = pg_user
        if pg_passwd is not None:
            config_dict['pg_passwd'] = pg_passwd
        if pg_dbname is not None:
            config_dict['pg_dbname'] = pg_dbname
            
        # Create PostgresConfig instance which will use env vars for missing values
        self.postgres_config = PostgresConfig(**config_dict)
            
        # Validate required fields
        missing_fields = []
        if not self.postgres_config.pg_host:
            missing_fields.append("PG_HOST")
        if not self.postgres_config.pg_port:
            missing_fields.append("PG_PORT")
        if not self.postgres_config.pg_user:
            missing_fields.append("PG_USER")
        if not self.postgres_config.pg_passwd:
            missing_fields.append("PG_PASSWD")
        if not self.postgres_config.pg_dbname:
            missing_fields.append("PG_DBNAME")
        
        if missing_fields:
            raise ValueError(
                f"Failed to configure postgres. Missing parameters or environment variables: {', '.join(missing_fields)}"
            )
        
        super().__init__(self.postgres_config)
    
    def create_connection_string(self) -> str:
        """Create the PostgreSQL connection string."""
        return f"postgresql+psycopg2://{self.postgres_config.pg_user}:{self.postgres_config.pg_passwd}@{self.postgres_config.pg_host}:{self.postgres_config.pg_port}/{self.postgres_config.pg_dbname}"
    
    def create_connect_args(self) -> Dict[str, Any]:
        """Create PostgreSQL connection arguments."""
        return {}
    
    def create_engine_kwargs(self) -> Dict[str, Any]:
        """Create PostgreSQL engine keyword arguments."""
        return {
            "pool_size": self.postgres_config.db_pool_size,
            "max_overflow": self.postgres_config.db_max_overflow,
            "pool_pre_ping": self.postgres_config.db_pool_pre_ping,
            "pool_recycle": self.postgres_config.db_pool_recycle
        }
