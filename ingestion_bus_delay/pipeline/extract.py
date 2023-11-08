from pipeline_api.settings import BASE_DIR
import pandas as pd


def extract_data(year: str):
    """
    Extract data from xlsx file
    :param year: year of the data
    :return: pandas dataframe
    """
    xls = pd.read_excel(f'{BASE_DIR}/bus_data/ttc-bus-delay-data-{year}.xlsx')
    output_df = pd.DataFrame()
    if isinstance(xls, dict):
        for key, df in xls.items():
            output_df = output_df.append(df)
    else:
        output_df = xls
    return output_df
