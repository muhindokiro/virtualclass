from django.apps import AppConfig


class VirtualConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "virtual"
    # allows python apps to run automatically when they contain the python to an application module
