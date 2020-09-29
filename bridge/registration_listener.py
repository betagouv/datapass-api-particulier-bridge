from bridge.email_client import send_mail
from flask import render_template


def on_user_registered(sender, **kwargs):
    application_id = kwargs["application_id"]
    application_name = kwargs["application_name"]
    contact_email = kwargs["contact_email"]
    data_pass_id = kwargs["data_pass_id"]
    html = render_template(
        "emails/user_registered.html",
        application_id=application_id,
        application_name=application_name,
        contact_email=contact_email,
        data_pass_id=data_pass_id,
    )

    send_mail(contact_email, "Votre raccordement à API Particulier", html)
