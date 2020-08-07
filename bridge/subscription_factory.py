import os
from bridge.crypto import generate_api_key
import bridge.gravitee_client as client


def subscribe(application_name, contact_email, data_pass_id, scopes):
    (api_key, api_key_hash) = generate_api_key()
    (dgfip_api_id, dgfip_plan_id) = _get_dgfip_references()
    (cnaf_api_id, cnaf_plan_id) = _get_cnaf_references()
    (introspect_api_id, introspect_plan_id) = _get_introspect_references()

    application = client.create_application(
        application_name, api_key_hash, data_pass_id
    )
    client.subscribe_to_api(application["id"], dgfip_plan_id, dgfip_api_id)
    client.subscribe_to_api(application["id"], cnaf_plan_id, cnaf_api_id)
    client.subscribe_to_api(application["id"], introspect_plan_id, introspect_api_id)
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
    client.create_application_metadata(application["id"], "api-key", "API Key", api_key)


def _get_dgfip_references():
    return (os.environ.get("DGFIP_API_ID"), os.environ.get("DGFIP_PLAN_ID"))


def _get_cnaf_references():
    return (os.environ.get("CNAF_API_ID"), os.environ.get("CNAF_PLAN_ID"))


def _get_introspect_references():
    return (os.environ.get("INTROSPECT_API_ID"), os.environ.get("INTROSPECT_PLAN_ID"))
