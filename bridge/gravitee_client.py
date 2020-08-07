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

    return r.json()


def subscribe_to_api(application_id, plan_id, api_id):
    (base_url, user, password) = _get_credentials()

    r = requests.post(
        "{}/apis/{}/subscriptions".format(base_url, api_id),
        params={"plan": plan_id, "application": application_id},
        auth=(user, password),
    )

    return r.json()


def update_dictionary(id, name, values):
    (base_url, user, password) = _get_credentials()

    r = requests.get(
        "{}/configuration/dictionaries/{}".format(base_url, id), auth=(user, password),
    )
    properties = r.json()["properties"]

    requests.put(
        "{}/configuration/dictionaries/{}".format(base_url, id),
        json={"name": name, "type": "MANUAL", "properties": {**values, **properties},},
        auth=(user, password),
    )

    requests.post(
        "{}/configuration/dictionaries/{}/_deploy".format(base_url, id),
        auth=(user, password),
    )


def create_application_metadata(application_id, name, value):
    (base_url, user, password) = _get_credentials()

    r = requests.post(
        "{}/applications/{}/metadata".format(base_url, application_id),
        json={"value": value, "name": name, "format": "string",},
        auth=(user, password),
    )

    return r.json()


def _get_credentials():
    return (
        current_app.config["GRAVITEE_URL"],
        current_app.config["GRAVITEE_ADMIN"],
        current_app.config["GRAVITEE_PASSWORD"],
    )
