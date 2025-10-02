"""
CAP Alerts - Django REST Framework Serializers
Provides proper validation for CAP alert data
"""

from rest_framework import serializers
from datetime import datetime, timezone
import re
from .models import (
    CAPAlert, CAPInfo, CAPArea, CAPResource,
    Status, MsgType, Scope, Urgency, Severity, Certainty,
    Category, ResponseType
)
from .utils import validate_cap_restricted_chars, validate_cap_datetime, validate_cap_value_name_value_format, validate_non_empty_string


class CAPAreaSerializer(serializers.ModelSerializer):
    """Serializer for CAP Area"""
    
    class Meta:
        model = CAPArea
        fields = [
            'area_desc', 'polygon', 'circle', 'circle_radius', 
            'geocode', 'altitude', 'ceiling'
        ]
        extra_kwargs = {
            'area_desc': {'required': True},
            'polygon': {'required': False},
            'circle': {'required': False},
            'circle_radius': {'required': False},
            'geocode': {'required': False},
            'altitude': {'required': False},
            'ceiling': {'required': False},
        }
    
    def validate_polygon(self, value):
        """Validate polygon according to CAP specification"""
        if value is not None:
            # Check if it's a valid PostGIS polygon
            if not hasattr(value, 'coords') or not value.coords:
                raise serializers.ValidationError("Polygon must have valid coordinates")
            
            # Get the exterior ring coordinates
            coords = list(value.coords[0])  # First ring (exterior)
            
            # Check minimum 4 coordinate pairs
            if len(coords) < 4:
                raise serializers.ValidationError("Polygon must have at least 4 coordinate pairs")
            
            # Check first and last pairs are the same (closed polygon)
            if coords[0] != coords[-1]:
                raise serializers.ValidationError("Polygon must be closed (first and last coordinate pairs must be the same)")
            
            # Validate WGS 84 coordinate ranges
            for coord in coords:
                lon, lat = coord
                if not (-180 <= lon <= 180):
                    raise serializers.ValidationError(f"Longitude must be between -180 and 180. Got: {lon}")
                if not (-90 <= lat <= 90):
                    raise serializers.ValidationError(f"Latitude must be between -90 and 90. Got: {lat}")
        
        return value
    
    def validate_circle(self, value):
        """Validate circle point according to CAP specification"""
        if value is not None:
            # Check if it's a valid PostGIS point
            if not hasattr(value, 'coords') or not value.coords:
                raise serializers.ValidationError("Circle must have valid coordinates")
            
            # Get coordinates
            coords = value.coords
            
            # Validate WGS 84 coordinate ranges
            lon, lat = coords
            if not (-180 <= lon <= 180):
                raise serializers.ValidationError(f"Circle longitude must be between -180 and 180. Got: {lon}")
            if not (-90 <= lat <= 90):
                raise serializers.ValidationError(f"Circle latitude must be between -90 and 90. Got: {lat}")
        
        return value
    
    def validate_circle_radius(self, value):
        """Validate circle radius according to CAP specification"""
        if value is not None:
            if value <= 0:
                raise serializers.ValidationError("Circle radius must be greater than 0 kilometers")
            if value > 20000:  # Reasonable limit (half Earth's circumference)
                raise serializers.ValidationError("Circle radius seems too large (max 20,000 km)")
        
        return value
    
    def validate(self, data):
        """Validate cross-field relationships"""
        # Check circle and circle_radius are both provided or both None
        circle = data.get('circle')
        circle_radius = data.get('circle_radius')
        
        if (circle is not None) != (circle_radius is not None):
            raise serializers.ValidationError("Both circle and circle_radius must be provided together, or both must be None")
        
        # Check altitude and ceiling relationship
        altitude = data.get('altitude')
        ceiling = data.get('ceiling')
        
        if altitude is not None and ceiling is not None:
            if altitude >= ceiling:
                raise serializers.ValidationError("Altitude must be less than ceiling when both are provided")
        
        return data
    
    def validate_area_desc(self, value):
        """Validate area_desc is a non-empty string"""
        return validate_non_empty_string(value, "area_desc")
    
    def validate_geocode(self, value):
        """Validate geocode format according to CAP specification"""
        return validate_cap_value_name_value_format(value, "geocode")
    
    def validate_altitude(self, value):
        """Validate altitude according to CAP specification"""
        if value is not None:
            # Reasonable altitude range: -1000 to 100,000 feet
            if value < -1000:
                raise serializers.ValidationError("Altitude seems too low (minimum -1000 feet)")
            if value > 100000:
                raise serializers.ValidationError("Altitude seems too high (maximum 100,000 feet)")
        
        return value
    
    def validate_ceiling(self, value):
        """Validate ceiling according to CAP specification"""
        if value is not None:
            # Reasonable ceiling range: -1000 to 100,000 feet
            if value < -1000:
                raise serializers.ValidationError("Ceiling seems too low (minimum -1000 feet)")
            if value > 100000:
                raise serializers.ValidationError("Ceiling seems too high (maximum 100,000 feet)")
        
        return value


