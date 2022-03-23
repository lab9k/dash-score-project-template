######!!!============================ Import components and libraries ============================######
## import required libraries and components
from dash import html, dcc
import plotly.express as px

from dash import Dash, Input, Output, State, html
from dash.exceptions import PreventUpdate
from datetime import datetime as dt

## import dash data dialogics gereric components
from storage import container as storage_container
import components.plots as plots
import components.maps as maps

### import your custom data components
from data.preprocess import gapminderdf
# from data.analyse import ...
# from data.prep import ...

### import page default variables
# from .layout import ...

######!!!============================ Prepare initial data ============================######


######!!!============================ Generate memory stores ============================######
# Add storage container to share data between callbacks as json
# storage_container.add_memory_store('store_id')



######!!!============================ Define callback functions ============================######
def callbacks(app: Dash):

    @app.callback(
        Output('plot_gdp', 'figure'),
        Input('filter_year', 'value'))
    def update_gdp(selected_year):
        pltdf = gapminderdf()
        pltdf = pltdf[pltdf.year == selected_year]
    
        fig = px.scatter(pltdf, x="gdpPercap", y="lifeExp",
                         size="pop", color="continent", hover_name="country",
                         log_x=True, size_max=55)
        fig.update_xaxes(range=[2, 5.1])
        fig.update_yaxes(range=[20, 90])
    
        fig.update_layout(transition_duration=500)

        return fig


