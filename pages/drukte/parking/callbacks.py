import dash
from dash.dependencies import Input, Output
from plotly import express as px

from pages.drukte.parking.data import dataframe


def callbacks(app: dash.Dash):
    @app.callback(
        Output('graph-with-slider', 'figure'),
        Input('year-slider', 'value'))
    def update_figure(selected_year):
        gdp_data = dataframe()
        filtered_df = gdp_data[gdp_data.year == selected_year]

        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                         size="pop", color="continent", hover_name="country",
                         log_x=True, size_max=55)

        fig.update_layout(transition_duration=500)

        return fig
