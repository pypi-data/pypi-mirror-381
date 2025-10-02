import pytest
import os
from unittest.mock import Mock, patch, MagicMock, call
from typing import Optional
from pydantic import HttpUrl

from contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory import (
    ContentGridExtensionFlowClientFactory,
    ExtensionFlowConfig
)
from contentgrid_extension_helpers.dependencies.authentication.user import ContentGridUserDependency
from contentgrid_extension_helpers.authentication.user import ContentGridUser
from contentgrid_application_client.application import ContentGridApplicationClient
from contentgrid_hal_client.security import IdentityAuthenticationManager


@pytest.fixture
def mock_user_dependency():
    """Mock user dependency."""
    return Mock(spec=ContentGridUserDependency)


@pytest.fixture
def sample_contentgrid_user():
    """Sample ContentGridUser for testing."""
    return ContentGridUser(
        **{
            "sub":"test-user",
            "iss":"test-issuer",
            "exp":1234567890,
            "name":"Test User",
            "email":"test@example.com",
            "access_token":"test-access-token",
            "context:application:domains":["test.domain.com", "another.domain.com"],
            "context:application:id":"test-app-id"
        }
    )


@pytest.fixture
def env_vars():
    """Set up environment variables for testing."""
    original_env = os.environ.copy()
    test_env = {
        "EXTENSION_CLIENT_NAME": "test-client",
        "EXTENSION_CLIENT_SECRET": "test-secret",
        "SYSTEM_EXCHANGE_URI": "https://test-system.com/token",
        "EXTENSION_AUTH_URL": "https://test-auth.com/token",
        "DELEGATED_EXCHANGE_URI": "https://test-delegated.com/token"
    }
    os.environ.update(test_env)
    yield test_env
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


class TestExtensionFlowConfig:
    """Test ExtensionFlowConfig class."""
    
    def test_config_with_env_vars(self, env_vars):
        """Test config creation with environment variables."""
        config = ExtensionFlowConfig()
        assert config.extension_client_name == "test-client"
        assert config.extension_client_secret == "test-secret"
        assert config.system_exchange_uri == "https://test-system.com/token"
        assert config.extension_auth_url == "https://test-auth.com/token"
        assert config.delegated_exchange_uri == "https://test-delegated.com/token"
    
    def test_config_with_explicit_values(self):
        """Test config creation with explicit values."""
        config = ExtensionFlowConfig(
            extension_client_name="explicit-client",
            extension_client_secret="explicit-secret",
            system_exchange_uri="https://explicit-system.com/token",
            extension_auth_url="https://explicit-auth.com/token",
            delegated_exchange_uri="https://explicit-delegated.com/token"
        )
        assert config.extension_client_name == "explicit-client"
        assert config.extension_client_secret == "explicit-secret"
        assert config.system_exchange_uri == "https://explicit-system.com/token"
        assert config.extension_auth_url == "https://explicit-auth.com/token"
        assert config.delegated_exchange_uri == "https://explicit-delegated.com/token"


