"""
CAP Alerts - Utility Functions
"""

def validate_cap_restricted_chars(value, field_name, restricted_chars):
    """
    Validate field for restricted characters.
    
    Args:
        value: The value to validate
        field_name: Name of the field for error messages
        restricted_chars: List of characters that are not allowed
        
    Returns:
        The validated value
        
    Raises:
        ValidationError: If value contains restricted characters
    """
    from rest_framework import serializers
    
    # Check for restricted characters
    for char in restricted_chars:
        if char in value:
            chars_str = ', '.join(f"'{c}'" for c in restricted_chars)
            raise serializers.ValidationError(f"{field_name.title()} must not contain restricted characters ({chars_str}). Found: '{char}'")
    
    return value


def validate_cap_datetime(value, field_name):
    """
    Validate CAP datetime format according to CAP specification.
    
    Args:
        value: The datetime value to validate
        field_name: Name of the field for error messages
        
    Returns:
        The validated value
        
    Raises:
        ValidationError: If datetime format is invalid
    """
    from rest_framework import serializers
    import re
    from datetime import datetime
    
    # Convert datetime to string to check format
    if hasattr(value, 'isoformat'):
        datetime_str = value.isoformat()
    else:
        datetime_str = str(value)
    
    # Check for alphabetic timezone designators (Z is not allowed)
    if 'Z' in datetime_str:
        raise serializers.ValidationError(f"{field_name.title()} must not use alphabetic timezone designators like 'Z'. Use '-00:00' for UTC instead.")
    
    # Validate complete CAP datetime format: YYYY-MM-DDTHH:MM:SS+/-HH:MM
    # Pattern breakdown:
    # YYYY-MM-DD: date part
    # T: separator
    # HH:MM:SS: time part (NO microseconds allowed in CAP 1.2)
    # +/-HH:MM: timezone part (optional)
    cap_datetime_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}([+-]\d{2}:\d{2})?$'
    
    if not re.match(cap_datetime_pattern, datetime_str):
        raise serializers.ValidationError(f"{field_name.title()} must be in CAP DateTime format: YYYY-MM-DDTHH:MM:SS+/-HH:MM (e.g., '2002-05-24T16:49:00-07:00'). Got: '{datetime_str}'")
    
    # If timezone is present, validate it's properly formatted
    if '+' in datetime_str or '-' in datetime_str:
        timezone_pattern = r'[+-]\d{2}:\d{2}$'
        if not re.search(timezone_pattern, datetime_str):
            raise serializers.ValidationError(f"{field_name.title()} timezone must be in format +/-HH:MM (e.g., '-07:00' for PDT, '-00:00' for UTC)")
    
    return value


def validate_cap_value_name_value_format(value, field_name):
    """
    Validate CAP valueName/value format for eventCode and parameter fields.
    
    Args:
        value: The value to validate (should be a list of dictionaries)
        field_name: Name of the field for error messages (e.g., "event code", "parameter")
        
    Returns:
        The validated value
        
    Raises:
        ValidationError: If value format is invalid
    """
    from rest_framework import serializers
    
    if value is not None:
        if not isinstance(value, list):
            raise serializers.ValidationError(f"{field_name.title()} must be a list")
        
        for item in value:
            if not isinstance(item, dict):
                raise serializers.ValidationError(f"Each {field_name} must be a dictionary")
            
            # Check required keys: valueName and value
            if 'valueName' not in item or 'value' not in item:
                raise serializers.ValidationError(f"{field_name.title()} must contain 'valueName' and 'value' keys")
            
            value_name = item.get('valueName')
            value_val = item.get('value')
            
            if not isinstance(value_name, str) or not value_name.strip():
                raise serializers.ValidationError(f"{field_name.title()} valueName must be a non-empty string")
            
            if not isinstance(value_val, str) or not value_val.strip():
                raise serializers.ValidationError(f"{field_name.title()} value must be a non-empty string")
    
    return value


def validate_non_empty_string(value, field_name):
    """
    Validate that a field is a non-empty string.
    
    Args:
        value: The value to validate
        field_name: Name of the field for error messages
        
    Returns:
        The validated value
        
    Raises:
        ValidationError: If value is None, not a string, or empty/whitespace
    """
    from rest_framework import serializers
    
    if value is None:
        raise serializers.ValidationError(f"{field_name.title()} is required")
    
    if not isinstance(value, str):
        raise serializers.ValidationError(f"{field_name.title()} must be a string")
    
    if not value.strip():
        raise serializers.ValidationError(f"{field_name.title()} cannot be empty or contain only whitespace")
    
    return value
