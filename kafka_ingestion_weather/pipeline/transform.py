import pandas as pd


def transform_data(data, city):
    """
    Transform data from json to csv format
    :param data:
    :param city:
    :records: list of dictionaries
    """
    result = []
    df = pd.DataFrame(data)  # test
    df['city'] = city
    df['year'] = df['time'].apply(lambda x: int(x[:4]))
    df['month'] = df['time'].apply(lambda x: int(x[5:7]))
    df['day'] = df['time'].apply(lambda x: int(x[8:10]))
    df['hour'] = df['time'].apply(lambda x: int(x[11:13]))
    records = df.to_dict(orient='records')
    return records