class TestContentGridExtensionFlowClientFactory:
    """Test ContentGridExtensionFlowClientFactory class."""
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_init_with_defaults(self, mock_identity_auth_manager, env_vars, mock_user_dependency):
        """Test initialization with default parameters."""
        mock_auth_manager_instance = Mock()
        mock_identity_auth_manager.return_value = mock_auth_manager_instance
        
        factory = ContentGridExtensionFlowClientFactory(
        )
        
        assert factory.extension_config.extension_client_name == "test-client"
        assert factory.extension_config.extension_client_secret == "test-secret"
        assert factory.identity_auth_manager == mock_auth_manager_instance
        
        # Verify IdentityAuthenticationManager was initialized correctly
        mock_identity_auth_manager.assert_called_once_with(
            auth_uri="https://test-auth.com/token",
            client_id="test-client",
            client_secret="test-secret",
            system_exchange_uri="https://test-system.com/token",
            delegated_exchange_uri="https://test-delegated.com/token"
        )
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_init_with_custom_parameters(self, mock_identity_auth_manager):
        """Test initialization with custom parameters."""
        mock_auth_manager_instance = Mock()
        mock_identity_auth_manager.return_value = mock_auth_manager_instance
        mock_user_dependency = Mock()
        
        factory = ContentGridExtensionFlowClientFactory(
            extension_auth_url="https://custom-auth.com/token",
            extension_client_name="custom-client",
            extension_client_secret="custom-secret",
            system_exchange_uri="https://custom-system.com/token",
            delegated_exchange_uri="https://custom-delegated.com/token"
        )
        
        assert factory.extension_config.extension_auth_url == "https://custom-auth.com/token"
        assert factory.extension_config.extension_client_name == "custom-client"
        assert factory.extension_config.extension_client_secret == "custom-secret"
        assert factory.extension_config.system_exchange_uri == "https://custom-system.com/token"
        assert factory.extension_config.delegated_exchange_uri == "https://custom-delegated.com/token"
        
        # Verify IdentityAuthenticationManager was initialized with custom values
        mock_identity_auth_manager.assert_called_once_with(
            auth_uri="https://custom-auth.com/token",
            client_id="custom-client",
            client_secret="custom-secret",
            system_exchange_uri="https://custom-system.com/token",
            delegated_exchange_uri="https://custom-delegated.com/token"
        )
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_config_property(self, mock_identity_auth_manager, env_vars):
        """Test config property returns the extension config."""
        mock_identity_auth_manager.return_value = Mock()
        
        factory = ContentGridExtensionFlowClientFactory()
        config = factory.config
        
        assert isinstance(config, ExtensionFlowConfig)
        assert config.extension_client_name == "test-client"
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.ContentGridApplicationClient')
    def test_get_client_with_origin(self, mock_app_client_class, mock_identity_auth_manager, sample_contentgrid_user):
        """Test get_client method with origin parameter."""
        mock_auth_manager_instance = Mock()
        mock_user_auth_manager = Mock()
        mock_auth_manager_instance.for_user.return_value = mock_user_auth_manager
        mock_identity_auth_manager.return_value = mock_auth_manager_instance
        
        mock_app_client_instance = Mock()
        mock_app_client_class.return_value = mock_app_client_instance
        
        factory = ContentGridExtensionFlowClientFactory()
        # Use a domain that's in the user's allowed domains
        origin = HttpUrl("https://test.domain.com")
        
        result = factory.get_client(sample_contentgrid_user, origin, mock_app_client_class)
        
        assert result == mock_app_client_instance
        
        # Verify auth manager was called with user token and origin
        mock_auth_manager_instance.for_user.assert_called_once_with(
            "test-access-token", 
            urls={"https://test.domain.com"}
        )
        
        # Verify ContentGridApplicationClient was initialized correctly
        mock_app_client_class.assert_called_once_with(
            client_endpoint="https://test.domain.com",
            auth_manager=mock_user_auth_manager
        )
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.ContentGridApplicationClient')
    def test_get_client_without_origin(self, mock_app_client_class, mock_identity_auth_manager, sample_contentgrid_user):
        """Test get_client method without origin parameter (uses first domain)."""
        mock_auth_manager_instance = Mock()
        mock_user_auth_manager = Mock()
        mock_auth_manager_instance.for_user.return_value = mock_user_auth_manager
        mock_identity_auth_manager.return_value = mock_auth_manager_instance
        
        mock_app_client_instance = Mock()
        mock_app_client_class.return_value = mock_app_client_instance
        
        factory = ContentGridExtensionFlowClientFactory()
        
        result = factory.get_client(sample_contentgrid_user, None, mock_app_client_class)
        
        assert result == mock_app_client_instance
        
        # Verify auth manager was called with user token and first domain
        mock_auth_manager_instance.for_user.assert_called_once_with(
            "test-access-token", 
            urls={"https://test.domain.com"}
        )
        
        # Verify ContentGridApplicationClient was initialized with first domain
        mock_app_client_class.assert_called_once_with(
            client_endpoint="https://test.domain.com",
            auth_manager=mock_user_auth_manager
        )
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_create_dependency(self, mock_identity_auth_manager, mock_user_dependency):
        """Test create_dependency method creates a proper FastAPI dependency."""
        mock_identity_auth_manager.return_value = Mock()
        
        factory = ContentGridExtensionFlowClientFactory()
        dependency_func = factory.create_client_dependency(user_dependency=mock_user_dependency)
        
        # Verify that the dependency function is callable
        assert callable(dependency_func)
        
        # Check the dependency function signature has the expected annotations
        import inspect
        sig = inspect.signature(dependency_func)
        assert len(sig.parameters) == 2
        assert 'user' in sig.parameters
        assert 'origin' in sig.parameters


