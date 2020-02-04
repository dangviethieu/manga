from apps.config.dev import DevConfig
from apps.config.test import TestingConfig
from apps.config.product import ProductConfig
from apps.config.base import BaseConfig


config_by_name = dict(
    dev=DevConfig,
    test=TestingConfig,
    product=ProductConfig
)

key = BaseConfig.SECRET_KEY

