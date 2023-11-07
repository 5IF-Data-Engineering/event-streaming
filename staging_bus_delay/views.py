from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
import time
from staging_bus_delay.pipeline.extract import (
    extract_data_weekday_weekend_hour,
    extract_data_weekday_weekend_hour_location_incident,
    extract_full_data
)
from staging_bus_delay.pipeline.transform import (
    transform_data_weekday_weekend_hour,
    transform_data_weekday_weekend_hour_location_incident,
    transform_full_data
)
from staging_bus_delay.pipeline.load import (
    load_data_weekday_weekend_hour,
    load_data_weekday_weekend_hour_location_incident,
    load_full_data
)


@api_view(['GET'])
def stagingWeekdayWeekendHourBusDelayDataPipeline(request):
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_data_weekday_weekend_hour()
    # Transformation
    transformed_data = transform_data_weekday_weekend_hour(data)
    # Load
    load_data_weekday_weekend_hour(transformed_data)
    processing_time = time.time() - start_time
    return JsonResponse({"processing_time": processing_time})


@api_view(['GET'])
def stagingWeekdayWeekendHourLocationIncidentBusDelayDataPipeline(request):
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_data_weekday_weekend_hour_location_incident()
    # Transformation
    transformed_data = transform_data_weekday_weekend_hour_location_incident(data)
    # Load
    load_data_weekday_weekend_hour_location_incident(transformed_data)
    processing_time = time.time() - start_time
    return JsonResponse({"processing_time": processing_time})


@api_view(['GET'])
def stagingFullBusDelayDataPipeline(request):
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_full_data()
    # Transformation
    transformed_data = transform_full_data(data)
    # Load
    load_full_data(transformed_data)
    processing_time = time.time() - start_time
    return JsonResponse({"processing_time": processing_time})