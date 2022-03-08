import dash
from dash.dependencies import Input, Output
from plotly import express as px


def callbacks(app: dash.Dash):
    from pages.drukte.parking.data import dataframe

    def create_callback_with_id(html_id: str):
        @app.callback(
            Output(html_id, 'figure'),
            Input(f'{html_id}-slider', 'value'))
        def update_figure_2(selected_year):
            gdp_data = dataframe()
            filtered_df = gdp_data[gdp_data.year == selected_year]

            fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                             size="pop", color="continent", hover_name="country",
                             log_x=True, size_max=55)

            fig.update_layout(transition_duration=500)

            return fig

    create_callback_with_id('graph-with-slider')
    create_callback_with_id('graph-with-slider-2')
