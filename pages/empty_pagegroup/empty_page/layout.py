######!!!============================ Import components and libraries ============================######
## import required libraries and components
from dash import html, dcc
import plotly.express as px

## import dash data dialogics gereric components
from layout.structure.grid import Column, Row
from components.tiles import pagetitletile, subtitletile, infotile, filtertile, plottile, maptile, tile
import components.plots as plots
import components.maps as maps

### import your custom data components
# from data.preprocess import 
# from data.analyse import 
# from data.prep import 


######!!!============================ Define page default variables ============================######
pagetitle = ''
pageinfo = '' 


######!!!============================ Prepare initial data ============================######


######!!!============================ Define page content ============================######


######!!!============================ Build page layout ============================######
layout = Column(children=[
    Row(content=pagetitletile(pagetitle)),
    Row(content=infotile(pageinfo)),
    Row(children=[
        ]) 
]).get_layout()
