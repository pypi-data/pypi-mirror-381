"""
Celery tasks for CAP Alerts
"""

from celery import shared_task
from django.utils import timezone
from .models import CAPTask, CAPAlert
from .engage.engage_client import EngageClient
from .engage.engage_exceptions import EngageAPIError, EngageConnectionError
from .meteoalarm.meteoalarm_client import MeteoalarmClient
from .meteoalarm.meteoalarm_exceptions import MeteoalarmAPIError, MeteoalarmConnectionError
import json


@shared_task(bind=True, max_retries=3)
def send_alert_task(self, task_id):
    """
    Send alert to external service (Engage or Meteoalarm)
    
    Args:
        task_id: UUID of CAPTask instance
    """
    try:
        # Get the task
        task = CAPTask.objects.get(id=task_id)
        task.status = 'processing'
        task.sent_at = timezone.now()  # Set sent_at when task starts processing
        task.save()
        
        # Get the alert
        alert = task.alert
        
        if task.client == 'engage':
            _send_to_engage(task, alert)
        elif task.client == 'meteoalarm':
            _send_to_meteoalarm(task, alert)
        else:
            raise ValueError(f"Unknown client: {task.client}")
            
        # Mark as successful
        task.status = 'success'
        task.save()
        
        return f"Successfully sent alert {alert.identifier} to {task.client}"
        
    except CAPTask.DoesNotExist:
        return f"Task {task_id} not found"
    except Exception as exc:
        # Update task with error
        try:
            task = CAPTask.objects.get(id=task_id)
            task.status = 'failed'
            task.error_message = str(exc)
            # If response_body is not set yet, set it with error info
            if not task.response_body:
                task.response_body = json.dumps({
                    'error': str(exc),
                    'status_code': 500
                }, indent=2)
                task.response_status_code = 500
            task.save()
        except:
            pass
            
        # Retry if we haven't exceeded max retries
        if self.request.retries < self.max_retries:
            raise self.retry(countdown=60 * (2 ** self.request.retries))
        
        return f"Failed to send alert: {exc}"


def _send_to_engage(task, alert):
    """Send alert to Engage API"""
    try:
        # Convert alert to Engage format
        engage_alert = alert.to_engage_weatherwarning()
        
        # Store request body
        task.request_body = json.dumps(engage_alert.to_dict(), indent=2)
        task.save()
        
        # Create client and send
        client = EngageClient()
        response = client.send_weather_warning(engage_alert)
        
        # Store successful response
        task.response_body = json.dumps(response, indent=2)
        task.response_status_code = 200
        task.save()
        
    except (EngageAPIError, EngageConnectionError) as e:
        # Store error response
        task.error_message = str(e)
        task.response_status_code = getattr(e, 'status_code', 500)
        task.response_body = json.dumps({
            'error': str(e),
            'status_code': getattr(e, 'status_code', 500)
        }, indent=2)
        task.save()
        raise
    except Exception as e:
        # Store general error
        task.error_message = str(e)
        task.response_status_code = 500
        task.response_body = json.dumps({
            'error': str(e),
            'status_code': 500
        }, indent=2)
        task.save()
        raise


def _send_to_meteoalarm(task, alert):
    """Send alert to Meteoalarm API"""
    try:
        # Store request body (XML)
        task.request_body = alert.to_xml()
        task.save()
        
        # Create client and send
        client = MeteoalarmClient()
        response = client.send_weather_warning(alert)
        
        # Store successful response
        task.response_body = json.dumps(response, indent=2)
        task.response_status_code = 200
        task.save()
        
    except (MeteoalarmAPIError, MeteoalarmConnectionError) as e:
        # Store error response
        task.error_message = str(e)
        task.response_status_code = getattr(e, 'status_code', 500)
        task.response_body = json.dumps({
            'error': str(e),
            'status_code': getattr(e, 'status_code', 500)
        }, indent=2)
        task.save()
        raise
    except Exception as e:
        # Store general error
        task.error_message = str(e)
        task.response_status_code = 500
        task.response_body = json.dumps({
            'error': str(e),
            'status_code': 500
        }, indent=2)
        task.save()
        raise


@shared_task
def send_alert(alert_id, receiver):
    """
    Send alert to specified receiver (engage or meteoalarm)
    
    Args:
        alert_id: CAPAlert ID (UUID)
        receiver: 'engage' or 'meteoalarm'
    """
    # Validate receiver
    if receiver not in ['engage', 'meteoalarm']:
        raise ValueError(f"Invalid receiver: {receiver}. Must be 'engage' or 'meteoalarm'")
    
    try:
        # Get the alert
        alert = CAPAlert.objects.get(id=alert_id)
        
        # Create task
        task = CAPTask.objects.create(
            alert=alert,
            client=receiver,
            status='pending'
        )
        
        # Queue the task
        send_alert_task.delay(task.id)
        
        return f"Queued {receiver} task {task.id} for alert {alert.identifier}"
        
    except CAPAlert.DoesNotExist:
        return f"Alert {alert_id} not found"
    except Exception as e:
        return f"Error creating {receiver} task: {e}"


