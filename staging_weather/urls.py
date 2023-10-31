from django.urls import path
from staging_weather.views import (
    stagingYearWeatherDataPipeline,
    stagingMonthWeatherDataPipeline,
    stagingHourWeatherDataPipeline,
    stagingYearMonthWeatherDataPipeline,
    stagingWeekdayWeekendWeatherDataPipeline,
    stagingYearMonthDayWeatherDataPipeline,
    stagingYearMonthWeekdayWeekendWeatherDataPipeline
)

urlpatterns = [
    path('staging_year_weather/', stagingYearWeatherDataPipeline, name='staging_year_weather_data_pipeline'),
    path('staging_month_weather/', stagingMonthWeatherDataPipeline, name='staging_month_weather_data_pipeline'),
    path('staging_hour_weather/', stagingHourWeatherDataPipeline, name='staging_hour_weather_data_pipeline'),
    path('staging_year_month_weather/', stagingYearMonthWeatherDataPipeline, name='staging_year_month_weather_data_pipeline'),
    path('staging_year_month_day_weather/', stagingYearMonthDayWeatherDataPipeline, name='staging_year_month_day_weather_data_pipeline'),
    path('staging_weekday_weekend_weather/', stagingWeekdayWeekendWeatherDataPipeline, name='staging_weekday_weekend_weather_data_pipeline'),
    path('staging_year_month_weekday_weekend_weather/', stagingYearMonthWeekdayWeekendWeatherDataPipeline, name='staging_year_month_weekday_weekend_weather_data_pipeline')
]
