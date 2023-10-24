from django.urls import path
from kafka_ingestion_weather.views import kafkaIngestionWeatherDataPipeline

urlpatterns = [
    path('kafka_ingestion_weather/', kafkaIngestionWeatherDataPipeline, name='kafka_ingestion_weather_data_pipeline'),
]
