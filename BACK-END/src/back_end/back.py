import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent # para cair o banco na mesma parta da conexão

con = sqlite3.connect(ROOT_PATH /'meu_banco.db')