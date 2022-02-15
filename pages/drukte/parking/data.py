import pandas as pd
from pages.drukte import preprocess


def get_df():
    queried_data = preprocess.query_data()

    def filters(**kwargs):
        return pd.read_json(queried_data, orient='split')

    return filters


dataframe = get_df()
