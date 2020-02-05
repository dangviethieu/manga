from apps.config import config_by_name

from flask import Flask, render_template


def create_app(config_name):
    app = Flask(__name__)
    # config app
    app.config.from_object(config_by_name[config_name])

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    with app.app_context():
        from apps.home.controller import home_bp
        app.register_blueprint(home_bp, url_prefix='/')
    return app

