from flask import Blueprint, render_template, abort, request, jsonify
from app.functions import db_functions, netmiko_functions
import json

bp = Blueprint("api_devices_routes", __name__, url_prefix="/api/devices")

@bp.route("/", methods=['GET', 'POST'])
def api_devices():
    content_type = request.headers.get('Content-Type')

    if request.method == 'POST':
        if not request.json:
            abort(400)

        devices = db_functions.db_create_device(**request.json)
        return jsonify(devices)

    else:
        device = db_functions.db_get_devices()
        device_json = jsonify(device)

        if content_type == "application/json":
            return device_json
        else:
            return render_template("api/index.html", output_result=json.dumps(device_json.json, indent=4))

@bp.route("/<int:id>", methods=['GET','POST'])
def api_device(id):
    content_type = request.headers.get('Content-Type')

    device = db_functions.db_get_device(id)
    device_json = jsonify(device)

    if content_type == "application/json":
        return device_json
    else:
        return render_template("api/index.html", output_result=json.dumps(device_json.json, indent=4))

@bp.route("/<int:id>/get_hostname", methods=['GET','POST'])
def api_device_get_hostname(id):
    content_type = request.headers.get('Content-Type')

    device = db_functions.db_get_device(id)
    device_user = db_functions.db_get_user(device.user)

    netmiko_session = netmiko_functions.NetmikoAPI(**{
        "device_type": device.vendor,
        "ip": device.ip_addr,
        "username": device_user.username,
        "password": device_user.password})

    output = netmiko_session.get_hostname()
    netmiko_json = jsonify(output)

    if content_type == "application/json":
        return netmiko_json
    else:
        return render_template("api/index.html", output_result=json.dumps(netmiko_json.json, indent=4))

@bp.route("/<int:id>/send_command", methods=['POST'])
def api_device_send_command(id):
    content_type = request.headers.get('Content-Type')
    if not content_type == "application/json":
        return jsonify({"error": True, "details": "Only application/json is accepted..."})

    if request.method == 'POST':
        if not request.json:
            abort(400)

        content = request.get_json()

        if not content["command_string"]:
            return jsonify({"error": True, "details": "command_string not found in body"})

        device = db_functions.db_get_device(id)
        device_user = db_functions.db_get_user(device.user)

        netmiko_session = netmiko_functions.NetmikoAPI(**{
            "device_type": device.vendor,
            "ip": device.ip_addr,
            "username": device_user.username,
            "password": device_user.password})

        output = netmiko_session.send_command(**content)

        json_output = jsonify({"error": False, "send_command": "{}".format(output)})

        return json_output

@bp.route("/<int:id>/get_interfaces", methods=['GET'])
def api_device_get_interfaces(id):
    content_type = request.headers.get('Content-Type')

    device = db_functions.db_get_device(id)
    device_user = db_functions.db_get_user(device.user)

    netmiko_session = netmiko_functions.NetmikoAPI(**{
        "device_type": device.vendor,
        "ip": device.ip_addr,
        "username": device_user.username,
        "password": device_user.password})

    output = netmiko_session.get_interfaces()
    netmiko_json = jsonify({"error": False, "get_interfaces": "{}".format(output)})

    if content_type == "application/json":
        return netmiko_json
    else:
        return render_template("api/index.html", output_result=json.dumps(netmiko_json.json, indent=4))