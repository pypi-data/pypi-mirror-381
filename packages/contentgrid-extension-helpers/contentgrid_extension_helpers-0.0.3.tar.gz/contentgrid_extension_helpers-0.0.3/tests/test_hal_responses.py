from typing_extensions import Unpack
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Any
from unittest.mock import Mock, patch

from contentgrid_hal_client.hal import HALLink
from contentgrid_hal_client.hal_forms import HALFormsTemplate, HALFormsMethod, HALFormsPropertyType, HALFormsProperty

from contentgrid_extension_helpers.responses.hal import (
    FastAPIHALResponse,
    FastAPIHALCollection,
    HALLinkFor,
    HALTemplateFor,
    get_route_from_app,
    _add_params
)

from fixtures import simple_app, app_with_db

class User(BaseModel):
    id: int
    name: str
    email: str


class UserResponse(FastAPIHALResponse):
    id: int
    name: str
    email: str


class UserCollection(FastAPIHALCollection[UserResponse]):
    total: int = 0


class CreateUserRequest(BaseModel):
    name: str
    email: str

class AdminUserResponse(FastAPIHALResponse):
    """Test admin user with additional fields"""
    id: int
    name: str
    email: str
    role: str
    permissions: list[str] = []

@pytest.fixture(params=["simple_app", "app_with_db"])
def test_app(request, simple_app, app_with_db):
    """Create a FastAPI app for testing - tests both simple_app and app_with_db sequentially"""
    
    # Select the app based on the parameter
    app = simple_app if request.param == "simple_app" else app_with_db
    
    @app.get("/users/{user_id}")
    async def get_user(user_id: int):
        return {"id": user_id, "name": "Test User", "email": "test@example.com"}
    
    @app.get("/users")
    async def list_users(page: int = 1, limit: int = 10):
        return {"users": [], "total": 0}
    
    @app.post("/users")
    async def create_user(user: CreateUserRequest):
        return {"id": 1, "name": user.name, "email": user.email}
    
    @app.put("/users/{user_id}")
    async def update_user(user_id: int, user: CreateUserRequest):
        return {"id": user_id, "name": user.name, "email": user.email}
    
    @app.delete("/users/{user_id}")
    async def delete_user(user_id: int):
        return {"detail": "User deleted"}
    
    return app


@pytest.fixture
def initialized_hal_response(test_app):
    """Initialize FastAPIHALResponse with test app"""
    FastAPIHALResponse.init_app(test_app)
    yield
    # Cleanup - remove app from class
    if hasattr(FastAPIHALResponse, '_app'):
        delattr(FastAPIHALResponse, '_app')
    if hasattr(FastAPIHALResponse, '_server_url'):
        delattr(FastAPIHALResponse, '_server_url')


class TestUtilityFunctions:
    """Test utility functions"""
    
    def test_get_route_from_app_success(self, test_app):
        """Test successful route retrieval"""
        route = get_route_from_app(test_app, "get_user")
        assert route.name == "get_user"
        assert route.path == "/users/{user_id}"
    
    def test_get_route_from_app_not_found(self, test_app):
        """Test route not found error"""
        with pytest.raises(ValueError, match="No route found for endpoint nonexistent"):
            get_route_from_app(test_app, "nonexistent")
    
    def test_add_params_with_params(self):
        """Test URL parameter addition"""
        url = "https://example.com/test"
        params = {"page": "1", "limit": "10"}
        result = _add_params(url, params)
        assert "page=1" in result
        assert "limit=10" in result
        assert result.startswith("https://example.com/test?")
    
    def test_add_params_without_params(self):
        """Test URL without parameters"""
        url = "https://example.com/test"
        result = _add_params(url, None)
        assert result == url
        
        result = _add_params(url, {})
        assert result == url


class TestHALLinkFor:
    """Test HALLinkFor model"""
    
    def test_hal_link_for_creation(self):
        """Test creating HALLinkFor instance"""
        link = HALLinkFor(
            endpoint_function_name="get_user",
            templated=True,
            path_params=lambda user : {"user_id": user.id},
            params={"include": "profile"}
        )
        
        assert link.endpoint_function_name == "get_user"
        assert link.templated is True
        assert callable(link.path_params)
        assert link.params == {"include": "profile"}
    
    def test_hal_link_for_defaults(self):
        """Test HALLinkFor default values"""
        link = HALLinkFor(endpoint_function_name="get_user")
        
        assert link.endpoint_function_name == "get_user"
        assert link.templated is False
        assert link.path_params == {}
        assert link.params == {}
    
    def test_hal_link_for_with_condition(self):
        """Test creating HALLinkFor instance with condition"""
        link = HALLinkFor(
            endpoint_function_name="get_user",
            condition=True
        )
        
        assert link.endpoint_function_name == "get_user"
        assert link.condition is True
        
        # Test with callable condition
        link_callable = HALLinkFor(
            endpoint_function_name="get_user",
            condition=lambda user: user.id > 0
        )
        
        assert callable(link_callable.condition)
        
    def test_hal_link_for_condition_defaults(self):
        """Test HALLinkFor condition default value"""
        link = HALLinkFor(endpoint_function_name="get_user")
        
        assert link.condition is True


