"""
Meteoalarm API Configuration
"""

import os
from django.conf import settings


class MeteoalarmConfig:
    """Configuration class for Meteoalarm API"""
    
    # API endpoints
    ENDPOINTS = {
        'alerts': '/alerts',
        'alerts_detail': '/alerts/{identifier}',
        'health_check': '/health',
        'status': '/status'
    }
    
    # HTTP headers
    DEFAULT_HEADERS = {
        'Content-Type': 'application/xml',
        'Accept': 'application/xml',
        'User-Agent': 'CAP-Alerts-Meteoalarm-Client/1.0'
    }
    
    @classmethod
    def get_base_url(cls):
        """Get base URL from Django settings"""
        return getattr(settings, 'METEOALARM_BASE_URL', None)
    
    @classmethod
    def get_api_key(cls):
        """Get API key from Django settings"""
        return getattr(settings, 'METEOALARM_API_KEY', None)
    
    @classmethod
    def get_timeout(cls):
        """Get timeout from Django settings"""
        return getattr(settings, 'METEOALARM_TIMEOUT', 30)
    
    @classmethod
    def get_headers(cls):
        """Get default headers"""
        return cls.DEFAULT_HEADERS.copy()
    
    @classmethod
    def is_configured(cls):
        """Check if Meteoalarm API is properly configured"""
        base_url = cls.get_base_url()
        api_key = cls.get_api_key()
        
        return bool(base_url and api_key)
    
    @classmethod
    def get_config_summary(cls):
        """Get configuration summary for debugging"""
        return {
            'base_url': cls.get_base_url(),
            'api_key_configured': bool(cls.get_api_key()),
            'timeout': cls.get_timeout(),
            'is_configured': cls.is_configured()
        }
