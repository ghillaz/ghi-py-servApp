

# simple app


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    """ Create an application instance """
    app = Flask(__name__)

    # initialize extenstions
    bootstrap.init_app(app)
    db.init_app(app)

    return app
