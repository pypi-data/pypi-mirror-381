"""
Engage API Response Models
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class EngageWeatherWarningArea:
    """Engage Weather Warning Area model"""
    areaDesc: str
    polygon: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'areaDesc': self.areaDesc,
            'polygon': self.polygon
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EngageWeatherWarningArea':
        """Create from dictionary"""
        return cls(
            areaDesc=data['areaDesc'],
            polygon=data.get('polygon')
        )


@dataclass
class EngageWeatherWarningInfo:
    """Engage Weather Warning Info model"""
    category: str
    event: str
    responseType: Optional[List[str]] = None
    urgency: Optional[str] = None
    severity: Optional[str] = None
    certainty: Optional[str] = None
    effective: Optional[int] = None
    onset: Optional[int] = None
    expires: Optional[int] = None
    senderName: Optional[str] = None
    headline: Optional[str] = None
    description: Optional[str] = None
    instruction: Optional[str] = None
    web: Optional[str] = None
    contact: Optional[str] = None
    parameter: Optional[List[Dict[str, str]]] = None
    area: Optional[List[EngageWeatherWarningArea]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'category': self.category,
            'event': self.event,
            'responseType': self.responseType or [],
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
            'parameter': self.parameter or [],
            'area': [area.to_dict() for area in (self.area or [])]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EngageWeatherWarningInfo':
        """Create from dictionary"""
        areas = []
        if data.get('area'):
            areas = [EngageWeatherWarningArea.from_dict(area_data) for area_data in data['area']]
        
        return cls(
            category=data['category'],
            event=data['event'],
            responseType=data.get('responseType'),
            urgency=data.get('urgency'),
            severity=data.get('severity'),
            certainty=data.get('certainty'),
            effective=data.get('effective'),
            onset=data.get('onset'),
            expires=data.get('expires'),
            senderName=data.get('senderName'),
            headline=data.get('headline'),
            description=data.get('description'),
            instruction=data.get('instruction'),
            web=data.get('web'),
            contact=data.get('contact'),
            parameter=data.get('parameter'),
            area=areas
        )


@dataclass
class EngageWeatherWarningAlert:
    """Engage Weather Warning Alert model"""
    identifier: str
    sender: str
    sent: int
    status: str
    msgType: str
    scope: str
    code: Optional[List[str]] = None
    note: Optional[str] = None
    references: Optional[str] = None
    incidents: Optional[str] = None
    info: Optional[List[EngageWeatherWarningInfo]] = None
    
    def to_dict(self) -> Dict[str, Any]:
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
            'info': [info.to_dict() for info in (self.info or [])]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EngageWeatherWarningAlert':
        """Create from dictionary"""
        info_list = []
        if data.get('info'):
            info_list = [EngageWeatherWarningInfo.from_dict(info_data) for info_data in data['info']]
        
        return cls(
            identifier=data['identifier'],
            sender=data['sender'],
            sent=data['sent'],
            status=data['status'],
            msgType=data['msgType'],
            scope=data['scope'],
            code=data.get('code'),
            note=data.get('note'),
            references=data.get('references'),
            incidents=data.get('incidents'),
            info=info_list
        )


@dataclass
class EngageAPIResponse:
    """Engage API Response model"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    status_code: Optional[int] = None
    errors: Optional[List[str]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'success': self.success,
            'data': self.data,
            'message': self.message,
            'status_code': self.status_code,
            'errors': self.errors or []
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EngageAPIResponse':
        """Create from dictionary"""
        return cls(
            success=data.get('success', False),
            data=data.get('data'),
            message=data.get('message'),
            status_code=data.get('status_code'),
            errors=data.get('errors')
        )


@dataclass
class EngageHealthCheck:
    """Engage API Health Check model"""
    status: str
    timestamp: Optional[int] = None
    version: Optional[str] = None
    uptime: Optional[int] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'status': self.status,
            'timestamp': self.timestamp,
            'version': self.version,
            'uptime': self.uptime
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EngageHealthCheck':
        """Create from dictionary"""
        return cls(
            status=data['status'],
            timestamp=data.get('timestamp'),
            version=data.get('version'),
            uptime=data.get('uptime')
        )
