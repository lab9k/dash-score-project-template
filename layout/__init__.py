from typing import List

from dash import html, dcc
from components import navigation
from utils.routing import PathUtil

content = html.Div(id="page-content")


def generate_layout(routes: List[PathUtil]):
    return html.Div([
        dcc.Store('memory_store_id'),
        dcc.Location(id='url'),
        navigation.navbar(routes),
        content
    ])
