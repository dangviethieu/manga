from apps.config.base import BaseConfig


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True

