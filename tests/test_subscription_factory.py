import bridge.gravitee_client as client
import bridge.subscription_factory as factory


def test_subscription(mocker):
    mocker.patch.multiple("bridge.gravitee_client", create_application=mocker.DEFAULT)
    application_name = mocker.sentinel.application_name
    contact_email = mocker.sentinel.contact_email
    data_pass_id = mocker.sentinel.data_pass_id
    scopes = mocker.sentinel.scopes
    application_id = mocker.sentinel.application_id

    client.create_application.return_value = {"id": application_id}

    factory.subscribe(application_name, contact_email, data_pass_id, scopes)
    client.create_application.assert_called_once()
