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
    records = df.to_dict(orient='records')
    return records
