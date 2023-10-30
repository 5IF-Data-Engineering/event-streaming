from django.urls import path
from ingestion_bus_delay.views import ingestionBusDelayDataPipeline

urlpatterns = [
    path('ingestion_bus_delay/', ingestionBusDelayDataPipeline, name='ingestion_bus_delay_data_pipeline'),
]
