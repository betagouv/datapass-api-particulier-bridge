from flask import Blueprint, request, current_app

bp = Blueprint("Application subscription", __name__, url_prefix="/applications")


@bp.route("/subscribe", methods=("POST",))
def subscribe():
    auth_header = request.headers.get("Authorization")
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = None

    if not auth_token:
        return "Forbidden", 401

    if auth_token != current_app.config.get("DATA_PASS_API_KEY"):
        return "Unauthorized", 403

    return "OK", 200
