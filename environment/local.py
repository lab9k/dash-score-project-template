import os
import dash_bootstrap_components as dbc
from plotly.colors import qualitative

EXTERNAL_STYLESHEETS = [
    dbc.themes.BOOTSTRAP
]
EXTERNAL_SCRIPTS = [
    'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js',
]

CACHE_TYPE = 'filesystem'
CACHE_LOCATION = 'cache-directory'
CACHE_TIMEOUT = 60

DEBUG = os.getenv('DEBUG', None) is not None

DEFAULT_URL = '/drukte/parking'

# Colors
# You can use a pre-made color palette from the plotly library:
# https://plotly.com/python/discrete-color/#0d016fab-a8a8-413e-86d1-e59bb9c023fa
# Or you can define your own color theme here, as an array of 11 css colors
DEFAULT_VISUALS_COLOR_THEME = qualitative.Vivid
