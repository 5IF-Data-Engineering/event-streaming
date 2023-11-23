from django.urls import path
from staging_bus_delay.views import (
    stagingFullBusDelayDataPipeline
)

urlpatterns = [
    path('staging_full_bus_delay/', stagingFullBusDelayDataPipeline, name='staging_full_bus_delay_data_pipeline'),
]
