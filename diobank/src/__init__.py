import os

from flask import Flask, current_app
import click
from datetime import datetime
import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
jwt = JWTManager()

class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, active={self.active})"

class Post(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(sa.ForeignKey('user.id'), nullable=False)
    created : Mapped[datetime] = mapped_column(sa.DateTime, default=sa.func.now())
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r}, author_id={self.author_id!r})"

@click.command('init-db')  #decorador @ açucar sintetico que transforma essa linha num comando de terminal chamado init-db
def init_db_command():
    global db
    with current_app.app_context():
        db.create_all()
    click.echo('Banco de dados inicializado com sucesso') 

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)  # avisa que tem coisas sensiveis para não subir no git ou controle de versão

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///blog.sqlite",
        JWT_SECRET_KEY="super-secret",
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
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    #registro de blueprint
    from src.controllers import user_control # type: ignore
    from src.controllers import post_control # type: ignore
    from src.controllers import auth # type: ignore

    app.register_blueprint(user_control.app)
    app.register_blueprint(post_control.app)
    app.register_blueprint(auth.app)

    return app