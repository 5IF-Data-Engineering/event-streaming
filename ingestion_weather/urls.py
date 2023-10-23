from django.urls import path
from ingestion_weather.views import ingestionWeatherDataPipeline

urlpatterns = [
    path('ingestion_weather/', ingestionWeatherDataPipeline, name='ingestion_weather_data_pipeline'),
]