import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent # para cair o banco na mesma parta da conexão

con = sqlite3.connect(ROOT_PATH /'meu_banco.db')# con é conexão

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
    con.commit

deletar_registro(con, cur, 1)