from flask import Blueprint, request, current_app, jsonify
import bridge.subscription_factory as subscription_factory

bp = Blueprint("Application subscription", __name__, url_prefix="/applications")


@bp.route("/subscribe", methods=("POST",))
def subscribe():
    content = request.json
    assert "name" in content
    assert "author_email" in content
    assert "technical_contact_email" in content
    assert "functional_contact_email" in content
    assert "data_pass_id" in content
    assert "scopes" in content

    application = subscription_factory.subscribe(
        content["name"],
        content["author_email"],
        content["technical_contact_email"],
        content["functional_contact_email"],
        content["data_pass_id"],
        content["scopes"],
    )

    return jsonify(application)
