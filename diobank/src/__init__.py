import os

from flask import Flask, current_app
import click
from datetime import datetime
import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)

class Post:
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(sa.ForeignKey('user.id'))
    created : Mapped[datetime] = mapped_column(sa.DateTime, default=sa.func.now())
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body : Mapped[str] = mapped_column(sa.String, nullable=False)

@click.command('init-db')  #decorador @ açucar sintetico que transforma essa linha num comando de terminal chamado init-db
def init_db_command():
    global db
    with current_app.app_context():
        db.create_all()
    click.echo('Banco de dados inicializado com sucesso') 

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)  # avisa que tem coisas sensiveis para não subir no git ou controle de versão

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///diobank.sqlite',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.cli.add_command(init_db_command)
    db.init_app(app)

    return app