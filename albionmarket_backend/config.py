

import os


class AppConfig(object):
    """Config object for the app that pulls from the environment."""
    DEBUG = bool(os.environ.get('FLASK_DEBUG', False))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres@192.168.99.100:32768/postgres')

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 600
