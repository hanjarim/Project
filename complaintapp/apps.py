from django.apps import AppConfig


class ComplaintappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'complaintapp'

    def ready(self):
        import complaintapp.signals
