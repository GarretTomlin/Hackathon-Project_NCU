from flask import Blueprint, render_template, redirect, url_for
from flask.globals import request
from flask_login import login_required, current_user
from .AI.supportai import assign_support_group
from .models import User
from . import db


support = Blueprint('support', __name__)


@support.route("/", methods=['GET'])
@login_required
def show_support():
    if current_user.group:
        support_group = User.query.filter_by(group=current_user.group).all()
        return render_template("support.html", user=current_user, members=support_group)
    return render_template("support.html", user=current_user)


@support.route('/join', methods=['POST'])
@login_required
def join_support():
    group = assign_support_group(request.form)
    patient = User.query.filter_by(id=current_user.id).first()
    patient.group = group[0]
    db.session.commit()
    return redirect(url_for("support.show_support"))
