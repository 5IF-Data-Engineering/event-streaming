import pandas as pd
import datetime


def transform_data(data, city):
    """
    Transform data from json format to list of data in json format
    :param data:
    :param city:
    :return: list of data in json format
    """
    df = pd.DataFrame(data)
    df['city'] = city
    df['year'] = df['time'].apply(lambda x: x[:4])
    df['month'] = df['time'].apply(lambda x: x[5:7])
    df['day'] = df['time'].apply(lambda x: x[8:10])
    df['day_of_week'] = df['time'].apply(lambda x: datetime.datetime.strptime(x[:10], '%Y-%m-%d').strftime('%A'))
    df['hour'] = df['time'].apply(lambda x: x[11:13])
    records = df.to_dict(orient='records')
    return records
