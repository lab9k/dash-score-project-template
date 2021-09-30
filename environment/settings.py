import os

EXTERNAL_STYLESHEETS = [
    'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css'
]
EXTERNAL_SCRIPTS = [
    'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js'
]

CACHE_TYPE = 'filesystem'
CACHE_LOCATION = 'cache-directory'

DEBUG = os.getenv('DEBUG', None) is not None

DEFAULT_URL = '/drukte/parking'
TIMEOUT = 60
