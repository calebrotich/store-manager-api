from flask import Flask
from instance.config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])


    from .api.v1 import v1_blueprint as v1_blueprint
    app.register_blueprint(v1_blueprint, url_prefix='/api/v1')

    return app
