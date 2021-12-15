from mysql.connector.errors import ProgrammingError
from MYSQL.db import nova_conexao

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('DROP TABLE emails')
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')