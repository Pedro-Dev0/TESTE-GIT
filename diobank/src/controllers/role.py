from flask import Blueprint, request
from src import Role, db  # type: ignore
from http import HTTPStatus
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Blueprint("role", __name__, url_prefix="/roles") # sempre plural o url padrão RESTful só usado nome app para conexão, não tem nada a ver com o init

@app.route("/", methods=["POST"])
def create_role():
    data = request.json
    role = Role(name=data["name"])
    db.session.add(role)
    db.session.commit()
    return {"message": "Role created!"}, HTTPStatus.CREATED