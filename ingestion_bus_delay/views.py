from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
import time
from ingestion_bus_delay.pipeline.extract import extract_data
from ingestion_bus_delay.pipeline.transform import transform_data
from ingestion_bus_delay.pipeline.load import load_data


@api_view(['GET'])
def ingestionBusDelayDataPipeline(request):
    year = request.query_params.get('year', None)
    city = request.query_params.get('city', None)

    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_data(year)
    # Transformation
    transformed_data = transform_data(data, city)
    # Load
    load_data(transformed_data)
    processing_time = time.time() - start_time
    return JsonResponse({"processing_time": processing_time})