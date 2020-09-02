from flask import Flask, Blueprint
from flask_restful import Api

from .config import Config
from .rest_Api import API
from .db_Model import DB
from .templates import ROUTES


def create_app(test_config: object = None):
    """create the flask app and set it up

    Args:
        test_config (object, optional): a config the app can start with. Defaults to None.

    Returns:
        Flask: the freshly created app
    """
    app = Flask(__name__)
    if not test_config:
        app.config.from_object(Config)
    else:
        app.config.from_object(test_config)
    app.register_blueprint(ROUTES)
    API.init_app(app)
    DB.init_app(app)
    with app.app_context():
        DB.create_all()
    return app
