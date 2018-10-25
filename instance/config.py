import os


class Config(object):
    """Parent configuration class."""
    DEBUG = True


class Development(Config):
    """Configurations for Development."""
    DEBUG = True


class Testing(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True

class Staging(Config):
    """Configurations for Staging."""
    DEBUG = True


class Production(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


config = {
    'development': Development,
    'testing': Testing,
    'staging': Staging,
    'production': Production,
    'db_url': "dbname='storemanager' host='localhost' port='5432' user='postgres' password='Password12#'",
    'test_db_url': "dbname='storemanagertest' host='localhost' port='5432' user='postgres' password='Password12#'"
}