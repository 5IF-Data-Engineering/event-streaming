from pipeline_api.settings import BASE_DIR
import pandas as pd


def extract_data(year: str):
    """
    Extract data from xlsx file
    :param year: year of the data
    :return: pandas dataframe
    """
    df = pd.ExcelFile(f"{BASE_DIR}/bus_data/ttc-bus-delay-data-{year}.xlsx").parse('Sheet1')
    return df
