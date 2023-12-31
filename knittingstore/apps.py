from django.apps import AppConfig


class KnittingstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'knittingstore'
    
    def ready(self):
        import knittingstore.hooks
