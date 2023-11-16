from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
import time
from enrichment_bus_weather.utils.join_tables import join_bus_weather_tables
from django.core.cache import cache
import json


@api_view(['GET'])
def joinBusWeatherView(request):
    # Check if data is already cached
    cached_key = f"join_bus_weather_data"
    cached_data = cache.get(cached_key)
    if cached_data is not None:
        returned_data = json.loads(cached_data)
        return JsonResponse(returned_data)
    start_time = time.time()
    join_bus_weather_tables()
    # Cache data
    data_to_cache = json.dumps({"processing_time": str(time.time() - start_time),
                                "message": "Joined bus and weather data"})
    cache.set(cached_key, data_to_cache)
    return JsonResponse({"processing_time": str(time.time() - start_time), "message": "Joined bus and weather data"})
