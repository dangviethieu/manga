from web.apps.config import config_by_name

from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    # config app
    app.config.from_object(config_by_name[config_name])
    return app

