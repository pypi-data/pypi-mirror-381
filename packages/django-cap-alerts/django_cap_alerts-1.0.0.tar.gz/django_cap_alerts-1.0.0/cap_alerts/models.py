"""
CAP Alerts - Django Models
"""

import uuid
import xml.etree.ElementTree as ET
import json
from django.db import models
from django.contrib.gis.db import models as gis_models
from enum import Enum
from datetime import datetime
import html


class Category(str, Enum):
    """CAP alert categories"""
    GEO = "Geo"
    MET = "Met"
    SAFETY = "Safety"
    SECURITY = "Security"
    RESCUE = "Rescue"
    FIRE = "Fire"
    HEALTH = "Health"
    ENV = "Env"
    TRANSPORT = "Transport"
    INFRA = "Infra"
    CBRNE = "CBRNE"
    OTHER = "Other"
    
    @classmethod
    def choices(cls):
        return [(item.value, item.value) for item in cls]


class ResponseType(str, Enum):
    """CAP response types"""
    SHELTER = "Shelter"
    EVACUATE = "Evacuate"
    PREPARE = "Prepare"
    EXECUTE = "Execute"
    AVOID = "Avoid"
    MONITOR = "Monitor"
    ASSESS = "Assess"
    ALLCLEAR = "AllClear"
    NONE = "None"
    
    @classmethod
    def choices(cls):
        return [(item.value, item.value) for item in cls]


class Urgency(str, Enum):
    """CAP urgency levels"""
    IMMEDIATE = "Immediate"
    EXPECTED = "Expected"
    FUTURE = "Future"
    PAST = "Past"
    UNKNOWN = "Unknown"
    
    @classmethod
    def choices(cls):
        return [(item.value, item.value) for item in cls]


class Severity(str, Enum):
    """CAP severity levels"""
    EXTREME = "Extreme"
    SEVERE = "Severe"
    MODERATE = "Moderate"
    MINOR = "Minor"
    UNKNOWN = "Unknown"
    
    @classmethod
    def choices(cls):
        return [(item.value, item.value) for item in cls]


class Certainty(str, Enum):
    """CAP certainty levels"""
    OBSERVED = "Observed"
    LIKELY = "Likely"
    POSSIBLE = "Possible"
    UNLIKELY = "Unlikely"
    UNKNOWN = "Unknown"
    
    @classmethod
    def choices(cls):
        return [(item.value, item.value) for item in cls]


class Status(str, Enum):
    """CAP alert status"""
    ACTUAL = "Actual"
    EXERCISE = "Exercise"
    SYSTEM = "System"
    TEST = "Test"
    DRAFT = "Draft"
    
    @classmethod
    def choices(cls):
        return [(item.value, item.value) for item in cls]


class MsgType(str, Enum):
    """CAP message types"""
    ALERT = "Alert"
    UPDATE = "Update"
    CANCEL = "Cancel"
    ACK = "Ack"
    ERROR = "Error"
    
    @classmethod
    def choices(cls):
        return [(item.value, item.value) for item in cls]


class Scope(str, Enum):
    """CAP alert scope"""
    PUBLIC = "Public"
    RESTRICTED = "Restricted"
    PRIVATE = "Private"
    
    @classmethod
    def choices(cls):
        return [(item.value, item.value) for item in cls]


