from typing import List

from dash import html, dcc
from components import navigation
from utils.routing import PathUtil

content = html.Div(id="page-content")


def generate_layout(routes: List[PathUtil], stores: List):
    return html.Div([
        *stores,
        dcc.Location(id='url'),
        navigation.navbar(routes),
        content
    ])
