from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
import time
from enrichment_bus_weather.utils.join_tables import join_bus_weather_tables


@api_view(['GET'])
def joinBusWeatherView(request):
    start_time = time.time()
    print("Joining bus and weather data")
    join_bus_weather_tables()
    return JsonResponse({"processing_time": str(time.time() - start_time), "message": "Joined bus and weather data"})
