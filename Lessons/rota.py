from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá humanos!</p>"

@app.route("/bemvindo/<usuario>/<int:idade>/<float:altura>")
def HAHA(usuario, idade, altura):
    return f"<p>WELLCOME {usuario.upper()}</p>"

@app.route("/json/<usuario>/<int:idade>/<float:altura>")
def guarda_json(usuario, idade, altura):
    return {
        "Usuário": usuario,
        "Idade": idade,
        "Altura": altura,
    }
        




"""
with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('HAHA', usuario='Pedro', idade=23, altura=1.80))
"""