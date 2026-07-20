import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent # para cair o banco na mesma parta da conexão

# O "with" garante que a conexão será fechada ao sair do bloco
with sqlite3.connect(ROOT_PATH / 'meu_banco.db') as con: # con é conexão
    cur = con.cursor() # cur é cursor só que abreviado

def criar_tabela(cur, con):
    cur.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
    con.commit()

def inserir_registros(con, cur, nome, email):
    data = (nome, email)
    cur.execute('INSERT INTO clientes (nome, email) VALUES (?,?)' , data)
    con.commit()

def atualizar_registro(con, cur, nome, email, id):
    data = (nome, email, id)
    cur.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    con.commit()

def deletar_registro(con, cur, id):
    data = (id,)
    cur.execute('DELETE FROM clientes WHERE id=?;', data)
    con.commit()

inserir_registros(con, cur, 'PEDROA', 'pedroaaaah@outlook.com' )
