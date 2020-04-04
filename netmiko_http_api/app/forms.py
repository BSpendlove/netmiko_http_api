from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class UserAddForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add')

class UserEditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Save')

class DeviceAddForm(FlaskForm):
    user = StringField('Related User', validators=[DataRequired()])
    ip_addr = StringField('IP Address', validators=[DataRequired()])
    friendly_name = StringField('Friendly Name')
    vendor = StringField('Vendor')
    submit = SubmitField('Add')

class DeviceEditForm(FlaskForm):
    user = StringField('Related User', validators=[DataRequired()])
    ip_addr = StringField('IP Address', validators=[DataRequired()])
    friendly_name = StringField('Friendly Name')
    vendor = StringField('Vendor')
    submit = SubmitField('Save')