from django.urls import path
from production_star_schema.views import (
    addTimeDimData,
    addLocationDimData,
    addIncidentDimData
)

urlpatterns = [
    path('add_time_data/', addTimeDimData, name='add_time_data'),
    path('add_location_data/', addLocationDimData, name='add_location_data'),
    path('add_incident_data/', addIncidentDimData, name='add_incident_data'),
]
