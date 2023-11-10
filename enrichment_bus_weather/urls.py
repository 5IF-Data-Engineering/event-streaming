from django.urls import path
from enrichment_bus_weather.views import (
    joinBusWeatherView,
)

urlpatterns = [
    path('join_bus_weather/', joinBusWeatherView, name='join_bus_weather'),
]
