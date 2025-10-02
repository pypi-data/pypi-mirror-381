from django.apps import AppConfig


class CapAlertsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cap_alerts'
    verbose_name = 'CAP Alerts'
    
    def ready(self):
        """Import signal handlers when the app is ready."""
        try:
            import cap_alerts.signals  # noqa
        except ImportError:
            pass
