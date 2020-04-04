from flask import Blueprint, render_template

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/")
def api_home():
    return render_template("api/index.html")