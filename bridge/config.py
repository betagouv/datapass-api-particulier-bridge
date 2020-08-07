import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATA_PASS_API_KEY = os.environ.get("DATA_PASS_API_KEY")
    GRAVITEE_URL = os.environ.get("GRAVITEE_URL")
    GRAVITEE_ADMIN = os.environ.get("GRAVITEE_ADMIN")
    GRAVITEE_PASSWORD = os.environ.get("GRAVITEE_PASSWORD")
    DATA_PASS_API_KEY = os.environ.get("DATA_PASS_API_KEY")
    DGFIP_API_ID = os.environ.get("DGFIP_API_ID")
    DGFIP_PLAN_ID = os.environ.get("DGFIP_PLAN_ID")
    CNAF_API_ID = os.environ.get("CNAF_API_ID")
    CNAF_PLAN_ID = os.environ.get("CNAF_PLAN_ID")
    INTROSPECT_API_ID = os.environ.get("INTROSPECT_API_ID")
    INTROSPECT_PLAN_ID = os.environ.get("INTROSPECT_PLAN_ID")


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