class TestContentGridExtensionFlowClientFactoryDependency:
    """Test the dependency function created by the factory."""
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.ContentGridApplicationClient')
    def test_dependency_function_with_origin(self, mock_app_client_class, mock_identity_auth_manager, 
                                           sample_contentgrid_user, mock_user_dependency):
        """Test the dependency function with origin parameter."""
        mock_auth_manager_instance = Mock()
        mock_user_auth_manager = Mock()
        mock_auth_manager_instance.for_user.return_value = mock_user_auth_manager
        mock_identity_auth_manager.return_value = mock_auth_manager_instance
        
        mock_app_client_instance = Mock()
        mock_app_client_class.return_value = mock_app_client_instance
        
        factory = ContentGridExtensionFlowClientFactory()
        dependency_func = factory.create_client_dependency(user_dependency=mock_user_dependency, client_type=mock_app_client_class)
        
        # Use a domain that's in the user's allowed domains
        origin = HttpUrl("https://another.domain.com")
        result = dependency_func(sample_contentgrid_user, origin)
        
        assert result == mock_app_client_instance
        
        # Verify the correct endpoint was used
        mock_app_client_class.assert_called_once_with(
            client_endpoint="https://another.domain.com",
            auth_manager=mock_user_auth_manager
        )
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.ContentGridApplicationClient')
    def test_dependency_function_without_origin(self, mock_app_client_class, mock_identity_auth_manager, 
                                              sample_contentgrid_user, mock_user_dependency):
        """Test the dependency function without origin parameter."""
        mock_auth_manager_instance = Mock()
        mock_user_auth_manager = Mock()
        mock_auth_manager_instance.for_user.return_value = mock_user_auth_manager
        mock_identity_auth_manager.return_value = mock_auth_manager_instance
        
        mock_app_client_instance = Mock()
        mock_app_client_class.return_value = mock_app_client_instance
        
        factory = ContentGridExtensionFlowClientFactory()
        dependency_func = factory.create_client_dependency(user_dependency=mock_user_dependency, client_type=mock_app_client_class)
        
        result = dependency_func(sample_contentgrid_user, None)
        
        assert result == mock_app_client_instance
        
        # Verify the first domain was used as endpoint
        mock_app_client_class.assert_called_once_with(
            client_endpoint="https://test.domain.com",
            auth_manager=mock_user_auth_manager
        )


class TestUserDependencyCallCount:
    """Test that user dependency is called only once when using the factory dependency."""
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.ContentGridApplicationClient')
    def test_user_dependency_called_once_per_request(self, mock_app_client_class, mock_identity_auth_manager, 
                                                   sample_contentgrid_user):
        """Test that user dependency is called exactly once per request."""
        mock_auth_manager_instance = Mock()
        mock_user_auth_manager = Mock()
        mock_auth_manager_instance.for_user.return_value = mock_user_auth_manager
        mock_identity_auth_manager.return_value = mock_auth_manager_instance
        
        mock_app_client_instance = Mock()
        mock_app_client_class.return_value = mock_app_client_instance
        
        # Create a mock user dependency that tracks calls
        mock_user_dependency = Mock()
        mock_user_dependency.return_value = sample_contentgrid_user
        
        factory = ContentGridExtensionFlowClientFactory()
        dependency_func = factory.create_client_dependency(user_dependency=mock_user_dependency, client_type=mock_app_client_class)
        
        # Simulate FastAPI calling the dependency with the user (already resolved)
        # In real FastAPI, the user parameter would already be resolved by the user_dependency
        result1 = dependency_func(sample_contentgrid_user, None)
        # Use a domain that's in the user's allowed domains
        result2 = dependency_func(sample_contentgrid_user, HttpUrl("https://test.domain.com"))
        
        # Both calls should succeed
        assert result1 == mock_app_client_instance
        assert result2 == mock_app_client_instance
        
        # Verify that ContentGridApplicationClient was created twice (once per call)
        assert mock_app_client_class.call_count == 2
        
        # Verify that auth manager for_user was called twice with the same token
        assert mock_auth_manager_instance.for_user.call_count == 2
        calls = mock_auth_manager_instance.for_user.call_args_list
        assert all(call[0][0] == "test-access-token" for call in calls)


