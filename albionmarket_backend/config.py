

import os


class AppConfig(object):
    """Config object for the app that pulls from the environment."""
    DEBUG = bool(os.environ.get('FLASK_DEBUG', False))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres@192.168.99.100:32771/postgres')

    CACHE_TYPE = 'redis'
    CACHE_DEFAULT_TIMEOUT = 600
    CACHE_REDIS_HOST = os.environ.get('CACHE_REDIS_HOST', 'redis')
    CACHE_REDIS_PORT = int(os.environ.get('CACHE_REDIS_PORT', '6379'))
    CACHE_REDIS_PASSWORD = os.environ.get('CACHE_REDIS_PASSWORD', 'pleasechangethis')