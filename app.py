import dash

import flask
from flask_caching import Cache

from environment import settings
from layout import generate_layout
from routes import create_render_function

flask_server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    server=flask_server,
    suppress_callback_exceptions=True,
    external_stylesheets=settings.EXTERNAL_STYLESHEETS,
    external_scripts=settings.EXTERNAL_SCRIPTS,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

cache = Cache(app.server, config={
    'CACHE_TYPE': settings.CACHE_TYPE,
    'CACHE_DIR': settings.CACHE_LOCATION
})

routes = create_render_function(app)
app.layout = generate_layout(routes)

server = app.server
