from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
import time
from ingestion_bus_delay.pipeline.extract import extract_data
from ingestion_bus_delay.pipeline.clean import clean_data
from ingestion_bus_delay.pipeline.transform import transform_data
from ingestion_bus_delay.pipeline.load import load_data
from pipeline_api.settings import CACHE_TTL
from django.core.cache import cache
import json


@api_view(['GET'])
def ingestionBusDelayDataPipeline(request):
    # Get query params
    year = request.query_params.get('year', None)
    city = request.query_params.get('city', None)
    # Check if data is already cached
    cached_key = f"ingestion_bus_delay_data_{year}"
    cached_data = cache.get(cached_key)
    if cached_data is not None:
        returned_data = json.loads(cached_data)
        return JsonResponse(returned_data)

    # If not cached, start pipeline
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_data(year)
    # Cleaning
    cleaned_data = clean_data(data)
    # Transformation
    transformed_data = transform_data(cleaned_data, city)
    # Load
    load_data(transformed_data)
    processing_time = time.time() - start_time

    # Cache data
    data_to_cache = json.dumps({"processing_time": processing_time})
    cache.set(cached_key, data_to_cache, timeout=CACHE_TTL)
    return JsonResponse({"processing_time": processing_time})