class TestHALTemplateFor:
    """Test HALTemplateFor model"""
    
    def test_hal_template_for_creation(self):
        """Test creating HALTemplateFor instance"""
        template = HALTemplateFor(
            endpoint_function_name="create_user",
            path_params={},
            params={}
        )
        
        assert template.endpoint_function_name == "create_user"
    
    def test_hal_template_for_with_condition(self):
        """Test creating HALTemplateFor instance with condition"""
        template = HALTemplateFor(
            endpoint_function_name="create_user",
            condition=False
        )
        
        assert template.endpoint_function_name == "create_user"
        assert template.condition is False
        
        # Test with callable condition
        template_callable = HALTemplateFor(
            endpoint_function_name="create_user",
            condition=lambda user: user.id == 1
        )
        
        assert callable(template_callable.condition)


class TestFastAPIHALResponse:
    """Test FastAPIHALResponse class"""
    
    def test_init_app(self, test_app):
        """Test app initialization"""
        FastAPIHALResponse.init_app(test_app)
        assert hasattr(FastAPIHALResponse, '_app')
        assert FastAPIHALResponse._app == test_app
    
    def test_add_server_url(self):
        """Test server URL setting"""
        server_url = "https://api.example.com"
        FastAPIHALResponse.add_server_url(server_url)
        assert hasattr(FastAPIHALResponse, '_server_url')
        assert FastAPIHALResponse._server_url == server_url
    
    def test_hal_response_creation(self):
        """Test basic HAL response creation"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com"
        )
        
        assert response.id == 1
        assert response.name == "John Doe"
        assert response.email == "john@example.com"
        assert response.links == {}
        assert response.templates is None
    
    def test_hal_response_with_links(self, initialized_hal_response):
        """Test HAL response with links"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _links={
                "self": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                )
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert "_links" in serialized
        assert "self" in serialized["_links"]
        assert  "/users/1" in serialized["_links"]["self"]["href"] 
    
    def test_hal_response_with_server_url(self, initialized_hal_response):
        """Test HAL response with server URL"""
        FastAPIHALResponse.add_server_url("https://api.example.com")
        
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _links={
                "self": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                )
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert serialized["_links"]["self"]["href"] == "https://api.example.com/users/1"
    
    def test_hal_response_with_regular_hal_link(self, initialized_hal_response):
        """Test HAL response with regular HALLink (not HALLinkFor)"""
        regular_link = HALLink(uri="https://example.com/external")
        
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _links={
                "external": regular_link
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert serialized["_links"]["external"]["href"] == "https://example.com/external"
    
    def test_hal_response_with_params(self, initialized_hal_response):
        """Test HAL response with query parameters"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _links={
                "collection": HALLinkFor(
                    endpoint_function_name="list_users",
                    params={"page": 1, "limit": 10}
                )
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        uri = serialized["_links"]["collection"]["href"]
        assert "/users?" in uri
        assert "page=1" in uri
        assert "limit=10" in uri
    
    def test_hal_response_templated_link(self, initialized_hal_response):
        """Test HAL response with templated link"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _links={
                "templated": HALLinkFor(
                    endpoint_function_name="get_user",
                    templated=True
                )
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert serialized["_links"]["templated"]["templated"] is True
        assert serialized["_links"]["templated"]["href"] == "/users/{user_id}"
    
    def test_expand_link_without_app(self):
        """Test link expansion without initialized app"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _links={
                "self": HALLinkFor(endpoint_function_name="get_user")
            }
        )
        
        with pytest.raises(ValueError, match="App not initialized"):
            response.model_dump(by_alias=True)
    
    
    def test_hal_response_with_templates(self, initialized_hal_response):
        """Test HAL response with templates"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _templates={
                "create": HALTemplateFor(endpoint_function_name="create_user")
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert "_templates" in serialized
        assert "create" in serialized["_templates"]
        template = serialized["_templates"]["create"]
        assert template["target"] == "/users"
        assert template["method"] == "POST"
        assert len(template["properties"]) == 2  # name and email fields
        
        # Check properties
        prop_names = [prop["name"] for prop in template["properties"]]
        assert "name" in prop_names
        assert "email" in prop_names
        
    def test_hal_response_with_dynamic_params(self, initialized_hal_response):
        """Test HAL response with dynamic parameters using lambda"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _links={
                "self": HALLinkFor(
                    endpoint_function_name="get_user", 
                    path_params=lambda user : {"user_id": user.id}, 
                    params=lambda x: {"name": x.name, "email": x.email}  # Dynamic params!
                )
            },
            _templates={
                "create": HALTemplateFor(endpoint_function_name="create_user")
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert "_links" in serialized
        assert "self" in serialized["_links"]
        link_href = serialized["_links"]["self"]["href"]
        assert "/users/1?" in link_href
        assert "name=John+Doe" in link_href
        assert "email=john%40example.com" in link_href
        
        assert "_templates" in serialized
        assert "create" in serialized["_templates"]
        template = serialized["_templates"]["create"]
        assert template["target"] == "/users"
        assert template["method"] == "POST"
        assert len(template["properties"]) == 2  # name and email fields
        
        # Check properties
        prop_names = [prop["name"] for prop in template["properties"]]
        assert "name" in prop_names
        assert "email" in prop_names
        
    def test_hal_response_with_template_no_body(self, initialized_hal_response):
        """Test HAL response with template for endpoint without body"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _templates={
                "delete": HALTemplateFor(endpoint_function_name="delete_user", path_params=lambda user : {"user_id": user.id})
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert "_templates" in serialized
        assert "delete" in serialized["_templates"]
        template = serialized["_templates"]["delete"]
        assert template["target"] == "/users/1"
        assert template["method"] == "DELETE"
        assert len(template["properties"]) == 0  # No body, so no properties
        
        
    def test_hal_response_with_advanced_lambda(self, initialized_hal_response):
        """Test HAL response with conditional lambda parameters"""
        
        class FilteredUserResponse(UserResponse):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.links = {
                    "self": HALLinkFor(
                        endpoint_function_name="get_user", 
                        path_params=lambda user : {"user_id": user.id},
                        params=lambda x: {"name": x.name} if x.id > 0 else {}
                    )
                }
        
        # Test with negative ID (should not include params)
        user_negative = FilteredUserResponse(id=-1, name="John", email="john@example.com")
        serialized_negative = user_negative.model_dump(by_alias=True)
        
        assert "_links" in serialized_negative
        assert "self" in serialized_negative["_links"]
        # Should have no query parameters since id <= 0
        assert serialized_negative["_links"]["self"]["href"] == "/users/-1"
        
        # Test with positive ID (should include params)
        user_positive = FilteredUserResponse(id=1, name="Jane", email="jane@example.com")
        serialized_positive = user_positive.model_dump(by_alias=True)
        
        assert "_links" in serialized_positive
        assert "self" in serialized_positive["_links"]
        # Should include name parameter since id > 0
        link_href = serialized_positive["_links"]["self"]["href"]
        assert "/users/1?" in link_href
        assert "name=Jane" in link_href
        
        # Test additional scenarios
        user_zero = FilteredUserResponse(id=0, name="Zero", email="zero@example.com")
        serialized_zero = user_zero.model_dump(by_alias=True)
        # ID is 0, so no params should be added
        assert serialized_zero["_links"]["self"]["href"] == "/users/0"
        
        # Test with higher ID to ensure it works consistently
        user_high = FilteredUserResponse(id=999, name="High User", email="high@example.com")
        serialized_high = user_high.model_dump(by_alias=True)
        link_href_high = serialized_high["_links"]["self"]["href"]
        assert "/users/999?" in link_href_high
        assert "name=High+User" in link_href_high  # URL encoded space
    
    def test_hal_response_with_regular_hal_template(self, initialized_hal_response):
        """Test HAL response with regular HALFormsTemplate"""
        regular_template = HALFormsTemplate(
            title="Custom Template",
            method=HALFormsMethod.PUT,
            target="/custom",
            properties=[]
        )
        
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _templates={
                "custom": regular_template
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert serialized["_templates"]["custom"]["title"] == "Custom Template"
        assert serialized["_templates"]["custom"]["method"] == "PUT"
        assert serialized["_templates"]["custom"]["target"] == "/custom"
    
    def test_template_expansion_with_nonexistent_route(self, initialized_hal_response):
        """Test template expansion with nonexistent route"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _templates={
                "invalid": HALTemplateFor(endpoint_function_name="nonexistent_route")
            }
        )
        
        # Should not raise an error but log an error and skip the template
        with patch('logging.error') as mock_log:
            serialized = response.model_dump(by_alias=True)
            mock_log.assert_called_once()
            assert "invalid" not in serialized["_templates"]
    
    def test_template_with_path_params(self, initialized_hal_response):
        """Test template with path parameters"""
        response = UserResponse(
            id=1,
            name="John Doe",
            email="john@example.com",
            _templates={
                "update": HALTemplateFor(
                    endpoint_function_name="update_user",
                    path_params=lambda user : {"user_id": user.id},
                )
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        template = serialized["_templates"]["update"]
        assert template["target"] == "/users/1"
        assert template["method"] == "PUT"


class TestFastAPIHALCollection:
    """Test FastAPIHALCollection class"""
    
    def test_collection_creation(self):
        """Test creating a typed HAL collection"""
        users = [
            UserResponse(id=1, name="John", email="john@example.com"),
            UserResponse(id=2, name="Jane", email="jane@example.com")
        ]
        
        collection = UserCollection(
            total=2,
            _embedded={"users": users}
        )
        
        assert collection.total == 2
        assert len(collection.embedded["users"]) == 2
        assert collection.embedded["users"][0].name == "John"
    
    def test_collection_serialization(self, initialized_hal_response):
        """Test collection serialization"""
        users = [
            UserResponse(
                id=1, 
                name="John", 
                email="john@example.com",
                _links={
                    "self": HALLinkFor(
                        endpoint_function_name="get_user",
                        path_params=lambda user : {"user_id": user.id},
                    )
                }
            )
        ]
        
        collection = UserCollection(
            total=1,
            _embedded={"users": users},
            _links={
                "self": HALLinkFor(endpoint_function_name="list_users")
            }
        )
        
        serialized = collection.model_dump(by_alias=True)
        assert serialized["total"] == 1
        assert "_embedded" in serialized
        assert "users" in serialized["_embedded"]
        assert len(serialized["_embedded"]["users"]) == 1
        assert "_links" in serialized
        assert "self" in serialized["_links"]
        
        # Check embedded user links are expanded
        user_links = serialized["_embedded"]["users"][0]["_links"]
        assert user_links["self"]["href"] == "/users/1"
    
    def test_empty_collection(self):
        """Test empty collection"""
        collection = UserCollection(total=0)
        
        assert collection.total == 0
        assert collection.embedded is None
        
        serialized = collection.model_dump(by_alias=True)
        assert serialized["total"] == 0
        assert "_embedded" not in serialized or serialized.get("_embedded") is None
    
    def test_collection_with_conditional_links(self, initialized_hal_response):
        """Test collection with conditional links on embedded items"""
        users = [
            UserResponse(
                id=1, 
                name="Regular User", 
                email="user@example.com",
                _links={
                    "self": HALLinkFor(
                        endpoint_function_name="get_user",
                        path_params=lambda user : {"user_id": user.id},
                        condition=True  # Always included
                    ),
                    "admin": HALLinkFor(
                        endpoint_function_name="list_users",
                        condition=lambda user: "Admin" in user.name  # Should be excluded
                    )
                }
            ),
            UserResponse(
                id=2, 
                name="Admin User", 
                email="admin@example.com",
                _links={
                    "self": HALLinkFor(
                        endpoint_function_name="get_user",
                        path_params=lambda user : {"user_id": user.id},
                        condition=True  # Always included
                    ),
                    "admin": HALLinkFor(
                        endpoint_function_name="list_users",
                        condition=lambda user: "Admin" in user.name  # Should be included
                    )
                }
            )
        ]
        
        collection = UserCollection(
            total=2,
            _embedded={"users": users},
            _links={
                "self": HALLinkFor(
                    endpoint_function_name="list_users",
                    condition=True
                )
            }
        )
        
        serialized = collection.model_dump(by_alias=True)
        assert serialized["total"] == 2
        assert "_embedded" in serialized
        assert len(serialized["_embedded"]["users"]) == 2
        
        # Check first user (Regular User) - should have self but not admin link
        user1_links = serialized["_embedded"]["users"][0]["_links"]
        assert "self" in user1_links
        assert "admin" not in user1_links
        
        # Check second user (Admin User) - should have both self and admin links
        user2_links = serialized["_embedded"]["users"][1]["_links"]
        assert "self" in user2_links
        assert "admin" in user2_links
        
        # Check collection links
        assert "_links" in serialized
        assert "self" in serialized["_links"]
    
    def test_collection_with_conditional_templates(self, initialized_hal_response):
        """Test collection with conditional templates"""
        collection = UserCollection(
            total=0,
            _templates={
                "create": HALTemplateFor(
                    endpoint_function_name="create_user",
                    condition=True  # Should be included
                ),
                "bulk_create": HALTemplateFor(
                    endpoint_function_name="create_user",
                    condition=lambda collection: collection.total == 0  # Should be included
                ),
                "archive_all": HALTemplateFor(
                    endpoint_function_name="create_user",  # Using create_user as placeholder
                    condition=lambda collection: collection.total > 100  # Should be excluded
                )
            }
        )
        
        serialized = collection.model_dump(by_alias=True)
        assert "_templates" in serialized
        assert "create" in serialized["_templates"]  # Always included
        assert "bulk_create" in serialized["_templates"]  # total == 0
        assert "archive_all" not in serialized["_templates"]  # total not > 100


class TestConditionalFunctionality:
    """Dedicated tests for condition functionality"""
    
    def test_condition_types(self, initialized_hal_response):
        """Test different condition types: bool, callable"""
        response = UserResponse(
            id=1,
            name="Test User",
            email="test@example.com",
            _links={
                "always": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                    condition=True
                ),
                "never": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                    condition=False
                ),
                "callable_true": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                    condition=lambda user: True
                ),
                "callable_false": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                    condition=lambda user: False
                )
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        links = serialized["_links"]
        
        assert "always" in links
        assert "never" not in links
        assert "callable_true" in links
        assert "callable_false" not in links
    
    def test_condition_with_server_url(self, initialized_hal_response):
        """Test that conditions work correctly with server URLs"""
        FastAPIHALResponse.add_server_url("https://api.example.com")
        
        response = UserResponse(
            id=1,
            name="Test User",
            email="test@example.com",
            _links={
                "included": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                    condition=True
                ),
                "excluded": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                    condition=False
                )
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert "included" in serialized["_links"]
        assert "excluded" not in serialized["_links"]
        assert serialized["_links"]["included"]["href"] == "https://api.example.com/users/1"
    
    def test_condition_with_templated_links(self, initialized_hal_response):
        """Test conditions with templated links"""
        response = UserResponse(
            id=1,
            name="Test User",
            email="test@example.com",
            _links={
                "templated_included": HALLinkFor(
                    endpoint_function_name="get_user",
                    templated=True,
                    condition=True
                ),
                "templated_excluded": HALLinkFor(
                    endpoint_function_name="get_user",
                    templated=True,
                    condition=False
                )
            }
        )
        
        serialized = response.model_dump(by_alias=True)
        assert "templated_included" in serialized["_links"]
        assert "templated_excluded" not in serialized["_links"]
        assert serialized["_links"]["templated_included"]["templated"] is True
    
    def test_condition_inheritance_in_collections(self, initialized_hal_response):
        """Test that conditions work properly in collection hierarchies"""
        user = UserResponse(
            id=1,
            name="Test User",
            email="test@example.com",
            _links={
                "conditional": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                    condition=lambda user: user.id % 2 == 1  # Odd IDs only
                )
            }
        )
        
        collection = UserCollection(
            total=1,
            _embedded={"users": [user]},
            _links={
                "self": HALLinkFor(
                    endpoint_function_name="list_users",
                    condition=lambda collection: collection.total > 0
                )
            }
        )
        
        serialized = collection.model_dump(by_alias=True)
        
        # Collection link should be included (total > 0)
        assert "self" in serialized["_links"]
        
        # User link should be included (id=1 is odd)
        user_links = serialized["_embedded"]["users"][0]["_links"]
        assert "conditional" in user_links
    
    def test_condition_with_multiple_evaluations(self, initialized_hal_response):
        """Test that conditions are evaluated fresh each time"""
        call_count = {"value": 0}
        
        def counting_condition(user):
            call_count["value"] += 1
            return call_count["value"] <= 1  # Only true on first call
        
        response = UserResponse(
            id=1,
            name="Test User",
            email="test@example.com",
            _links={
                "conditional": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                    condition=counting_condition
                )
            }
        )
        
        # First serialization - condition should be True
        serialized1 = response.model_dump(by_alias=True)
        assert "conditional" in serialized1["_links"]
        
        # Reset for second test
        call_count["value"] = 0
        
        # Create new response instance to test fresh evaluation
        response2 = UserResponse(
            id=1,
            name="Test User",
            email="test@example.com",
            _links={
                "conditional": HALLinkFor(
                    endpoint_function_name="get_user",
                    path_params=lambda user : {"user_id": user.id},
                    condition=counting_condition
                )
            }
        )
        
        serialized2 = response2.model_dump(by_alias=True)
        assert "conditional" in serialized2["_links"]  # Should still be true on fresh instance
    
    def test_condition_performance_with_many_links(self, initialized_hal_response):
        """Test performance with many conditional links"""
        links = {}
        for i in range(100):
            # Need to capture i in the lambda closure properly
            links[f"link_{i}"] = HALLinkFor(
                endpoint_function_name="get_user",
                path_params=lambda user, idx=i: {"user_id": user.id + idx},
                condition=lambda user, idx=i: idx % 2 == 0  # Only even indices
            )
        
        response = UserResponse(
            id=1,
            name="Test User",
            email="test@example.com",
            _links=links
        )
        
        serialized = response.model_dump(by_alias=True)
        included_links = serialized["_links"]
        
        # Should have 50 links (even indices 0, 2, 4, ..., 98)
        assert len(included_links) == 50
        
        # Check that only even-indexed links are included
        for key in included_links.keys():
            index = int(key.split("_")[1])
            assert index % 2 == 0


class TestIntegration:
    """Integration tests with FastAPI"""
    
    def test_hal_response_in_fastapi_endpoint(self, test_app, initialized_hal_response):
        """Test HAL response in actual FastAPI endpoint"""
        
        @test_app.get("/hal-user/{user_id}", response_model=UserResponse)
        async def get_hal_user(user_id: int):
            return UserResponse(
                id=user_id,
                name="Test User",
                email="test@example.com",
                _links={
                    "self": HALLinkFor(
                        endpoint_function_name="get_user",
                        path_params=lambda user : {"user_id": user.id},
                    )
                }
            )
        
        client = TestClient(test_app)
        response = client.get("/hal-user/123")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 123
        assert data["name"] == "Test User"
        assert "_links" in data
        assert data["_links"]["self"]["href"] == "/users/123"
    
    def test_hal_collection_in_fastapi_endpoint(self, test_app, initialized_hal_response):
        """Test HAL collection in actual FastAPI endpoint"""
        
        @test_app.get("/hal-users", response_model=UserCollection)
        async def get_hal_users():
            users = [
                UserResponse(
                    id=1,
                    name="User 1",
                    email="user1@example.com",
                    _links={
                        "self": HALLinkFor(
                            endpoint_function_name="get_user",
                            path_params=lambda user : {"user_id": user.id},
                        )
                    }
                )
            ]
            return UserCollection(
                total=1,
                _embedded={"users": users},
                _links={
                    "self": HALLinkFor(endpoint_function_name="list_users")
                }
            )
        
        client = TestClient(test_app)
        response = client.get("/hal-users")
        
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1
        assert "_embedded" in data
        assert len(data["_embedded"]["users"]) == 1
        assert data["_embedded"]["users"][0]["_links"]["self"]["href"] == "/users/1"
        assert data["_links"]["self"]["href"] == "/users"
    
    def test_hal_response_in_fastapi_endpoint_with_conditions(self, test_app, initialized_hal_response):
        """Test HAL response with conditions in actual FastAPI endpoint"""
        
        @test_app.get("/conditional-user/{user_id}", response_model=UserResponse)
        async def get_conditional_user(user_id: int):
            return UserResponse(
                id=user_id,
                name="Test User" if user_id <= 10 else "Admin User",
                email="test@example.com",
                _links={
                    "self": HALLinkFor(
                        endpoint_function_name="get_user",
                        path_params=lambda user : {"user_id": user.id},
                        condition=True  # Always included
                    ),
                    "admin": HALLinkFor(
                        endpoint_function_name="list_users",
                        condition=lambda user: user.id > 10  # Only for admin users
                    )
                },
                _templates={
                    "edit": HALTemplateFor(
                        endpoint_function_name="update_user",
                        path_params=lambda user : {"user_id": user.id},
                        condition=lambda user: user.id <= 10  # Only for regular users
                    )
                }
            )
        
        client = TestClient(test_app)
        
        # Test regular user (id <= 10)
        response = client.get("/conditional-user/5")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 5
        assert data["name"] == "Test User"
        assert "_links" in data
        assert "self" in data["_links"]
        assert "admin" not in data["_links"]  # Should be excluded
        assert "_templates" in data
        assert "edit" in data["_templates"]  # Should be included
        
        # Test admin user (id > 10)
        response = client.get("/conditional-user/15")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 15
        assert data["name"] == "Admin User"
        assert "_links" in data
        assert "self" in data["_links"]
        assert "admin" in data["_links"]  # Should be included
        assert "_templates" in data
        assert "edit" not in data["_templates"]  # Should be excluded
    
    def test_hal_collection_with_dynamic_conditions(self, test_app, initialized_hal_response):
        """Test HAL collection with dynamic conditions based on collection state"""
        
        @test_app.get("/dynamic-users", response_model=UserCollection)
        async def get_dynamic_users(include_admin: bool = False):
            users = []
            if include_admin:
                users.append(UserResponse(
                    id=1,
                    name="Admin User",
                    email="admin@example.com",
                    _links={
                        "self": HALLinkFor(
                            endpoint_function_name="get_user",
                            path_params=lambda user : {"user_id": user.id}
                        )
                    }
                ))
            
            return UserCollection(
                total=len(users),
                _embedded={"users": users} if users else None,
                _links={
                    "self": HALLinkFor(
                        endpoint_function_name="list_users",
                        condition=True
                    )
                },
                _templates={
                    "create": HALTemplateFor(
                        endpoint_function_name="create_user",
                        condition=True
                    ),
                    "admin_create": HALTemplateFor(
                        endpoint_function_name="create_user",
                        condition=lambda collection: collection.total > 0  # Only if users exist
                    )
                }
            )
        
        client = TestClient(test_app)
        
        # Test empty collection
        response = client.get("/dynamic-users?include_admin=false")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 0
        assert "_templates" in data
        assert "create" in data["_templates"]
        assert "admin_create" not in data["_templates"]  # No users, so excluded
        
        # Test non-empty collection
        response = client.get("/dynamic-users?include_admin=true")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1
        assert "_templates" in data
        assert "create" in data["_templates"]
        assert "admin_create" in data["_templates"]  # Has users, so included

class TestHALJSONSchemaGeneration:
    """Test JSON schema generation for HAL response classes"""
    
    def test_basic_hal_response_schema(self):
        """Test JSON schema for basic HAL response"""
        schema = UserResponse.model_json_schema(by_alias=True)
        
        # Check basic structure
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        properties = schema["properties"]
        
        # Check user-defined properties
        assert "id" in properties
        assert "name" in properties
        assert "email" in properties
        
        assert properties["id"]["type"] == "integer"
        assert properties["name"]["type"] == "string"
        assert properties["email"]["type"] == "string"
        
        # Check HAL-specific properties
        assert "_links" in properties
        assert properties["_links"]["type"] == "object"
        
        # _templates should be present and nullable
        assert "_templates" in properties
        templates_prop = properties["_templates"]
        assert "anyOf" in templates_prop or "type" in templates_prop
        # Should allow null values
        if "anyOf" in templates_prop:
            types = [item.get("type") for item in templates_prop["anyOf"]]
            assert "null" in types
    
    def test_hal_response_with_additional_fields_schema(self):
        """Test JSON schema for HAL response with additional fields"""
        schema = AdminUserResponse.model_json_schema(by_alias=True)
        
        properties = schema["properties"]
        
        # Check all fields are present (use actual field names from schema)
        expected_user_fields = ["id", "name", "email", "role", "permissions"]
        for field in expected_user_fields:
            assert field in properties
        
        # Check HAL fields
        assert "_links" in properties
        assert "_templates" in properties
        
        # Check specific field types
        assert properties["role"]["type"] == "string"
        assert properties["permissions"]["type"] == "array"
        assert properties["permissions"]["items"]["type"] == "string"
        
        # Check default values in schema
        if "default" in properties["permissions"]:
            assert properties["permissions"]["default"] == []
    
    def test_hal_collection_schema(self):
        """Test JSON schema for HAL collection"""
        schema = UserCollection.model_json_schema(by_alias=True)
        
        properties = schema["properties"]
        
        # Check collection-specific properties
        assert "total" in properties
        assert properties["total"]["type"] == "integer"
        
        # Check embedded property
        assert "_embedded" in properties
        embedded_prop = properties["_embedded"]
        
        # Should be nullable object
        if "anyOf" in embedded_prop:
            types = [item.get("type") for item in embedded_prop["anyOf"]]
            assert "null" in types
            assert "object" in types
        
        # Check HAL properties are inherited
        assert "_links" in properties
        assert "_templates" in properties
    
    def test_nested_schema_definitions(self):
        """Test that nested schemas are properly defined"""
        schema = UserCollection.model_json_schema(by_alias=True)
        
        # Should have definitions/defs section for nested models
        defs_key = "$defs" if "$defs" in schema else "definitions"
        if defs_key in schema:
            defs = schema[defs_key]
            
            # Should include UserResponse definition
            user_response_def = None
            for def_name, def_schema in defs.items():
                if "properties" in def_schema and "id" in def_schema["properties"]:
                    user_response_def = def_schema
                    break
            
            if user_response_def:
                assert "id" in user_response_def["properties"]
                assert "name" in user_response_def["properties"]
                # Check for HAL fields
                assert "_links" in user_response_def["properties"]
    
    def test_schema_with_required_fields(self):
        """Test that required fields are properly marked in schema"""
        schema = UserResponse.model_json_schema(by_alias=True)
        
        # Check required fields
        required_fields = schema.get("required", [])
        
        # User-defined fields should be required (unless they have defaults)
        assert "id" in required_fields
        assert "name" in required_fields
        assert "email" in required_fields
        
        # HAL fields might not be required if they have defaults
        # This is implementation dependent, so we just check they exist in properties
        properties = schema["properties"]
        assert "_links" in properties
        assert "_templates" in properties
    
    def test_schema_field_descriptions(self):
        """Test that field descriptions are included in schema"""
        schema = UserCollection.model_json_schema(by_alias=True)
        
        properties = schema["properties"]
        
        # Check if embedded field has description
        if "_embedded" in properties and "description" in properties["_embedded"]:
            assert "Embedded resources" in properties["_embedded"]["description"]
    
    def test_schema_aliases(self):
        """Test that field aliases are properly handled in schema"""
        schema = UserResponse.model_json_schema(by_alias=True)
        
        properties = schema["properties"]
        
        # The actual behavior might vary - check what's actually there
        # Either aliases are used or original names, but HAL fields should be present
        has_links = "_links" in properties
        has_templates = "_templates" in properties
        
        assert has_links, "No links field found in schema"
        assert has_templates, "No templates field found in schema"
        
        # Check that we don't have both versions
        assert not ("links" in properties and "_links" in properties), "Both links and _links present"
        assert not ("templates" in properties and "_templates" in properties), "Both templates and _templates present"
    
    def test_schema_with_inheritance(self):
        """Test schema generation with class inheritance"""
        # Test that inherited HAL properties are present
        schema = AdminUserResponse.model_json_schema(by_alias=True)
        
        properties = schema["properties"]
        
        # Should have user properties
        user_properties = ["id", "name", "email"]
        admin_properties = ["role", "permissions"]
        
        all_user_properties = user_properties + admin_properties
        for prop in all_user_properties:
            assert prop in properties, f"Property {prop} missing from schema"
        
        # Should have HAL properties
        assert "_links" in properties
        assert "_templates" in properties
    
    def test_schema_title_and_metadata(self):
        """Test that schema includes proper title and metadata"""
        schema = UserResponse.model_json_schema(by_alias=True)
        
        # Should have a title
        assert "title" in schema
        assert schema["title"] == "UserResponse"
        
        # Check collection schema
        collection_schema = UserCollection.model_json_schema(by_alias=True)
        assert "title" in collection_schema
        assert collection_schema["title"] == "UserCollection"
    
    def test_schema_for_generic_collection(self):
        """Test schema generation for generic typed collection"""
        schema = UserCollection.model_json_schema(by_alias=True)
        
        # Should handle generic typing properly
        assert "type" in schema
        assert schema["type"] == "object"
        
        # Should not have issues with Generic[T] parameter
        properties = schema["properties"]
        # Check for embedded field
        assert "_embedded" in properties, "No embedded field found in collection schema"
    
    def test_multiple_hal_classes_schema_independence(self):
        """Test that different HAL classes generate independent schemas"""
        user_schema = UserResponse.model_json_schema(by_alias=True)
        admin_schema = AdminUserResponse.model_json_schema(by_alias=True)
        collection_schema = UserCollection.model_json_schema(by_alias=True)
        
        # Should have different titles
        assert user_schema["title"] != admin_schema["title"]
        assert user_schema["title"] != collection_schema["title"]
        assert admin_schema["title"] != collection_schema["title"]
        
        # Should have different required fields
        user_required = set(user_schema.get("required", []))
        admin_required = set(admin_schema.get("required", []))
        collection_required = set(collection_schema.get("required", []))
        
        # Admin should have more or equal required fields than user
        # (some fields might have defaults and not be required)
        assert len(admin_required) >= len(user_required) or len(admin_required) == len(user_required)
        
        # Check that schemas have different properties
        user_props = set(user_schema["properties"].keys())
        admin_props = set(admin_schema["properties"].keys())
        collection_props = set(collection_schema["properties"].keys())
        
        # Admin should have additional properties
        assert "role" in admin_props
        assert "permissions" in admin_props
        assert "role" not in user_props
        assert "permissions" not in user_props
        
        # Collection should have total property
        assert "total" in collection_props
        assert "total" not in user_props
        assert "total" not in admin_props
    
    def test_schema_validation_compatibility(self):
        """Test that generated schemas are compatible with JSON Schema validation"""
        schemas = [
            UserResponse.model_json_schema(by_alias=True),
            AdminUserResponse.model_json_schema(by_alias=True),
            UserCollection.model_json_schema(by_alias=True)
        ]
        
        for schema in schemas:
            # Basic JSON Schema structure
            assert "type" in schema
            assert "properties" in schema
            
            # All properties should have types defined
            for prop_name, prop_def in schema["properties"].items():
                assert "type" in prop_def or "anyOf" in prop_def or "$ref" in prop_def, \
                    f"Property {prop_name} missing type definition"
    
    def test_schema_embedded_objects_have_correct_hal_fields(self):
        """Test that embedded objects in collections have correct HAL schema definitions"""
        schema = UserCollection.model_json_schema(by_alias=True)
        
        properties = schema["properties"]
        
        # Check that _embedded field exists
        assert "_embedded" in properties
        embedded_prop = properties["_embedded"]
        
        # Check that it's properly defined as nullable object
        assert "anyOf" in embedded_prop
        any_of_types = embedded_prop["anyOf"]
        
        # Should have null type and object type
        type_values = [item.get("type") for item in any_of_types if "type" in item]
        assert "null" in type_values
        assert "object" in type_values
        
        # Find the object definition (not the null one)
        object_def = None
        for item in any_of_types:
            if item.get("type") == "object":
                object_def = item
                break
        
        assert object_def is not None, "No object definition found in _embedded anyOf"
        
        # Check that object has properties with pattern properties or additionalProperties
        # Since _embedded can contain different resource types, it should allow flexible structure
        has_pattern_properties = "patternProperties" in object_def
        has_additional_properties = "additionalProperties" in object_def
        has_properties = "properties" in object_def
        
        # At least one of these should be present to define the structure
        assert has_pattern_properties or has_additional_properties or has_properties, \
            "Object definition should have properties, patternProperties, or additionalProperties"
        
        # If using definitions/defs, check that UserResponse is properly defined there
        defs_key = "$defs" if "$defs" in schema else "definitions"
        if defs_key in schema:
            defs = schema[defs_key]
            
            # Find UserResponse definition
            user_response_def = None
            for def_name, def_schema in defs.items():
                # Look for a definition that has the UserResponse structure
                if ("properties" in def_schema and 
                    "id" in def_schema.get("properties", {}) and
                    "name" in def_schema.get("properties", {}) and
                    "email" in def_schema.get("properties", {})):
                    user_response_def = def_schema
                    break
            
            if user_response_def:
                user_props = user_response_def["properties"]
                
                # Verify that the embedded UserResponse has all expected fields
                assert "id" in user_props
                assert "name" in user_props  
                assert "email" in user_props
                
                # Most importantly, verify HAL fields are present with correct aliases
                assert "_links" in user_props, "Embedded UserResponse should have _links field"
                assert "_templates" in user_props, "Embedded UserResponse should have _templates field"
                
                # Verify the HAL field types
                assert user_props["_links"]["type"] == "object"
                
                # _templates should be nullable
                templates_def = user_props["_templates"]
                if "anyOf" in templates_def:
                    template_types = [item.get("type") for item in templates_def["anyOf"]]
                    assert "null" in template_types
                    assert "object" in [item.get("type") for item in templates_def["anyOf"] if item.get("type") != "null"]
                
                # Verify user fields have correct types
                assert user_props["id"]["type"] == "integer"
                assert user_props["name"]["type"] == "string"
                assert user_props["email"]["type"] == "string"
    
    def test_schema_openapi_compatibility(self, test_app):
        """Test that schemas work with FastAPI OpenAPI generation"""
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        
        # Add endpoints with HAL response models
        @test_app.get("/test-user", response_model=UserResponse)
        async def test_user():
            return {"id": 1, "name": "Test", "email": "test@example.com"}
        
        @test_app.get("/test-collection", response_model=UserCollection)
        async def test_collection():
            return {"total": 0}
        
        # Should be able to generate OpenAPI schema without errors
        openapi_schema = test_app.openapi()
        
        assert "paths" in openapi_schema
        assert "/test-user" in openapi_schema["paths"]
        assert "/test-collection" in openapi_schema["paths"]
        
        # Check that response schemas are included
        assert "components" in openapi_schema
        assert "schemas" in openapi_schema["components"]
        
        schemas = openapi_schema["components"]["schemas"]
        
        # Should include our HAL response schemas
        schema_names = list(schemas.keys())
        assert any("UserResponse" in name for name in schema_names)
        assert any("UserCollection" in name for name in schema_names)


if __name__ == "__main__":
    pytest.main([__file__])