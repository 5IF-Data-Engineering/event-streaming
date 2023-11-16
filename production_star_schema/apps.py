from django.apps import AppConfig


class ProductionStarSchemaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'production_star_schema'
