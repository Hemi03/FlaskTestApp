from flask import Flask
from flask_restful import Api

from .config import Config
from .rest_Api import API
from .db_Model import DB


def create_app(test_config: object = None):
    app = Flask(__name__)
    if not test_config:
        app.config.from_object(Config)
    else:
        app.config.from_object(test_config)
    API.init_app(app)
    DB.init_app(app)
    with app.app_context():
        DB.create_all()
    return app
