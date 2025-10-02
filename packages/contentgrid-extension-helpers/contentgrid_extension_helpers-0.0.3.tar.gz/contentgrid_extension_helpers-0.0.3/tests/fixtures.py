from pytest import fixture
from fastapi.testclient import TestClient
from contentgrid_extension_helpers.dependencies.sqlalch.db import PostgresSessionFactory, SQLiteSessionFactory
import os
import logging
import docker

# Set initial environment variables
os.environ["DB_TYPE"] = "postgresql+psycopg2"

from testcontainers.postgres import PostgresContainer
from server.base_server import app
from server.server_with_db import app_with_db

postgres = PostgresContainer("postgres:16-alpine", dbname="contentgrid_test")

# Global variables to store the apps after container setup
_app_with_db = app_with_db
_simple_app = app

@fixture(scope="session")
def postgres_session_factory():
    """Setup database container for all tests."""
    
    postgres.start()
    
    logging.info(f"Started PostgreSQL container: {postgres.get_connection_url()}")
    
    # Update environment variables with actual container connection details
    conn_factory = PostgresSessionFactory(pg_host=postgres.get_container_host_ip(),
                                          pg_port=str(postgres.get_exposed_port(5432)),
                                          pg_dbname=postgres.dbname,
                                          pg_user=postgres.username,
                                          pg_passwd=postgres.password)
    conn_factory.create_db_and_tables()
    logging.info("Database tables created successfully")
    
    yield conn_factory  # This makes it a teardown fixture
    
    # Cleanup - only if we started the container
    try:
        postgres.stop()
        logging.info("PostgreSQL container stopped successfully")
    except (docker.errors.NotFound, docker.errors.APIError) as e:
        logging.warning(f"Container cleanup warning: {e}")
    except Exception as e:
        logging.error(f"Unexpected error during container cleanup: {e}")

@fixture(scope="session")
def sqlite_session_factory():
    conn_factory = SQLiteSessionFactory()
    conn_factory.create_db_and_tables()
    
    yield conn_factory
    
    conn_factory.wipe_database()


@fixture
def app_with_db():
    """Provides the FastAPI app instance with database access."""
    return _app_with_db

@fixture
def simple_app():
    """Provides the FastAPI app instance without database access."""
    if _simple_app is None:
        raise RuntimeError("Simple app not initialized.")
    return _simple_app

@fixture
def client_no_db(simple_app):
    """Provides a TestClient for the app without database."""
    return TestClient(simple_app)

@fixture
def client(app_with_db, clean_database):
    """Provides a TestClient for the app with database."""
    return TestClient(app_with_db)
        
@fixture
def clean_database(sqlite_session_factory):
    # """Clean all database tables between tests."""
    sqlite_session_factory.wipe_database()
    
    yield  # This allows the test to run
    
    # # Optional: cleanup after test as well
    sqlite_session_factory.wipe_database()