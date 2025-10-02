"""
CAP Alerts - Manager Class
"""

from django.db.models import Q
from django.core.exceptions import ValidationError
from .models import CAPAlert, CAPInfo, CAPArea, CAPResource, CAPTask
from .exceptions import CAPAlertNotFound, CAPAlertValidationError
from .serializers import CAPAlertSerializer, CAPAlertUpdateSerializer
from .tasks import send_alert


class CAPManager:
    """Manager class for CAP alerts with full CRUD operations and advanced filtering"""
    
    def create_alert(self, data):
        """Create a new CAP alert from dictionary data with proper validation"""
        try:
            # Use serializer for validation and creation
            serializer = CAPAlertSerializer(data=data)
            if serializer.is_valid():
                alert = serializer.save()
                return alert
            else:
                # Convert serializer errors to our custom exception
                error_messages = []
                for field, errors in serializer.errors.items():
                    if isinstance(errors, list):
                        error_messages.extend([f"{field}: {error}" for error in errors])
                    else:
                        error_messages.append(f"{field}: {errors}")
                
                raise CAPAlertValidationError(f"Validation errors: {'; '.join(error_messages)}")
            
        except CAPAlertValidationError:
            raise
        except Exception as e:
            raise CAPAlertValidationError(f"Error creating alert: {e}")
    
    def get_alert(self, identifier_or_id):
        """Get alert by identifier or id (UUID)"""
        try:
            # Try to get by identifier first
            return CAPAlert.objects.select_related().prefetch_related(
                'info_blocks__areas', 'info_blocks__resources'
            ).get(identifier=identifier_or_id)
        except CAPAlert.DoesNotExist:
            try:
                # If not found by identifier, try by id (UUID)
                return CAPAlert.objects.select_related().prefetch_related(
                    'info_blocks__areas', 'info_blocks__resources'
                ).get(id=identifier_or_id)
            except CAPAlert.DoesNotExist:
                raise CAPAlertNotFound(f"Alert with identifier or id '{identifier_or_id}' not found")
            except (ValueError, Exception):
                # If identifier_or_id is not a valid UUID or any other error, raise the original error
                raise CAPAlertNotFound(f"Alert with identifier '{identifier_or_id}' not found")
    
    def update_alert(self, identifier_or_id, data):
        """Update existing alert with proper validation by identifier or id (UUID)"""
        try:
            alert = self.get_alert(identifier_or_id)
            
            # Use update serializer for validation and update
            serializer = CAPAlertUpdateSerializer(alert, data=data, partial=True)
            if serializer.is_valid():
                alert = serializer.save()
                return alert
            else:
                # Convert serializer errors to our custom exception
                error_messages = []
                for field, errors in serializer.errors.items():
                    if isinstance(errors, list):
                        error_messages.extend([f"{field}: {error}" for error in errors])
                    else:
                        error_messages.append(f"{field}: {errors}")
                
                raise CAPAlertValidationError(f"Validation errors: {'; '.join(error_messages)}")
            
        except CAPAlertNotFound:
            raise
        except CAPAlertValidationError:
            raise
        except Exception as e:
            raise CAPAlertValidationError(f"Error updating alert: {e}")
    
    def delete_alert(self, identifier_or_id):
        """Delete alert by identifier or id (UUID)"""
        try:
            alert = self.get_alert(identifier_or_id)
            alert.delete()
            return True
        except CAPAlertNotFound:
            raise
        except Exception as e:
            raise CAPAlertValidationError(f"Error deleting alert: {e}")
    
    def list_alerts(self, filters=None, order_by='-sent', count_only=False):
        """
        List alerts with advanced filtering across all entities
        
        filters = {
            # CAPAlert fields
            'sent__lte': '2023-05-12',
            'status': 'Actual',
            'sender__icontains': 'admin',
            'created_at__gte': '2023-01-01',
            'updated_at__lte': '2023-12-31',
            
            # CAPInfo fields (via info_blocks__)
            'info_blocks__severity': 'Extreme',
            'info_blocks__description__icontains': 'flood',
            'info_blocks__urgency__in': ['Immediate', 'Expected'],
            'info_blocks__event__icontains': 'earthquake',
            'info_blocks__category__contains': 'Geo',
            
            # CAPArea fields (via info_blocks__areas__)
            'info_blocks__areas__area_desc__icontains': 'Athens',
            'info_blocks__areas__altitude__gte': 100,
            'info_blocks__areas__ceiling__lte': 1000,
            
            # CAPResource fields (via info_blocks__resources__)
            'info_blocks__resources__mime_type': 'image/png',
            'info_blocks__resources__size__gte': 1024,
            'info_blocks__resources__resource_desc__icontains': 'map'
        }
        
        order_by options:
        - '-sent', 'sent' (default: -sent)
        - '-created_at', 'created_at'
        - '-updated_at', 'updated_at'
        - 'status', '-status'
        - 'sender', '-sender'
        - 'info_blocks__severity', '-info_blocks__severity'
        - 'info_blocks__urgency', '-info_blocks__urgency'
        - 'info_blocks__event', '-info_blocks__event'
        """
        try:
            queryset = CAPAlert.objects.select_related().prefetch_related(
                'info_blocks__areas', 'info_blocks__resources'
            ).all()
            
            if filters:
                # Build Q objects for complex filtering
                q_objects = Q()
                
                for field, value in filters.items():
                    if field.startswith('info_blocks__'):
                        # Handle related field filtering
                        q_objects &= Q(**{field: value})
                    else:
                        # Handle direct field filtering
                        q_objects &= Q(**{field: value})
                
                queryset = queryset.filter(q_objects)
            
            # Apply ordering
            if order_by:
                queryset = queryset.order_by(order_by)
            
            if count_only:
                return queryset.count()
            
            return queryset
            
        except Exception as e:
            raise CAPAlertValidationError(f"Error filtering alerts: {e}")
    
    def get_alerts_by_status(self, status):
        """Get alerts by status"""
        return self.list_alerts({'status': status})
    
    def get_alerts_by_sender(self, sender):
        """Get alerts by sender"""
        return self.list_alerts({'sender': sender})
    
    def get_alerts_by_date_range(self, start_date, end_date):
        """Get alerts within date range"""
        return self.list_alerts({
            'sent__gte': start_date,
            'sent__lte': end_date
        })
    
    def search_alerts(self, query):
        """Full text search across multiple fields"""
        return self.list_alerts({
            'identifier__icontains': query
        }) | self.list_alerts({
            'info_blocks__description__icontains': query
        }) | self.list_alerts({
            'info_blocks__headline__icontains': query
        }) | self.list_alerts({
            'info_blocks__event__icontains': query
        }) | self.list_alerts({
            'info_blocks__areas__area_desc__icontains': query
        })
    
    def get_engage_weather_warning(self, identifier_or_id):
        """Get Engage Weather Warning format for an alert"""
        try:
            alert = self.get_alert(identifier_or_id)
            return alert.to_engage_weatherwarning()
        except CAPAlertNotFound:
            raise
        except Exception as e:
            raise CAPAlertValidationError(f"Error converting to Engage Weather Warning: {e}")
    
    def send_alert(self, alert, receiver):
        """
        Send alert to specified receiver (engage or meteoalarm)
        
        Args:
            alert: CAPAlert instance
            receiver: 'engage' or 'meteoalarm'
            
        Returns:
            Task result message
            
        Raises:
            ValueError: If receiver is not 'engage' or 'meteoalarm'
        """
        # Validate receiver
        if receiver not in ['engage', 'meteoalarm']:
            raise ValueError(f"Invalid receiver: {receiver}. Must be 'engage' or 'meteoalarm'")
        
        try:
            # Queue the task
            result = send_alert.delay(alert.id, receiver)
            return f"Queued {receiver} task for alert {alert.identifier}"
        except Exception as e:
            raise CAPAlertValidationError(f"Error queuing {receiver} task: {e}")
    
    # ==================== CAP TASK MANAGEMENT METHODS ====================
    
    def get_task(self, task_id):
        """Get task by id (UUID) with associated alert data"""
        try:
            return CAPTask.objects.select_related('alert').prefetch_related(
                'alert__info_blocks__areas', 'alert__info_blocks__resources'
            ).get(id=task_id)
        except CAPTask.DoesNotExist:
            raise CAPAlertNotFound(f"Task with id '{task_id}' not found")
        except (ValueError, Exception):
            raise CAPAlertNotFound(f"Task with id '{task_id}' not found")
    
    def list_tasks(self, filters=None, order_by='-created_at', count_only=False):
        """
        List tasks with advanced filtering across all entities
        
        filters = {
            # CAPTask fields
            'status': 'success',
            'status__in': ['pending', 'processing'],
            'client': 'engage',
            'client__in': ['engage', 'meteoalarm'],
            'response_status_code': 200,
            'response_status_code__gte': 200,
            'response_status_code__lt': 400,
            'created_at__gte': '2023-01-01',
            'created_at__lte': '2023-12-31',
            'updated_at__gte': '2023-01-01',
            'updated_at__lte': '2023-12-31',
            'error_message__isnull': True,
            'error_message__icontains': 'timeout',
            'request_body__icontains': 'weather',
            'response_body__icontains': 'success',
            
            # CAPAlert fields (via alert__)
            'alert__identifier': 'alert-123',
            'alert__identifier__icontains': 'alert',
            'alert__status': 'Actual',
            'alert__status__in': ['Actual', 'Exercise'],
            'alert__sender__icontains': 'admin',
            'alert__sent__gte': '2023-01-01',
            'alert__sent__lte': '2023-12-31',
            'alert__created_at__gte': '2023-01-01',
            'alert__created_at__lte': '2023-12-31',
            'alert__updated_at__gte': '2023-01-01',
            'alert__updated_at__lte': '2023-12-31',
            
            # CAPInfo fields (via alert__info_blocks__)
            'alert__info_blocks__severity': 'Extreme',
            'alert__info_blocks__severity__in': ['Extreme', 'Severe'],
            'alert__info_blocks__description__icontains': 'flood',
            'alert__info_blocks__urgency__in': ['Immediate', 'Expected'],
            'alert__info_blocks__event__icontains': 'earthquake',
            'alert__info_blocks__category__contains': 'Geo',
            'alert__info_blocks__headline__icontains': 'warning',
            'alert__info_blocks__certainty': 'Observed',
            'alert__info_blocks__effective__gte': '2023-01-01',
            'alert__info_blocks__effective__lte': '2023-12-31',
            'alert__info_blocks__expires__gte': '2023-01-01',
            'alert__info_blocks__expires__lte': '2023-12-31',
            
            # CAPArea fields (via alert__info_blocks__areas__)
            'alert__info_blocks__areas__area_desc__icontains': 'Athens',
            'alert__info_blocks__areas__altitude__gte': 100,
            'alert__info_blocks__areas__ceiling__lte': 1000,
            
            # CAPResource fields (via alert__info_blocks__resources__)
            'alert__info_blocks__resources__mime_type': 'image/png',
            'alert__info_blocks__resources__size__gte': 1024,
            'alert__info_blocks__resources__resource_desc__icontains': 'map'
        }
        
        order_by options:
        - '-created_at', 'created_at' (default: -created_at)
        - '-updated_at', 'updated_at'
        - 'status', '-status'
        - 'client', '-client'
        - 'response_status_code', '-response_status_code'
        - 'alert__identifier', '-alert__identifier'
        - 'alert__sent', '-alert__sent'
        - 'alert__status', '-alert__status'
        - 'alert__info_blocks__severity', '-alert__info_blocks__severity'
        - 'alert__info_blocks__urgency', '-alert__info_blocks__urgency'
        - 'alert__info_blocks__event', '-alert__info_blocks__event'
        """
        try:
            queryset = CAPTask.objects.select_related('alert').prefetch_related(
                'alert__info_blocks__areas', 'alert__info_blocks__resources'
            ).all()
            
            if filters:
                # Build Q objects for complex filtering
                q_objects = Q()
                
                for field, value in filters.items():
                    q_objects &= Q(**{field: value})
                
                queryset = queryset.filter(q_objects)
            
            # Apply ordering
            if order_by:
                queryset = queryset.order_by(order_by)
            
            if count_only:
                return queryset.count()
            
            return queryset
            
        except Exception as e:
            raise CAPAlertValidationError(f"Error filtering tasks: {e}")
    
    def get_tasks_by_status(self, status):
        """Get tasks by status"""
        return self.list_tasks({'status': status})
    
    def get_tasks_by_client(self, client):
        """Get tasks by client (engage or meteoalarm)"""
        return self.list_tasks({'client': client})
    
    def get_tasks_by_alert(self, alert_identifier_or_id):
        """Get tasks for a specific alert"""
        return self.list_tasks({'alert__identifier': alert_identifier_or_id})
    
    def get_tasks_by_date_range(self, start_date, end_date):
        """Get tasks within date range"""
        return self.list_tasks({
            'created_at__gte': start_date,
            'created_at__lte': end_date
        })
    
    def get_failed_tasks(self):
        """Get all failed tasks"""
        return self.list_tasks({'status': 'failed'})
    
    def get_successful_tasks(self):
        """Get all successful tasks"""
        return self.list_tasks({'status': 'success'})
    
    def get_pending_tasks(self):
        """Get all pending tasks"""
        return self.list_tasks({'status': 'pending'})
    
    def get_processing_tasks(self):
        """Get all processing tasks"""
        return self.list_tasks({'status': 'processing'})
    
    def get_tasks_by_response_code(self, status_code):
        """Get tasks by HTTP response status code"""
        return self.list_tasks({'response_status_code': status_code})
    
    def get_tasks_with_errors(self):
        """Get tasks that have error messages"""
        return self.list_tasks({'error_message__isnull': False})
    
    def search_tasks(self, query):
        """Full text search across multiple task and alert fields"""
        try:
            # Build Q objects for OR search across multiple fields
            q_objects = Q()
            search_fields = [
                'alert__identifier__icontains',
                'alert__info_blocks__description__icontains',
                'alert__info_blocks__headline__icontains',
                'alert__info_blocks__event__icontains',
                'error_message__icontains',
                'request_body__icontains',
                'response_body__icontains'
            ]
            
            for field in search_fields:
                q_objects |= Q(**{field: query})
            
            queryset = CAPTask.objects.select_related('alert').prefetch_related(
                'alert__info_blocks__areas', 'alert__info_blocks__resources'
            ).filter(q_objects)
            
            return queryset.order_by('-created_at')
            
        except Exception as e:
            raise CAPAlertValidationError(f"Error searching tasks: {e}")
    
    def update_task_status(self, task_id, status):
        """Update task status with validation against STATUS_CHOICES"""
        # Validate status against the enum choices
        valid_statuses = [choice[0] for choice in CAPTask.STATUS_CHOICES]
        if status not in valid_statuses:
            raise CAPAlertValidationError(f"Invalid status '{status}'. Must be one of: {', '.join(valid_statuses)}")
        
        try:
            task = self.get_task(task_id)
            task.status = status
            task.save()
            return task
        except CAPAlertNotFound:
            raise
        except Exception as e:
            raise CAPAlertValidationError(f"Error updating task status: {e}")
    
    def delete_task(self, task_id):
        """Delete task by id (UUID)"""
        try:
            task = self.get_task(task_id)
            task.delete()
            return True
        except CAPAlertNotFound:
            raise
        except Exception as e:
            raise CAPAlertValidationError(f"Error deleting task: {e}")
    