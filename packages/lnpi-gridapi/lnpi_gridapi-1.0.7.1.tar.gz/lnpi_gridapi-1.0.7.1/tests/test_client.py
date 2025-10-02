"""
Tests for GridAPI client.
"""

import pytest
from unittest.mock import Mock, patch
from gridapi import GridAPIClient
from gridapi.exceptions import AuthenticationError, NotFoundError, ValidationError


class TestGridAPIClient:
    """Test cases for GridAPIClient."""
    
    def test_client_initialization_with_token(self):
        """Test client initialization with token."""
        client = GridAPIClient(
            base_url="https://api.example.com",
            token="test-token"
        )
        
        assert client.base_url == "https://api.example.com"
        assert client.auth.token == "test-token"
        assert client.auth.session_id is None
    
    def test_client_initialization_with_session_id(self):
        """Test client initialization with session ID."""
        client = GridAPIClient(
            base_url="https://api.example.com",
            session_id="test-session"
        )
        
        assert client.base_url == "https://api.example.com"
        assert client.auth.token is None
        assert client.auth.session_id == "test-session"
    
    def test_client_initialization_without_auth(self):
        """Test client initialization without authentication raises error."""
        with pytest.raises(AuthenticationError):
            GridAPIClient(base_url="https://api.example.com")
    
    def test_client_managers_initialization(self):
        """Test that managers are properly initialized."""
        client = GridAPIClient(
            base_url="https://api.example.com",
            token="test-token"
        )
        
        assert hasattr(client, 'grid')
        assert hasattr(client, 'image')
        assert hasattr(client, 'taskflow')
    
    @patch('requests.Session.request')
    def test_get_request(self, mock_request):
        """Test GET request handling."""
        # Mock response
        mock_response = Mock()
        mock_response.json.return_value = {"id": 1, "name": "Test"}
        mock_response.raise_for_status.return_value = None
        mock_response.content = b'{"id": 1, "name": "Test"}'
        mock_request.return_value = mock_response
        
        client = GridAPIClient(
            base_url="https://api.example.com",
            token="test-token"
        )
        
        result = client.get("/test")
        
        assert result == {"id": 1, "name": "Test"}
        mock_request.assert_called_once()
    
    @patch('requests.Session.request')
    def test_post_request(self, mock_request):
        """Test POST request handling."""
        # Mock response
        mock_response = Mock()
        mock_response.json.return_value = {"id": 1, "name": "Created"}
        mock_response.raise_for_status.return_value = None
        mock_response.content = b'{"id": 1, "name": "Created"}'
        mock_request.return_value = mock_response
        
        client = GridAPIClient(
            base_url="https://api.example.com",
            token="test-token"
        )
        
        data = {"name": "Test Study"}
        result = client.post("/studies", data=data)
        
        assert result == {"id": 1, "name": "Created"}
        mock_request.assert_called_once()
    
    @patch('requests.Session.request')
    def test_http_error_handling(self, mock_request):
        """Test HTTP error handling."""
        # Mock 404 response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"detail": "Not found"}
        mock_response.content = b'{"detail": "Not found"}'
        
        # Mock HTTPError
        from requests.exceptions import HTTPError
        mock_response.raise_for_status.side_effect = HTTPError("404 Client Error")
        mock_request.return_value = mock_response
        
        client = GridAPIClient(
            base_url="https://api.example.com",
            token="test-token"
        )
        
        with pytest.raises(NotFoundError):
            client.get("/nonexistent")
    
    def test_url_building(self):
        """Test URL building."""
        client = GridAPIClient(
            base_url="https://api.example.com",
            token="test-token"
        )
        
        # Test with leading slash
        url = client._build_url("/test")
        assert url == "https://api.example.com/test"
        
        # Test without leading slash
        url = client._build_url("test")
        assert url == "https://api.example.com/test"
        
        # Test with trailing slash in base_url
        client.base_url = "https://api.example.com/"
        url = client._build_url("test")
        assert url == "https://api.example.com/test"


class TestAuthHandler:
    """Test cases for AuthHandler."""
    
    def test_token_auth_headers(self):
        """Test token authentication headers."""
        from gridapi.auth import AuthHandler
        
        auth = AuthHandler(token="test-token")
        headers = auth.get_headers()
        
        assert headers["Authorization"] == "Token test-token"
    
    def test_session_auth_cookies(self):
        """Test session authentication cookies."""
        from gridapi.auth import AuthHandler
        
        auth = AuthHandler(session_id="test-session")
        cookies = auth.get_cookies()
        
        assert cookies["sessionid"] == "test-session"
    
    def test_no_auth_raises_error(self):
        """Test that no authentication raises error."""
        from gridapi.auth import AuthHandler
        
        with pytest.raises(AuthenticationError):
            AuthHandler()


if __name__ == "__main__":
    pytest.main([__file__])
