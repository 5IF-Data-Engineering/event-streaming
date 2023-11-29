from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
import time
from pipeline_api.settings import (
    CACHE_TTL
)
from staging_bus_delay.pipeline.extract import (
    extract_full_data
)
from staging_bus_delay.pipeline.transform import (
    transform_full_data
)
from staging_bus_delay.pipeline.load import (
    load_full_data
)
from django.core.cache import cache
import json


@api_view(['GET'])
def stagingFullBusDelayDataPipeline(request):
    year = request.query_params.get('year', None)
    # check if data is already cached
    cached_key = f"staging_full_bus_delay_data_{year}"
    cached_data = cache.get(cached_key)
    if cached_data is not None:
        returned_data = json.loads(cached_data)
        return JsonResponse(returned_data)
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_full_data(year)
    # Transformation
    transformed_data = transform_full_data(data, year)
    # Load
    load_full_data(transformed_data)
    processing_time = time.time() - start_time
    # Cache data
    data_to_cache = json.dumps({"processing_time": processing_time})
    cache.set(cached_key, data_to_cache, timeout=CACHE_TTL)
    return JsonResponse({"processing_time": processing_time})