class CAPAlert(models.Model):
    """CAP Alert model - represents the main alert message container"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    identifier = models.CharField(max_length=255, unique=True, null=False, blank=False) # το εχει το weather warning
    sender = models.CharField(max_length=255, null=False, blank=False)# το εχει το weather warning
    sent = models.DateTimeField(null=False, blank=False)# το εχει το weather warning
    status = models.CharField(max_length=50, choices=Status.choices(), null=False, blank=False)  # το εχει το weather warning
    msg_type = models.CharField(max_length=50, choices=MsgType.choices(), null=False, blank=False)  # το εχει το weather warning
    scope = models.CharField(max_length=50, choices=Scope.choices(), null=False, blank=False) # το εχει το weather warning
    source = models.CharField(max_length=255, blank=True, null=True) 
    restriction = models.TextField(blank=True, null=True) 
    addresses = models.JSONField(blank=True, null=True) 
    code = models.JSONField(blank=True, null=True)# το εχει το weather warning
    note = models.TextField(blank=True, null=True)# το εχει το weather warning
    references = models.JSONField(blank=True, null=True)
    incidents = models.JSONField(blank=True, null=True)# το εχει το weather warning
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cap_alerts'
        ordering = ['-sent']

    def to_dict(self):
        return {
            'id': self.id,
            'identifier': self.identifier,
            'sender': self.sender,
            'sent': self.sent.isoformat(),
            'status': self.status,
            'msg_type': self.msg_type,
            'scope': self.scope,
            'source': self.source,
            'restriction': self.restriction,
            'addresses': self.addresses,
            'code': self.code,
            'note': self.note,
            'references': self.references,
            'incidents': self.incidents,
        }
    
    def _format_cap_datetime(self, dt):
        """Format datetime to CAP 1.2 specification format"""
        if dt is None:
            return None
        
        # Convert to ISO format and replace 'Z' with '+00:00' for UTC
        iso_str = dt.isoformat()
        if iso_str.endswith('+00:00'):
            return iso_str
        elif iso_str.endswith('Z'):
            return iso_str.replace('Z', '+00:00')
        else:
            return iso_str
    
    def _xml_escape(self, text):
        """Escape text for XML output"""
        if text is None:
            return ""
        return html.escape(str(text))
    
    def _add_text_element(self, parent, tag, text, namespace="cap"):
        """Add a text element to XML parent"""
        if text is not None and str(text).strip():
            element = ET.SubElement(parent, f"{namespace}:{tag}")
            element.text = str(text).strip()
            return element
        return None
    
    def _add_list_elements(self, parent, tag, items, namespace="cap"):
        """Add multiple elements for list items"""
        if items and isinstance(items, list):
            for item in items:
                if item and str(item).strip():
                    element = ET.SubElement(parent, f"{namespace}:{tag}")
                    element.text = str(item).strip()
    
    def _add_value_name_value_elements(self, parent, tag, items, namespace="cap"):
        """Add valueName/value elements for structured data"""
        if items and isinstance(items, list):
            for item in items:
                if isinstance(item, dict) and 'valueName' in item and 'value' in item:
                    element = ET.SubElement(parent, f"{namespace}:{tag}")
                    
                    value_name_elem = ET.SubElement(element, f"{namespace}:valueName")
                    value_name_elem.text = str(item['valueName']).strip()
                    
                    value_elem = ET.SubElement(element, f"{namespace}:value")
                    value_elem.text = str(item['value']).strip()
    
    def _format_polygon_coords(self, polygon):
        """Format PostGIS polygon to CAP coordinate string"""
        if polygon is None or not hasattr(polygon, 'coords'):
            return None
        
        coords = list(polygon.coords[0])  # Get exterior ring
        coord_strings = []
        for coord in coords:
            lon, lat = coord
            coord_strings.append(f"{lat},{lon}")  # CAP uses lat,lon format
        
        return " ".join(coord_strings)
    
    def _format_circle_coords(self, circle, radius):
        """Format PostGIS point and radius to CAP circle string"""
        if circle is None or not hasattr(circle, 'coords') or radius is None:
            return None
        
        coords = circle.coords
        lon, lat = coords
        return f"{lat},{lon} {radius}"  # CAP uses lat,lon radius format
    
    def to_xml(self, include_stylesheet=True):
        """Generate CAP 1.2 compliant XML from alert data"""
        # Create root element with namespace
        root = ET.Element("cap:alert")
        root.set("xmlns:cap", "urn:oasis:names:tc:emergency:cap:1.2")
        
        # Add XML declaration and stylesheet
        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
        if include_stylesheet:
            stylesheet = '<?xml-stylesheet type="text/xsl" href="https://cap-sources.s3.amazonaws.com/gr-gscp-en/alert-style.xsl"?>'
        else:
            stylesheet = ""
        
        # Alert level elements (required) - in correct CAP 1.2 order
        self._add_text_element(root, "identifier", self.identifier)
        self._add_text_element(root, "sender", self.sender)
        self._add_text_element(root, "sent", self._format_cap_datetime(self.sent))
        self._add_text_element(root, "status", self.status)
        self._add_text_element(root, "msgType", self.msg_type)
        self._add_text_element(root, "source", self.source)  # source comes after msgType
        self._add_text_element(root, "scope", self.scope)
        
        # Optional alert level elements - in correct CAP 1.2 order
        # According to CAP 1.2 spec, the order should be:
        # restriction, addresses, code, note, references, incidents, info
        self._add_text_element(root, "restriction", self.restriction)
        self._add_text_element(root, "addresses", " ".join([f'"{addr}"' if ' ' in addr else addr for addr in self.addresses]) if self.addresses else None)
        self._add_list_elements(root, "code", self.code)
        self._add_text_element(root, "note", self.note)
        self._add_text_element(root, "references", " ".join(self.references) if self.references else None)
        self._add_text_element(root, "incidents", " ".join([f'"{inc}"' if ' ' in inc else inc for inc in self.incidents]) if self.incidents else None)
        
        # Add info blocks (must come after all other alert elements)
        for info in self.info_blocks.all():
            info_xml = info.to_xml()
            root.append(info_xml)
        
        # Convert to string with proper formatting
        ET.indent(root, space="  ", level=0)
        xml_str = ET.tostring(root, encoding='unicode', xml_declaration=False)
        
        # Add XML declaration and stylesheet at the beginning
        if include_stylesheet and stylesheet:
            return f"{xml_declaration}\n{stylesheet}\n{xml_str}"
        else:
            return f"{xml_declaration}\n{xml_str}"
    
    def to_json(self):
        """Generate JSON representation of CAP alert data"""
        alert_data = {
            "alert": {
                "identifier": self.identifier,
                "sender": self.sender,
                "sent": self._format_cap_datetime(self.sent),
                "status": self.status,
                "msgType": self.msg_type,
                "scope": self.scope,
                "source": self.source,
                "restriction": self.restriction,
                "addresses": self.addresses,
                "code": self.code,
                "note": self.note,
                "references": self.references,
                "incidents": self.incidents,
                "info": []
            }
        }
        
        # Add info blocks using their to_json method
        for info in self.info_blocks.all():
            info_data = info.to_json()
            alert_data["alert"]["info"].append(info_data)
        
        return json.dumps(alert_data, indent=2, ensure_ascii=False)
    
    def to_engage_weatherwarning(self) -> 'EngageWeatherWarningAlert':
        """Convert to EngageWeatherWarningAlert object"""
        # Convert sent datetime to Unix timestamp
        sent_unix = int(self.sent.timestamp())
        
        # Convert info blocks to EngageWeatherWarningInfo objects
        info_objects = [info.to_engage_weatherwarning() for info in self.info_blocks.all()]
        
        return EngageWeatherWarningAlert(
            identifier=self.identifier,
            sender=self.sender,
            sent=sent_unix,
            status=self.status,
            msgType=self.msg_type,
            scope=self.scope,
            code=["MET"] if self.code and "MET" in self.code else None,
            note=self.note,
            references=" ".join(self.references) if self.references else None,
            incidents=" ".join(self.incidents) if self.incidents else None,
            info=info_objects
        )


class CAPTask(models.Model):
    """Model to track API requests to external services"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]
    
    CLIENT_CHOICES = [
        ('engage', 'Engage'),
        ('meteoalarm', 'Meteoalarm'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alert = models.ForeignKey(CAPAlert, on_delete=models.CASCADE, related_name='tasks')
    client = models.CharField(max_length=20, choices=CLIENT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    request_body = models.TextField(blank=True, null=True)
    response_body = models.TextField(blank=True, null=True)
    response_status_code = models.IntegerField(blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'cap_tasks'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.client} task for {self.alert.identifier} - {self.status}"


class CAPInfo(models.Model):
    """CAP Info model - represents the information sub-element of an alert message"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alert = models.ForeignKey(CAPAlert, on_delete=models.CASCADE, related_name='info_blocks')
    language = models.CharField(max_length=10, default='en-US')
    category = models.JSONField(null=False, blank=False)  # List of categories
    event = models.CharField(max_length=255, null=False, blank=False)
    response_type = models.JSONField(blank=True, null=True)  # List of response types
    urgency = models.CharField(max_length=50, choices=Urgency.choices(), null=False, blank=False)  # Immediate, Expected, Future, Past, Unknown
    severity = models.CharField(max_length=50, choices=Severity.choices(), null=False, blank=False)  # Extreme, Severe, Moderate, Minor, Unknown
    certainty = models.CharField(max_length=50, choices=Certainty.choices(), null=False, blank=False)  # Observed, Likely, Possible, Unlikely, Unknown
    audience = models.TextField(blank=True, null=True)
    event_code = models.JSONField(blank=True, null=True)
    effective = models.DateTimeField(blank=True, null=True)
    onset = models.DateTimeField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    sender_name = models.CharField(max_length=255, blank=True, null=True)
    headline = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)
    web = models.CharField(max_length=500, blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    parameter = models.JSONField(blank=True, null=True)
    
    class Meta:
        db_table = 'cap_info'

    def to_dict(self):
        return {
            'id': self.id,
            'alert_id': self.alert.id,
            'language': self.language,
            'category': self.category,
            'event': self.event,
            'response_type': self.response_type,
            'urgency': self.urgency,
            'severity': self.severity,
            'certainty': self.certainty,
            'audience': self.audience,
            'event_code': self.event_code,
            'effective': self.effective.isoformat() if self.effective else None,
            'onset': self.onset.isoformat() if self.onset else None,
            'expires': self.expires.isoformat() if self.expires else None,
            'sender_name': self.sender_name,
            'headline': self.headline,
            'description': self.description,
            'instruction': self.instruction,
            'web': self.web,
            'contact': self.contact,
            'parameter': self.parameter,
        }
    
    def _format_cap_datetime(self, dt):
        """Return datetime as-is - no formatting should be done in the model"""
        if dt is None:
            return None
        return dt.isoformat()
    
    def _xml_escape(self, text):
        """Escape text for XML output"""
        if text is None:
            return ""
        return html.escape(str(text))
    
    def _add_text_element(self, parent, tag, text, namespace="cap"):
        """Add a text element to XML parent"""
        if text is not None and str(text).strip():
            element = ET.SubElement(parent, f"{namespace}:{tag}")
            element.text = str(text).strip()
            return element
        return None
    
    def _add_list_elements(self, parent, tag, items, namespace="cap"):
        """Add multiple elements for list items"""
        if items and isinstance(items, list):
            for item in items:
                if item and str(item).strip():
                    element = ET.SubElement(parent, f"{namespace}:{tag}")
                    element.text = str(item).strip()
    
    def _add_value_name_value_elements(self, parent, tag, items, namespace="cap"):
        """Add valueName/value elements for structured data"""
        if items and isinstance(items, list):
            for item in items:
                if isinstance(item, dict) and 'valueName' in item and 'value' in item:
                    element = ET.SubElement(parent, f"{namespace}:{tag}")
                    
                    value_name_elem = ET.SubElement(element, f"{namespace}:valueName")
                    value_name_elem.text = str(item['valueName']).strip()
                    
                    value_elem = ET.SubElement(element, f"{namespace}:value")
                    value_elem.text = str(item['value']).strip()
    
    def to_xml(self):
        """Generate CAP 1.2 compliant XML for info block"""
        info_elem = ET.Element("cap:info")
        
        # Required info elements - in correct CAP 1.2 order
        self._add_text_element(info_elem, "language", self.language or "en-US")
        self._add_list_elements(info_elem, "category", self.category)
        self._add_text_element(info_elem, "event", self.event)
        self._add_list_elements(info_elem, "responseType", self.response_type)
        self._add_text_element(info_elem, "urgency", self.urgency)
        self._add_text_element(info_elem, "severity", self.severity)
        self._add_text_element(info_elem, "certainty", self.certainty)
        
        # Optional info elements - in correct CAP 1.2 order
        self._add_text_element(info_elem, "audience", self.audience)
        self._add_value_name_value_elements(info_elem, "eventCode", self.event_code)
        self._add_text_element(info_elem, "effective", self._format_cap_datetime(self.effective))
        self._add_text_element(info_elem, "onset", self._format_cap_datetime(self.onset))
        self._add_text_element(info_elem, "expires", self._format_cap_datetime(self.expires))
        self._add_text_element(info_elem, "senderName", self.sender_name)
        self._add_text_element(info_elem, "headline", self.headline)
        self._add_text_element(info_elem, "description", self.description)
        self._add_text_element(info_elem, "instruction", self.instruction)
        self._add_text_element(info_elem, "web", self.web)
        self._add_text_element(info_elem, "contact", self.contact)
        self._add_value_name_value_elements(info_elem, "parameter", self.parameter)
        
        # Add resources
        for resource in self.resources.all():
            resource_xml = resource.to_xml()
            info_elem.append(resource_xml)
        
        # Add areas
        for area in self.areas.all():
            area_xml = area.to_xml()
            info_elem.append(area_xml)
        
        return info_elem
    
    def to_json(self):
        """Generate JSON representation of CAP info data"""
        info_data = {
            "language": self.language or "en-US",
            "category": self.category,
            "event": self.event,
            "responseType": self.response_type,
            "urgency": self.urgency,
            "severity": self.severity,
            "certainty": self.certainty,
            "audience": self.audience,
            "eventCode": self.event_code,
            "effective": self._format_cap_datetime(self.effective),
            "onset": self._format_cap_datetime(self.onset),
            "expires": self._format_cap_datetime(self.expires),
            "senderName": self.sender_name,
            "headline": self.headline,
            "description": self.description,
            "instruction": self.instruction,
            "web": self.web,
            "contact": self.contact,
            "parameter": self.parameter,
            "resource": [],
            "area": []
        }
        
        # Add resources
        for resource in self.resources.all():
            resource_data = resource.to_json()
            info_data["resource"].append(resource_data)
        
        # Add areas
        for area in self.areas.all():
            area_data = area.to_json()
            info_data["area"].append(area_data)
        
        return info_data
    
    def to_engage_weatherwarning(self) -> 'EngageWeatherWarningInfo':
        """Convert to EngageWeatherWarningInfo object"""
        # Convert datetime fields to Unix timestamps
        effective_unix = int(self.effective.timestamp()) if self.effective else None
        onset_unix = int(self.onset.timestamp()) if self.onset else None
        expires_unix = int(self.expires.timestamp()) if self.expires else None
        
        # Convert areas to EngageWeatherWarningArea objects
        areas = [area.to_engage_weatherwarning() for area in self.areas.all()]
        
        return EngageWeatherWarningInfo(
            category=self.category[0] if self.category and len(self.category) > 0 else "Met",
            event=self.event,
            responseType=self.response_type,
            urgency=self.urgency,
            severity=self.severity,
            certainty=self.certainty,
            effective=effective_unix,
            onset=onset_unix,
            expires=expires_unix,
            senderName=self.sender_name,
            headline=self.headline,
            description=self.description,
            instruction=self.instruction,
            web=self.web,
            contact=self.contact,
            parameter=self.parameter,
            area=areas
        )


class CAPArea(models.Model):
    """CAP Area model - represents the affected area of an alert message"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    info = models.ForeignKey(CAPInfo, on_delete=models.CASCADE, related_name='areas')
    area_desc = models.TextField()
    polygon = gis_models.PolygonField(blank=True, null=True)  # PostGIS
    circle = gis_models.PointField(blank=True, null=True)  # PostGIS
    circle_radius = models.FloatField(blank=True, null=True)  # radius in kilometers
    geocode = models.JSONField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    ceiling = models.FloatField(blank=True, null=True)
    
    class Meta:
        db_table = 'cap_areas'

    def to_dict(self):
        return {
            'id': self.id,
            'info_id': self.info.id,
            'area_desc': self.area_desc,
            'polygon': str(self.polygon) if self.polygon else None,
            'circle': str(self.circle) if self.circle else None,
            'circle_radius': self.circle_radius,
            'geocode': self.geocode,
            'altitude': self.altitude,
            'ceiling': self.ceiling,
        }
    
    def _add_text_element(self, parent, tag, text, namespace="cap"):
        """Add a text element to XML parent"""
        if text is not None and str(text).strip():
            element = ET.SubElement(parent, f"{namespace}:{tag}")
            element.text = str(text).strip()
            return element
        return None
    
    def _add_value_name_value_elements(self, parent, tag, items, namespace="cap"):
        """Add valueName/value elements for structured data"""
        if items and isinstance(items, list):
            for item in items:
                if isinstance(item, dict) and 'valueName' in item and 'value' in item:
                    element = ET.SubElement(parent, f"{namespace}:{tag}")
                    
                    value_name_elem = ET.SubElement(element, f"{namespace}:valueName")
                    value_name_elem.text = str(item['valueName']).strip()
                    
                    value_elem = ET.SubElement(element, f"{namespace}:value")
                    value_elem.text = str(item['value']).strip()
    
    def _format_polygon_coords(self, polygon):
        """Format PostGIS polygon to CAP coordinate string"""
        if polygon is None or not hasattr(polygon, 'coords'):
            return None
        
        coords = list(polygon.coords[0])  # Get exterior ring
        coord_strings = []
        for coord in coords:
            lon, lat = coord
            coord_strings.append(f"{lat},{lon}")  # CAP uses lat,lon format
        
        return " ".join(coord_strings)
    
    def _format_circle_coords(self, circle, radius):
        """Format PostGIS point and radius to CAP circle string"""
        if circle is None or not hasattr(circle, 'coords') or radius is None:
            return None
        
        coords = circle.coords
        lon, lat = coords
        return f"{lat},{lon} {radius}"  # CAP uses lat,lon radius format
    
    def to_xml(self):
        """Generate CAP 1.2 compliant XML for area block"""
        area_elem = ET.Element("cap:area")
        
        # Area elements in correct CAP 1.2 order
        self._add_text_element(area_elem, "areaDesc", self.area_desc)
        
        # Add polygon
        polygon_coords = self._format_polygon_coords(self.polygon)
        if polygon_coords:
            self._add_text_element(area_elem, "polygon", polygon_coords)
        
        # Add circle
        circle_coords = self._format_circle_coords(self.circle, self.circle_radius)
        if circle_coords:
            self._add_text_element(area_elem, "circle", circle_coords)
        
        # Add geocodes
        self._add_value_name_value_elements(area_elem, "geocode", self.geocode)
        
        # Add altitude and ceiling
        self._add_text_element(area_elem, "altitude", self.altitude)
        self._add_text_element(area_elem, "ceiling", self.ceiling)
        
        return area_elem
    
    def to_json(self):
        """Generate JSON representation of CAP area data"""
        return {
            "areaDesc": self.area_desc,
            "polygon": self._format_polygon_coords(self.polygon),
            "circle": self._format_circle_coords(self.circle, self.circle_radius),
            "geocode": self.geocode,
            "altitude": self.altitude,
            "ceiling": self.ceiling
        }
    
    def to_engage_weatherwarning(self) -> 'EngageWeatherWarningArea':
        """Convert to EngageWeatherWarningArea object"""
        return EngageWeatherWarningArea(
            areaDesc=self.area_desc,
            polygon=self._format_polygon_coords(self.polygon) if self.polygon else None
        )


class CAPResource(models.Model):
    """CAP Resource model - represents additional files with supplemental information"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    info = models.ForeignKey(CAPInfo, on_delete=models.CASCADE, related_name='resources')
    resource_desc = models.TextField()
    mime_type = models.CharField(max_length=100)
    size = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=500, blank=True, null=True)
    deref_uri = models.TextField(blank=True, null=True)  # base64 encoded
    digest = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'cap_resources'

    def to_dict(self):
        return {
            'id': self.id,
            'info_id': self.info.id,
            'resource_desc': self.resource_desc,
            'mime_type': self.mime_type,
            'size': self.size,
            'uri': self.uri,
            'deref_uri': self.deref_uri,
            'digest': self.digest,
        }
    
    def _add_text_element(self, parent, tag, text, namespace="cap"):
        """Add a text element to XML parent"""
        if text is not None and str(text).strip():
            element = ET.SubElement(parent, f"{namespace}:{tag}")
            element.text = str(text).strip()
            return element
        return None
    
    def to_xml(self):
        """Generate CAP 1.2 compliant XML for resource block"""
        resource_elem = ET.Element("cap:resource")
        
        self._add_text_element(resource_elem, "resourceDesc", self.resource_desc)
        self._add_text_element(resource_elem, "mimeType", self.mime_type)
        self._add_text_element(resource_elem, "size", self.size)
        self._add_text_element(resource_elem, "uri", self.uri)
        self._add_text_element(resource_elem, "derefUri", self.deref_uri)
        self._add_text_element(resource_elem, "digest", self.digest)
        
        return resource_elem
    
    def to_json(self):
        """Generate JSON representation of CAP resource data"""
        return {
            "resourceDesc": self.resource_desc,
            "mimeType": self.mime_type,
            "size": self.size,
            "uri": self.uri,
            "derefUri": self.deref_uri,
            "digest": self.digest
        }


class EngageWeatherWarningArea:
    """Data class for Engage Weather Warning Area"""
    def __init__(self, areaDesc: str, polygon: str = None):
        self.areaDesc = areaDesc
        self.polygon = polygon
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'areaDesc': self.areaDesc,
            'polygon': self.polygon
        }


class EngageWeatherWarningInfo:
    """Data class for Engage Weather Warning Info"""
    def __init__(self, category: str, event: str, responseType: list = None, 
                 urgency: str = None, severity: str = None, certainty: str = None,
                 effective: int = None, onset: int = None, expires: int = None,
                 senderName: str = None, headline: str = None, description: str = None,
                 instruction: str = None, web: str = None, contact: str = None,
                 parameter: list = None, area: list = None):
        self.category = category
        self.event = event
        self.responseType = responseType or []
        self.urgency = urgency
        self.severity = severity
        self.certainty = certainty
        self.effective = effective
        self.onset = onset
        self.expires = expires
        self.senderName = senderName
        self.headline = headline
        self.description = description
        self.instruction = instruction
        self.web = web
        self.contact = contact
        self.parameter = parameter or []
        self.area = area or []
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'category': self.category,
            'event': self.event,
            'responseType': self.responseType,
            'urgency': self.urgency,
            'severity': self.severity,
            'certainty': self.certainty,
            'effective': self.effective,
            'onset': self.onset,
            'expires': self.expires,
            'senderName': self.senderName,
            'headline': self.headline,
            'description': self.description,
            'instruction': self.instruction,
            'web': self.web,
            'contact': self.contact,
            'parameter': self.parameter,
            'area': [item.to_dict() if hasattr(item, 'to_dict') else str(item) for item in self.area]
        }


class EngageWeatherWarningAlert:
    """Data class for Engage Weather Warning Alert"""
    def __init__(self, identifier: str, sender: str, sent: int, status: str, 
                 msgType: str, scope: str, code: list = None, note: str = None,
                 references: str = None, incidents: str = None, info: list = None):
        self.identifier = identifier
        self.sender = sender
        self.sent = sent
        self.status = status
        self.msgType = msgType
        self.scope = scope
        self.code = code or ["MET"]
        self.note = note
        self.references = references
        self.incidents = incidents
        self.info = info or []
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'identifier': self.identifier,
            'sender': self.sender,
            'sent': self.sent,
            'status': self.status,
            'msgType': self.msgType,
            'scope': self.scope,
            'code': self.code,
            'note': self.note,
            'references': self.references,
            'incidents': self.incidents,
            'info': [item.to_dict() if hasattr(item, 'to_dict') else str(item) for item in self.info]
        }