from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user


support = Blueprint('support', __name__)


@support.route("/", methods=['GET'])
@login_required
def show_support():
    pass


@support.route('/join', methods=['POST'])
@login_required
def join_support():
    pass
