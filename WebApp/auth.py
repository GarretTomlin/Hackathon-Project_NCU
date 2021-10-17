from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask.globals import session
from .models import Therapist, User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user, login_manager


auth = Blueprint('auth', __name__)


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        role = int(request.form.get('role'))

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exist', category='error')

        elif len(email) < 4:
            flash('Incorrect Email', category='error')
        elif len(first_name) < 2:
            flash('name too short', category='error')
        elif len(last_name) < 2:
            flash('name too short', category='error')
        elif password != confirm_password:
            flash('password does not match with confirm password', category='error')
        elif len(password) < 7:
            flash('password should be longer', category='error')
        else:
            if role == 0:
                new_user = User(email=email, role=role, first_name=first_name, last_name=last_name,
                                password=generate_password_hash(password, method='sha256'))
            else:
                new_user = Therapist(email=email, role=role, first_name=first_name, last_name=last_name,
                                     password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')

            return redirect(url_for('views.chat'))
    return render_template("signup.html")


@auth.route("/signin",  methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        therapist = Therapist.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Login Successfully", category='success')
                login_user(user)
                return redirect(url_for('views.chat'))

        else:
            print("here runs")
            print(therapist.first_name)
            if check_password_hash(therapist.password, password):
                flash("Login Successfully", category='success')
                login_user(therapist)
                return redirect(url_for('views.chat'))
            else:
                flash('Incorrect Credentials', category='error')

        flash('Incorrect Credentials', category='error')
    return render_template('signin.html')


@auth.route("/signout")
@login_required
def signout():
    logout_user()
    return redirect(url_for('views.home'))
