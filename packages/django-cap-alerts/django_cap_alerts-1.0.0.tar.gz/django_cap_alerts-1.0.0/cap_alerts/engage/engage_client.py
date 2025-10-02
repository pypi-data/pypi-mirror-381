"""
Engage API Client
"""

import requests
from typing import Optional, Dict, Any
from .engage_exceptions import EngageAPIError, EngageConnectionError, EngageAuthenticationError
from .engage_config import EngageConfig


class EngageClient:
    """Client for Engage Weather Warning API"""
    
    def __init__(self, base_url: str = None, token: str = None, timeout: int = 30):
        """
        Initialize Engage API client
        
        Args:
            base_url: Base URL for Engage API
            token: JWT token for authentication
            timeout: Request timeout in seconds
        """
        self.base_url = base_url or EngageConfig.get_base_url()
        self.token = token or EngageConfig.get_token()
        self.timeout = timeout
        self.session = requests.Session()
        
        # Set default headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        # Add JWT token if provided
        if self.token:
            self.session.cookies.set('Token', self.token)
    
    def _make_request(self, method: str, endpoint: str, data: Dict[Any, Any] = None) -> Dict[Any, Any]:
        """
        Make HTTP request to Engage API
        
        Args:
            method: HTTP method (POST, PUT)
            endpoint: API endpoint
            data: Request data for POST/PUT requests
            
        Returns:
            Response data as dictionary
            
        Raises:
            EngageAPIError: API error response
            EngageConnectionError: Connection error
            EngageAuthenticationError: Authentication error
        """
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        try:
            if method.upper() == 'POST':
                response = self.session.post(url, json=data, timeout=self.timeout)
            elif method.upper() == 'PUT':
                response = self.session.put(url, json=data, timeout=self.timeout)
            else:
                raise EngageAPIError(f"Unsupported HTTP method: {method}")
            
            # Handle different response codes
            if response.status_code == 201:
                # Successfully created
                try:
                    return response.json()
                except:
                    return {"status": "created", "status_code": 201}
            elif response.status_code == 204:
                # Successfully updated
                return {"status": "updated", "status_code": 204}
            elif response.status_code == 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', 'Bad request')
                except:
                    error_message = f"Bad request: {response.text}"
                raise EngageAPIError(error_message, 400)
            elif response.status_code == 401:
                raise EngageAuthenticationError("Unauthorized - invalid JWT token")
            elif response.status_code == 403:
                raise EngageAuthenticationError("Forbidden - insufficient permissions")
            elif response.status_code == 500:
                raise EngageAPIError("Internal server error", 500)
            elif response.status_code == 503:
                raise EngageAPIError("Service unavailable", 503)
            elif response.status_code >= 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', f"API error: {response.status_code}")
                except:
                    error_message = f"API error: {response.status_code} - {response.text}"
                raise EngageAPIError(error_message, response.status_code)
            
            # Parse successful response
            try:
                return response.json()
            except:
                return {"status": "success", "data": response.text}
                
        except requests.exceptions.ConnectionError as e:
            raise EngageConnectionError(f"Failed to connect to Engage API: {e}")
        except requests.exceptions.Timeout as e:
            raise EngageConnectionError(f"Request timeout: {e}")
        except requests.exceptions.RequestException as e:
            raise EngageConnectionError(f"Request error: {e}")
    
    
    def send_weather_warning(self, engage_alert: 'EngageWeatherWarningAlert') -> Dict[Any, Any]:
        """
        Send weather warning to Engage API (POST /weather-warnings)
        
        Args:
            engage_alert: EngageWeatherWarningAlert object
            
        Returns:
            API response data
            
        Raises:
            EngageAPIError: API error
            EngageConnectionError: Connection error
        """
        return self._make_request('POST', '/weather-warnings', engage_alert.to_dict())
    
    def update_weather_warning(self, engage_alert: 'EngageWeatherWarningAlert') -> Dict[Any, Any]:
        """
        Update weather warning in Engage API (PUT /weather-warnings)
        
        Args:
            engage_alert: Updated EngageWeatherWarningAlert object
            
        Returns:
            API response data
            
        Raises:
            EngageAPIError: API error
            EngageConnectionError: Connection error
        """
        return self._make_request('PUT', '/weather-warnings',  engage_alert.to_dict())