class TestDependencyIntegration:
    """Test integration scenarios that mirror real usage patterns."""
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.ContentGridApplicationClient')
    def test_usage_pattern_from_dependencies_file(self, mock_app_client_class, mock_identity_auth_manager, 
                                                 sample_contentgrid_user):
        """Test the usage pattern as shown in the dependencies.py file."""
        mock_auth_manager_instance = Mock()
        mock_user_auth_manager = Mock()
        mock_auth_manager_instance.for_user.return_value = mock_user_auth_manager
        mock_identity_auth_manager.return_value = mock_auth_manager_instance
        
        mock_app_client_instance = Mock()
        mock_app_client_class.return_value = mock_app_client_instance
        
        # Simulate the usage pattern from dependencies.py
        contentgrid_user_dependency = ContentGridUserDependency()
        
        def get_contentgrid_user(user: ContentGridUser) -> ContentGridUser:
            """Simulate the get_contentgrid_user function from dependencies.py"""
            return user
        
        extension_flow_factory = ContentGridExtensionFlowClientFactory()
        contentgrid_application_client_dependency = extension_flow_factory.create_client_dependency(user_dependency=mock_user_dependency, client_type=mock_app_client_class)
        
        def get_contentgrid_application_client(client: ContentGridApplicationClient) -> ContentGridApplicationClient:
            """Simulate the get_contentgrid_application_client function from dependencies.py"""
            return client
        
        # Test the dependency chain
        user = get_contentgrid_user(sample_contentgrid_user)
        client = contentgrid_application_client_dependency(user, None)
        final_client = get_contentgrid_application_client(client)
        
        assert final_client == mock_app_client_instance
        
        # Verify the client was created with the first domain
        mock_app_client_class.assert_called_once_with(
            client_endpoint="https://test.domain.com",
            auth_manager=mock_user_auth_manager
        )
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_factory_configuration_flexibility(self, mock_identity_auth_manager):
        """Test that factory can be configured flexibly for different environments."""
        mock_identity_auth_manager.return_value = Mock()
        
        # Test with minimal configuration
        factory_minimal = ContentGridExtensionFlowClientFactory()
        assert factory_minimal.identity_auth_manager is not None
        
        # Test with partial configuration
        factory_partial = ContentGridExtensionFlowClientFactory(
            extension_client_name="partial-client",
            system_exchange_uri="https://partial-system.com/token"
        )
        assert factory_partial.extension_config.extension_client_name == "partial-client"
        assert factory_partial.extension_config.system_exchange_uri == "https://partial-system.com/token"
        
        # Test with full configuration
        factory_full = ContentGridExtensionFlowClientFactory(
            extension_auth_url="https://full-auth.com/token",
            extension_client_name="full-client",
            extension_client_secret="full-secret",
            system_exchange_uri="https://full-system.com/token",
            delegated_exchange_uri="https://full-delegated.com/token"
        )
        assert factory_full.extension_config.extension_auth_url == "https://full-auth.com/token"
        assert factory_full.extension_config.extension_client_name == "full-client"
        assert factory_full.extension_config.extension_client_secret == "full-secret"


