from django.urls import path
from staging_bus_delay.views import (
    stagingWeekdayWeekendHourBusDelayDataPipeline,
    stagingWeekdayWeekendHourLocationIncidentBusDelayDataPipeline,
    stagingFullBusDelayDataPipeline
)

urlpatterns = [
    path('staging_weekday_weekend_hour_bus_delay/', stagingWeekdayWeekendHourBusDelayDataPipeline, name='staging_weekday_weekend_hour_bus_delay_data_pipeline'),
    path('staging_weekday_weekend_hour_location_incident_bus_delay/', stagingWeekdayWeekendHourLocationIncidentBusDelayDataPipeline, name='staging_weekday_weekend_hour_location_incident_bus_delay_data_pipeline'),
    path('staging_full_bus_delay/', stagingFullBusDelayDataPipeline, name='staging_full_bus_delay_data_pipeline'),
]
