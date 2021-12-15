from MYSQL.versao01.conexao_db import conectar_banco_dados

# A variável conexao receber a função conectar_banco_dados(), do arquivo conexao_db, que está dentro do mesmo pacote
conexao = conectar_banco_dados()

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')


for i, database in enumerate(cursor, start=1):  # O start significa o número da coluna na tabela
    print(f'Banco de dados {i}: {database[0]}')
