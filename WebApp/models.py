from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    patient_appointments = db.relationship(
        'Appointment', backref="user", foreign_keys="Appointment.user_id", lazy=True)
    therapist_appointments = db.relationship(
        'Appointment', backref="therapist", foreign_keys="Appointment.therapist_id", lazy=True)
    group = db.Column(db.Integer, nullable=True)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
