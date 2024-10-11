from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, cors
from .routes.products import product_blueprint
# import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    cors.init_app(app)

    # Register blueprints (routes)
    app.register_blueprint(product_blueprint, url_prefix='/product')
    # app.register_blueprint(orders.api, url_prefix='/api/orders')
    # app.register_blueprint(users.api, url_prefix='/api/users')

    return app
