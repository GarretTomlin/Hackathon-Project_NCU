from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Therapist, User, Appointment
from . import db
from datetime import datetime, timedelta

appointment = Blueprint("appointment", __name__)


@appointment.route("/", methods=["GET"])
@login_required
def show_appointments():
    if current_user.role == 1:
        role = "Therapist"
        appointments = Appointment.query.filter_by(
            therapist_id=current_user.id).all()
        if len(current_user.appointments) == 0:
            return render_template("appointment.html", appointments=[], role=role)

        return render_template("appointment.html", appointments=appointments, role=role)

    else:
        role = "Patient"
        appointments = Appointment.query.filter_by(
            user_id=current_user.id).all()
        therapists = Therapist.query.filter_by(role=1).all()
        if len(current_user.appointments) == 0:
            return render_template("appointment.html", therapists=therapists, appointments=[], role=role)
        return render_template("appointment.html", therapists=therapists, appointments=appointments, role=role)


@appointment.route("/book", methods=["POST"])
@login_required
def book_appointment():
    therapist_id = request.form.get("therapist_id")
    new_appointment = Appointment(
        time=datetime.now() + timedelta(days=10), user_id=current_user.id, therapist_id=therapist_id)
    db.session.add(new_appointment)
    db.session.commit()
    return redirect(url_for("appointment.show_appointments"))
