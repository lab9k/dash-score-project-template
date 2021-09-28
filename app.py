import dash

import flask
from flask_caching import Cache

from environment import settings
from layout import layout

flask_server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    server=flask_server,
    suppress_callback_exceptions=True,
    external_stylesheets=settings.EXTERNAL_STYLESHEETS,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

cache = Cache(app.server, config={
    'CACHE_TYPE': settings.CACHE_TYPE,
    'CACHE_DIR': settings.CACHE_LOCATION
})

app.layout = layout

server = app.server
