from django.apps import AppConfig


class Base16AdminConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "base16_admin"
