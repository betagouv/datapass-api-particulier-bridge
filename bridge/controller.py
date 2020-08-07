from flask import Blueprint, request, current_app, jsonify
import bridge.subscription_factory as subscription_factory

bp = Blueprint("Application subscription", __name__, url_prefix="/applications")


@bp.route("/subscribe", methods=("POST",))
def subscribe():
    auth_token = request.headers.get("X-Gravitee-API-Key")

    if not auth_token:
        return "Forbidden", 401

    if auth_token != current_app.config.get("DATA_PASS_API_KEY"):
        return "Unauthorized", 403

    content = request.json
    assert "name" in content
    assert "email" in content
    assert "data_pass_id" in content
    assert "scopes" in content

    application = subscription_factory.subscribe(
        content["name"], content["email"], content["data_pass_id"], content["scopes"]
    )

    return jsonify(application)
