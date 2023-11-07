from django.urls import path
from staging_weather.views import (
    stagingYearMonthWeatherDataPipeline,
    stagingYearMonthDayWeatherDataPipeline,
    stagingFullWeatherDataPipeline,
    stagingWeekdayWeekendHourWeatherDataPipeline
)

urlpatterns = [
    path('staging_year_month_weather/', stagingYearMonthWeatherDataPipeline, name='staging_year_month_weather_data_pipeline'),
    path('staging_year_month_day_weather/', stagingYearMonthDayWeatherDataPipeline, name='staging_year_month_day_weather_data_pipeline'),
    path('staging_full_weather/', stagingFullWeatherDataPipeline, name='staging_full_weather_data_pipeline'),
    path('staging_weekday_weekend_hour_weather/', stagingWeekdayWeekendHourWeatherDataPipeline, name='staging_weekday_weekend_hour_weather_data_pipeline'),
]