class TestDomainValidationSecurity:
    """Test domain validation security features."""
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_invalid_domain_raises_http_exception_production(self, mock_identity_auth_manager, sample_contentgrid_user):
        """Test that invalid domains raise HTTPException in production mode."""
        from fastapi import HTTPException
        
        mock_identity_auth_manager.return_value = Mock()
        factory = ContentGridExtensionFlowClientFactory()
        
        invalid_domains = [
            "https://malicious.com",
            "https://example.com", 
            "https://evil.domain.com",
            "https://not-allowed.org",
            "https://hacker.site"
        ]
        
        for invalid_domain in invalid_domains:
            origin = HttpUrl(invalid_domain)
            with pytest.raises(HTTPException) as exc_info:
                factory.get_client(sample_contentgrid_user, origin)
            
            assert exc_info.value.status_code == 403
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_valid_domains_work_in_production(self, mock_identity_auth_manager, sample_contentgrid_user):
        """Test that valid domains work correctly in production mode."""
        mock_auth_manager_instance = Mock()
        mock_user_auth_manager = Mock()
        mock_auth_manager_instance.for_user.return_value = mock_user_auth_manager
        mock_identity_auth_manager.return_value = mock_auth_manager_instance
        
        factory = ContentGridExtensionFlowClientFactory()
        
        # These domains should work (they're in the user's allowed domains)
        valid_domains = [
            "https://test.domain.com",
            "https://another.domain.com"
        ]
        
        for valid_domain in valid_domains:
            origin = HttpUrl(valid_domain)
            # Should not raise an exception
            result = factory.get_client(sample_contentgrid_user, origin)
            assert result is not None
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_dependency_function_invalid_domain_production(self, mock_identity_auth_manager, sample_contentgrid_user, mock_user_dependency):
        """Test that dependency function raises HTTPException for invalid domains in production."""
        from fastapi import HTTPException
        
        mock_identity_auth_manager.return_value = Mock()
        factory = ContentGridExtensionFlowClientFactory()
        dependency_func = factory.create_client_dependency(user_dependency=mock_user_dependency)
        
        # This domain is not in the user's allowed domains
        origin = HttpUrl("https://unauthorized.domain.com")
        
        with pytest.raises(HTTPException) as exc_info:
            dependency_func(sample_contentgrid_user, origin)
        
        assert exc_info.value.status_code == 403
    
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_subdomain_attack_prevention(self, mock_identity_auth_manager, sample_contentgrid_user):
        """Test that subdomain attacks are prevented."""
        from fastapi import HTTPException
        
        mock_identity_auth_manager.return_value = Mock()
        factory = ContentGridExtensionFlowClientFactory()
        
        # These look similar to allowed domains but should be rejected
        malicious_subdomains = [
            "https://malicious.test.domain.com",  # subdomain of allowed domain
            "https://evil.another.domain.com",    # subdomain of allowed domain
            "https://test.domain.com.evil.com",   # domain that ends with allowed domain
            "https://faketest.domain.com",        # similar but different domain
        ]
        
        for malicious_domain in malicious_subdomains:
            origin = HttpUrl(malicious_domain)
            with pytest.raises(HTTPException) as exc_info:
                factory.get_client(sample_contentgrid_user, origin)
            
            assert exc_info.value.status_code == 403



class TestErrorHandling:
    """Test error handling in ContentGridExtensionFlowClientFactory."""
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_identity_auth_manager_initialization_error(self, mock_identity_auth_manager):
        """Test handling of IdentityAuthenticationManager initialization errors."""
        mock_identity_auth_manager.side_effect = Exception("Auth manager initialization failed")
        
        with pytest.raises(Exception, match="Auth manager initialization failed"):
            ContentGridExtensionFlowClientFactory(
                extension_client_name="test-client",
                extension_client_secret="test-secret"
            )
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_domain_validation_in_production(self, mock_identity_auth_manager, sample_contentgrid_user):
        """Test that domain validation works in production mode."""
        from fastapi import HTTPException
        
        mock_identity_auth_manager.return_value = Mock()
        
        factory = ContentGridExtensionFlowClientFactory()
        # Use a domain that's NOT in the user's allowed domains
        origin = HttpUrl("https://evil.domain.com")
        
        with pytest.raises(HTTPException) as exc_info:
            factory.get_client(sample_contentgrid_user, origin)
        
        assert exc_info.value.status_code == 403

