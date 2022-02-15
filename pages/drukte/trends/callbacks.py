from dash import Input, Dash, Output, html
from dash.exceptions import PreventUpdate

from storage import container as storage_container

storage_container.add_memory_store('test_input_store')


def callbacks(app: Dash):
    @app.callback(
        Output('test_input_store', 'data'),
        Input('test_input', 'value'),

    )
    def input_callback(values):
        return values

    @app.callback(
        Output('test_output', 'children'),
        Input('test_input_store', 'data'),
    )
    def output_from_store(data):
        if data is None:
            raise PreventUpdate
        return [html.Ul(children=[html.Li(data)])]
