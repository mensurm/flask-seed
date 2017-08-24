# Application configuration  #####

import logging
import os


class BaseConfiguration(object):
    APP_NAME = 'APP_NAME'
    APP_PORT = 8080
    THREADED = False
    HOST = '0.0.0.0'

    LOGGING_LEVEL = logging.DEBUG
    LOGGING_MESSAGE_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_TIME_FORMAT = '%d-%m-%Y %H:%M:%S'
    basedir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    LOGGING_LOCATION = os.path.join(basedir, 'app.log')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '2de121289-4564daad-4MNcb5f6-eFA-5583c7182'


class DevelopmentConfiguration(BaseConfiguration):
    """Configuration class for development environment"""

    DEBUG = True
    # DATABASE_URI = {development db uri}

class TestingConfiguration(BaseConfiguration):
    """ Configuration class for integration tests """
    DEBUG = True
    basedir = os.path.abspath(os.path.dirname(__file__))

    #use an in memory sqlite database for tests
    DATABASE_URI = 'sqlite:///' + os.path.abspath(os.getcwd())+"/test.db"


class ProductionConfiguration(BaseConfiguration):

    DEBUG = False
    # DATABASE_URI = {production db uri}


