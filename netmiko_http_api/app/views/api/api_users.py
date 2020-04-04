from flask import Blueprint, render_template, abort, request, jsonify
from app.functions import db_functions
import json

bp = Blueprint("api_users_routes", __name__, url_prefix="/api/users")

@bp.route("/", methods=['GET', 'POST'])
def api_users():
    content_type = request.headers.get('Content-Type')

    if request.method == 'POST':
        if not request.json:
            abort(400)

        users_json = db_functions.db_create_user(**request.json)
        return jsonify(users_json)

    else:
        users = db_functions.db_get_users()
        users_json = jsonify(users)

        if content_type == "application/json":
            return users_json
        else:
            return render_template("api/index.html", output_result=json.dumps(users_json.json, indent=4))

@bp.route("/<int:id>", methods=['GET','POST'])
def api_user(id):
    content_type = request.headers.get('Content-Type')

    user = db_functions.db_get_user(id)
    user_json = jsonify(user)

    if content_type == "application/json":
        return user_json
    else:
        return render_template("api/index.html", output_result=json.dumps(user_json.json, indent=4))