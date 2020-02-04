import os

PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))


class BaseConfig:
    DEBUG = True
    SECRET_KEY = 'my_secret_key'

