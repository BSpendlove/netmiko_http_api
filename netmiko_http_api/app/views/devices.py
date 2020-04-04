from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.functions import db_functions
from app.forms import DeviceAddForm, DeviceEditForm

bp = Blueprint("devices", __name__, url_prefix="/devices")

@bp.route("/")
def devices_home():
    return render_template("devices/index.html", devices=db_functions.db_get_devices())

@bp.route("/create", methods=['GET', 'POST'])
def devices_create():
    form = DeviceAddForm()

    if request.method == "GET":
        return render_template("devices/create.html", form=form)
    else:
        if form.validate_on_submit():
            data = {
                "user": form.user.data,
                "ip_addr": form.ip_addr.data,
                "friendly_name": form.friendly_name.data,
                "vendor": form.vendor.data
            }

            db_functions.db_create_device(**data)
            flash("Device has been successfully created!")

        return redirect(url_for('devices.devices_home'))

@bp.route("/<int:id>/delete", methods=['GET'])
def devices_delete(id):
    db_functions.db_delete_device(id)
    flash("Device has been successfully deleted!")
    return redirect(url_for('devices.devices_home'))

@bp.route("/<int:id>/edit", methods=['GET','POST'])
def devices_edit(id):
    device = db_functions.db_get_device(id)
    form = DeviceEditForm(obj=device)

    if request.method == "GET":
        return render_template("devices/edit.html", form=form)
    else:
        if form.validate_on_submit():
            data = {
                "user": form.user.data,
                "ip_addr": form.ip_addr.data,
                "friendly_name": form.friendly_name.data,
                "vendor": form.vendor.data
            }

            db_functions.db_update_device(device, **data)
            flash("Device has been successfully updated!")
        return redirect(url_for('devices.devices_home'))

@bp.route("/<int:id>", methods=['GET'])
def devices_view(id):
    device = db_functions.db_get_device(id)
    return render_template("devices/view.html", device=device)