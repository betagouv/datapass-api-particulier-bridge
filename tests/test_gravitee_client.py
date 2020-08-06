import requests
import bridge.gravitee_client as client


def test_application_creation(mocker, app):
    mocker.patch("requests.post")
    name = mocker.sentinel.name
    hashed_token = mocker.sentinel.hashed_token
    data_pass_id = mocker.sentinel.data_pass_id

    client.create_application(name, hashed_token, data_pass_id)
    requests.post.assert_called_once()


def test_subscription(mocker, app):
    mocker.patch("requests.post")
    application_id = "application_id"
    api_id = "api_id"
    plan_id = "plan_id"

    client.subscribe_to_api(application_id, plan_id, api_id)
    requests.post.assert_called_once()
    assert (
        requests.post.call_args[0][0]
        == "https://portail.test/apis/api_id/subscriptions"
    )


def test_dictionary_update(mocker, app):
    mocker.patch("requests.post")
    mocker.patch("requests.put")

    dictionary_name = "test_dictionary"
    values = mocker.sentinel.values

    client.update_dictionary(dictionary_name, values)
    requests.put.assert_called_once()
    requests.post.assert_called_once()

    assert (
        requests.put.call_args[0][0]
        == "https://portail.test/configuration/dictionaries/test_dictionary"
    )
    assert (
        requests.post.call_args[0][0]
        == "https://portail.test/configuration/dictionaries/test_dictionary/_deploy"
    )


def test_application_metadata_creation(mocker, app):
    mocker.patch("requests.post")

    application_id = "application_id"
    key = "key"
    name = "name"
    value = "value"

    client.create_application_metadata(application_id, key, name, value)
    requests.post.assert_called_once()

    assert requests.post.call_args[1]["json"] == {
        "key": key,
        "name": name,
        "value": value,
        "format": "string",
        "applicationId": application_id,
    }
