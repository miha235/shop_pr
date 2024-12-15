# blog/apps.py
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # добавьте эту строку, если используете Django 3.2+
    name = "blog"  # Укажите имя приложения здесь, чтобы оно было доступно
