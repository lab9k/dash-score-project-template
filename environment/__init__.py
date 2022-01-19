import os
import importlib

os.environ.setdefault('SCORE_DASH_SETTINGS', 'environment.local')


def _load_settings():
    env_module = os.environ.get('SCORE_DASH_SETTINGS')
    return importlib.import_module(env_module)


settings = _load_settings()
