######!!!============================ Import components and libraries ============================######
import pandas as pd


######!!!====== Gapminder data =====!!!######

def get_df():
    def query_data():
        # This could be an expensive data querying step
        print('Querying data')
        gdp_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
        return gdp_data.to_json(date_format='iso', orient='split')

    queried_data = query_data()

    def filters(**kwargs):
        return pd.read_json(queried_data, orient='split')

    return filters


gapminderdf = get_df()


######!!!====== SCORE partners =====!!!######
##### Set data directory parameters
indir = "./data/localdata/"
infile = "score_partners.csv"
##### Read data
scorepartners = pd.read_csv(indir+infile, sep=';')
##### Prepare data

######!!!====== dataset =====!!!######
##### Set data directory parameters

##### Read data

##### Prepare data
