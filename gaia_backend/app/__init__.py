# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Import parts of our application
        from . import routes

        # Register Blueprints
        app.register_blueprint(routes.bp)

    return app