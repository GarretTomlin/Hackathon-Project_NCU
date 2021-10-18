from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, Appointment
from . import db


profile = Blueprint("profile", __name__)


@profile.route("/", methods=['GET'])
@login_required
def show_profile():
    print(current_user.first_name)
    return render_template('profile.html', user=current_user)


@profile.route("/edit", methods=['POST'])
@login_required
def edit_profile():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    updated_rows = User.query.filter_by(id=current_user.id).update(
        dict(first_name=first_name, last_name=last_name, email=email))

    if updated_rows:
        db.session.commit()
        flash("Changes made!", category="success")
        return redirect(url_for('profile.show_profile'))
    flash("Please have correct information.", category="warning")
    return redirect(url_for('profile.show_profile'))


@profile.route("/remove", methods=['DELETE'])
@login_required
def remove_profile():
    Appointment.query.filter_by(user_id=current_user.id).delete()
    User.query.filter_by(id=current_user.id).delete()
    db.session.commit()
    return redirect(url_for('views.home'))
