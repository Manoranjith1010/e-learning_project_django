"""
App configuration for coding app
"""

from django.apps import AppConfig


class CodingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.coding'
    verbose_name = 'Coding Challenges'
