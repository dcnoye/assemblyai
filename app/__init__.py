from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiate Flask extensions
migrate = Migrate()
db = SQLAlchemy()


def create_app(extra_config_settings={}):
    """Create a Flask application.
    """
    # Instantiate Flask
    app = Flask(__name__)

    # Load App Config settings
    app.config.from_object('app.settings')

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Register blueprints
    from app.views.home_views import home_blueprint
    app.register_blueprint(home_blueprint)

    from app.views.apis import api_blueprint
    app.register_blueprint(api_blueprint)

    configure_database(app)

    return app

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()
