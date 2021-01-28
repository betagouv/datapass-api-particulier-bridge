from bridge.email_client import send_mail
from flask import render_template


def on_user_registered(sender, **kwargs):
    application_id = kwargs["application_id"]
    application_name = kwargs["application_name"]
    technical_contact_email = kwargs["technical_contact_email"]
    functional_contact_email = kwargs["functional_contact_email"]
    author_email = kwargs["author_email"]
    data_pass_id = kwargs["data_pass_id"]

    technical_contact_notification_html = render_template(
        "emails/technical_contact_notification.html",
        application_id=application_id,
        application_name=application_name,
        contact_email=technical_contact_email,
        data_pass_id=data_pass_id,
        signupLink="https://auth.api.gouv.fr/users/sign-up?login_hint={}&force_email=true".format(
            technical_contact_email
        ),
    )

    author_notification_html = render_template(
        "emails/author_notification.html",
        application_id=application_id,
        application_name=application_name,
        contact_email=author_email,
        data_pass_id=data_pass_id,
    )

    send_mail(
        technical_contact_email,
        "Votre raccordement à API Particulier",
        technical_contact_notification_html,
    )

    send_mail(
        author_email, "Votre raccordement à API Particulier", author_notification_html,
    )
