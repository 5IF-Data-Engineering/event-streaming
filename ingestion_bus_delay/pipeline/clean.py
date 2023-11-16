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
