from . import database
from flask_login import UserMixin


class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    role = database.Column(database.Integer, nullable=False)
    name = database.Column(database.String(100), nullable=False)
    email = database.Column(database.String(100), unique=True, nullable=False)
    password = database.Column(database.String(100), nullable=False)
    phone_num = database.Column(database.String(100), nullable=False)
    address = database.Column(database.String(100), nullable=False)
    appointments = database.relationship("Appointment", backref="user")


class Appointment(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    time = database.Column(database.DateTime, nullable=False)
    user_id = database.Column(
        database.Integer, database.ForeignKey('user.id'), nullable=False)
