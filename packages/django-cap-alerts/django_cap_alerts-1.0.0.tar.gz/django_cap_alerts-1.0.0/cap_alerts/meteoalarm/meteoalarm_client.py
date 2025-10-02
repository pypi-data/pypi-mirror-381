"""
Meteoalarm API Client
"""

import requests
from typing import Optional, Dict, Any
from .meteoalarm_exceptions import MeteoalarmAPIError, MeteoalarmConnectionError, MeteoalarmAuthenticationError
from .meteoalarm_config import MeteoalarmConfig


class MeteoalarmClient:
    """Client for Meteoalarm Weather Warning API"""
    
    def __init__(self, base_url: str = None, api_key: str = None, timeout: int = 30):
        """
        Initialize Meteoalarm API client
        
        Args:
            base_url: Base URL for Meteoalarm API
            api_key: API key for authentication
            timeout: Request timeout in seconds
        """
        self.base_url = base_url or MeteoalarmConfig.get_base_url()
        self.api_key = api_key or MeteoalarmConfig.get_api_key()
        self.timeout = timeout
        self.session = requests.Session()
        
        # Set default headers
        self.session.headers.update({
            'Content-Type': 'application/xml',
            'Accept': 'application/xml',
            'User-Agent': 'CAP-Alerts-Meteoalarm-Client/1.0'
        })
        
        # Add API key if provided
        if self.api_key:
            self.session.headers.update({
                'X-API-Key': self.api_key
            })
    
    def _make_request(self, method: str, endpoint: str, data: str = None) -> Dict[Any, Any]:
        """
        Make HTTP request to Meteoalarm API
        
        Args:
            method: HTTP method (POST, PUT, GET, DELETE)
            endpoint: API endpoint
            data: CAP XML data for POST/PUT requests
            
        Returns:
            Response data as dictionary
            
        Raises:
            MeteoalarmAPIError: API error response
            MeteoalarmConnectionError: Connection error
            MeteoalarmAuthenticationError: Authentication error
        """
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        try:
            if method.upper() == 'POST':
                response = self.session.post(url, data=data, timeout=self.timeout)
            else:
                raise MeteoalarmAPIError(f"Unsupported HTTP method: {method}")
            
            # Handle different response codes
            if response.status_code == 201:
                # Successfully created
                try:
                    return response.json()
                except:
                    return {"status": "created", "status_code": 201, "message": response.text}
            elif response.status_code == 204:
                # Successfully updated
                return {"status": "updated", "status_code": 204}
            elif response.status_code == 200:
                # Successfully retrieved
                try:
                    return response.json()
                except:
                    return {"status": "success", "status_code": 200, "data": response.text}
            elif response.status_code == 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', 'Bad request')
                except:
                    error_message = f"Bad request: {response.text}"
                raise MeteoalarmAPIError(error_message, 400)
            elif response.status_code == 401:
                raise MeteoalarmAuthenticationError("Unauthorized - invalid API key")
            elif response.status_code == 403:
                raise MeteoalarmAuthenticationError("Forbidden - insufficient permissions")
            elif response.status_code == 404:
                raise MeteoalarmAPIError("Resource not found", 404)
            elif response.status_code == 500:
                raise MeteoalarmAPIError("Internal server error", 500)
            elif response.status_code == 503:
                raise MeteoalarmAPIError("Service unavailable", 503)
            elif response.status_code >= 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', f"API error: {response.status_code}")
                except:
                    error_message = f"API error: {response.status_code} - {response.text}"
                raise MeteoalarmAPIError(error_message, response.status_code)
            
            # Parse successful response
            try:
                return response.json()
            except:
                return {"status": "success", "data": response.text}
                
        except requests.exceptions.ConnectionError as e:
            raise MeteoalarmConnectionError(f"Failed to connect to Meteoalarm API: {e}")
        except requests.exceptions.Timeout as e:
            raise MeteoalarmConnectionError(f"Request timeout: {e}")
        except requests.exceptions.RequestException as e:
            raise MeteoalarmConnectionError(f"Request error: {e}")
    
    def send_weather_warning(self, cap_alert: 'CAPAlert') -> Dict[Any, Any]:
        """
        Send CAP alert to Meteoalarm (POST /alerts)
        
        Args:
            cap_alert: CAPAlert object with to_xml() method
            
        Returns:
            API response data
            
        Raises:
            MeteoalarmAPIError: API error
            MeteoalarmConnectionError: Connection error
        """
        # Get CAP XML from the alert
        return self._make_request('POST', '/alerts', data=cap_alert.to_xml())

