from typing import List

from dash import html, dcc
from components import navigation
from utils.routing import PathUtil

content = html.Div(id="page-content")


def generate_layout(routes: List[PathUtil], store_ids: List[str]):
    return html.Div([
        *[dcc.Store(x) for x in store_ids],
        dcc.Location(id='url'),
        navigation.navbar(routes),
        content
    ])
