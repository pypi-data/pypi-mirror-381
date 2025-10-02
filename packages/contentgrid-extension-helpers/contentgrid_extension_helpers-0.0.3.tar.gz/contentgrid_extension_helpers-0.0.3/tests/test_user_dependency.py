import pytest
import os
from unittest.mock import Mock, patch, MagicMock
from typing import List, Optional
from pydantic import BaseModel, Field

from contentgrid_extension_helpers.dependencies.authentication.user import (
    ContentGridUserDependency,
    ContentGridUserConfig
)
from contentgrid_extension_helpers.authentication.user import ContentGridUser


# Custom user models for testing
class CustomUser(BaseModel):
    sub: str
    iss: str
    exp: float
    name: str | None = None
    email: str | None = None
    access_token: str
    role: str = "user"
    permissions: List[str] = []


class AdminUser(BaseModel):
    sub: str
    iss: str
    exp: float
    name: str | None = None
    email: str | None = None
    access_token: str
    role: str = "admin"
    is_super_admin: bool = False


class MinimalUser(BaseModel):
    sub: str
    access_token: str


@pytest.fixture
def mock_jwks_client():
    """Mock JWKS client for testing."""
    return Mock()


@pytest.fixture
def mock_user_dependency():
    """Mock user dependency function."""
    async def mock_dependency(token: str):
        return ContentGridUser(
            sub="test-user",
            iss="test-issuer",
            exp=1234567890,
            name="Test User",
            email="test@example.com",
            access_token=token,
            domains=["test.domain.com"],
            application_id="test-app-id"
        )
    return mock_dependency


@pytest.fixture
def env_vars():
    """Set up environment variables for testing."""
    original_env = os.environ.copy()
    test_env = {
        "EXTENSION_NAME": "test-extension",
        "OAUTH_ISSUER": "https://test-issuer.com",
        "EXTENSION_AUTH_URL": "https://test-auth.com"
    }
    os.environ.update(test_env)
    yield test_env
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


class TestContentGridUserConfig:
    """Test ContentGridUserConfig class."""
    
    def test_config_with_env_vars(self, env_vars):
        """Test config creation with environment variables."""
        config = ContentGridUserConfig()
        assert config.extension_name == "test-extension"
        assert config.oauth_issuer == "https://test-issuer.com"
        assert config.extension_auth_url == "https://test-auth.com"
    
    def test_config_with_explicit_values(self):
        """Test config creation with explicit values."""
        config = ContentGridUserConfig(
            extension_name="explicit-extension",
            oauth_issuer="https://explicit-issuer.com",
            extension_auth_url="https://explicit-auth.com"
        )
        assert config.extension_name == "explicit-extension"
        assert config.oauth_issuer == "https://explicit-issuer.com"
        assert config.extension_auth_url == "https://explicit-auth.com"


