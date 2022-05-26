import os
from typing import Any

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from . import default_settings
from .utils import load_module_recursively

db: Any = SQLAlchemy()


def create_app(web: bool = True):
    app = Flask(__name__)
    app.config.from_object(default_settings)
    if 'APP_CONFIG' in os.environ:
        app.config.from_envvar('APP_CONFIG', silent=False)
    else:
        config_local = os.path.abspath(os.path.join(os.path.basename(__file__), '../config_local.py')) # TODO
        app.config.from_pyfile(config_local, silent=True)

    db.init_app(app)

    if web:
        configure_login_manager(app)
        configure_views(app)

    return app


def configure_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # pylint: disable=import-outside-toplevel
        from vault.services import UserService
        return UserService.get(id)


def configure_views(app):
    with app.app_context():
        # pylint: disable=import-outside-toplevel
        from vault import views
        load_module_recursively(views)
