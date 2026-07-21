import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent  # salva o banco na mesma pasta do script


def criar_tabela(cur, con):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS clientes ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nome VARCHAR(100), "
        "email VARCHAR(150))"
    )
    con.commit()


def inserir_registros(con, cur, nome, email):
    data = (nome, email)
    # uso do tupla 'data' para evitar SQL Injection (concatenação)
    cur.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", data)
    con.commit()


def atualizar_registro(con, cur, nome, email, id_cliente):
    data = (nome, email, id_cliente)
    cur.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    con.commit()


def deletar_registro(con, cur, id_cliente):
    data = (id_cliente,)
    cur.execute("DELETE FROM clientes WHERE id=?;", data)
    con.commit()


def inserir_muitos(con, cur, dados):
    cur.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    con.commit()


def visualizar_cliente(cur, id_cliente):
    # uso do fetchone para retornar apenas um registro
    cur.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))
    return cur.fetchone()


def listar_clientes(cur):
    cur.execute("SELECT * FROM clientes")
    return cur.fetchall()


# O "with" garante que a conexão será fechada ao sair do bloco
with sqlite3.connect(ROOT_PATH / "meu_banco.db") as con:
    cur = con.cursor()  # cur é a variável do cursor

    criar_tabela(cur, con)

    cliente = visualizar_cliente(cur, 1)
    print(cliente)

    clientes = listar_clientes(cur)
    for usuario in clientes:
        print(usuario)

    """
    dados = [
        ("Guilherme", "guilherme@gmail.com"),
        ("Larissa", "larissa@gmail.com"),  # teste de inserção em lote
        ("Vitoria", "vitoria@gmail.com"),
    ]

    inserir_muitos(con, cur, dados)
    """
