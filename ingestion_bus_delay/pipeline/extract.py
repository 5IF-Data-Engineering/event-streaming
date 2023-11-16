from pipeline_api.settings import BASE_DIR
import pandas as pd


def clean_data(df: pd.DataFrame):
    """
    Remove the rows with missing location and incident values
    :param df: pandas dataframe
    :return: pandas dataframe
    """
    df = df[df['Location'].notna()]
    df = df[df['Incident'].notna()]
    return df


def extract_data(year: str):
    """
    Extract data from xlsx file
    :param year: year of the data
    :return: pandas dataframe
    """
    df = pd.ExcelFile(f"{BASE_DIR}/bus_data/ttc-bus-delay-data-{year}.xlsx").parse('Sheet1')
    df = clean_data(df)
    return df
