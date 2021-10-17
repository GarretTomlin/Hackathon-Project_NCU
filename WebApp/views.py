from flask import Flask, app, redirect, url_for, render_template, request, Blueprint
from flask_login import login_required


views = Blueprint('views', __name__)


@views.route("/home")
def home():
    return render_template("index.html")


@views.route("/chat")
@login_required
def chat():

    return render_template("chat.html")
