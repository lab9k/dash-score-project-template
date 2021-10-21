from dash import html
from pages.drukte.trends.data import dataframe

dataframe()
layout = html.P("Hello drukte trends")
