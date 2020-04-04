from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.functions import db_functions
from app.forms import UserAddForm, UserEditForm

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("/")
def users_home():
    return render_template("users/index.html", users=db_functions.db_get_users())

@bp.route("/create", methods=['GET', 'POST'])
def users_create():
    form = UserAddForm()

    if request.method == "GET":
        return render_template("users/create.html", form=form)
    else:
        if form.validate_on_submit():
            data = {
                "username": form.username.data,
                "password": form.password.data,
            }

            db_functions.db_create_user(**data)
            flash("User has been successfully created!")

        return redirect(url_for('users.users_home'))

@bp.route("/<int:id>", methods=['GET', 'POST'])
def users_edit(id):
    user = db_functions.db_get_user(id)
    form = UserEditForm(obj=user)

    if request.method == "GET":
        return render_template("users/edit.html", form=form)
    else:
        if form.validate_on_submit():
            data = {
                "username": form.username.data,
                "password": form.password.data
            }

            db_functions.db_update_user(user, **data)
            flash("User has been successfully updated!")
        return redirect(url_for('users.users_home'))

@bp.route("/<int:id>/delete", methods=['GET'])
def users_delete(id):
    db_functions.db_delete_user(id)
    flash("User has been successfully deleted!")
    return redirect(url_for('users.users_home'))