from mysql.connector.errors import ProgrammingError
from MYSQL.db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Luiza', '96543-7856'),
    ('Julia', '96543-7856')
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as error:
        print(f'Error: {error.msg}')

    else:
        print(f' {cursor.rowcount} Contatos inserido no DB')
