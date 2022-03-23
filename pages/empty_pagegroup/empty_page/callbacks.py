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
# from data.preprocess import ...
# from data.analyse import ...
# from data.prep import ...

### import page default variables
# from .layout import ...

######!!!============================ Generate memory stores ============================######
# Add storage container to share data between callbacks as json
# storage_container.add_memory_store('store_id')


######!!!============================ Define callback functions ============================######
def callbacks(app: Dash):
    pass




