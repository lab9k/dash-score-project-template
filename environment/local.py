import os

EXTERNAL_STYLESHEETS = [
]
EXTERNAL_SCRIPTS = [
    'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js',
]

CACHE_TYPE = 'filesystem'
CACHE_LOCATION = 'cache-directory'
CACHE_TIMEOUT = 60

DEBUG = os.getenv('DEBUG', None) is None

DEFAULT_URL = '/drukte/parking'

# Set username and password for the app. you can change the value by setting the environment variables
LOGIN_USERNAME = os.getenv('LOGIN_USERNAME', 'admin')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD', 'admin')
