from dash import html, dcc
from pages.drukte.trends.data import dataframe
from storage import container as storage_container
from layout.structure.grid import Column, Row

dataframe()
layout = Column(children=[
    Row(content=html.Div(children=[
        dcc.Input('test_input')
    ])),
    Row(content=html.Div(children=[
        html.P(id='test_output')
    ]))
]).get_layout()


def process_changes(value):
    print(value)
    return [html.Ul(children=[html.Li(value)])]