class TestEdgeCasesAndSecurity:
    """Test edge cases and security scenarios for domain validation."""
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_empty_user_domains_production(self, mock_identity_auth_manager):
        """Test behavior when user has no domains in production."""
        from fastapi import HTTPException
        
        mock_identity_auth_manager.return_value = Mock()
        factory = ContentGridExtensionFlowClientFactory()
        
        # Create user with empty domains list
        user_no_domains = ContentGridUser(
            **{
                "sub":"test-user",
                "iss":"test-issuer", 
                "exp":1234567890,
                "name":"Test User",
                "email":"test@example.com",
                "access_token":"test-access-token",
                "context:application:domains":[],  # Empty domains
                "context:application:id":"test-app-id"
            }
        )
        
        origin = HttpUrl("https://any.domain.com")
        
        # Should still raise exception even with empty domains
        with pytest.raises(HTTPException) as exc_info:
            factory.get_client(user_no_domains, origin)
        
        assert exc_info.value.status_code == 403
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_no_origin_no_user_domains_production(self, mock_identity_auth_manager):
        """Test behavior when no origin provided and user has no domains."""
        from fastapi import HTTPException
        
        mock_identity_auth_manager.return_value = Mock()
        factory = ContentGridExtensionFlowClientFactory()
        
        # Create user with empty domains list
        user_no_domains = ContentGridUser(
            **{
                "sub":"test-user",
                "iss":"test-issuer",
                "exp":1234567890, 
                "name":"Test User",
                "email":"test@example.com",
                "access_token":"test-access-token",
                "context:application:domains":[],  # Empty domains
                "context:application:id":"test-app-id"
            }
        )
        
        # No origin provided, no domains available
        with pytest.raises(ValueError) as exc_info:
            factory.get_client(user_no_domains, None)
        
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_unicode_domain_attack_prevention(self, mock_identity_auth_manager, sample_contentgrid_user):
        """Test that unicode domain attacks are prevented."""
        from fastapi import HTTPException
        
        mock_identity_auth_manager.return_value = Mock()
        factory = ContentGridExtensionFlowClientFactory()
        
        # Unicode domains that might look similar to allowed domains
        unicode_attacks = [
            "https://tеst.domain.com",  # Cyrillic 'e' instead of Latin 'e'
            "https://test.dοmain.com",  # Greek omicron instead of Latin 'o'
            "https://tëst.domain.com",  # Latin 'e' with diaeresis
        ]
        
        for unicode_domain in unicode_attacks:
            try:
                origin = HttpUrl(unicode_domain)
                with pytest.raises(HTTPException) as exc_info:
                    factory.get_client(sample_contentgrid_user, origin)
                
                assert exc_info.value.status_code == 403
            except Exception:
                # If HttpUrl parsing fails, that's also acceptable security behavior
                pass
    
    @patch('contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory.IdentityAuthenticationManager')
    def test_ip_address_rejection(self, mock_identity_auth_manager, sample_contentgrid_user):
        """Test that IP addresses are rejected even if they resolve to allowed domains."""
        from fastapi import HTTPException
        
        mock_identity_auth_manager.return_value = Mock()
        factory = ContentGridExtensionFlowClientFactory()
        
        # IP addresses should be rejected
        ip_addresses = [
            "https://192.168.1.1",
            "https://10.0.0.1", 
            "https://127.0.0.1",
            "https://8.8.8.8",
            "https://[::1]",  # IPv6 localhost
            "https://[2001:db8::1]",  # IPv6 address
        ]
        
        for ip_address in ip_addresses:
            origin = HttpUrl(ip_address)
            with pytest.raises(HTTPException) as exc_info:
                factory.get_client(sample_contentgrid_user, origin)
            
            assert exc_info.value.status_code == 403


if __name__ == "__main__":
    pytest.main([__file__])
