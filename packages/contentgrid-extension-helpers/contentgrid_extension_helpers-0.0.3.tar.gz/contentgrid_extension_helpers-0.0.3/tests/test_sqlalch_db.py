import pytest
import os
import tempfile
from pathlib import Path
from sqlmodel import text, SQLModel, Field, Session
from contentgrid_extension_helpers.dependencies.sqlalch.db import (
    PostgresSessionFactory, 
    SQLiteSessionFactory,
    PostgresConfig,
    SQLiteConfig
)
from fixtures import postgres_session_factory, sqlite_session_factory


# Test model for database operations
class TestUser(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    email: str


# Parametrized fixture for both database types
@pytest.fixture(params=['sqlite', 'postgres'])
def db_session_factory(request, sqlite_session_factory, postgres_session_factory):
    """Parametrized fixture that provides both SQLite and PostgreSQL factories."""
    session_factory = None
    if request.param == 'sqlite':
        session_factory = sqlite_session_factory
    else:
        session_factory = postgres_session_factory
    
    yield session_factory
    
    session_factory.wipe_database()


class TestCommonDatabaseOperations:
    """Common tests that run for both SQLite and PostgreSQL."""
    
    def test_basic_connection(self, db_session_factory):
        """Test basic database connection for both SQLite and PostgreSQL."""
        session_generator = db_session_factory()
        session = next(session_generator)
        
        try:
            result = session.exec(text("SELECT 1")).first()[0]
            assert result == 1
        finally:
            try:
                next(session_generator)
            except StopIteration:
                pass
    
    def test_health_check(self, db_session_factory):
        """Test database health check for both database types."""
        assert db_session_factory.database_health_check() is True
    
    def test_context_manager_session(self, db_session_factory):
        """Test context manager session usage for both database types."""
        with db_session_factory.get_db_session() as session:
            result = session.exec(text("SELECT 1")).first()[0]
            assert result == 1
    
    def test_table_creation_and_operations(self, db_session_factory):
        """Test table creation and basic CRUD operations."""
        # Create tables
        SQLModel.metadata.create_all(db_session_factory.engine)
        
        with db_session_factory.get_db_session() as session:
            # Insert test data
            user = TestUser(id=1, name="Test User", email="test@example.com")
            session.add(user)
            session.commit()
            
            # Query test data
            retrieved_user = session.get(TestUser, 1)
            assert retrieved_user is not None
            assert retrieved_user.name == "Test User"
            assert retrieved_user.email == "test@example.com"
            
            # Update test
            retrieved_user.name = "Updated User"
            session.add(retrieved_user)
            session.commit()
            
            # Verify update
            updated_user = session.get(TestUser, 1)
            assert updated_user.name == "Updated User"
            
            # Count test
            result = session.exec(text("SELECT COUNT(*) FROM testuser")).first()[0]
            assert result >= 1
    
    def test_wipe_database(self, db_session_factory):
        """Test database wipe functionality for both database types."""
        # Create tables and insert data
        SQLModel.metadata.create_all(db_session_factory.engine)
        
        with db_session_factory.get_db_session() as session:
            user = TestUser(id=999, name="To be deleted", email="delete@example.com")
            session.add(user)
            session.commit()
        
        # Verify data exists
        with db_session_factory.get_db_session() as session:
            count_before = session.exec(text("SELECT COUNT(*) FROM testuser")).first()[0]
            assert count_before >= 1
        
        # Wipe database
        db_session_factory.wipe_database()
        
        # Verify tables are recreated but empty
        with db_session_factory.get_db_session() as session:
            count_after = session.exec(text("SELECT COUNT(*) FROM testuser")).first()[0]
            assert count_after == 0


class TestSQLiteSpecific:
    """SQLite-specific tests using the sqlite_session_factory fixture."""
    
    def test_sqlite_factory_properties(self, sqlite_session_factory):
        """Test SQLite-specific factory properties."""
        assert "sqlite:///" in sqlite_session_factory.create_connection_string()
    
    def test_sqlite_factory_creation_with_custom_file(self):
        """Test SQLite factory creation with custom database file."""
        custom_file = "test_custom.db"
        factory = SQLiteSessionFactory(sqlite_file_name=custom_file)
        assert factory.db_config.sqlite_file_name == custom_file
        assert factory.create_connection_string() == f"sqlite:///{custom_file}"
    
    def test_sqlite_factory_creation_with_debug(self):
        """Test SQLite factory creation with debug enabled."""
        factory = SQLiteSessionFactory(debug=True)
        assert factory.db_config.debug is True
    
    def test_sqlite_file_validation(self):
        """Test SQLite file name validation."""
        with pytest.raises(ValueError, match="SQLite file name must end with '.db'"):
            SQLiteSessionFactory(sqlite_file_name="invalid_file.txt")


class TestPostgreSQLSpecific:
    """PostgreSQL-specific tests using the postgres_session_factory fixture."""
    
    def test_postgres_factory_properties(self, postgres_session_factory):
        """Test PostgreSQL-specific factory properties."""
        assert "postgresql+psycopg2://" in postgres_session_factory.create_connection_string()
        assert postgres_session_factory.create_connect_args() == {}
        
        # Test engine kwargs
        engine_kwargs = postgres_session_factory.create_engine_kwargs()
        assert "pool_size" in engine_kwargs
        assert "max_overflow" in engine_kwargs
        assert "pool_pre_ping" in engine_kwargs
        assert "pool_recycle" in engine_kwargs
    
    def test_postgres_factory_creation_missing_params(self):
        """Test PostgreSQL factory creation fails with missing parameters."""
        with pytest.raises(ValueError, match="Failed to configure postgres"):
            PostgresSessionFactory()
    
    def test_postgres_factory_creation_with_params(self):
        """Test PostgreSQL factory creation with explicit parameters."""
        factory = PostgresSessionFactory(
            pg_host="localhost",
            pg_port=5432,
            pg_user="testuser",
            pg_passwd="testpass",
            pg_dbname="testdb"
        )
        
        expected_connection = "postgresql+psycopg2://testuser:testpass@localhost:5432/testdb"
        assert factory.create_connection_string() == expected_connection
        assert factory.create_connect_args() == {}
        
        # Test engine kwargs
        engine_kwargs = factory.create_engine_kwargs()
        assert engine_kwargs["pool_size"] == 10
        assert engine_kwargs["max_overflow"] == 20
        assert engine_kwargs["pool_pre_ping"] is True
        assert engine_kwargs["pool_recycle"] == 3600
    
    def test_postgres_factory_custom_pool_settings(self):
        """Test PostgreSQL factory with custom pool settings."""
        factory = PostgresSessionFactory(
            pg_host="localhost",
            pg_port=5432,
            pg_user="testuser", 
            pg_passwd="testpass",
            pg_dbname="testdb",
            db_pool_size=5,
            db_max_overflow=15,
            db_pool_pre_ping=False,
            db_pool_recycle=1800
        )
        
        engine_kwargs = factory.create_engine_kwargs()
        assert engine_kwargs["pool_size"] == 5
        assert engine_kwargs["max_overflow"] == 15
        assert engine_kwargs["pool_pre_ping"] is False
        assert engine_kwargs["pool_recycle"] == 1800
    
    def test_postgres_factory_with_env_vars(self, monkeypatch):
        """Test PostgreSQL factory using environment variables."""
        # Set environment variables
        monkeypatch.setenv("PG_HOST", "env_host")
        monkeypatch.setenv("PG_PORT", "5433")
        monkeypatch.setenv("PG_USER", "env_user")
        monkeypatch.setenv("PG_PASSWD", "env_pass")
        monkeypatch.setenv("PG_DBNAME", "env_db")
        
        factory = PostgresSessionFactory()
        
        expected_connection = "postgresql+psycopg2://env_user:env_pass@env_host:5433/env_db"
        assert factory.create_connection_string() == expected_connection
    
    def test_postgres_factory_params_override_env_vars(self, monkeypatch):
        """Test that explicit parameters override environment variables."""
        # Set environment variables
        monkeypatch.setenv("PG_HOST", "env_host")
        monkeypatch.setenv("PG_PORT", "5433")
        monkeypatch.setenv("PG_USER", "env_user")
        monkeypatch.setenv("PG_PASSWD", "env_pass")
        monkeypatch.setenv("PG_DBNAME", "env_db")
        
        # Override with explicit parameters
        factory = PostgresSessionFactory(
            pg_host="param_host",
            pg_port=5434,
            pg_user="param_user"
            # pg_passwd and pg_dbname should come from env vars
        )
        
        expected_connection = "postgresql+psycopg2://param_user:env_pass@param_host:5434/env_db"
        assert factory.create_connection_string() == expected_connection


class TestConfigClasses:
    """Test the configuration classes directly."""
    
    def test_postgres_config_defaults(self):
        """Test PostgreSQL configuration defaults."""
        config = PostgresConfig()
        assert config.pg_host is None
        assert config.pg_port is None
        assert config.pg_user is None
        assert config.pg_passwd is None
        assert config.pg_dbname is None
        assert config.db_pool_size == 10
        assert config.db_max_overflow == 20
        assert config.db_pool_recycle == 3600
        assert config.db_pool_pre_ping is True
    
    def test_sqlite_config_defaults(self):
        """Test SQLite configuration defaults."""
        config = SQLiteConfig()
        assert config.sqlite_file_name == "database.db"
        assert config.debug is False
    
    def test_sqlite_config_validation(self):
        """Test SQLite configuration validation."""
        # Valid file
        config = SQLiteConfig(sqlite_file_name="valid.db")
        assert config.sqlite_file_name == "valid.db"
        
        # Invalid file
        with pytest.raises(ValueError, match="SQLite file name must end with '.db'"):
            SQLiteConfig(sqlite_file_name="invalid.txt")


class TestDatabaseIntegration:
    """Integration tests using the actual fixtures."""
    
    def test_postgres_complex_operations(self, postgres_session_factory):
        """Test complex operations with PostgreSQL using fixture."""
        # Create tables
        SQLModel.metadata.create_all(postgres_session_factory.engine)
        
        with postgres_session_factory.get_db_session() as session:
            # Bulk insert
            users = [
                TestUser(id=i, name=f"User {i}", email=f"user{i}@example.com")
                for i in range(1, 6)
            ]
            session.add_all(users)
            session.commit()
            
            # Complex query
            result = session.exec(
                text("SELECT COUNT(*) FROM testuser WHERE name LIKE 'User%'")
            ).first()[0]
            assert result == 5
            
            # Transaction test
            try:
                user = TestUser(id=6, name="Rollback User", email="rollback@example.com")
                session.add(user)
                # Simulate error
                if True:  # This would be a real condition
                    session.rollback()
                    raise Exception("Simulated error")
            except Exception:
                pass  # Expected
            
            # Verify rollback worked
            count = session.exec(text("SELECT COUNT(*) FROM testuser")).first()[0]
            assert count == 5  # Should still be 5, not 6
    
    def test_sqlite_file_operations(self, sqlite_session_factory):
        """Test SQLite-specific file operations using fixture."""
        # The fixture handles the file, we just test operations
        SQLModel.metadata.create_all(sqlite_session_factory.engine)
        
        with sqlite_session_factory.get_db_session() as session:
            # Test SQLite-specific features
            session.exec(text("PRAGMA table_info(testuser)"))
            
            # Insert and verify
            user = TestUser(id=1, name="SQLite User", email="sqlite@example.com")
            session.add(user)
            session.commit()
            
            # Test case-insensitive search (SQLite feature)
            result = session.exec(
                text("SELECT * FROM testuser WHERE email LIKE '%SQLITE%'")
            ).first()
            assert result is not None