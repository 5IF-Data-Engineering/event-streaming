from django.http import HttpResponse, JsonResponse, FileResponse
from event_streaming.settings import (
    BASE_DIR,
    KAFKA_HOST,
    KAFKA_PORT,
)
from rest_framework.decorators import api_view
from ingestion_weather.pipeline.extract import extract_data
from ingestion_weather.pipeline.transform import transform_data
from ingestion_weather.producer.producer_event import producer_event
import time


@api_view(['GET'])
def ingestionWeatherDataPipeline(request):
    topic_name = request.query_params.get('topic_name', None)
    lat = request.query_params.get('lat', None)
    lon = request.query_params.get('lon', None)
    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)
    file_name = request.query_params.get('file_name', None)
    daily = request.query_params.get('daily', None)
    city = request.query_params.get('city', None)

    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_data(lat, lon, start_date, end_date, daily)
    if daily is None:
        name_event = "Hourly weather extraction for " + city
        description_event = "Hourly weather extraction for " + city + " from " + start_date + " to " + end_date
    else:
        name_event = "Daily weather extraction for " + city
        description_event = "Daily weather extraction for " + city + " from " + start_date + " to " + end_date
    producer_event(topic_name, name_event, description_event)

    # Transformation
    transform_data(data, city, file_name, daily)
    if daily is None:
        name_event = "Hourly weather transformation for " + city
        description_event = "Hourly weather transformation for " + city + " from " + start_date + " to " + end_date
    else:
        name_event = "Daily weather transformation for " + city
        description_event = "Daily weather transformation for " + city + " from " + start_date + " to " + end_date
    producer_event(topic_name, name_event, description_event)

    processing_time = time.time() - start_time
    return JsonResponse({"processing_time": processing_time})
    # if daily is None:
    #     path_file = f"{BASE_DIR}/data/{city}/hourly/{file_name}.csv"
    # else:
    #     path_file = f"{BASE_DIR}/data/{city}/daily/{file_name}.csv"
    # return FileResponse(open(path_file, 'rb'))
