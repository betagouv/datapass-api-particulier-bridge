import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATA_PASS_API_KEY = os.environ.get("DATA_PASS_API_KEY")


class DevConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    DATA_PASS_API_KEY = "test_api_key"
    GRAVITEE_URL = "https://portail.test"
    GRAVITEE_ADMIN = "admin"
    GRAVITEE_PASSWORD = "password"
