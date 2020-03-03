"""Flask config class."""
import os
from os.path import join


class Config(object):
    """Set Flask base configuration"""
    SECRET_KEY = 'dfdQbTOExternjy5xmCNaA'

    # General Config
    DEBUG = False
    TESTING = False

    # Forms config
    WTF_CSRF_SECRET_KEY = 'f7Z-JN0ftel5Sp_TywHuxA'

    # Database config
    CWD = os.getcwd()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(CWD, 'cscourses.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevConfig(Config):
    DEBUG = True
