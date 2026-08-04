import sqlite3
from flask import g, current_app

def get_db():
    """Conecta ao banco SQLite ou reutiliza a conexão existente na requisição."""
    if 'db' not in g:
        # Acessa o caminho do banco definido no app.config['DATABASE']
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Permite acessar colunas pelos nomes (ex: linha['nome'])
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    """Fecha a conexão ao final de cada requisição."""
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    """Registra o encerramento da conexão no ciclo de vida do Flask."""
    app.teardown_appcontext(close_db)