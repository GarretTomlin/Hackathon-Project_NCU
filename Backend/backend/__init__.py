from logging import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

database = SQLAlchemy()


# Creating the application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True

    database.init_app(app)

    manager = LoginManager()
    manager.login_view = "auth.login"
    manager.init_app(app)

    from .routes.auth import auth
    from .models import User
    app.register_blueprint(auth, url_prefix="/auth")

    @manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