class CAPResourceSerializer(serializers.ModelSerializer):
    """Serializer for CAP Resource"""
    
    class Meta:
        model = CAPResource
        fields = [
            'resource_desc', 'mime_type', 'size', 'uri', 
            'deref_uri', 'digest'
        ]
        extra_kwargs = {
            'resource_desc': {'required': True},
            'mime_type': {'required': True},
            'size': {'required': False},
            'uri': {'required': False},
            'deref_uri': {'required': False},
            'digest': {'required': False},
        }
    
    def validate_resource_desc(self, value):
        """Validate resource_desc is a non-empty string"""
        return validate_non_empty_string(value, "resource_desc")
    
    def validate_mime_type(self, value):
        """Validate MIME type format according to RFC 2046"""
        # First validate it's a non-empty string
        validate_non_empty_string(value, "mime_type")
        
        import re
        # RFC 2046 MIME type pattern: type/subtype
        mime_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9!#$&\-\^_]*/[a-zA-Z0-9][a-zA-Z0-9!#$&\-\^_]*$'
        
        if not re.match(mime_pattern, value):
            raise serializers.ValidationError(f"MIME type must be in valid format (e.g., 'text/plain', 'image/jpeg'). Got: '{value}'")
        
        return value
    
    def validate_size(self, value):
        """Validate size according to CAP specification"""
        if value is not None:
            if value <= 0:
                raise serializers.ValidationError("Size must be greater than 0 bytes")
        
        return value
    
    def validate_uri(self, value):
        """Validate URI format"""
        if value is not None and value.strip():
            import re
            # Basic URI validation pattern
            uri_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
            
            if not re.match(uri_pattern, value):
                raise serializers.ValidationError(f"URI must be a valid absolute URI (e.g., 'https://example.com/resource'). Got: '{value}'")
        
        return value
    
    def validate_deref_uri(self, value):
        """Validate derefUri base64 format and size"""
        if value is not None and value.strip():
            import base64
            try:
                # Try to decode base64 to validate format
                decoded_data = base64.b64decode(value)
                
                # Check size limit (5MB decoded data)
                if len(decoded_data) > 5 * 1024 * 1024:  # 5MB
                    raise serializers.ValidationError("derefUri content is too large (max 5MB)")
                    
            except Exception:
                raise serializers.ValidationError("derefUri must be valid base64 encoded data")
        
        return value
    
    def validate(self, data):
        """Validate cross-field relationships"""
        uri = data.get('uri')
        deref_uri = data.get('deref_uri')
        
        # At least one of uri or deref_uri must be provided
        if not uri and not deref_uri:
            raise serializers.ValidationError("Either uri or deref_uri must be provided")
        
        return data
    
    def validate_digest(self, value):
        """Validate digest SHA-1 format"""
        if value is not None and value.strip():
            import re
            # SHA-1 hash is 40 hexadecimal characters
            sha1_pattern = r'^[a-fA-F0-9]{40}$'
            
            if not re.match(sha1_pattern, value):
                raise serializers.ValidationError("Digest must be a valid SHA-1 hash (40 hexadecimal characters)")
        
        return value


