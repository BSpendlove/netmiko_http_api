from . import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
    id: int
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    devices = db.relationship('Device', backref="device", lazy='dynamic')

    def __repr__(self):
        return '<cfl_pybgp User Object ({})>'.format(self.id)

@dataclass
class Device(db.Model):
    id: int
    user: str
    ip_addr: str
    friendly_name: str
    vendor: str

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ip_addr = db.Column(db.String(64), index=True, unique=True)
    friendly_name = db.Column(db.String(64))
    vendor = db.Column(db.String(64))

    def __repr__(self):
        return '<cfl_pybgp Device Object ({})>'.format(self.id)