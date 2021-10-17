from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'jnsjndsnbjlkjeijogd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.jinja_env.globals.update(len=len)

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .profile import profile
    from .appointments import appointment
    from .support import support

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(profile, url_prefix='/profile')
    app.register_blueprint(appointment, url_prefix='/appointments')
    app.register_blueprint(support, url_prefix="/support")

    create_database(app)
    # db.drop_all(app=app)

    login_manager = LoginManager()
    login_manager.login_views = 'views.home'
    login_manager.init_app(app)

    from .models import User
    from .models import Therapist

    @login_manager.user_loader
    def load_user(id):
        return Therapist.query.get(int(id)) if User.query.get(int(id)) is None else User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('WebApp/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')
