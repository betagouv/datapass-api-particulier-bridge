from flask import current_app
from bridge.crypto import generate_api_key
from blinker import Namespace
import bridge.gravitee_client as client
from .registration_listener import on_user_registered

subscription_signals = Namespace()
user_registered = subscription_signals.signal("user-registered")


def subscribe(
    application_name,
    owner_email,
    technical_contact_email,
    functional_contact_email,
    data_pass_id,
    scopes,
):
    (api_key, api_key_hash) = generate_api_key()
    (dgfip_api_id, dgfip_plan_id) = _get_dgfip_references()
    (cnaf_api_id, cnaf_plan_id) = _get_cnaf_references()
    (introspect_api_id, introspect_plan_id) = _get_introspect_references()

    # Create the application
    application = client.create_application(
        application_name, api_key_hash, data_pass_id
    )

    # Subscribe the application to all data providers APIs
    client.subscribe_to_api(application["id"], dgfip_plan_id, dgfip_api_id)
    client.subscribe_to_api(application["id"], cnaf_plan_id, cnaf_api_id)
    client.subscribe_to_api(application["id"], introspect_plan_id, introspect_api_id)

    # Update Gravitee dictionaries to fill information upon future calls
    client.update_dictionary(
        "application-names",
        "Application Names",
        {application["id"]: application["name"]},
    )
    client.update_dictionary(
        "api-particulier-scopes",
        "API Particulier Scopes",
        {api_key_hash[0:64]: ",".join(scopes)},
    )

    # Fill the application metadata with the API Key TODO: improve this not very stealth way of providing the API Key
    client.create_application_metadata(application["id"], "API Key", api_key)

    owner_id = _find_or_register_user(owner_email)
    technical_contact_id = _find_or_register_user(technical_contact_email)
    functional_contact_id = _find_or_register_user(functional_contact_email)

    # Add other contacts as application users
    client.add_user_to_application(owner_id, application["id"])
    client.add_user_to_application(functional_contact_id, application["id"])

    # Give the application ownership to the technical user
    client.transfer_ownership(technical_contact_id, application["id"])

    # Notify listeners that a new registration have been made, send a mail
    user_registered.send(
        current_app._get_current_object(),
        application_id=application["id"],
        application_name=application_name,
        author_email=owner_email,
        technical_contact_email=technical_contact_email,
        functional_contact_email=functional_contact_email,
        data_pass_id=data_pass_id,
    )

    return application


def init_app(app):
    user_registered.connect(on_user_registered, app)


def _get_dgfip_references():
    return (current_app.config["DGFIP_API_ID"], current_app.config["DGFIP_PLAN_ID"])


def _get_cnaf_references():
    return (current_app.config["CNAF_API_ID"], current_app.config["CNAF_PLAN_ID"])


def _get_introspect_references():
    return (
        current_app.config["INTROSPECT_API_ID"],
        current_app.config["INTROSPECT_PLAN_ID"],
    )


def _find_or_register_user(email):
    # Register the contact in the API Manager if they don't have an account yet
    contact_user_id = None
    candidates = client.search_user_by_email(email)
    if len(candidates) > 0 and candidates[0]["email"] == email:
        contact_user_id = candidates[0]["id"]
    else:
        contact_user = client.register_user(email)
        contact_user_id = contact_user["id"]

    return contact_user_id
