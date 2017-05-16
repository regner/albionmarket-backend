

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache


db = SQLAlchemy()
migrate = Migrate()
cache = Cache()


def configure_extensions(app):
    """Registers all relevant extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
