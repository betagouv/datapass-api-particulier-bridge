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
        == "https://admin-api.portail.test/management/organizations/DEFAULT/environments/DEFAULT/apis/api_id/subscriptions"
    )


def test_dictionary_update(mocker, app):
    mocker.patch("requests.post")
    mocker.patch("requests.put")
    mocker.patch("requests.get")

    dictionary_id = "test_dictionary"
    dictionary_name = "Test dictionary"
    values = {"yo": "lo"}

    requests.get.return_value.json.return_value = {
        "id": "application-names",
        "name": "Application Names",
        "type": "manual",
        "state": "stopped",
        "properties": {"crou": "te"},
        "created_at": 1595512468564,
        "updated_at": 1596032119000,
        "deployed_at": 1596032119000,
    }

    client.update_dictionary(dictionary_id, dictionary_name, values)
    requests.get.assert_called_once()
    requests.put.assert_called_once()
    requests.post.assert_called_once()

    assert (
        requests.put.call_args[0][0]
        == "https://admin-api.portail.test/management/organizations/DEFAULT/environments/DEFAULT/configuration/dictionaries/test_dictionary"
    )
    assert requests.put.call_args[1]["json"]["properties"] == {"crou": "te", "yo": "lo"}
    assert (
        requests.post.call_args[0][0]
        == "https://admin-api.portail.test/management/organizations/DEFAULT/environments/DEFAULT/configuration/dictionaries/test_dictionary/_deploy"
    )


def test_application_metadata_creation(mocker, app):
    mocker.patch("requests.post")

    application_id = "application_id"
    name = "name"
    value = "value"

    client.create_application_metadata(application_id, name, value)
    requests.post.assert_called_once()

    assert requests.post.call_args[1]["json"] == {
        "name": name,
        "value": value,
        "format": "string",
    }


def test_user_search(mocker, app):
    mocker.patch("requests.get")

    email = "georges@moustaki.fr"
    escaped_email = "georges moustaki.fr"
    client.search_user_by_email(email)

    requests.get.assert_called_once()

    assert requests.get.call_args[1]["params"] == {
        "q": escaped_email,
        "page": 1,
        "size": 1,
    }


def test_user_registration(mocker, app):
    mocker.patch("requests.post")

    email = "georges@moustaki.fr"

    client.register_user(email)
    requests.post.assert_called_once()

    assert requests.post.call_args[1]["json"] == {
        "email": email,
        "source": "apigouvfr",
        "sourceId": email,
    }


def test_transfer_ownership(mocker, app):
    mocker.patch("requests.post")

    user_id = "georges_moustaki"
    application_id = "application_id"

    client.transfer_ownership(user_id, application_id)

    requests.post.assert_called_once()
    assert requests.post.call_args[1]["json"] == {"id": user_id, "role": "OWNER"}


def test_add_user_to_application(mocker, app):
    mocker.patch("requests.post")

    user_id = "georges_moustaki"
    application_id = "application_id"

    client.add_user_to_application(user_id, application_id)

    requests.post.assert_called_once()
    assert requests.post.call_args[1]["json"] == {"id": user_id, "role": "USER"}
