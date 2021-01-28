from flask import current_app
import requests


def create_application(name, hashed_token, data_pass_id):
    (base_url, user, password) = _get_credentials()

    r = requests.post(
        "{}/applications".format(base_url),
        json={
            "name": name,
            "description": "Numéro de demande : {}".format(data_pass_id),
            "type": "web",
            "clientId": hashed_token,
        },
        auth=(user, password),
    )
    r.raise_for_status()

    return r.json()


def subscribe_to_api(application_id, plan_id, api_id):
    (base_url, user, password) = _get_credentials()

    r = requests.post(
        "{}/apis/{}/subscriptions".format(base_url, api_id),
        params={"plan": plan_id, "application": application_id},
        auth=(user, password),
    )
    r.raise_for_status()

    return r.json()


def update_dictionary(id, name, values):
    (base_url, user, password) = _get_credentials()

    r = requests.get(
        "{}/configuration/dictionaries/{}".format(base_url, id), auth=(user, password),
    )
    r.raise_for_status()
    properties = r.json()["properties"]

    requests.put(
        "{}/configuration/dictionaries/{}".format(base_url, id),
        json={"name": name, "type": "MANUAL", "properties": {**values, **properties},},
        auth=(user, password),
    ).raise_for_status()

    requests.post(
        "{}/configuration/dictionaries/{}/_deploy".format(base_url, id),
        auth=(user, password),
    ).raise_for_status()


def create_application_metadata(application_id, name, value):
    (base_url, user, password) = _get_credentials()

    r = requests.post(
        "{}/applications/{}/metadata".format(base_url, application_id),
        json={"value": value, "name": name, "format": "string",},
        auth=(user, password),
    )
    r.raise_for_status()

    return r.json()


def search_user_by_email(email):
    (base_url, user, password) = _get_credentials()

    escaped_email = email.replace("@", " ")
    r = requests.get(
        "{}/users".format(base_url),
        params={"q": escaped_email, "page": 1, "size": 1},
        auth=(user, password),
    )
    r.raise_for_status()

    return r.json()["data"]


def register_user(email):
    (base_url, user, password) = _get_credentials()
    source = current_app.config["AUTHENTICATION_SOURCE"]

    requests.post(
        "{}/users/registration".format(base_url),
        json={"email": email, "source": source, "sourceId": email,},
        auth=(user, password),
    ).raise_for_status()


def transfer_ownership(user_id, application_id):
    (base_url, user, password) = _get_credentials()

    requests.post(
        "{}/applications/{}/members/transfer_ownership".format(
            base_url, application_id
        ),
        json={"id": user_id, "role": "OWNER"},
        auth=(user, password),
    ).raise_for_status()


def add_user_to_application(user_id, application_id):
    (base_url, user, password) = _get_credentials()

    requests.post(
        "{}/applications/{}/members".format(base_url, application_id),
        json={"id": user_id, "role": "USER"},
        auth=(user, password),
    ).raise_for_status()


def _get_credentials():
    return (
        f"https://admin-api.{current_app.config['GRAVITEE_DOMAIN']}/management/organizations/DEFAULT/environments/DEFAULT",
        current_app.config["GRAVITEE_ADMIN"],
        current_app.config["GRAVITEE_PASSWORD"],
    )
