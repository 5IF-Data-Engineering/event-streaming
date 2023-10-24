from django.apps import AppConfig


class KafkaIngestionWeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kafka_ingestion_weather'
