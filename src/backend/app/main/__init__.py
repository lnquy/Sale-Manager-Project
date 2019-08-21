import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.url_map.strict_slashes = False
    app.logger.setLevel(logging.DEBUG)

    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app