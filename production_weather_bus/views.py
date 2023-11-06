from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
import time

from production_weather_bus.pipeline.extract import (
    extract_data,
)
from production_weather_bus.pipeline.transform import (
    transform_data,
)
from production_weather_bus.pipeline.load import (
    load_data,
)

# Create your views here.

@api_view(['GET'])
def productionDataPipeline(request):
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_data()
    # Transformation
    transformed_data = transform_data(data)
    # Load
    load_data(transformed_data)
    processing_time = time.time() - start_time
    return JsonResponse({"processing_time": processing_time})
