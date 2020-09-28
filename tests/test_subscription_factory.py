import bridge.gravitee_client as client
import bridge.subscription_factory as factory


def test_subscription(mocker, app):
    mocker.patch.multiple(
        "bridge.gravitee_client",
        create_application=mocker.DEFAULT,
        subscribe_to_api=mocker.DEFAULT,
        update_dictionary=mocker.DEFAULT,
        create_application_metadata=mocker.DEFAULT,
        register_user=mocker.DEFAULT,
        transfer_ownership=mocker.DEFAULT,
        search_user_by_email=mocker.DEFAULT,
    )
    application_name = mocker.sentinel.application_name
    contact_email = "jean@moust.com"
    data_pass_id = mocker.sentinel.data_pass_id
    scopes = ["scope1", "scope2"]
    application_id = mocker.sentinel.application_id

    client.create_application.return_value = {
        "id": application_id,
        "name": application_name,
    }
    user_id = mocker.sentinel.user_id
    client.register_user.return_value = {"id": user_id}

    factory.subscribe(application_name, contact_email, data_pass_id, scopes)

    client.create_application.assert_called_once()
    assert client.subscribe_to_api.call_count == 3
    assert client.update_dictionary.call_count == 2

    client.create_application_metadata.assert_called_once()

    client.search_user_by_email.assert_called_once()
    client.register_user.assert_called_once()
    client.transfer_ownership.assert_called_once()
