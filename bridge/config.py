class Config(object):
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
