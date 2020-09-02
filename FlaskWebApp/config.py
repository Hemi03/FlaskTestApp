import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """a standart config for the Flask App
    """
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SECRET_KEY = 'akdsfalkjeifahbbneif213'


class TestingConfig(Config):
    """the Flask App config for Integration tests
    """
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):
    DEBUG = False
