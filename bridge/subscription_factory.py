from bridge.crypto import generate_api_key
import bridge.gravitee_client as client


def subscribe(application_name, contact_email, data_pass_id, scopes):
    (api_key, api_key_hash) = generate_api_key()
    client.create_application(application_name, api_key_hash, data_pass_id)
