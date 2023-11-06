from django.urls import path
from production_weather_bus.views import (
    productionDataPipeline,
)

urlpatterns = [
    path('production_data_pipeline/', productionDataPipeline, name='productionDataPipeline'),
]