class CAPInfoSerializer(serializers.ModelSerializer):
    """Serializer for CAP Info"""
    
    # Nested serializers for related objects
    areas = CAPAreaSerializer(many=True, required=False)
    resources = CAPResourceSerializer(many=True, required=False)
    
    class Meta:
        model = CAPInfo
        fields = [
            'language', 'category', 'event', 'response_type', 'urgency', 
            'severity', 'certainty', 'audience', 'event_code', 'effective', 
            'onset', 'expires', 'sender_name', 'headline', 'description', 
            'instruction', 'web', 'contact', 'parameter','areas', 'resources'
        ]
        extra_kwargs = {
            'language': {'required': True},
            'category': {'required': True},
            'event': {'required': True},
            'urgency': {'required': True},
            'severity': {'required': True},
            'certainty': {'required': True},
            'audience': {'required': False},
            'event_code': {'required': False},
            'effective': {'required': False},
            'onset': {'required': False},
            'expires': {'required': False},
            'sender_name': {'required': False},   
            'headline': {'required': False},
            'description': {'required': False},
            'instruction': {'required': False},
            'web': {'required': False},
            'contact': {'required': False},
            'parameter': {'required': False},
        }
    
    def validate_category(self, value):
        """Validate category values"""
        if not value or not isinstance(value, list):
            raise serializers.ValidationError("Category must be a non-empty list")
        
        valid_categories = [choice[0] for choice in Category.choices()]
        for category in value:
            if category not in valid_categories:
                raise serializers.ValidationError(f"Invalid category: {category}")
        
        return value
    
    def validate_response_type(self, value):
        """Validate response_type values"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Response type must be a list")
            
            valid_response_types = [choice[0] for choice in ResponseType.choices()]
            for response_type in value:
                if response_type not in valid_response_types:
                    raise serializers.ValidationError(f"Invalid response type: {response_type}")
        
        return value
    
    def validate_urgency(self, value):
        """Validate urgency value"""
        valid_urgencies = [choice[0] for choice in Urgency.choices()]
        if value not in valid_urgencies:
            raise serializers.ValidationError(f"Invalid urgency: {value}")
        return value
    
    def validate_severity(self, value):
        """Validate severity value"""
        valid_severities = [choice[0] for choice in Severity.choices()]
        if value not in valid_severities:
            raise serializers.ValidationError(f"Invalid severity: {value}")
        return value
    
    def validate_certainty(self, value):
        """Validate certainty value"""
        valid_certainties = [choice[0] for choice in Certainty.choices()]
        if value not in valid_certainties:
            raise serializers.ValidationError(f"Invalid certainty: {value}")
        return value
    
    def validate_language(self, value):
        """Validate language code per RFC 3066"""
        if value is not None and value.strip():
            import re
            # RFC 3066 language tag pattern: language[-script][-region]
            # Examples: en, en-US, zh-Hans, zh-Hans-CN
            rfc3066_pattern = r'^[a-zA-Z]{1,8}(-[a-zA-Z]{1,8})?(-[a-zA-Z0-9]{1,8})?$'
            
            if not re.match(rfc3066_pattern, value):
                raise serializers.ValidationError(f"Language must be a valid RFC 3066 language identifier (e.g., 'en', 'en-US', 'zh-Hans'). Got: '{value}'")
        
        return value
    
    def validate_event(self, value):
        """Validate event is a non-empty string"""
        return validate_non_empty_string(value, "event")
    
    def validate_event_code(self, value):
        """Validate eventCode format according to CAP specification"""
        return validate_cap_value_name_value_format(value, "event code")
    
    def validate_effective(self, value):
        """Validate effective datetime"""
        if value is not None:
            # Use the existing utility function to validate CAP format
            validate_cap_datetime(value, "effective")
        return value
    
    def validate_onset(self, value):
        """Validate onset datetime"""
        if value is not None:
            # Use the existing utility function to validate CAP format
            validate_cap_datetime(value, "onset")
        return value
    
    def validate_expires(self, value):
        """Validate expires datetime"""
        if value is not None:
            # Use the existing utility function to validate CAP format
            validate_cap_datetime(value, "expires")
        return value
    
    def validate_headline(self, value):
        """Validate headline length"""
        if value is not None and len(value) > 160:
            raise serializers.ValidationError(f"Headline should be 160 characters or less for optimal display. Got {len(value)} characters.")
        return value
    
    def validate_web(self, value):
        """Validate web URI format"""
        if value is not None and value.strip():
            import re
            # Basic URI validation pattern
            uri_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
            
            if not re.match(uri_pattern, value):
                raise serializers.ValidationError(f"Web must be a valid absolute URI (e.g., 'https://example.com/page'). Got: '{value}'")
        
        return value
    
    def validate_sender_name(self, value):
        """Validate sender_name is a non-empty string"""
        if value is not None:
            return validate_non_empty_string(value, "sender_name")
        return value
    
    def validate_headline(self, value):
        """Validate headline length and string format"""
        if value is not None and value.strip():
            # First validate it's a non-empty string
            validate_non_empty_string(value, "headline")
            if len(value) > 160:
                raise serializers.ValidationError(f"Headline should be 160 characters or less for optimal display. Got {len(value)} characters.")
        return value
    
    def validate_description(self, value):
        """Validate description is a string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "description")
        return value
    
    def validate_instruction(self, value):
        """Validate instruction is a non-empty string"""
        if value is not None:
            return validate_non_empty_string(value, "instruction")
        return value
    
    def validate_parameter(self, value):
        """Validate parameter format according to CAP specification"""
        return validate_cap_value_name_value_format(value, "parameter")
    
    def create(self, validated_data):
        """Create CAPInfo with nested objects"""
        areas_data = validated_data.pop('areas', [])
        resources_data = validated_data.pop('resources', [])
        
        info = CAPInfo.objects.create(**validated_data)
        
        # Create areas
        for area_data in areas_data:
            CAPArea.objects.create(info=info, **area_data)
        
        # Create resources
        for resource_data in resources_data:
            CAPResource.objects.create(info=info, **resource_data)
        
        return info
    
    def to_representation(self, instance):
        """Include nested objects in representation"""
        data = super().to_representation(instance)
        data['areas'] = CAPAreaSerializer(instance.areas.all(), many=True).data
        data['resources'] = CAPResourceSerializer(instance.resources.all(), many=True).data
        return data


