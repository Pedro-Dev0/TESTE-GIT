from flask import Blueprint, request
from src import User, db
from http import HTTPStatus

app = Blueprint("user", __name__, url_prefix="/users") # sempre plural o url padrão RESTful

def _create_user():
    data = request.json
    user = User(username=data["username"])
    db.session.add(user)
    db.session.commit()

@app.route('/', methods= ["GET", 'POST'])
def handle_user():
    if request.method == "POST":
        _create_user()
        return {"message": "User created!"}, HTTPStatus.CREATED
    else:
        return {"users": []}
    