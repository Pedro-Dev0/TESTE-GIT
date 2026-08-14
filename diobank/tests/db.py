import sqlite3
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:  # essa parte é se a gaveta g já tem uma conexão com nosso banco se não ai criamos uma gaveta se já tiver pula direto para o return g.db, para não pesar e reaproveitar chamadas já feitas em vez de ficar varias requisições...
        g.db = sqlite3.connect(  # conexao de fato acontecendo 
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES  # detalhe técnico para que possamos converter TIMESTAMP do schema para objetos datetime(sem isso fica string)
        )
        g.db.row_factory = sqlite3.Row  # devolver como dicionario para ser mais legivel como linha['username'] em vez de linha[0]
    return g.db  # devolve toda essa conexão nova ou reaproveitada.

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:  # aqui é algo que se tiver alguma conexão aberta sem uso ele sempre vai fechar...(para não pesar varias conexões ou travar)
        db.close()

def init_db():
    db = get_db()  # chama essa função para pegar a conexão
    with current_app.open_resource('schema.sql') as f:  # abre o schema.sql que está na mesma pasta de forma segura
        db.executescript(f.read() .decode('utf8'))  #lê o conteudo e transforma em texto, e ainda executa tudo de uma vez o schema.sql para criação do banco

@click.command('init-db')  #decorador @ açucar sintetico que transforma essa linha num comando de terminal chamado init-db
def init_db_command():
    """Limpa as tabelas existentes e cria novas tabelas com o schema.sql"""
    init_db()
    click.echo('Banco de dados inicializado com sucesso')  #imprime mensagens que funcionam melhor com essa parte do que print!

def init_app(app):
    app.teardown_appcontext(close_db)  #fica o close_db para ser chamado automaticamente pelo Flask sempre que uma requisição terminar, não precisa ficar chamando manualmente
    app.cli.add_command(init_db_command)  #fica o comando init-db no app para aparecer quando você digitar flask --help ou flask init-db






