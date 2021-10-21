import pandas as pd

from app import cache
from environment import settings


@cache.memoize(timeout=settings.CACHE_TIMEOUT)
def query_data():
    # This could be an expensive data querying step
    print('Querying data')
    gdp_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
    return gdp_data.to_json(date_format='iso', orient='split')
