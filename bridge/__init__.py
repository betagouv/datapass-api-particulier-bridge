import os

from flask import Flask
from flask_mail import Mail


def create_app(config="bridge.config.ProductionConfig"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev",)
    app.config.from_object(config)

    from . import controller
    from .email_client import mail
    import bridge.subscription_factory as subscription_factory

    app.register_blueprint(controller.bp)
    mail.init_app(app)
    subscription_factory.init_app(app)

    return app
