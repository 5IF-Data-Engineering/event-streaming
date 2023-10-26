import requests
import json


def extract_data(lat: str, lon: str, start_date: str, end_date: str, daily=None):
    link = "https://archive-api.open-meteo.com/v1/archive?"
    if daily is None:
        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": start_date,
            "end_date": end_date,
            "hourly": "temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation,rain,snowfall," +
                      "snow_depth,surface_pressure,cloudcover,vapor_pressure_deficit,windspeed_10m," +
                      "soil_temperature_0_to_7cm,soil_temperature_7_to_28cm,soil_temperature_28_to_100cm," +
                      "soil_moisture_0_to_7cm,soil_moisture_7_to_28cm,soil_moisture_28_to_100cm",
            "timezone": "America/Toronto"
        }
    else:
        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": start_date,
            "end_date": end_date,
            "daily": "temperature_2m_max,temperature_2m_min,temperature_2m_mean,apparent_temperature_max,"
                     "apparent_temperature_min,apparent_temperature_mean,sunrise,sunset,precipitation_sum,rain_sum,"
                     "snowfall_sum,precipitation_hours,windspeed_10m_max,shortwave_radiation_sum,"
                     "et0_fao_evapotranspiration",
            "timezone": "America/Toronto"
        }
    response = requests.get(link, params=params)
    data = json.loads(response.text)
    return data
