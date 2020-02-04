from web.config.dev import DevConfig
from web.config.test import TestingConfig
from web.config.product import ProductConfig
from web.config.base import BaseConfig


config_by_name = dict(
    dev=DevConfig,
    test=TestingConfig,
    product=ProductConfig
)

key = BaseConfig.SECRET_KEY

