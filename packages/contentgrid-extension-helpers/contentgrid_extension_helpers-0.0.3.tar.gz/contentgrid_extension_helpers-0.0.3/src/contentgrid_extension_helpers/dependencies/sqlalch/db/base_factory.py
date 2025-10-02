import logging
from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Optional, Dict, Any, Generator
from sqlmodel import SQLModel, Session, create_engine, text
from pydantic_settings import BaseSettings

class DatabaseConfig(BaseSettings):
    debug: bool = False

class DatabaseSessionFactory(ABC):
    """Abstract factory class to create database connections based on configuration."""
    
    def __init__(self, config : Optional[DatabaseConfig] = None):
        """Initialize with database configuration."""
        self.db_config = config if config else DatabaseConfig()
        
        # Get values from abstract methods and validate them
        connection_string = self.create_connection_string()
        connect_args = self.create_connect_args()
        engine_kwargs = self.create_engine_kwargs()
        
        # Assert that required values are provided
        assert connection_string is not None and connection_string.strip(), "Connection string must be a non-empty string"
        assert isinstance(connect_args, dict), "Connect args must be a dictionary"
        assert isinstance(engine_kwargs, dict), "Engine kwargs must be a dictionary"
        
        self.engine = create_engine(
            connection_string,
            connect_args=connect_args,
            echo="debug" if self.db_config.debug else None,  # Log SQL queries in debug mode
            **engine_kwargs
        )
    
    @abstractmethod
    def create_connection_string(self) -> str:
        """Create the database connection string."""
        pass
    
    @abstractmethod
    def create_connect_args(self) -> Dict[str, Any]:
        """Create connection arguments."""
        pass
    
    @abstractmethod
    def create_engine_kwargs(self) -> Dict[str, Any]:
        """Create engine keyword arguments."""
        pass
        
    def create_db_and_tables(self) -> None:
        """Create database tables from SQLModel metadata."""
        SQLModel.metadata.create_all(self.engine)
        
    # IMPORTANT : NO AUTOCOMMITS
    # SQLAlchemy session management
    # This function is used for dependency injection in FastAPI
    # It provides a session that is NOT automatically committed. 
    # It is the responsibility of the caller to commit one or more transactions.
    # When an error occurs the session is rolledback.
    def __call__(self) -> Generator[Session, None, None]:
        """Get a database session for dependency injection."""
        session = Session(self.engine)
        try:
            yield session
        except Exception as e:
            logging.exception(f"Database session error - Unexpected error: {e}")
            session.rollback()
            raise
        finally:
            session.close()

    # Context managers can no be used for dependency injection in FastAPI
    # but they are useful for manual session management in scripts or tests.
    @contextmanager
    def get_db_session(self) -> Generator[Session, None, None]:
        """Context manager for database sessions."""
        session = Session(self.engine)
        try:
            yield session
            session.commit()
        except Exception as e:
            logging.exception(f"Database transaction error - Unexpected error: {e}")
            session.rollback()
            raise
        finally:
            session.close()
    
    def database_health_check(self) -> bool:
        """Check if database connection is healthy."""
        try:
            with self.get_db_session() as session:
                # Simple query to test connection
                session.exec(text("SELECT 1"))
                return True
        except Exception as e:
            logging.exception(f"Database health check failed - Unexpected error: {e}")
            return False
        
    def wipe_database(self) -> None:
        """Wipes the database by dropping all tables and recreating them."""
        from sqlmodel import SQLModel
        try:
            SQLModel.metadata.drop_all(self.engine)
            SQLModel.metadata.create_all(self.engine)
            logging.debug("Database tables dropped and recreated successfully")
        except Exception as e:
            logging.warning(f"Database cleanup failed: {e}")