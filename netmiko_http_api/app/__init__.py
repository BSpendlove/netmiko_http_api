from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bootstrap = Bootstrap(app)

from app.views.api import api_index as api_routes
from app.views.api import api_devices as api_devices_routes
from app.views.api import api_users as api_users_routes
from app.views import devices as devices_routes
from app.views import users as users_routes

@app.route("/")
def index():
    return render_template("index.html")

#API Routes
app.register_blueprint(api_routes.bp)
app.register_blueprint(api_devices_routes.bp)
app.register_blueprint(api_users_routes.bp)

app.register_blueprint(devices_routes.bp)
app.register_blueprint(users_routes.bp)