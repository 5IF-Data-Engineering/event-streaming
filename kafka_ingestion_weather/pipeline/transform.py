import pandas as pd
from event_streaming.settings import BASE_DIR


def transform_data(data, daily=None):
    """
    Transform data from json to csv format
    :param data:
    :param daily: if daily is None, then hourly data is extracted
    :return: list of data in json format
    """
    result = []
    if daily is None:
        df = pd.DataFrame(data['hourly']) # test
        for index, row in df.iterrows():
            data = {
                "time": row['time'],
                "temperature_2m": row['temperature_2m'],
                "relativehumidity_2m": row['relativehumidity_2m'],
                "dewpoint_2m": row['dewpoint_2m'],
                "apparent_temperature": row['apparent_temperature'],
                "precipitation": row['precipitation'],
                "rain": row['rain'],
                "snowfall": row['snowfall'],
                "snow_depth": row['snow_depth'],
                "surface_pressure": row['surface_pressure'],
                "cloudcover": row['cloudcover'],
                "vapor_pressure_deficit": row['vapor_pressure_deficit'],
                "windspeed_10m": row['windspeed_10m'],
                "soil_temperature_0_to_7cm": row['soil_temperature_0_to_7cm'],
                "soil_temperature_7_to_28cm": row['soil_temperature_7_to_28cm'],
                "soil_temperature_28_to_100cm": row['soil_temperature_28_to_100cm'],
                "soil_moisture_0_to_7cm": row['soil_moisture_0_to_7cm'],
                "soil_moisture_7_to_28cm": row['soil_moisture_7_to_28cm'],
                "soil_moisture_28_to_100cm": row['soil_moisture_28_to_100cm'],
            }
            result.append(data)
    else:
        df = pd.DataFrame(data)
        for index, row in df.iterrows():
            data = {
                "time": row['time'],
                "temperature_2m_max": row['temperature_2m_max'],
                "temperature_2m_min": row['temperature_2m_min'],
                "temperature_2m_mean": row['temperature_2m_mean'],
                "apparent_temperature_max": row['apparent_temperature_max'],
                "apparent_temperature_min": row['apparent_temperature_min'],
                "apparent_temperature_mean": row['apparent_temperature_mean'],
                "sunrise": row['sunrise'],
                "sunset": row['sunset'],
                "precipitation_sum": row['precipitation_sum'],
                "rain_sum": row['rain_sum'],
                "snowfall_sum": row['snowfall_sum'],
                "precipitation_hours": row['precipitation_hours'],
                "windspeed_10m_max": row['windspeed_10m_max'],
                "shortwave_radiation_sum": row['shortwave_radiation_sum'],
                "et0_fao_evapotranspiration": row['et0_fao_evapotranspiration']
            }
            result.append(data)
    return result
