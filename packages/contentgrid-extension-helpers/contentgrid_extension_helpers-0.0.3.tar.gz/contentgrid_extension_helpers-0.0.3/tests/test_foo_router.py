import pytest
from fastapi.testclient import TestClient
from contentgrid_hal_client.exceptions import NotFound
from fixtures import *


def test_create_foo_success(client: TestClient):
    """Test successful creation of a new foo."""
    foo_data = {
        "name": "Test Foo",
        "description": "A test foo for testing",
        "secret_s3_path": "s3://test-bucket/test-foo"
    }
    
    response = client.post("/foos/", json=foo_data)
    assert response.status_code == 200
    
    created_foo = response.json()
    assert created_foo["name"] == foo_data["name"]
    assert created_foo["description"] == foo_data["description"]
    assert "id" in created_foo
    assert isinstance(created_foo["id"], int)
    # secret_s3_path should not be in the public response
    assert "secret_s3_path" not in created_foo


def test_create_foo_missing_required_field(client: TestClient):
    """Test creation fails when required fields are missing."""
    foo_data = {
        "name": "Test Foo",
        "description": "A test foo for testing"
        # missing secret_s3_path
    }
    
    response = client.post("/foos/", json=foo_data)
    assert response.status_code == 422  # Validation error


def test_get_all_foos_empty(client: TestClient):
    """Test retrieving all foos when none exist."""
    response = client.get("/foos/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_all_foos_with_data(client: TestClient):
    """Test retrieving all foos with existing data."""
    # Create a few foos first
    foo_data_1 = {
        "name": "Foo 1",
        "description": "First foo",
        "secret_s3_path": "s3://test-bucket/foo1"
    }
    foo_data_2 = {
        "name": "Foo 2", 
        "description": "Second foo",
        "secret_s3_path": "s3://test-bucket/foo2"
    }
    
    client.post("/foos/", json=foo_data_1)
    client.post("/foos/", json=foo_data_2)
    
    response = client.get("/foos/")
    assert response.status_code == 200
    
    foos = response.json()
    assert len(foos) == 2
    assert all("id" in foo for foo in foos)
    assert all("name" in foo for foo in foos)
    assert all("description" in foo for foo in foos)
    assert all("secret_s3_path" not in foo for foo in foos)  # Should not be public


def test_get_all_foos_with_pagination(client: TestClient):
    """Test pagination parameters for retrieving foos."""
    # Create multiple foos
    for i in range(5):
        foo_data = {
            "name": f"Foo {i}",
            "description": f"Description {i}",
            "secret_s3_path": f"s3://test-bucket/foo{i}"
        }
        client.post("/foos/", json=foo_data)
    
    # Test offset and limit
    response = client.get("/foos/?offset=2&limit=2")
    assert response.status_code == 200
    
    foos = response.json()
    assert len(foos) == 2


def test_get_all_foos_limit_validation(client: TestClient):
    """Test that limit parameter is validated (max 100)."""
    response = client.get("/foos/?limit=150")
    assert response.status_code == 422  # Validation error


def test_get_foo_by_id_success(client: TestClient):
    """Test successfully retrieving a foo by ID."""
    # Create a foo first
    foo_data = {
        "name": "Test Foo",
        "description": "A test foo",
        "secret_s3_path": "s3://test-bucket/test-foo"
    }
    
    create_response = client.post("/foos/", json=foo_data)
    created_foo = create_response.json()
    foo_id = created_foo["id"]
    
    # Get the foo by ID
    response = client.get(f"/foos/{foo_id}")
    assert response.status_code == 200
    
    retrieved_foo = response.json()
    assert retrieved_foo["id"] == foo_id
    assert retrieved_foo["name"] == foo_data["name"]
    assert retrieved_foo["description"] == foo_data["description"]
    assert "secret_s3_path" not in retrieved_foo


def test_get_foo_by_id_not_found(client: TestClient):
    """Test retrieving a foo with non-existent ID."""
    non_existent_id = 99999
    
    response = client.get(f"/foos/{non_existent_id}")
    assert response.status_code == 404
    
    error_response = response.json()
    assert "title" in error_response
    assert "not found" in error_response["title"].lower()


def test_get_foo_by_id_invalid_id(client: TestClient):
    """Test retrieving a foo with invalid ID format."""
    response = client.get("/foos/invalid_id")
    assert response.status_code == 422  # Validation error


def test_update_foo_success(client: TestClient):
    """Test successfully updating a foo."""
    # Create a foo first
    foo_data = {
        "name": "Original Foo",
        "description": "Original description",
        "secret_s3_path": "s3://test-bucket/original"
    }
    
    create_response = client.post("/foos/", json=foo_data)
    created_foo = create_response.json()
    foo_id = created_foo["id"]
    
    # Update the foo
    update_data = {
        "name": "Updated Foo",
        "description": "Updated description",
        "secret_s3_path": "s3://test-bucket/updated"
    }
    
    response = client.patch(f"/foos/{foo_id}", json=update_data)
    assert response.status_code == 200
    
    updated_foo = response.json()
    assert updated_foo["id"] == foo_id
    assert updated_foo["name"] == update_data["name"]
    assert updated_foo["description"] == update_data["description"]
    assert "secret_s3_path" not in updated_foo


def test_update_foo_partial(client: TestClient):
    """Test partial update of a foo (only some fields)."""
    # Create a foo first
    foo_data = {
        "name": "Original Foo",
        "description": "Original description", 
        "secret_s3_path": "s3://test-bucket/original"
    }
    
    create_response = client.post("/foos/", json=foo_data)
    created_foo = create_response.json()
    foo_id = created_foo["id"]
    
    # Update only the name
    update_data = {
        "name": "Partially Updated Foo"
    }
    
    response = client.patch(f"/foos/{foo_id}", json=update_data)
    assert response.status_code == 200
    
    updated_foo = response.json()
    assert updated_foo["id"] == foo_id
    assert updated_foo["name"] == update_data["name"]
    assert updated_foo["description"] == foo_data["description"]  # Should remain unchanged


def test_update_foo_not_found(client: TestClient):
    """Test updating a foo with non-existent ID."""
    non_existent_id = 99999
    update_data = {
        "name": "Updated Foo"
    }
    
    response = client.patch(f"/foos/{non_existent_id}", json=update_data)
    assert response.status_code == 404
    
    error_response = response.json()
    assert "title" in error_response
    assert "not found" in error_response["title"].lower()


def test_update_foo_invalid_id(client: TestClient):
    """Test updating a foo with invalid ID format."""
    update_data = {
        "name": "Updated Foo"
    }
    
    response = client.patch("/foos/invalid_id", json=update_data)
    assert response.status_code == 422  # Validation error


def test_delete_foo_success(client: TestClient):
    """Test successfully deleting a foo."""
    # Create a foo first
    foo_data = {
        "name": "Foo to Delete",
        "description": "This foo will be deleted",
        "secret_s3_path": "s3://test-bucket/to-delete"
    }
    
    create_response = client.post("/foos/", json=foo_data)
    created_foo = create_response.json()
    foo_id = created_foo["id"]
    
    # Delete the foo
    response = client.delete(f"/foos/{foo_id}")
    assert response.status_code == 200
    
    delete_result = response.json()
    assert delete_result.get("ok") is True
    
    # Verify the foo is actually deleted
    get_response = client.get(f"/foos/{foo_id}")
    assert get_response.status_code == 404


def test_delete_foo_not_found(client: TestClient):
    """Test deleting a foo with non-existent ID."""
    non_existent_id = 99999
    
    response = client.delete(f"/foos/{non_existent_id}")
    assert response.status_code == 404
    
    error_response = response.json()
    assert "title" in error_response
    assert "not found" in error_response["title"].lower()


def test_delete_foo_invalid_id(client: TestClient):
    """Test deleting a foo with invalid ID format."""
    response = client.delete("/foos/invalid_id")
    assert response.status_code == 422  # Validation error


def test_crud_workflow(client: TestClient):
    """Test complete CRUD workflow for a foo."""
    # Create
    foo_data = {
        "name": "CRUD Test Foo",
        "description": "Testing full CRUD operations",
        "secret_s3_path": "s3://test-bucket/crud-test"
    }
    
    create_response = client.post("/foos/", json=foo_data)
    assert create_response.status_code == 200
    created_foo = create_response.json()
    foo_id = created_foo["id"]
    
    # Read
    read_response = client.get(f"/foos/{foo_id}")
    assert read_response.status_code == 200
    read_foo = read_response.json()
    assert read_foo["name"] == foo_data["name"]
    
    # Update
    update_data = {
        "name": "Updated CRUD Test Foo",
        "description": "Updated description for CRUD test"
    }
    update_response = client.patch(f"/foos/{foo_id}", json=update_data)
    assert update_response.status_code == 200
    updated_foo = update_response.json()
    assert updated_foo["name"] == update_data["name"]
    assert updated_foo["description"] == update_data["description"]
    
    # Delete
    delete_response = client.delete(f"/foos/{foo_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["ok"] is True
    
    # Verify deletion
    final_read_response = client.get(f"/foos/{foo_id}")
    assert final_read_response.status_code == 404


def test_foo_data_privacy(client: TestClient):
    """Test that sensitive data (secret_s3_path) is not exposed in public responses."""
    # Create a foo with sensitive data
    foo_data = {
        "name": "Privacy Test Foo",
        "description": "Testing data privacy",
        "secret_s3_path": "s3://secret-bucket/very-secret-path"
    }
    
    create_response = client.post("/foos/", json=foo_data)
    created_foo = create_response.json()
    foo_id = created_foo["id"]
    
    # Check that secret_s3_path is not in any public response
    assert "secret_s3_path" not in created_foo
    
    # Check individual get
    get_response = client.get(f"/foos/{foo_id}")
    get_foo = get_response.json()
    assert "secret_s3_path" not in get_foo
    
    # Check list get
    list_response = client.get("/foos/")
    foos = list_response.json()
    for foo in foos:
        assert "secret_s3_path" not in foo
    
    # Check update response
    update_response = client.patch(f"/foos/{foo_id}", json={"name": "Updated Name"})
    updated_foo = update_response.json()
    assert "secret_s3_path" not in updated_foo


def test_multiple_foos_isolation(client: TestClient):
    """Test that operations on one foo don't affect others."""
    # Create multiple foos
    foo1_data = {
        "name": "Foo 1",
        "description": "First foo",
        "secret_s3_path": "s3://test-bucket/foo1"
    }
    foo2_data = {
        "name": "Foo 2",
        "description": "Second foo", 
        "secret_s3_path": "s3://test-bucket/foo2"
    }
    
    foo1_response = client.post("/foos/", json=foo1_data)
    foo2_response = client.post("/foos/", json=foo2_data)
    
    foo1_id = foo1_response.json()["id"]
    foo2_id = foo2_response.json()["id"]
    
    # Update foo1
    client.patch(f"/foos/{foo1_id}", json={"name": "Updated Foo 1"})
    
    # Check that foo2 is unchanged
    foo2_check = client.get(f"/foos/{foo2_id}")
    assert foo2_check.json()["name"] == foo2_data["name"]
    
    # Delete foo1
    client.delete(f"/foos/{foo1_id}")
    
    # Check that foo2 still exists
    foo2_final_check = client.get(f"/foos/{foo2_id}")
    assert foo2_final_check.status_code == 200
    assert foo2_final_check.json()["name"] == foo2_data["name"]
