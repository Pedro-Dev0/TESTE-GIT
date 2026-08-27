from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from src import User, db  # type: ignore
from http import HTTPStatus
from sqlalchemy import inspect

app = Blueprint("auth", __name__, url_prefix="/auth") # sempre plural o url padrão RESTful só usado nome app para conexão, não tem nada a ver com o init

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return {"msg": "Bad username or password"}, HTTPStatus.UNAUTHORIZED

    access_token = create_access_token(identity=username)
    return {"access_token": access_token}