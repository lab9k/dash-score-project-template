from dash import html, dcc
from layout.structure.grid import Column, Row

from pages.drukte.parking.data import dataframe


def get_content_with_id(html_id: str):
    return html.Div([
        html.H1("GDP viewer"),
        html.Hr(),
        dcc.Graph(id=html_id),
        dcc.Slider(
            id=f'{html_id}-slider',
            min=dataframe()['year'].min(),
            max=dataframe()['year'].max(),
            value=dataframe()['year'].min(),
            marks={str(year): str(year) for year in dataframe()['year'].unique()},
            step=None
        )
    ])


layout = Column(children=[
    Row(children=[
        Column(content=get_content_with_id('graph-with-slider')),
        Column(),
    ]),
    Row(children=[
        Column(),
        Column(content=get_content_with_id('graph-with-slider-2')),
        Column(content=dcc.Input('some_output_id'), styles={'backgroundColor': 'deeppink'})
    ])
]).get_layout()


def process_args(one, two):
    print(one, two)
    return [f'({one} -> {two})']
