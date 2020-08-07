from flask import Blueprint, request, current_app

bp = Blueprint("Application subscription", __name__, url_prefix="/applications")


@bp.route("/subscribe", methods=("POST",))
def subscribe():
    auth_token = request.headers.get("X-Gravitee-API-Key")

    if not auth_token:
        return "Forbidden", 401

    if auth_token != current_app.config.get("DATA_PASS_API_KEY"):
        return "Unauthorized", 403

    return "OK", 200
