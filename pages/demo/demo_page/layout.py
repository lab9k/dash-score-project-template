######!!!============================ Import components and libraries ============================######
## import required libraries and components
from dash import html, dcc
import plotly.express as px
import dash_leaflet as dl
import dash_leaflet.express as dlx  
import json

## import dash data dialogics gereric components
from layout.structure.grid import Column, Row
from components.tiles import pagetitletile, subtitletile, infotile, filtertile, plottile, maptile, tile
import components.plots as plots
import components.maps as maps

### import your custom data components
from data.preprocess import gapminderdf, scorepartners
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

def text_score(comp_id:str):
    txt = ("SCORE is a collaborative project between 9 cities throughout the North Sea Region. The partner cities and their organizations each have experience in using shared data to ensure healthy urban development in the region. ",html.Br(),
           "SCORE aims to increase efficiency and quality of public services in cities through smart and open data-driven solutions. ",html.Br(),
           "The partners develop innovative solutions based on open data and focus on sharing insights and methodologies for developing better public services. For instance in the shape of better management of sustainable mobility, improving air quality, monitoring flooding and furthering crowd management. ")
    content= filtertile(children=[
        html.P(txt)]
        )
    return content

def map_score(comp_id:str=None):
    geo = scorepartners[['Partner_EN','lat', 'long']]
    geo=geo.rename(columns={'long':'lon'})
    geo['tooltip']=geo['Partner_EN']
    geojson =json.loads(geo.to_json(orient='records'))
    geojson = dlx.dicts_to_geojson(geojson)
    geojson = dl.GeoJSON(data=geojson, cluster=True)
    
    overlyrs=[{'layer':geojson,'name':'SCORE partners', 'checked':True, 'legend':True}]
    layers={'overlayers':[*overlyrs]}
    mapchildren=maps.lfmap_lyrs(layers=layers, legend=True)
    mapfig=maps.lfmap_fig(comp_id=comp_id, mapchildren=mapchildren)

    content = maptile(
        tiletitle='SCORE partners',
        mapfigure=mapfig, 
    )
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
                         ], extra_classes=[' col-xl-7']),
        Column(children=[
            Row(content=subtitletile('Project SCORE: Smart Cities + Open Data Re-use')),
            Row(content= text_score(comp_id=text_score)),
            Row(content=map_score(comp_id='map_score'))
            ])
        ]) 
]).get_layout()



