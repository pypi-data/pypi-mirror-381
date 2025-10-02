from fastapi.testclient import TestClient
from fixtures import *


def test_health_check(client: TestClient):
    """Tests the health check endpoint."""
    
    response = client.get("/health/database")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    
def test_retrieve_session(client: TestClient):
    """Tests the session retrieval endpoint."""
    response = client.get("/session")
    assert response.status_code == 200
    assert "result" in response.json()
    assert response.json()["result"] == 1  # The query SELECT 1 should return 1

def test_session_returns_json_serializable_data(client: TestClient):
    """Tests that the session endpoint returns properly serialized JSON data."""
    response = client.get("/session")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert "result" in json_data
    assert isinstance(json_data["result"], (int, type(None)))  # Should be an integer or None