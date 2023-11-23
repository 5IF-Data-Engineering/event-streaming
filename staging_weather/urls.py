from django.urls import path
from staging_weather.views import (
    stagingFullWeatherDataPipeline
)

urlpatterns = [
    path('staging_full_weather/', stagingFullWeatherDataPipeline, name='staging_full_weather_data_pipeline'),
]
