from django.apps import AppConfig


class BraceletsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bracelets'

    def ready(self):
        # Import signal handlers for application startup and initial data seeding.
        from . import signals  # noqa: F401
