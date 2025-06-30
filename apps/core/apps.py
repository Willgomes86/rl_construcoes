from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Use the full dotted path so Django can correctly locate the app
    name = 'apps.core'
