import os
import sys
import logging
from typing import Any
from logging import StreamHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from . import default_settings

db: Any = SQLAlchemy()


class Application(Flask):
    def __init__(self):
        super(Application, self).__init__(__name__)
        self.config.from_object(default_settings)

        # 生产环境配置
        if 'APP_CONFIG' in os.environ:
            self.config.from_envvar('APP_CONFIG', silent=False)
        else:
            config_local = os.path.abspath(os.path.join(
                os.path.basename(__file__), '../config_local.py'))
            self.config.from_pyfile(config_local, silent=True)

    def prepare_login_manager(self):
        login_manager = LoginManager()
        login_manager.init_app(self)

        @login_manager.user_loader
        def load_user(id):
            # pylint: disable=import-outside-toplevel
            from vault.services import UserService
            return UserService.get(id)

    def ready(self, **kwargs):
        if kwargs.get('db', True):
            db.init_app(self)

        if kwargs.get('web', True):
            self.prepare_login_manager()

        if not self.debug:
            hdl = StreamHandler(sys.stderr)
            fmt = logging.Formatter((
                '[%(asctime)s %(levelname)-9s '
                '%(module)s:%(lineno)d <%(process)d>] %(message)s'))

            hdl.setFormatter(fmt)
            hdl.setLevel(logging.INFO)
            self.logger.addHandler(hdl)
            self.logger.setLevel(logging.INFO)


app = Application()
