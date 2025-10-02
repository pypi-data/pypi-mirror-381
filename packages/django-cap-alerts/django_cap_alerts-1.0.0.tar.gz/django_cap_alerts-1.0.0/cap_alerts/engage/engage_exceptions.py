"""
Engage API Exceptions
"""


class EngageAPIError(Exception):
    """Base exception for Engage API errors"""
    
    def __init__(self, message: str, status_code: int = None, response_data: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data or {}
    
    def __str__(self):
        if self.status_code:
            return f"Engage API Error {self.status_code}: {self.message}"
        return f"Engage API Error: {self.message}"


class EngageConnectionError(EngageAPIError):
    """Exception for connection-related errors"""
    
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
    
    def __str__(self):
        return f"Engage Connection Error: {self.message}"


class EngageAuthenticationError(EngageAPIError):
    """Exception for authentication-related errors"""
    
    def __init__(self, message: str, status_code: int = 401):
        super().__init__(message, status_code)
        self.message = message
        self.status_code = status_code
    
    def __str__(self):
        return f"Engage Authentication Error: {self.message}"


class EngageValidationError(EngageAPIError):
    """Exception for validation errors"""
    
    def __init__(self, message: str, validation_errors: dict = None):
        super().__init__(message, status_code=400)
        self.message = message
        self.validation_errors = validation_errors or {}
    
    def __str__(self):
        if self.validation_errors:
            return f"Engage Validation Error: {self.message} - {self.validation_errors}"
        return f"Engage Validation Error: {self.message}"


class EngageNotFoundError(EngageAPIError):
    """Exception for resource not found errors"""
    
    def __init__(self, message: str, resource_id: str = None):
        super().__init__(message, status_code=404)
        self.message = message
        self.resource_id = resource_id
    
    def __str__(self):
        if self.resource_id:
            return f"Engage Not Found Error: {self.message} (ID: {self.resource_id})"
        return f"Engage Not Found Error: {self.message}"


class EngageServerError(EngageAPIError):
    """Exception for server errors"""
    
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message, status_code)
        self.message = message
        self.status_code = status_code
    
    def __str__(self):
        return f"Engage Server Error {self.status_code}: {self.message}"
