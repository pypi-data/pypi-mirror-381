# CAP Manager API Documentation

## Overview

The `CAPManager` class provides a comprehensive interface for managing CAP alerts with full CRUD operations, advanced filtering, and external API integration.

## Basic Usage

```python
from cap_alerts.manager import CAPManager

manager = CAPManager()
```

## Alert Management

### create_alert(data)
Creates a new CAP alert from dictionary data with validation.

**Parameters:**
- `data` (dict): Alert data dictionary

**Returns:** CAPAlert instance

**Raises:** CAPAlertValidationError

**Example:**
```python
from datetime import datetime, timedelta

now = datetime.now()
alert_data = {
    # Alert level fields (required)
    'identifier': 'GR-ATHENS-20250110-001',
    'sender': 'weather@example.com',
    'sent': now.strftime('%Y-%m-%dT%H:%M:%S+00:00'),
    'status': 'Actual',  # Actual, Exercise, System, Test, Draft
    'msg_type': 'Alert',  # Alert, Update, Cancel, Ack, Error
    'scope': 'Public',   # Public, Restricted, Private
    
    # Optional alert fields
    'source': 'National Weather Service',
    'code': ['MET', 'SEVERE', 'THUNDERSTORM'],
    'note': 'Severe weather warning for Athens metropolitan area',
    'references': ['weather@example.com,GR-ATHENS-20250109-001,2025-01-09T15:00:00+00:00'],
    'incidents': ['INC-ATHENS-20250110-001'],
    
    # Info blocks (at least one required)
    'info': [
        {
            # Required info fields
            'language': 'en-US',
            'category': ['Met'],  # Geo, Met, Safety, Security, Rescue, Fire, Health, Env, Transport, Infra, CBRNE, Other
            'event': 'Severe Thunderstorm Warning',
            'urgency': 'Immediate',  # Immediate, Expected, Future, Past, Unknown
            'severity': 'Severe',    # Extreme, Severe, Moderate, Minor, Unknown
            'certainty': 'Observed', # Observed, Likely, Possible, Unlikely, Unknown
            
            # Optional info fields
            'response_type': ['Monitor', 'Prepare', 'Execute'],
            'audience': 'General public and emergency services',
            'event_code': [
                {'valueName': 'SAME', 'value': 'SVR'},
                {'valueName': 'FIPS', 'value': '12345'},
                {'valueName': 'UGC', 'value': 'GRC001'}
            ],
            'effective': now.strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            'onset': (now + timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            'expires': (now + timedelta(hours=3)).strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            'sender_name': 'National Weather Service Athens',
            'headline': 'Severe Thunderstorm Warning for Athens',
            'description': 'A severe thunderstorm is approaching the Athens metropolitan area with potential for damaging winds, large hail, and heavy rainfall.',
            'instruction': 'Seek shelter immediately in a sturdy building. Stay away from windows and avoid driving if possible.',
            'web': 'https://weather.gov/alerts/athens-severe',
            'contact': 'weather@example.com, emergency@example.com',
            'parameter': [
                {'valueName': 'WindSpeed', 'value': '70 mph'},
                {'valueName': 'HailSize', 'value': '1.5 inches'},
                {'valueName': 'Rainfall', 'value': '2 inches/hour'}
            ],
            
            # Areas (at least one required)
            'areas': [
                {
                    'area_desc': 'Athens Metropolitan Area',
                    'polygon': 'POLYGON((23.7348 37.9755, 23.8348 37.9755, 23.8348 37.8755, 23.7348 37.8755, 23.7348 37.9755))',
                    'geocode': [
                        {'valueName': 'FIPS6', 'value': '123456'},
                        {'valueName': 'UGC', 'value': 'GRC001'},
                        {'valueName': 'ISO3166-2', 'value': 'GR-A1'}
                    ],
                    'altitude': 0.0,
                    'ceiling': 1000.0
                }
            ],
            
            # Resources (optional)
            'resources': [
                {
                    'resource_desc': 'Weather radar image',
                    'mime_type': 'image/png',
                    'size': 1024000,
                    'uri': 'https://example.com/radar-athens.png',
                    'deref_uri': 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==',
                    'digest': 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
                }
            ]
        }
    ]
}

alert = manager.create_alert(alert_data)
```

> **Note:** This example follows the [OASIS CAP v1.2 specification](https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html) and includes all required fields plus common optional fields for a complete weather alert.

### get_alert(identifier_or_id)
Retrieves an alert by identifier or UUID.

**Parameters:**
- `identifier_or_id` (str/UUID): Alert identifier or UUID

**Returns:** CAPAlert instance

**Raises:** CAPAlertNotFound

**Example:**
```python
alert = manager.get_alert('alert-123')
# or
alert = manager.get_alert('550e8400-e29b-41d4-a716-446655440000')
```

### update_alert(identifier_or_id, data)
Updates an existing alert with validation.

**Parameters:**
- `identifier_or_id` (str/UUID): Alert identifier or UUID
- `data` (dict): Update data dictionary

**Returns:** Updated CAPAlert instance

**Raises:** CAPAlertNotFound, CAPAlertValidationError

**Example:**
```python
updated_alert = manager.update_alert('alert-123', {'status': 'Exercise'})
```

### delete_alert(identifier_or_id)
Deletes an alert by identifier or UUID.

**Parameters:**
- `identifier_or_id` (str/UUID): Alert identifier or UUID

**Returns:** True if successful

**Raises:** CAPAlertNotFound, CAPAlertValidationError

**Example:**
```python
success = manager.delete_alert('alert-123')
```

## Advanced Filtering

