from mysql.connector.errors import ProgrammingError
from MYSQL.db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
argumentos = ('João', '96543-7856')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, argumentos)
        conexao.commit()
    except ProgrammingError as error:
        print(f'Error: {error.msg}')

    else:
        print('Contato inserido no DB', cursor.lastrowid)
