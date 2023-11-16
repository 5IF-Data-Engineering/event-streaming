from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
import time
from staging_weather.pipeline.extract import (
    extract_data_year_month,
    extract_data_year_month_day,
    extract_full_data,
    extract_data_weekday_weekend_hour
)
from staging_weather.pipeline.transform import (
    transform_data_year_month,
    transform_data_year_month_day,
    transform_full_data,
    transform_data_weekday_weekend_hour
)
from staging_weather.pipeline.load import (
    load_data_year_month,
    load_data_year_month_day,
    load_full_data,
    load_data_weekday_weekend_hour
)
from django.core.cache import cache
from pipeline_api.settings import CACHE_TTL
import json


@api_view(['GET'])
def stagingYearMonthWeatherDataPipeline(request):
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_data_year_month()
    # Transformation
    transformed_data = transform_data_year_month(data)
    # Load
    load_data_year_month(transformed_data)
    processing_time = time.time() - start_time
    return JsonResponse({"processing_time": processing_time})


@api_view(['GET'])
def stagingYearMonthDayWeatherDataPipeline(request):
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_data_year_month_day()
    # Transformation
    transformed_data = transform_data_year_month_day(data)
    # Load
    load_data_year_month_day(transformed_data)
    processing_time = time.time() - start_time
    return JsonResponse({"processing_time": processing_time})


@api_view(['GET'])
def stagingFullWeatherDataPipeline(request):
    # Check if data is already cached
    cached_key = f"staging_full_weather_data"
    cached_data = cache.get(cached_key)
    if cached_data is not None:
        returned_data = json.loads(cached_data)
        return JsonResponse(returned_data)
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_full_data()
    # Transformation
    transformed_data = transform_full_data(data)
    # Load
    load_full_data(transformed_data)
    processing_time = time.time() - start_time
    # Cache data
    data_to_cache = json.dumps({"processing_time": processing_time})
    cache.set(cached_key, data_to_cache, timeout=CACHE_TTL)
    return JsonResponse({"processing_time": processing_time})


@api_view(['GET'])
def stagingWeekdayWeekendHourWeatherDataPipeline(request):
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
