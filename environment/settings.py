import os

EXTERNAL_STYLESHEETS = []

CACHE_TYPE = 'filesystem'
CACHE_LOCATION = 'cache-directory'

DEBUG = os.getenv('DEBUG', None) is not None
