from web.apps.config.dev import DevConfig
from web.apps.config.test import TestingConfig
from web.apps.config.product import ProductConfig
from web.apps.config.base import BaseConfig


config_by_name = dict(
    dev=DevConfig,
    test=TestingConfig,
    product=ProductConfig
)

key = BaseConfig.SECRET_KEY

