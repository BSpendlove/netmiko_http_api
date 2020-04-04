from flask import jsonify
from app.functions.json_format import generic_json
from app.models import db, User, Device

"""
    User Model functions
"""
def db_create_user(**kwargs):
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()
    return user

def db_delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user

def db_get_user(id):
    user = User.query.get(id)
    return user

def db_get_users():
    users = User.query.all()
    return users

def db_update_user(user, **kwargs):
    for key, value in kwargs.items():
        setattr(user, key, value)
    db.session.commit()
    return user

"""
    Device Model functions
"""
def db_create_device(**kwargs):
    device = Device(**kwargs)
    db.session.add(device)
    db.session.commit()
    return device

def db_delete_device(id):
    device = Device.query.get(id)
    db.session.delete(device)
    db.session.commit()
    return device

def db_get_device(id):
    device = Device.query.get(id)
    return device

def db_get_devices():
    devices = Device.query.all()
    return devices

def db_update_device(device, **kwargs):
    for key, value in kwargs.items():
        setattr(device, key, value)
    db.session.commit()
    return device