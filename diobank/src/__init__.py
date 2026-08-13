from flask import Flask
import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)  # avisa que tem coisas sensiveis para não subir no git ou controle de versão

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='diobank.sqlite',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)

    return app