"""
CAP Alerts - Custom Exceptions
"""


class CAPAlertNotFound(Exception):
    """Exception raised when a CAP alert is not found"""
    pass


class CAPAlertValidationError(Exception):
    """Exception raised when CAP alert data validation fails"""
    pass


class CAPAlertDuplicateError(Exception):
    """Exception raised when trying to create a duplicate CAP alert"""
    pass
