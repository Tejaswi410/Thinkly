from django.apps import AppConfig as DjangoAppConfig


class ThinklyConfig(DjangoAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
    verbose_name = "Thinkly"

