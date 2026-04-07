from django.apps import AppConfig


class CafeteriaAppConfig(AppConfig):
    name = 'cafeteria_app'

    def ready(self):
        import cafeteria_app.models  # Ensure signals are loaded