class TestContentGridUserDependency:
    """Test ContentGridUserDependency class."""
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    def test_init_with_defaults(self, mock_create_dependency, mock_get_jwks, env_vars):
        """Test initialization with default parameters."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        mock_create_dependency.return_value = Mock()
        
        dependency = ContentGridUserDependency()
        
        assert dependency.user_model == ContentGridUser
        assert dependency.audience == "contentgrid:extension:test-extension"
        mock_get_jwks.assert_called_once_with("https://test-issuer.com")
        mock_create_dependency.assert_called_once()
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    def test_init_with_custom_parameters(self, mock_create_dependency, mock_get_jwks):
        """Test initialization with custom parameters."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        mock_create_dependency.return_value = Mock()
        
        dependency = ContentGridUserDependency(
            extension_name="custom-extension",
            oauth_issuer="https://custom-issuer.com",
            custom_audience="custom:audience",
            user_model=CustomUser,
            algorithms=["RS256", "ES256"],
            verify_exp=False,
            verify_aud=False,
            verify_iss=False,
            verify_nbf=True,
            verify_iat=True
        )
        
        assert dependency.user_model == CustomUser
        assert dependency.audience == "custom:audience"
        mock_get_jwks.assert_called_once_with("https://custom-issuer.com")
        mock_create_dependency.assert_called_once_with(
            jwks_client=mock_jwks_client,
            oidc_issuer="https://custom-issuer.com",
            audience="custom:audience",
            user_model=CustomUser,
            algorithms=["RS256", "ES256"],
            verify_exp=False,
            verify_aud=False,
            verify_iss=False,
            verify_nbf=True,
            verify_iat=True
        )
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    def test_config_property(self, mock_create_dependency, mock_get_jwks, env_vars):
        """Test config property returns the user config."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        mock_create_dependency.return_value = Mock()
        
        dependency = ContentGridUserDependency()
        config = dependency.config
        
        assert isinstance(config, ContentGridUserConfig)
        assert config.extension_name == "test-extension"
        assert config.oauth_issuer == "https://test-issuer.com"
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    @pytest.mark.asyncio
    async def test_call_returns_correct_user_type(self, mock_create_dependency, mock_get_jwks):
        """Test that __call__ returns the correct user model type."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        
        # Create a custom user instance that will be returned by the dependency
        custom_user = CustomUser(
            sub="test-user",
            iss="test-issuer",
            exp=1234567890,
            name="Test User",
            email="test@example.com",
            access_token="test-token",
            role="admin",
            permissions=["read", "write"]
        )
        
        async def mock_dependency_func(token: str):
            return custom_user
        
        mock_create_dependency.return_value = mock_dependency_func
        
        dependency = ContentGridUserDependency[CustomUser](
            extension_name="test-extension",
            oauth_issuer="https://test-issuer.com",
            user_model=CustomUser
        )
        
        result = await dependency("test-token")
        
        assert isinstance(result, CustomUser)
        assert result.sub == "test-user"
        assert result.role == "admin"
        assert result.permissions == ["read", "write"]
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    @pytest.mark.asyncio
    async def test_call_with_contentgrid_user(self, mock_create_dependency, mock_get_jwks, env_vars):
        """Test that __call__ works with default ContentGridUser."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        
        # Create a ContentGridUser instance
        content_grid_user = ContentGridUser(
            **{
                "sub": "test-user",
                "aud": "contentgrid:extension:extract",
                "restrict:principal_claims": "24ZPEGV0IS5MAF8C2BjmaqH1p7wL4YS409zlL8ZE+nEUHsFFDu80eDpJXoFvZIb1Hh9bxamGaK0gE14wvA+btCuDrg5lkGcdCVj3zm/RWnIFKzlGUVn7Zkj4z4PCzsq/itKVNXEYBtAS/d0NRFSiZGvy775kFdK1VOi+hxsic1bHAZTvSs1jEFuddxEULExh2MqZ5h43n/vEhB0sxkmXevR7XSE4iolDzCWGrw6HzUZYP/QlSlz/S3cK+aeoShAP1G2SbuTGub5h1fsKMM22eg==",
                "iss": "https://extensions.sandbox.contentgrid.cloud/authentication/external",
                "may_act": {
                    "sub": "extract",
                    "iss": "https://auth.sandbox.contentgrid.cloud/realms/extensions"
                },
                "context:application:domains": [
                    "test.domain.com"
                ],
                "exp": 1234567890,
                "context:application:id": "test-app-id",
                "access_token" : "test-token",
            }
        )
        
        async def mock_dependency_func(token: str):
            return content_grid_user
        
        mock_create_dependency.return_value = mock_dependency_func
        
        dependency = ContentGridUserDependency()
        
        result = await dependency("test-token")
        
        assert isinstance(result, ContentGridUser)
        assert result.sub == "test-user"
        assert result.domains == ["test.domain.com"]
        assert result.application_id == "test-app-id"
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    @pytest.mark.asyncio
    async def test_call_with_minimal_user(self, mock_create_dependency, mock_get_jwks):
        """Test that __call__ works with a minimal user model."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        
        # Create a minimal user instance
        minimal_user = MinimalUser(
            sub="test-user",
            access_token="test-token"
        )
        
        async def mock_dependency_func(token: str):
            return minimal_user
        
        mock_create_dependency.return_value = mock_dependency_func
        
        dependency = ContentGridUserDependency[MinimalUser](
            extension_name="test-extension",
            oauth_issuer="https://test-issuer.com",
            user_model=MinimalUser
        )
        
        result = await dependency("test-token")
        
        assert isinstance(result, MinimalUser)
        assert result.sub == "test-user"
        assert result.access_token == "test-token"
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    @pytest.mark.asyncio
    async def test_call_with_admin_user(self, mock_create_dependency, mock_get_jwks):
        """Test that __call__ works with an admin user model."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        
        # Create an admin user instance
        admin_user = AdminUser(
            sub="admin-user",
            iss="test-issuer",
            exp=1234567890,
            name="Admin User",
            email="admin@example.com",
            access_token="admin-token",
            role="admin",
            is_super_admin=True
        )
        
        async def mock_dependency_func(token: str):
            return admin_user
        
        mock_create_dependency.return_value = mock_dependency_func
        
        dependency = ContentGridUserDependency[AdminUser](
            extension_name="test-extension",
            oauth_issuer="https://test-issuer.com",
            user_model=AdminUser
        )
        
        result = await dependency("admin-token")
        
        assert isinstance(result, AdminUser)
        assert result.sub == "admin-user"
        assert result.role == "admin"
        assert result.is_super_admin is True


class TestContentGridUserDependencyGenericTyping:
    """Test the generic typing functionality of ContentGridUserDependency."""
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    def test_generic_type_parameter(self, mock_create_dependency, mock_get_jwks):
        """Test that the generic type parameter is correctly handled."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        mock_create_dependency.return_value = Mock()
        
        # Test with CustomUser type parameter
        dependency = ContentGridUserDependency[CustomUser](
            extension_name="test-extension",
            oauth_issuer="https://test-issuer.com",
            user_model=CustomUser
        )
        
        assert dependency.user_model == CustomUser
        
        # Verify the create_current_user_dependency was called with CustomUser
        call_args = mock_create_dependency.call_args
        assert call_args[1]['user_model'] == CustomUser
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    def test_default_user_model_without_type_parameter(self, mock_create_dependency, mock_get_jwks, env_vars):
        """Test that default user model is used when no type parameter is provided."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        mock_create_dependency.return_value = Mock()
        
        # Test without type parameter
        dependency = ContentGridUserDependency()
        
        assert dependency.user_model == ContentGridUser
        
        # Verify the create_current_user_dependency was called with ContentGridUser
        call_args = mock_create_dependency.call_args
        assert call_args[1]['user_model'] == ContentGridUser


class TestContentGridUserDependencyErrorHandling:
    """Test error handling in ContentGridUserDependency."""
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    def test_jwks_client_error(self, mock_get_jwks):
        """Test that JWKS client errors are properly propagated."""
        mock_get_jwks.side_effect = Exception("JWKS client error")
        
        with pytest.raises(Exception, match="JWKS client error"):
            ContentGridUserDependency(
                extension_name="test-extension",
                oauth_issuer="https://test-issuer.com"
            )
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    @pytest.mark.asyncio
    async def test_user_dependency_error(self, mock_create_dependency, mock_get_jwks):
        """Test that user dependency errors are properly propagated."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        
        async def failing_dependency(token: str):
            raise Exception("User dependency error")
        
        mock_create_dependency.return_value = failing_dependency
        
        dependency = ContentGridUserDependency(
            extension_name="test-extension",
            oauth_issuer="https://test-issuer.com"
        )
        
        with pytest.raises(Exception, match="User dependency error"):
            await dependency("test-token")


