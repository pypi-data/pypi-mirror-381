"""
Engage API Configuration
"""

import os
from django.conf import settings


class EngageConfig:
    """Configuration class for Engage API"""
    
    # API endpoints
    ENDPOINTS = {
        'weather_warnings': '/weather-warnings'
    }
    
    # HTTP headers
    DEFAULT_HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'CAP-Alerts-Client/1.0'
    }
    
    @classmethod
    def get_base_url(cls):
        """Get base URL from Django settings"""
        return getattr(settings, 'ENGAGE_BASE_URL', None)
    
    @classmethod
    def get_token(cls):
        """Get JWT token from Django settings"""
        return getattr(settings, 'ENGAGE_API_KEY', None)
    
    @classmethod
    def get_timeout(cls):
        """Get timeout from Django settings"""
        return getattr(settings, 'ENGAGE_TIMEOUT', 30)
    
    @classmethod
    def get_headers(cls):
        """Get default headers"""
        return cls.DEFAULT_HEADERS.copy()
    
    @classmethod
    def is_configured(cls):
        """Check if Engage API is properly configured"""
        base_url = cls.get_base_url()
        token = cls.get_token()
        
        return bool(base_url and token)
    
    @classmethod
    def get_config_summary(cls):
        """Get configuration summary for debugging"""
        return {
            'base_url': cls.get_base_url(),
            'token_configured': bool(cls.get_token()),
            'timeout': cls.get_timeout(),
            'is_configured': cls.is_configured()
        }
