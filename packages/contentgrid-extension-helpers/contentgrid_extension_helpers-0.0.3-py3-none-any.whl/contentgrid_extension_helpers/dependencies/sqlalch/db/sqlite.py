from typing import Dict, Any, Optional

from pydantic import field_validator
from .base_factory import DatabaseConfig, DatabaseSessionFactory


class SQLiteConfig(DatabaseConfig):
    sqlite_file_name: str = "database.db"

    @field_validator("sqlite_file_name")
    def validate_sqlite_file_name(cls, value: str) -> str:
        if not value.endswith('.db'):
            raise ValueError("SQLite file name must end with '.db'")
        return value


class SQLiteSessionFactory(DatabaseSessionFactory):
    """Factory class to create SQLite database connections."""
    
    def __init__(self, debug: Optional[bool]= None, sqlite_file_name : Optional[str] = None):
        config_dict = {}
        if debug is not None:
            config_dict['debug'] = debug
        if sqlite_file_name is not None:
            config_dict['sqlite_file_name'] = sqlite_file_name
        
        db_config = SQLiteConfig(**config_dict)
        super().__init__(db_config)
    
    def create_connection_string(self) -> str:
        """Create the SQLite connection string."""
        config = self.db_config
        if not isinstance(config, SQLiteConfig):
            raise ValueError("SQLiteConfig is required for SQLiteSessionFactory")
        return f"sqlite:///{config.sqlite_file_name}"
    
    def create_connect_args(self) -> Dict[str, Any]:
        """Create SQLite connection arguments."""
        return {"check_same_thread": False}
    
    def create_engine_kwargs(self) -> Dict[str, Any]:
        """Create SQLite engine keyword arguments."""
        return {}  # No pool config for SQLite
