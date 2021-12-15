from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from contextlib import contextmanager

paramentros = dict(
    host='localhost',
    port='3307',
    user='root',
    passwd='',
    database='agenda'
)


@contextmanager
def nova_conexao():
    conexao = connect(**paramentros)
    try:
        yield conexao
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

