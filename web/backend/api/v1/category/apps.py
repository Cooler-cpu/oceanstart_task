from tabnanny import verbose
from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.v1.category'
    verbose_name = 'Категории'
