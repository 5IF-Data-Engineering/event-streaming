import pandas as pd
from event_streaming.settings import BASE_DIR


def transform_data(data, city):
    """
    Transform data from json format to list of data in json format
    :param data:
    :param city:
    :return: list of data in json format
    """
    df = pd.DataFrame(data)
    df['city'] = city
    records = df.to_dict(orient='records')
    return records