class TestTypingExamples:
    """Examples showing how the improved typing works in practice."""
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    def test_typing_example_default_user(self, mock_create_dependency, mock_get_jwks, env_vars):
        """Example: Using default ContentGridUser type."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        mock_create_dependency.return_value = Mock()
        
        # Default usage - returns ContentGridUser
        user_dependency = ContentGridUserDependency()
        
        # Type checkers will know this returns ContentGridUser
        assert user_dependency.user_model == ContentGridUser
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    def test_typing_example_custom_user(self, mock_create_dependency, mock_get_jwks):
        """Example: Using a custom user type with explicit generic parameter."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        mock_create_dependency.return_value = Mock()
        
        # Custom user with type parameter - returns CustomUser
        user_dependency = ContentGridUserDependency[CustomUser](
            extension_name="my-extension",
            oauth_issuer="https://my-issuer.com",
            user_model=CustomUser
        )
        
        # Type checkers will know this returns CustomUser
        assert user_dependency.user_model == CustomUser
    
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.get_oauth_jwks_client')
    @patch('contentgrid_extension_helpers.dependencies.authentication.user.create_current_user_dependency')
    def test_typing_example_admin_user(self, mock_create_dependency, mock_get_jwks):
        """Example: Using AdminUser type for role-based authentication."""
        mock_config = {"jwks_uri": "https://test.com/jwks"}
        mock_jwks_client = Mock()
        mock_get_jwks.return_value = (mock_config, mock_jwks_client)
        mock_create_dependency.return_value = Mock()
        
        # Admin user type - returns AdminUser with admin-specific fields
        admin_dependency = ContentGridUserDependency[AdminUser](
            extension_name="admin-extension",
            oauth_issuer="https://admin-issuer.com",
            user_model=AdminUser
        )
        
        # Type checkers will know this returns AdminUser with is_super_admin field
        assert admin_dependency.user_model == AdminUser


if __name__ == "__main__":
    pytest.main([__file__])
