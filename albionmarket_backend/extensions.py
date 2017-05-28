

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_cors import CORS
from raven.contrib.flask import Sentry


db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
cors = CORS()
sentry = Sentry()


def configure_extensions(app):
    """Registers all relevant extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    cors.init_app(app)
    sentry.init_app(app)
