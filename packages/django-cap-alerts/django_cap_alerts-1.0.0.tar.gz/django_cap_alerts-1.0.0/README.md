# Django CAP Alerts

A Django package for handling CAP (Common Alerting Protocol) alerts with PostGIS support, external API integrations, and Celery task processing.

## Features

- **CAP Alert Models**: Complete Django models for CAP alert structure following [OASIS CAP v1.2 specification](https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html)
- **PostGIS Support**: Geographic data handling with PostGIS
- **REST API**: Django REST Framework serializers for API endpoints
- **External Integrations**: 
  - Meteoalarm API integration
  - Engage API integration
- **Celery Tasks**: Asynchronous alert processing
- **Validation**: Comprehensive CAP specification validation
- **Manager Class**: Business logic layer for CRUD operations

## Installation

```bash
pip install django-cap-alerts
```

## Requirements

- Django 4.2+
- PostgreSQL 16+ with PostGIS 3.4+ extension
- Redis 7+ (for Celery)
- Python 3.8+

## Quick Start

1. **Add to INSTALLED_APPS**:

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.gis',  # PostGIS support
    'rest_framework',
    'rest_framework_gis',
    'cap_alerts',  # Add this
]
```

2. **Configure Database**:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. **Run Migrations**:

```bash
python manage.py migrate
```

4. **Configure External APIs** (Optional):

```python
# settings.py
METEOALARM_BASE_URL = 'https://your-meteoalarm-api.com'
METEOALARM_API_KEY = 'your-api-key'
METEOALARM_TIMEOUT = 30

ENGAGE_BASE_URL = 'https://your-engage-api.com'
ENGAGE_API_KEY = 'your-jwt-token'
ENGAGE_TIMEOUT = 30
```

5. **Configure Celery** (Optional):

```python
# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

## Usage

### Creating Alerts

```python
from cap_alerts.manager import CAPManager

manager = CAPManager()

# Create a new alert
alert_data = {
    'identifier': 'unique-alert-id',
    'sender': 'sender@example.com',
    'sent': '2023-12-01T10:00:00Z',
    'status': 'Actual',
    'msg_type': 'Alert',
    'scope': 'Public',
    'info': [
        {
            'language': 'en',
            'category': 'Met',
            'event': 'Severe Weather',
            'urgency': 'Immediate',
            'severity': 'Extreme',
            'certainty': 'Observed',
            'headline': 'Severe Weather Warning',
            'description': 'Severe weather conditions expected',
            'areas': [
                {
                    'area_desc': 'Athens, Greece',
                    'polygon': 'POINT(23.7275 37.9838)',
                }
            ]
        }
    ]
}

alert = manager.create_alert(alert_data)
```

### Retrieving Alerts

```python
# Get alert by identifier
alert = manager.get_alert('unique-alert-id')

# List alerts with filters
alerts = manager.list_alerts({
    'status': 'Actual',
    'sent__gte': '2023-01-01',
    'info_blocks__severity': 'Extreme'
})

# Search alerts
results = manager.search_alerts('weather warning')
```

### External API Integration

```python
from cap_alerts.manager import CAPManager

manager = CAPManager()

# Send alert to external services
result = manager.send_alert(alert, 'engage')
result = manager.send_alert(alert, 'meteoalarm')
```

### CAP Tasks Management

```python
# Get task details
task = manager.get_task(task_id)

# List tasks with filters
tasks = manager.list_tasks({
    'status': 'success',
    'client': 'engage',
    'created_at__gte': '2023-01-01'
})

# Get tasks by status
failed_tasks = manager.get_failed_tasks()
successful_tasks = manager.get_successful_tasks()
```

## Models

The package provides the following main models:

- **CAPAlert**: Main alert container
- **CAPInfo**: Alert information blocks
- **CAPArea**: Geographic areas
- **CAPResource**: Alert resources (images, files, etc.)
- **CAPTask**: Task tracking for external API calls

## API Documentation

For detailed API documentation including all manager methods, filtering options, and advanced usage examples, see:

- [Manager Documentation](docs/MANAGER_DOCS.md)

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Support

For issues and questions, please use the GitHub issue tracker.
