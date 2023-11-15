import pandas as pd
import datetime


def transform_data(data: pd.DataFrame, city: str):
    """
    Transform data from ingestion_weather.pipeline.extract.extract_data
    :param data: pd.DataFrame
    :param city: str
    :return: pd.DataFrame
    """
    data.rename(columns={'Date': 'date', 'Route': 'route', 'Time': 'time', 'Day': 'day_of_week', 'Location': 'location',
                         'Incident': 'incident',
                         'Min Delay': 'min_delay', 'Min Gap': 'min_gap', 'Direction': 'direction',
                         'Vehicle': 'vehicle'}, inplace=True)
    if "Time Tmp" in data.columns:
        data.drop(columns=['Time Tmp'], inplace=True)
    data['year'] = data['date'].apply(lambda x: int(x.year))
    data['month'] = data['date'].apply(lambda x: int(x.month))
    data['day'] = data['date'].apply(lambda x: int(x.day))
    data['day_of_week'] = data['day_of_week'].apply(lambda x: str(x))
    data['location'] = data['location'].apply(lambda x: str(x))
    data['incident'] = data['incident'].apply(lambda x: str(x))
    data['city'] = city
    if isinstance(data['time'][0], datetime.time):
        data['time'] = data['time'].apply(lambda x: x.strftime('%H:%M:%S'))
    data['hour'] = data['time'].apply(lambda x: int(x[:2]))
    return data
