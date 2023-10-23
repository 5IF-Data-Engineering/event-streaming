import pandas as pd
from event_streaming.settings import BASE_DIR


def transform_data(data, city: str, file_name: str, daily=None):
    """
    Transform data from json to csv format
    :param data:
    :param city:
    :param file_name:
    :param daily: if daily is None, then hourly data is extracted
    """
    if daily is None:
        df = pd.DataFrame(data['hourly'])
        df.to_csv(f"{BASE_DIR}/data/{city}/hourly/{file_name}.csv", index=False)
    else:
        df = pd.DataFrame(data['daily'])
        df.to_csv(f"{BASE_DIR}/data/{city}/daily/{file_name}.csv", index=False)
    return
