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
from data.preprocess import gapminderdf
# from data.analyse import 
# from data.prep import 


######!!!============================ Define page default variables ============================######
pagetitle = 'Demo page'
pageinfo = 'This page demonstrates how a basic Dash Data Dialogics page looks like. ' 




######!!!============================ Define page content ============================######
def plot_gdp(comp_id:str=None):
    content = plottile(
        tiletitle='GDP vs. life expectancy',
        id=comp_id,
    )
    return content

def filter_year(comp_id:str):
    filtercomp = dcc.Slider(
            id=comp_id,
            min=gapminderdf()['year'].min(),
            max=gapminderdf()['year'].max(),
            value=gapminderdf()['year'].min(),
            marks={str(year): str(year) for year in gapminderdf()['year'].unique()},
            step=None,
        )
    content = filtertile(children=[
        html.Div('Year:'),
        filtercomp])
    return content





######!!!============================ Build page layout ============================######
layout = Column(children=[
    Row(content=pagetitletile(pagetitle)),
    Row(content=infotile(pageinfo)),
    Row(children=[
        Column(children=[
            Row(content=subtitletile('Gross domestic product (GDP)')),
            Row(content=filter_year('filter_year')),
            Row(content=plot_gdp('plot_gdp'))
                         ]),
        Column(children=[
            Row(content=subtitletile('SCORE partner cities')),
            ])
        ]) 
]).get_layout()



