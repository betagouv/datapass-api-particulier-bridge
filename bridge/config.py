import os


class Config(object):
    DEBUG = False
    TESTING = False
    GRAVITEE_DOMAIN = os.environ.get("GRAVITEE_DOMAIN")
    GRAVITEE_ADMIN = os.environ.get("GRAVITEE_ADMIN")
    GRAVITEE_PASSWORD = os.environ.get("GRAVITEE_PASSWORD")
    DGFIP_API_ID = os.environ.get("DGFIP_API_ID")
    DGFIP_PLAN_ID = os.environ.get("DGFIP_PLAN_ID")
    CNAF_API_ID = os.environ.get("CNAF_API_ID")
    CNAF_PLAN_ID = os.environ.get("CNAF_PLAN_ID")
    INTROSPECT_API_ID = os.environ.get("INTROSPECT_API_ID")
    INTROSPECT_PLAN_ID = os.environ.get("INTROSPECT_PLAN_ID")
    AUTHENTICATION_SOURCE = os.environ.get("AUTHENTICATION_SOURCE")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT", 25)
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")


class DevConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    DATA_PASS_API_KEY = "test_api_key"
    GRAVITEE_DOMAIN = "portail.test"
    GRAVITEE_ADMIN = "admin"
    GRAVITEE_PASSWORD = "password"
    AUTHENTICATION_SOURCE = "apigouvfr"
    MAIL_DEFAULT_SENDER = "georges@moustaki.fr"
