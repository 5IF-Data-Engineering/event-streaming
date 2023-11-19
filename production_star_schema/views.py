from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
import time
from production_star_schema.utils.create_tables import create_prod_tables
from production_star_schema.utils.time_dim import insert_time_dim_data
from production_star_schema.utils.location_dim import insert_location_dim_data
from production_star_schema.utils.incident_dim import insert_incident_dim_data
from django.core.cache import cache
import json


@api_view(['GET'])
def createProductionTables(request):
    # Check if data is already cached
    cached_key = "create_production_tables"
    cached_data = cache.get(cached_key)
    if cached_data is not None:
        returned_data = json.loads(cached_data)
        return JsonResponse(returned_data)
    start_time = time.time()
    # Create tables
    create_prod_tables()
    processing_time = time.time() - start_time
    # Cache data
    data_to_cache = json.dumps({"processing_time": processing_time})
    cache.set(cached_key, data_to_cache)
    return JsonResponse({"processing_time": processing_time})


@api_view(['GET'])
def addTimeDimData(request):
    # Check if data is already cached
    cached_key = "add_time_dim_data"
    cached_data = cache.get(cached_key)
    if cached_data is not None:
        returned_data = json.loads(cached_data)
        return JsonResponse(returned_data)
    start_time = time.time()
    insert_time_dim_data()
    processing_time = time.time() - start_time
    # Cache data
    data_to_cache = json.dumps({"processing_time": processing_time})
    cache.set(cached_key, data_to_cache)
    return JsonResponse({"processing_time": processing_time})


@api_view(['GET'])
def addLocationDimData(request):
    # Check if data is already cached
    cached_key = "add_location_dim_data"
    cached_data = cache.get(cached_key)
    if cached_data is not None:
        returned_data = json.loads(cached_data)
        return JsonResponse(returned_data)
    start_time = time.time()
    insert_location_dim_data()
    processing_time = time.time() - start_time
    # Cache data
    data_to_cache = json.dumps({"processing_time": processing_time})
    cache.set(cached_key, data_to_cache)
    return JsonResponse({"processing_time": processing_time})


@api_view(['GET'])
def addIncidentDimData(request):
    # Check if data is already cached
    cached_key = "add_incident_dim_data"
    cached_data = cache.get(cached_key)
    if cached_data is not None:
        returned_data = json.loads(cached_data)
        return JsonResponse(returned_data)
    start_time = time.time()
    insert_incident_dim_data()
    processing_time = time.time() - start_time
    # Cache data
    data_to_cache = json.dumps({"processing_time": processing_time})
    cache.set(cached_key, data_to_cache)
    return JsonResponse({"processing_time": processing_time})
