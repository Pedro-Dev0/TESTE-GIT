import os

from flask import Flask, current_app
import click
from datetime import datetime
import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_migrate import Migrate

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()

class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, active={self.active!r})"

class Post(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"), nullable=False)
    created: Mapped[datetime] = mapped_column(sa.DateTime, default=sa.func.now())
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, author_id={self.author_id!r}, created={self.created!r}, title={self.title!r}, body={self.body!r})"

@click.command('init-db')
def init_db_command():
    with current_app.app_context():
            db.create_all()
    click.echo('Banco de dados inicializado com sucesso')