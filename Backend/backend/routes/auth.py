from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['POST'])
def login():
    return '<h1>Hello</h1>'


@auth.route("/logout", methods=["POST"])
def logout():
    pass


@auth.route("/register", methods=["POST"])
def register():
    role = request.form.get('role')
    name = request.form.get('name')
    email = request.form.get('email')
    password = generate_password_hash(
        request.form.get('password'), method='sha256')
    phone_num = request.form.get('phone_num')
    address = request.form.get('address')

    found_user = User.query.filter_by(email=email).first()

    if found_user:
        pass

    else:
        new_user = User()

    pass
