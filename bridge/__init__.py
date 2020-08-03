import os

from flask import Flask


def create_app(config="bridge.config.ProductionConfig"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev",)

    app.config.from_object(config)

    from . import subscribe

    app.register_blueprint(subscribe.bp)
    return app
