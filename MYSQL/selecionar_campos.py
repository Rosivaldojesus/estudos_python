from mysql.connector.errors import ProgrammingError
from MYSQL.db import nova_conexao

sql = 'SELECT tel, nome FROM contatos'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

    else:
        for contato in cursor.fetchall():
            print('\t'.join(str(campo) for campo in contato ))