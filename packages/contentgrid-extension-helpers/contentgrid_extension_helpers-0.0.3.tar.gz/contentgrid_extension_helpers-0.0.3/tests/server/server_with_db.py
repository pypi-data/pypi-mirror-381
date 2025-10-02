from fastapi import Depends
from server.base_server import app
from contentgrid_extension_helpers.config import extension_config
from sqlmodel import text, Session
from server.routers.foo_router import foo_router
from server.routers.client_router import client_router
from server.dependencies import db_factory

app_with_db = app

@app_with_db.get("/health/database")
async def health_check():
    """Health check endpoint to verify database connection."""
    return {"status": "healthy"}

@app_with_db.get("/session")
async def retrieve_session_test(session: Session = Depends(db_factory)):
    """Endpoint to test database session."""
    result = session.exec(text("SELECT 1")).first()
    # Convert the SQLAlchemy result to a JSON-serializable format
    return {"result": result[0] if result else None}

app_with_db.include_router(foo_router)
app_with_db.include_router(client_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app_with_db, host="0.0.0.0", port=extension_config.server_port or 5003, workers=extension_config.web_concurrency or 1)