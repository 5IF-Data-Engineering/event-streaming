from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from kafka_ingestion_weather.kafka.producer_extract import producer_extract_data
from kafka_ingestion_weather.kafka.consumer_transform import consumer_transform_data
from kafka_ingestion_weather.kafka.consumer_load import consumer_load_data


@api_view(['GET'])
def kafkaIngestionWeatherDataPipeline(request):
    transform_topic_name = request.query_params.get('transform_topic_name', None)
    load_topic_name = request.query_params.get('load_topic_name', None)
    lat = request.query_params.get('lat', None)
    lon = request.query_params.get('lon', None)
    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)
    daily = request.query_params.get('daily', None)

    # Start pipeline
    # Extraction
    producer_extract_data(transform_topic_name, lat, lon, start_date, end_date, daily)

    # Transformation
    consumer_transform_data(transform_topic_name, load_topic_name, daily)

    # Load
    consumer_load_data(load_topic_name, daily)

    return JsonResponse({"message": "Pipeline finished"})