class CAPAlertSerializer(serializers.ModelSerializer):
    """Serializer for CAP Alert"""
    
    # Nested serializer for info blocks
    info = CAPInfoSerializer(many=True, required=True)
    
    class Meta:
        model = CAPAlert
        fields = [
            'identifier', 'sender', 'sent', 'status', 'msg_type', 'scope',
            'source', 'restriction', 'addresses', 'code', 'note', 'references',
            'incidents', 'info'
        ]
        extra_kwargs = {
            'identifier': {'required': True},
            'sender': {'required': True},
            'sent': {'required': True},
            'status': {'required': True},
            'msg_type': {'required': True},
            'source': {'required': False},
            'scope': {'required': True},
            'restriction': {'required': False},
            'addresses': {'required': False},
            'code': {'required': False},
            'note': {'required': False},
            'references': {'required': False},
            'incidents': {'required': False},
        }
    
    def validate_identifier(self, value):
        """Validate identifier is a non-empty string, unique, and has no restricted characters"""
        # First validate it's a non-empty string
        validate_non_empty_string(value, "identifier")
        
        if CAPAlert.objects.filter(identifier=value).exists():
            raise serializers.ValidationError(f"Alert with identifier '{value}' already exists")
        
        # Validate restricted characters using utility function
        validate_cap_restricted_chars(value, "identifier", [' ', ',', '<', '&'])
        
        return value
    
    def validate_status(self, value):
        """Validate status value"""
        valid_statuses = [choice[0] for choice in Status.choices()]
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Invalid status: {value}")
        return value
    
    def validate_msg_type(self, value):
        """Validate msg_type value"""
        valid_msg_types = [choice[0] for choice in MsgType.choices()]
        if value not in valid_msg_types:
            raise serializers.ValidationError(f"Invalid msg_type: {value}")
        return value
    
    def validate_scope(self, value):
        """Validate scope value"""
        valid_scopes = [choice[0] for choice in Scope.choices()]
        if value not in valid_scopes:
            raise serializers.ValidationError(f"Invalid scope: {value}")
        return value
    
    def validate_sender(self, value):
        """Validate sender is a non-empty string and has no restricted characters"""
        # First validate it's a non-empty string
        validate_non_empty_string(value, "sender")
        # Then validate restricted characters
        validate_cap_restricted_chars(value, "sender", [' ', ',', '<', '&'])
        return value
    
    def validate_sent(self, value):
        """Validate sent datetime"""
        if value > datetime.now(timezone.utc):
            raise serializers.ValidationError("Sent time cannot be in the future")
        
        # Validate CAP datetime format
        validate_cap_datetime(value, "sent")
        
        return value
    
    def validate_addresses(self, value):
        """Validate addresses format"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Addresses must be a list")
            
            for address in value:
                if not isinstance(address, str) or not address.strip():
                    raise serializers.ValidationError("Each address must be a non-empty string")
        
        return value
    
    def validate_source(self, value):
        """Validate source is a string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "source")
        return value
    
    def validate_restriction(self, value):
        """Validate restriction is a non-empty string"""
        if value is not None:
            return validate_non_empty_string(value, "restriction")
        return value
    
    def validate_note(self, value):
        """Validate note is a string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "note")
        return value
    
    def validate_incidents(self, value):
        """Validate incidents format"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Incidents must be a list")
            
            for incident in value:
                if not isinstance(incident, str) or not incident.strip():
                    raise serializers.ValidationError("Each incident must be a non-empty string")
        
        return value
    
    def validate_code(self, value):
        """Validate code format"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Code must be a list")
            
            for code_item in value:
                if not isinstance(code_item, str) or not code_item.strip():
                    raise serializers.ValidationError("Each code item must be a non-empty string")
        
        return value
    
    def validate_references(self, value):
        """Validate references format according to CAP specification"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("References must be a list")
            
            for ref in value:
                if not isinstance(ref, str) or not ref.strip():
                    raise serializers.ValidationError("Each reference must be a non-empty string")
                
                # Split by comma and validate format: sender,identifier,sent
                parts = ref.split(',')
                if len(parts) != 3:
                    raise serializers.ValidationError(f"Reference must be in format 'sender,identifier,sent'. Got: '{ref}'")
                
                sender, identifier, sent_str = parts
                
                # Check no field is empty
                if not sender.strip() or not identifier.strip() or not sent_str.strip():
                    raise serializers.ValidationError(f"Reference parts cannot be empty. Got: '{ref}'")
                
                # Validate sent is valid CAP datetime using utility function
                try:
                    from datetime import datetime
                    # Parse the datetime string to a datetime object for validation
                    ref_datetime = datetime.fromisoformat(sent_str.strip().replace('Z', '+00:00'))
                    # Use the existing utility function to validate CAP format
                    validate_cap_datetime(ref_datetime, "reference sent time")
                except ValueError as e:
                    raise serializers.ValidationError(f"Reference sent time is not a valid datetime: '{sent_str.strip()}'")
                
                # Validate sender format (should be email or URI-like)
                sender = sender.strip()
                email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                uri_pattern = r'^[a-zA-Z][a-zA-Z0-9+.-]*:'
                
                if not (re.match(email_pattern, sender) or re.match(uri_pattern, sender)):
                    raise serializers.ValidationError(f"Reference sender must be a valid email address or URI. Got: '{sender}'")
                
                # Validate identifier format (should not contain restricted characters)
                identifier = identifier.strip()
                validate_cap_restricted_chars(identifier, "reference identifier", [' ', ',', '<', '&'])
        
        return value
    
    def validate(self, data):
        """Validate cross-field relationships"""
        # Check restriction is required when scope is "Restricted"
        if data.get('scope') == 'Restricted' and not data.get('restriction'):
            raise serializers.ValidationError("Restriction is required when scope is 'Restricted'")
        
        # Check restriction should not be used when scope is not "Restricted"
        if data.get('scope') != 'Restricted' and data.get('restriction'):
            raise serializers.ValidationError("Restriction should be used only when scope is 'Restricted'")
        
        # Check addresses is required when scope is "Private"
        if data.get('scope') == 'Private' and not data.get('addresses'):
            raise serializers.ValidationError("Addresses is required when scope is 'Private'")
        
        # Validate references sent time is not in the future compared to current alert sent time
        if data.get('references') and data.get('sent'):
            from datetime import datetime
            current_sent = data.get('sent')
            
            for ref in data.get('references', []):
                if isinstance(ref, str) and ',' in ref:
                    parts = ref.split(',')
                    if len(parts) == 3:
                        ref_sent_str = parts[2].strip()
                        try:
                            # Parse reference sent time
                            ref_sent = datetime.fromisoformat(ref_sent_str.replace('Z', '+00:00'))
                            
                            # Check if reference sent time is in the future compared to current alert sent time
                            if ref_sent > current_sent:
                                raise serializers.ValidationError(f"Reference sent time '{ref_sent_str}' cannot be in the future compared to current alert sent time '{current_sent.isoformat()}'")
                                
                        except ValueError:
                            # Skip invalid datetime formats (already validated in validate_references)
                            pass
        
        return data
    
    def create(self, validated_data):
        """Create CAPAlert with nested info blocks"""
        info_data = validated_data.pop('info', [])
        
        alert = CAPAlert.objects.create(**validated_data)
        
        # Create info blocks
        for info_item in info_data:
            areas_data = info_item.pop('areas', [])
            resources_data = info_item.pop('resources', [])
            
            info = CAPInfo.objects.create(alert=alert, **info_item)
            
            # Create areas
            for area_data in areas_data:
                CAPArea.objects.create(info=info, **area_data)
            
            # Create resources
            for resource_data in resources_data:
                CAPResource.objects.create(info=info, **resource_data)
        
        return alert


class CAPAreaUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating CAP Area"""
    
    class Meta:
        model = CAPArea
        fields = [
            'area_desc', 'polygon', 'circle', 'circle_radius', 
            'geocode', 'altitude', 'ceiling'
        ]
        extra_kwargs = {
            'area_desc': {'required': False},
            'polygon': {'required': False},
            'circle': {'required': False},
            'circle_radius': {'required': False},
            'geocode': {'required': False},
            'altitude': {'required': False},
            'ceiling': {'required': False},
        }
    
    def validate_area_desc(self, value):
        """Validate area_desc is a non-empty string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "area_desc")
        return value
    
    def validate_polygon(self, value):
        """Validate polygon according to CAP specification"""
        if value is not None:
            # Check if it's a valid PostGIS polygon
            if not hasattr(value, 'coords') or not value.coords:
                raise serializers.ValidationError("Polygon must have valid coordinates")
            
            # Get the exterior ring coordinates
            coords = list(value.coords[0])  # First ring (exterior)
            
            # Check minimum 4 coordinate pairs
            if len(coords) < 4:
                raise serializers.ValidationError("Polygon must have at least 4 coordinate pairs")
            
            # Check first and last pairs are the same (closed polygon)
            if coords[0] != coords[-1]:
                raise serializers.ValidationError("Polygon must be closed (first and last coordinate pairs must be the same)")
            
            # Validate WGS 84 coordinate ranges
            for coord in coords:
                lon, lat = coord
                if not (-180 <= lon <= 180):
                    raise serializers.ValidationError(f"Longitude must be between -180 and 180. Got: {lon}")
                if not (-90 <= lat <= 90):
                    raise serializers.ValidationError(f"Latitude must be between -90 and 90. Got: {lat}")
        
        return value
    
    def validate_circle(self, value):
        """Validate circle point according to CAP specification"""
        if value is not None:
            # Check if it's a valid PostGIS point
            if not hasattr(value, 'coords') or not value.coords:
                raise serializers.ValidationError("Circle must have valid coordinates")
            
            # Get coordinates
            coords = value.coords
            
            # Validate WGS 84 coordinate ranges
            lon, lat = coords
            if not (-180 <= lon <= 180):
                raise serializers.ValidationError(f"Circle longitude must be between -180 and 180. Got: {lon}")
            if not (-90 <= lat <= 90):
                raise serializers.ValidationError(f"Circle latitude must be between -90 and 90. Got: {lat}")
        
        return value
    
    def validate_circle_radius(self, value):
        """Validate circle radius according to CAP specification"""
        if value is not None:
            if value <= 0:
                raise serializers.ValidationError("Circle radius must be greater than 0 kilometers")
            if value > 20000:  # Reasonable limit (half Earth's circumference)
                raise serializers.ValidationError("Circle radius seems too large (max 20,000 km)")
        
        return value
    
    def validate(self, data):
        """Validate cross-field relationships"""
        # Check circle and circle_radius are both provided or both None
        circle = data.get('circle')
        circle_radius = data.get('circle_radius')
        
        if (circle is not None) != (circle_radius is not None):
            raise serializers.ValidationError("Both circle and circle_radius must be provided together, or both must be None")
        
        # Check altitude and ceiling relationship
        altitude = data.get('altitude')
        ceiling = data.get('ceiling')
        
        if altitude is not None and ceiling is not None:
            if altitude >= ceiling:
                raise serializers.ValidationError("Altitude must be less than ceiling when both are provided")
        
        return data
    
    def validate_geocode(self, value):
        """Validate geocode format according to CAP specification"""
        return validate_cap_value_name_value_format(value, "geocode")
    
    def validate_altitude(self, value):
        """Validate altitude according to CAP specification"""
        if value is not None:
            # Reasonable altitude range: -1000 to 100,000 feet
            if value < -1000:
                raise serializers.ValidationError("Altitude seems too low (minimum -1000 feet)")
            if value > 100000:
                raise serializers.ValidationError("Altitude seems too high (maximum 100,000 feet)")
        
        return value
    
    def validate_ceiling(self, value):
        """Validate ceiling according to CAP specification"""
        if value is not None:
            # Reasonable ceiling range: -1000 to 100,000 feet
            if value < -1000:
                raise serializers.ValidationError("Ceiling seems too low (minimum -1000 feet)")
            if value > 100000:
                raise serializers.ValidationError("Ceiling seems too high (maximum 100,000 feet)")
        
        return value


class CAPResourceUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating CAP Resource"""
    
    class Meta:
        model = CAPResource
        fields = [
            'resource_desc', 'mime_type', 'size', 'uri', 
            'deref_uri', 'digest'
        ]
        extra_kwargs = {
            'resource_desc': {'required': False},
            'mime_type': {'required': False},
            'size': {'required': False},
            'uri': {'required': False},
            'deref_uri': {'required': False},
            'digest': {'required': False},
        }
    
    def validate_resource_desc(self, value):
        """Validate resource_desc is a non-empty string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "resource_desc")
        return value
    
    def validate_mime_type(self, value):
        """Validate MIME type format according to RFC 2046"""
        if value is not None and value.strip():
            # First validate it's a non-empty string
            validate_non_empty_string(value, "mime_type")
            
            import re
            # RFC 2046 MIME type pattern: type/subtype
            mime_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9!#$&\-\^_]*/[a-zA-Z0-9][a-zA-Z0-9!#$&\-\^_]*$'
            
            if not re.match(mime_pattern, value):
                raise serializers.ValidationError(f"MIME type must be in valid format (e.g., 'text/plain', 'image/jpeg'). Got: '{value}'")
        
        return value
    
    def validate_size(self, value):
        """Validate size according to CAP specification"""
        if value is not None:
            if value <= 0:
                raise serializers.ValidationError("Size must be greater than 0 bytes")
        
        return value
    
    def validate_uri(self, value):
        """Validate URI format"""
        if value is not None and value.strip():
            import re
            # Basic URI validation pattern
            uri_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
            
            if not re.match(uri_pattern, value):
                raise serializers.ValidationError(f"URI must be a valid absolute URI (e.g., 'https://example.com/resource'). Got: '{value}'")
        
        return value
    
    def validate_deref_uri(self, value):
        """Validate derefUri base64 format and size"""
        if value is not None and value.strip():
            import base64
            try:
                # Try to decode base64 to validate format
                decoded_data = base64.b64decode(value)
                
                # Check size limit (5MB decoded data)
                if len(decoded_data) > 5 * 1024 * 1024:  # 5MB
                    raise serializers.ValidationError("derefUri content is too large (max 5MB)")
                    
            except Exception:
                raise serializers.ValidationError("derefUri must be valid base64 encoded data")
        
        return value
    
    def validate(self, data):
        """Validate cross-field relationships"""
        uri = data.get('uri')
        deref_uri = data.get('deref_uri')
        
        # At least one of uri or deref_uri must be provided
        if not uri and not deref_uri:
            raise serializers.ValidationError("Either uri or deref_uri must be provided")
        
        return data
    
    def validate_digest(self, value):
        """Validate digest SHA-1 format"""
        if value is not None and value.strip():
            import re
            # SHA-1 hash is 40 hexadecimal characters
            sha1_pattern = r'^[a-fA-F0-9]{40}$'
            
            if not re.match(sha1_pattern, value):
                raise serializers.ValidationError("Digest must be a valid SHA-1 hash (40 hexadecimal characters)")
        
        return value


class CAPInfoUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating CAP Info"""
    
    # Nested serializers for related objects
    areas = CAPAreaUpdateSerializer(many=True, required=False)
    resources = CAPResourceUpdateSerializer(many=True, required=False)
    
    class Meta:
        model = CAPInfo
        fields = [
            'language', 'category', 'event', 'response_type', 'urgency', 
            'severity', 'certainty', 'audience', 'event_code', 'effective', 
            'onset', 'expires', 'sender_name', 'headline', 'description', 
            'instruction', 'web', 'contact', 'parameter','areas', 'resources'
        ]
        extra_kwargs = {
            'language': {'required': False},
            'category': {'required': False},
            'event': {'required': False},
            'urgency': {'required': False},
            'severity': {'required': False},
            'certainty': {'required': False},
            'audience': {'required': False},
            'event_code': {'required': False},
            'effective': {'required': False},
            'onset': {'required': False},
            'expires': {'required': False},
            'sender_name': {'required': False},   
            'headline': {'required': False},
            'description': {'required': False},
            'instruction': {'required': False},
            'web': {'required': False},
            'contact': {'required': False},
            'parameter': {'required': False},
        }
    
    def validate_category(self, value):
        """Validate category values"""
        if value is not None:
            if not value or not isinstance(value, list):
                raise serializers.ValidationError("Category must be a non-empty list")
            
            valid_categories = [choice[0] for choice in Category.choices()]
            for category in value:
                if category not in valid_categories:
                    raise serializers.ValidationError(f"Invalid category: {category}")
        
        return value
    
    def validate_response_type(self, value):
        """Validate response_type values"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Response type must be a list")
            
            valid_response_types = [choice[0] for choice in ResponseType.choices()]
            for response_type in value:
                if response_type not in valid_response_types:
                    raise serializers.ValidationError(f"Invalid response type: {response_type}")
        
        return value
    
    def validate_urgency(self, value):
        """Validate urgency value"""
        if value is not None:
            valid_urgencies = [choice[0] for choice in Urgency.choices()]
            if value not in valid_urgencies:
                raise serializers.ValidationError(f"Invalid urgency: {value}")
        return value
    
    def validate_severity(self, value):
        """Validate severity value"""
        if value is not None:
            valid_severities = [choice[0] for choice in Severity.choices()]
            if value not in valid_severities:
                raise serializers.ValidationError(f"Invalid severity: {value}")
        return value
    
    def validate_certainty(self, value):
        """Validate certainty value"""
        if value is not None:
            valid_certainties = [choice[0] for choice in Certainty.choices()]
            if value not in valid_certainties:
                raise serializers.ValidationError(f"Invalid certainty: {value}")
        return value
    
    def validate_language(self, value):
        """Validate language code per RFC 3066"""
        if value is not None and value.strip():
            import re
            # RFC 3066 language tag pattern: language[-script][-region]
            # Examples: en, en-US, zh-Hans, zh-Hans-CN
            rfc3066_pattern = r'^[a-zA-Z]{1,8}(-[a-zA-Z]{1,8})?(-[a-zA-Z0-9]{1,8})?$'
            
            if not re.match(rfc3066_pattern, value):
                raise serializers.ValidationError(f"Language must be a valid RFC 3066 language identifier (e.g., 'en', 'en-US', 'zh-Hans'). Got: '{value}'")
        
        return value
    
    def validate_event(self, value):
        """Validate event is a non-empty string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "event")
        return value
    
    def validate_event_code(self, value):
        """Validate eventCode format according to CAP specification"""
        return validate_cap_value_name_value_format(value, "event code")
    
    def validate_effective(self, value):
        """Validate effective datetime"""
        if value is not None:
            # Use the existing utility function to validate CAP format
            validate_cap_datetime(value, "effective")
        return value
    
    def validate_onset(self, value):
        """Validate onset datetime"""
        if value is not None:
            # Use the existing utility function to validate CAP format
            validate_cap_datetime(value, "onset")
        return value
    
    def validate_expires(self, value):
        """Validate expires datetime"""
        if value is not None:
            # Use the existing utility function to validate CAP format
            validate_cap_datetime(value, "expires")
        return value
    
    def validate_sender_name(self, value):
        """Validate sender_name is a non-empty string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "sender_name")
        return value
    
    def validate_headline(self, value):
        """Validate headline length and string format"""
        if value is not None and value.strip():
            # First validate it's a non-empty string
            validate_non_empty_string(value, "headline")
            if len(value) > 160:
                raise serializers.ValidationError(f"Headline should be 160 characters or less for optimal display. Got {len(value)} characters.")
        return value
    
    def validate_description(self, value):
        """Validate description is a string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "description")
        return value
    
    def validate_instruction(self, value):
        """Validate instruction is a non-empty string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "instruction")
        return value
    
    def validate_web(self, value):
        """Validate web URI format"""
        if value is not None and value.strip():
            import re
            # Basic URI validation pattern
            uri_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
            
            if not re.match(uri_pattern, value):
                raise serializers.ValidationError(f"Web must be a valid absolute URI (e.g., 'https://example.com/page'). Got: '{value}'")
        
        return value
    
    def validate_parameter(self, value):
        """Validate parameter format according to CAP specification"""
        return validate_cap_value_name_value_format(value, "parameter")
    
    def update(self, instance, validated_data):
        """Update CAPInfo with nested objects"""
        areas_data = validated_data.pop('areas', None)
        resources_data = validated_data.pop('resources', None)
        
        # Update info fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update areas if provided
        if areas_data is not None:
            # Clear existing areas
            instance.areas.all().delete()
            
            # Create new areas
            for area_data in areas_data:
                CAPArea.objects.create(info=instance, **area_data)
        
        # Update resources if provided
        if resources_data is not None:
            # Clear existing resources
            instance.resources.all().delete()
            
            # Create new resources
            for resource_data in resources_data:
                CAPResource.objects.create(info=instance, **resource_data)
        
        return instance
    
    def to_representation(self, instance):
        """Include nested objects in representation"""
        data = super().to_representation(instance)
        data['areas'] = CAPAreaUpdateSerializer(instance.areas.all(), many=True).data
        data['resources'] = CAPResourceUpdateSerializer(instance.resources.all(), many=True).data
        return data


class CAPAlertUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating CAP Alert - more flexible for partial updates"""
    
    # Nested serializer for info blocks (optional for updates)
    info = CAPInfoUpdateSerializer(many=True, required=False)
    
    class Meta:
        model = CAPAlert
        fields = [
            'status', 'msg_type', 'scope', 'source', 'restriction', 
            'addresses', 'code', 'note', 'references', 'incidents', 'info'
        ]
        extra_kwargs = {
            'status': {'required': False},
            'msg_type': {'required': False},
            'scope': {'required': False},
            'source': {'required': False},
            'restriction': {'required': False},
            'addresses': {'required': False},
            'code': {'required': False},
            'note': {'required': False},
            'references': {'required': False},
            'incidents': {'required': False},
        }
    
    def validate_status(self, value):
        """Validate status value"""
        valid_statuses = [choice[0] for choice in Status.choices()]
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Invalid status: {value}")
        return value
    
    def validate_msg_type(self, value):
        """Validate msg_type value"""
        valid_msg_types = [choice[0] for choice in MsgType.choices()]
        if value not in valid_msg_types:
            raise serializers.ValidationError(f"Invalid msg_type: {value}")
        return value
    
    def validate_scope(self, value):
        """Validate scope value"""
        valid_scopes = [choice[0] for choice in Scope.choices()]
        if value not in valid_scopes:
            raise serializers.ValidationError(f"Invalid scope: {value}")
        return value
    
    def validate_source(self, value):
        """Validate source is a string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "source")
        return value
    
    def validate_restriction(self, value):
        """Validate restriction is a non-empty string"""
        if value is not None:
            return validate_non_empty_string(value, "restriction")
        return value
    
    def validate_note(self, value):
        """Validate note is a string"""
        if value is not None and value.strip():
            return validate_non_empty_string(value, "note")
        return value
    
    def validate_incidents(self, value):
        """Validate incidents format"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Incidents must be a list")
            
            for incident in value:
                if not isinstance(incident, str) or not incident.strip():
                    raise serializers.ValidationError("Each incident must be a non-empty string")
        
        return value
    
    def validate_code(self, value):
        """Validate code format"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Code must be a list")
            
            for code_item in value:
                if not isinstance(code_item, str) or not code_item.strip():
                    raise serializers.ValidationError("Each code item must be a non-empty string")
        
        return value
    
    def validate_addresses(self, value):
        """Validate addresses format"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("Addresses must be a list")
            
            for address in value:
                if not isinstance(address, str) or not address.strip():
                    raise serializers.ValidationError("Each address must be a non-empty string")
        
        return value
    
    def validate_references(self, value):
        """Validate references format according to CAP specification"""
        if value is not None:
            if not isinstance(value, list):
                raise serializers.ValidationError("References must be a list")
            
            for ref in value:
                if not isinstance(ref, str) or not ref.strip():
                    raise serializers.ValidationError("Each reference must be a non-empty string")
                
                # Split by comma and validate format: sender,identifier,sent
                parts = ref.split(',')
                if len(parts) != 3:
                    raise serializers.ValidationError(f"Reference must be in format 'sender,identifier,sent'. Got: '{ref}'")
                
                sender, identifier, sent_str = parts
                
                # Check no field is empty
                if not sender.strip() or not identifier.strip() or not sent_str.strip():
                    raise serializers.ValidationError(f"Reference parts cannot be empty. Got: '{ref}'")
                
                # Validate sent is valid CAP datetime using utility function
                try:
                    from datetime import datetime
                    # Parse the datetime string to a datetime object for validation
                    ref_datetime = datetime.fromisoformat(sent_str.strip().replace('Z', '+00:00'))
                    # Use the existing utility function to validate CAP format
                    validate_cap_datetime(ref_datetime, "reference sent time")
                except ValueError as e:
                    raise serializers.ValidationError(f"Reference sent time is not a valid datetime: '{sent_str.strip()}'")
                
                # Validate sender format (should be email or URI-like)
                sender = sender.strip()
                email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                uri_pattern = r'^[a-zA-Z][a-zA-Z0-9+.-]*:'
                
                if not (re.match(email_pattern, sender) or re.match(uri_pattern, sender)):
                    raise serializers.ValidationError(f"Reference sender must be a valid email address or URI. Got: '{sender}'")
                
                # Validate identifier format (should not contain restricted characters)
                identifier = identifier.strip()
                validate_cap_restricted_chars(identifier, "reference identifier", [' ', ',', '<', '&'])
        
        return value
    
    def validate(self, data):
        """Validate cross-field relationships"""
        # Check restriction is required when scope is "Restricted"
        if data.get('scope') == 'Restricted' and not data.get('restriction'):
            raise serializers.ValidationError("Restriction is required when scope is 'Restricted'")
        
        # Check restriction should not be used when scope is not "Restricted"
        if data.get('scope') != 'Restricted' and data.get('restriction'):
            raise serializers.ValidationError("Restriction should be used only when scope is 'Restricted'")
        
        # Check addresses is required when scope is "Private"
        if data.get('scope') == 'Private' and not data.get('addresses'):
            raise serializers.ValidationError("Addresses is required when scope is 'Private'")
        
        return data
    
    def update(self, instance, validated_data):
        """Update CAPAlert with nested info blocks"""
        info_data = validated_data.pop('info', None)
        
        # Update alert fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update info blocks if provided
        if info_data is not None:
            # Clear existing info blocks
            instance.info_blocks.all().delete()
            
            # Create new info blocks
            for info_item in info_data:
                areas_data = info_item.pop('areas', [])
                resources_data = info_item.pop('resources', [])
                
                info = CAPInfo.objects.create(alert=instance, **info_item)
                
                # Create areas
                for area_data in areas_data:
                    CAPArea.objects.create(info=info, **area_data)
                
                # Create resources
                for resource_data in resources_data:
                    CAPResource.objects.create(info=info, **resource_data)
        
        return instance