### list_alerts(filters=None, order_by='-sent', count_only=False)
Lists alerts with advanced filtering across all entities.

**Parameters:**
- `filters` (dict, optional): Filter criteria
- `order_by` (str, optional): Ordering field (default: '-sent')
- `count_only` (bool, optional): Return count only (default: False)

**Returns:** QuerySet or count

**Filter Examples:**
```python
# Basic filters
filters = {
    'status': 'Actual',
    'sender__icontains': 'admin',
    'sent__gte': '2023-01-01'
}

# Related field filters
filters = {
    'info_blocks__severity': 'Extreme',
    'info_blocks__areas__area_desc__icontains': 'Athens'
}

alerts = manager.list_alerts(filters)
```

### get_alerts_by_status(status)
Gets alerts by status.

**Parameters:**
- `status` (str): Alert status

**Returns:** QuerySet

### get_alerts_by_sender(sender)
Gets alerts by sender.

**Parameters:**
- `sender` (str): Sender identifier

**Returns:** QuerySet

### get_alerts_by_date_range(start_date, end_date)
Gets alerts within date range.

**Parameters:**
- `start_date` (str): Start date (ISO format)
- `end_date` (str): End date (ISO format)

**Returns:** QuerySet

### search_alerts(query)
Full text search across multiple fields.

**Parameters:**
- `query` (str): Search query

**Returns:** QuerySet

**Example:**
```python
results = manager.search_alerts('weather warning')
```

## External API Integration

### get_engage_weather_warning(identifier_or_id)
Converts alert to Engage Weather Warning format.

**Parameters:**
- `identifier_or_id` (str/UUID): Alert identifier or UUID

**Returns:** Engage Weather Warning object

**Raises:** CAPAlertNotFound, CAPAlertValidationError

### send_alert(alert, receiver)
Sends alert to external service asynchronously.

**Parameters:**
- `alert` (CAPAlert): Alert instance
- `receiver` (str): 'engage' or 'meteoalarm'

**Returns:** Task result message

**Raises:** ValueError, CAPAlertValidationError

**Example:**
```python
result = manager.send_alert(alert, 'engage')
```

## Task Management

### get_task(task_id)
Gets task by UUID with associated alert data.

**Parameters:**
- `task_id` (UUID): Task UUID

**Returns:** CAPTask instance

**Raises:** CAPAlertNotFound

### list_tasks(filters=None, order_by='-created_at', count_only=False)
Lists tasks with advanced filtering.

**Parameters:**
- `filters` (dict, optional): Filter criteria
- `order_by` (str, optional): Ordering field (default: '-created_at')
- `count_only` (bool, optional): Return count only (default: False)

**Returns:** QuerySet or count

**Filter Examples:**
```python
filters = {
    'status': 'success',
    'client': 'engage',
    'response_status_code': 200
}
tasks = manager.list_tasks(filters)
```

### get_tasks_by_status(status)
Gets tasks by status.

**Parameters:**
- `status` (str): Task status

**Returns:** QuerySet

### get_tasks_by_client(client)
Gets tasks by client.

**Parameters:**
- `client` (str): 'engage' or 'meteoalarm'

**Returns:** QuerySet

### get_tasks_by_alert(alert_identifier_or_id)
Gets tasks for a specific alert.

**Parameters:**
- `alert_identifier_or_id` (str/UUID): Alert identifier or UUID

**Returns:** QuerySet

### get_tasks_by_date_range(start_date, end_date)
Gets tasks within date range.

**Parameters:**
- `start_date` (str): Start date (ISO format)
- `end_date` (str): End date (ISO format)

**Returns:** QuerySet

### get_failed_tasks()
Gets all failed tasks.

**Returns:** QuerySet

### get_successful_tasks()
Gets all successful tasks.

**Returns:** QuerySet

### get_pending_tasks()
Gets all pending tasks.

**Returns:** QuerySet

### get_processing_tasks()
Gets all processing tasks.

**Returns:** QuerySet

### get_tasks_by_response_code(status_code)
Gets tasks by HTTP response status code.

**Parameters:**
- `status_code` (int): HTTP status code

**Returns:** QuerySet

### get_tasks_with_errors()
Gets tasks that have error messages.

**Returns:** QuerySet

### search_tasks(query)
Full text search across task and alert fields.

**Parameters:**
- `query` (str): Search query

**Returns:** QuerySet

### update_task_status(task_id, status)
Updates task status with validation.

**Parameters:**
- `task_id` (UUID): Task UUID
- `status` (str): New status

**Returns:** Updated CAPTask instance

**Raises:** CAPAlertNotFound, CAPAlertValidationError

### delete_task(task_id)
Deletes task by UUID.

**Parameters:**
- `task_id` (UUID): Task UUID

**Returns:** True if successful

**Raises:** CAPAlertNotFound, CAPAlertValidationError

## Error Handling

The manager uses custom exceptions:

- `CAPAlertNotFound`: When alert/task is not found
- `CAPAlertValidationError`: When validation fails or other errors occur

## Examples

### Complete Workflow
```python
from cap_alerts.manager import CAPManager

manager = CAPManager()

# Create alert
alert = manager.create_alert(alert_data)

# Send to external services
manager.send_alert(alert, 'engage')
manager.send_alert(alert, 'meteoalarm')

# Check task status
tasks = manager.get_tasks_by_alert(alert.identifier)
for task in tasks:
    print(f"Task {task.id}: {task.status}")

# Search and filter
recent_alerts = manager.get_alerts_by_date_range('2023-01-01', '2023-12-31')
extreme_alerts = manager.list_alerts({'info_blocks__severity': 'Extreme'})
```
