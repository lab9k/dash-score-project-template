from dash import html, dcc

content = html.Div(id="page-content")
layout = html.Div([dcc.Location(id='url'), content])
