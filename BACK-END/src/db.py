import sqlite3
import click
from flask import g, current_app

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# 1. Função que lê o schema.sql e executa os comandos SQL no banco
def init_db():
    db = get_db()
    # Abre o arquivo schema.sql localizado na mesma pasta
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# 2. Cria o comando do terminal
@click.command('init-db')
def init_db_command():
    """Limpa as tabelas existentes e cria novas tabelas com o schema.sql."""
    init_db()
    click.echo('Banco de dados inicializado com sucesso!')

# 3. Registra o encerramento do banco E o novo comando do CLI no Flask
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command) # Insere o comando 'flask init-db' no terminal