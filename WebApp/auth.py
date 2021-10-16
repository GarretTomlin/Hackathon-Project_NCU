from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask.globals import session
from .models import User
from werkzeug.security import generate_password_hash , check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint('auth', __name__)

@auth.route("/signup", methods=['GET', 'POST'] )
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        user = User.query.filter_by(email=email).first()
        


        if user:
             flash('Email already exist' , category='error')

        elif len(email) < 4:
            flash('Incorrect Email' , category='error')
        elif len(first_name) < 2:
           flash('name too short' , category='error')
        elif len(last_name) < 2:
            flash('name too short' , category='error')
        elif password != confirm_password:
            flash('password does not match with confirm password' , category='error')
        elif len(password) < 7:
           flash('password should be longer' , category='error')
        else:
            new_user  = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
           
            return redirect(url_for('views.chat'))
        pass
    return render_template("signup.html")

@auth.route("/signin",  methods=['GET', 'POST'] )
def signin(): 
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Login Successfully",category='success')
               
                return redirect(url_for('views.chat'))
            else:
                flash('Incorrect password, try again. ', category='error')
        else:
            flash('Email does not exits', category='error')
    return render_template('signin.html')

@auth.route("/signout" )
@login_required
def signout(): 
    logout_user(user)
    return redirect(url_for('views.home'))
    





