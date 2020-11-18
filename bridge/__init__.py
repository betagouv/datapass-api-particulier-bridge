import os

from flask import Flask
from flask_mail import Mail
from sentry_sdk.integrations.flask import FlaskIntegration
import sentry_sdk


def create_app(config="bridge.config.ProductionConfig"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev",)
    app.config.from_object(config)

    sentry_sdk.init(
        dsn=app.config["SENTRY_DSN"],
        integrations=[FlaskIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production,
        traces_sample_rate=1.0
    )
    from . import controller
    from .email_client import mail
    import bridge.subscription_factory as subscription_factory

    app.register_blueprint(controller.bp)
    mail.init_app(app)
    subscription_factory.init_app(app)

    return app
